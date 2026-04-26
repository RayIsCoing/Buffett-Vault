# Buffett Perspective

**[中文版](README.zh-CN.md)** | English

An AI investment analysis skill built on Warren Buffett's 70 years of investment philosophy. Not a quote machine — a complete cognitive framework that searches primary sources, combines real-time data, and delivers clear investment verdicts.

## What It Does

You ask about any company. The agent:

1. **Searches real-time data** — latest earnings, news, stock price
2. **Searches the Vault** — 49 shareholder letters, 35 annual meeting transcripts, 68 interviews, 49 quarterly 13F filings
3. **Runs a 6-step analysis** — circle of competence, moat, management, owner earnings, margin of safety, verdict
4. **Delivers a clear action call** — Strong Buy / Buy / Accumulate on Weakness / Watch / Avoid

Every analysis must cite specific vault sources. No citations = invalid output.

## Install

**One line (auto-detects your platform):**

```bash
curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash
```

**Or tell your agent:**

> Install this skill: https://github.com/RayIsCoing/Buffett-Vault
>
> Run: `curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash`

<details>
<summary>Manual install by platform</summary>

| Platform | Command |
|----------|---------|
| Claude Code | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.claude/skills/buffett-perspective` |
| Codex CLI | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.agents/skills/buffett-perspective` |
| OpenClaw | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.openclaw/workspace/skills/buffett-perspective` |
| Cursor | `git clone https://github.com/RayIsCoing/Buffett-Vault.git .cursor/skills/buffett-perspective` then add to Rules for AI |

</details>

## Try It

```
Analyze NVIDIA from Buffett's perspective
What would Buffett think about the current AI bubble?
Is Costco a wonderful business at today's price?
```

## Data Sources

| Source | Count | Coverage |
|--------|-------|----------|
| Shareholder Letters | 49 | 1977–2025 |
| Partnership Letters | 7 | 1957–1976 |
| Annual Meeting Transcripts | 35 | 1985–2025 |
| CNBC Interviews | 39 | 2008–2026 |
| Podcast Transcripts | 26 | Various |
| 13F SEC Filings (CSV) | 49 | 2013 Q4–2025 Q4 |
| Structured Notes | 4 | Holdings history, rejected investments, philosophy evolution |

All files are plain text (.txt / .csv / .md), searchable by the agent via grep/read tools.

## How It Works

```
User question → Real-time search → Vault retrieval → 6-step analysis → Verdict with sources
```

The agent reads `SKILL.md` (Buffett's persona, cognitive framework, anti-rejection rules) and the platform-specific operating manual (`CLAUDE.md` for Claude Code, `AGENTS.md` for Codex/OpenClaw/others). An `INDEX.md` maps topics to specific files so the agent knows exactly where to search.

| File | Read By | Purpose |
|------|---------|---------|
| `SKILL.md` | All agents | Buffett persona prompt: voice, framework, 6-step engine, case library |
| `CLAUDE.md` | Claude Code | Operating manual (Chinese): workflow, retrieval methods, output format |
| `AGENTS.md` | Codex / OpenClaw / Cursor | Operating manual (English): same content, AGENTS.md protocol |
| `INDEX.md` | All agents | Topic → file search map, eliminates guesswork |

## Triggers

On platforms with skill triggers (Claude Code, Codex, OpenClaw):

`buffett` · `巴菲特` · `warren buffett` · `berkshire` · `伯克希尔` · `value investing` · `价值投资` · `moat analysis` · `护城河` · `股东信` · `buffett mode` · `ask warren` · `buffett perspective`

## About PDFs

Original PDFs are not included (already extracted to .txt). Shareholder letters are available at [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html).

## License

`SKILL.md`, `CLAUDE.md`, `AGENTS.md`, and `Notes/` are original content under MIT License.
Shareholder letters, meeting transcripts, and interview texts are copyrighted by Berkshire Hathaway / original sources.
