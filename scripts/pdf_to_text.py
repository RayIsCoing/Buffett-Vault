#!/usr/bin/env python3
"""
Batch-convert all PDFs in the Buffett vault to .txt files for grep-ability.
Idempotent: skips files where .txt already exists and is newer than the .pdf.

Usage:
    python3 pdf_to_text.py              # convert all vault PDFs
    python3 pdf_to_text.py --force      # re-convert everything
    python3 pdf_to_text.py --dir PATH   # convert only a specific subdirectory
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

VAULT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SEARCH_DIRS = [
    VAULT_ROOT / "Attachments" / "shareholder-letters",
    VAULT_ROOT / "Attachments" / "partnership-letters",
    VAULT_ROOT / "Attachments" / "speeches",
    VAULT_ROOT / "Attachments" / "articles",
    VAULT_ROOT / "Attachments" / "interviews",
]


def check_pdftotext():
    """Verify pdftotext (poppler) is installed."""
    try:
        subprocess.run(
            ["pdftotext", "-v"],
            capture_output=True,
            check=False,
        )
        return True
    except FileNotFoundError:
        print("ERROR: pdftotext not found. Install poppler:", file=sys.stderr)
        print("  macOS:   brew install poppler", file=sys.stderr)
        print("  Ubuntu:  apt-get install poppler-utils", file=sys.stderr)
        return False


def convert_pdf(pdf_path: Path, force: bool = False) -> Tuple[str, Optional[Path]]:
    """
    Convert a single PDF to .txt in the same directory.
    Returns (status, output_path) where status is 'converted', 'skipped', or 'failed'.
    """
    txt_path = pdf_path.with_suffix(".txt")

    # Skip if txt already exists and is newer than the PDF (unless --force)
    if not force and txt_path.exists():
        if txt_path.stat().st_mtime >= pdf_path.stat().st_mtime:
            return ("skipped", txt_path)

    try:
        # -layout preserves spacing; -nopgbrk removes page break chars
        result = subprocess.run(
            ["pdftotext", "-layout", "-nopgbrk", str(pdf_path), str(txt_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            print(f"  ! pdftotext failed for {pdf_path.name}: {result.stderr.strip()}",
                  file=sys.stderr)
            return ("failed", None)
        return ("converted", txt_path)
    except Exception as e:
        print(f"  ! Exception converting {pdf_path.name}: {e}", file=sys.stderr)
        return ("failed", None)


def find_pdfs(search_dirs: List[Path]) -> List[Path]:
    """Find all PDFs under the given directories."""
    pdfs = []
    for d in search_dirs:
        if not d.exists():
            continue
        pdfs.extend(sorted(d.rglob("*.pdf")))
    return pdfs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true",
                        help="Re-convert even if .txt already exists")
    parser.add_argument("--dir", type=Path,
                        help="Convert only PDFs under this directory")
    args = parser.parse_args()

    if not check_pdftotext():
        sys.exit(1)

    search_dirs = [args.dir] if args.dir else DEFAULT_SEARCH_DIRS
    pdfs = find_pdfs(search_dirs)

    if not pdfs:
        print("No PDFs found.")
        return

    print(f"Found {len(pdfs)} PDF(s). Starting conversion...")
    print()

    counts = {"converted": 0, "skipped": 0, "failed": 0}
    for pdf in pdfs:
        rel = pdf.relative_to(VAULT_ROOT)
        status, _ = convert_pdf(pdf, force=args.force)
        counts[status] += 1
        symbol = {"converted": "✓", "skipped": "-", "failed": "✗"}[status]
        print(f"  {symbol} {rel}")

    print()
    print(f"Done. Converted: {counts['converted']}, "
          f"Skipped: {counts['skipped']}, Failed: {counts['failed']}")


if __name__ == "__main__":
    main()
