#!/bin/bash
# Buffett Perspective Skill — Auto-Install
# Detects your AI agent platform and installs to the correct directory.
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash

set -e

REPO="https://github.com/RayIsCoing/Buffett-Vault.git"
NAME="buffett-perspective"
INSTALLED=0

echo "🎩 Buffett Perspective Skill Installer"
echo "======================================="
echo ""

# Claude Code
if [ -d "$HOME/.claude" ]; then
    TARGET="$HOME/.claude/skills/$NAME"
    if [ -d "$TARGET" ]; then
        echo "✅ Claude Code: already installed at $TARGET (pulling latest...)"
        git -C "$TARGET" pull --ff-only 2>/dev/null || echo "   ⚠️  Pull failed, skipping update"
    else
        echo "📦 Claude Code detected → installing to $TARGET"
        mkdir -p "$HOME/.claude/skills"
        git clone "$REPO" "$TARGET"
    fi
    INSTALLED=1
fi

# Codex CLI
if [ -d "$HOME/.agents" ] || command -v codex &>/dev/null; then
    TARGET="$HOME/.agents/skills/$NAME"
    if [ -d "$TARGET" ]; then
        echo "✅ Codex CLI: already installed at $TARGET (pulling latest...)"
        git -C "$TARGET" pull --ff-only 2>/dev/null || echo "   ⚠️  Pull failed, skipping update"
    else
        echo "📦 Codex CLI detected → installing to $TARGET"
        mkdir -p "$HOME/.agents/skills"
        git clone "$REPO" "$TARGET"
    fi
    INSTALLED=1
fi

# OpenClaw
if [ -d "$HOME/.openclaw" ] || command -v openclaw &>/dev/null; then
    TARGET="$HOME/.openclaw/workspace/skills/$NAME"
    if [ -d "$TARGET" ]; then
        echo "✅ OpenClaw: already installed at $TARGET (pulling latest...)"
        git -C "$TARGET" pull --ff-only 2>/dev/null || echo "   ⚠️  Pull failed, skipping update"
    else
        echo "📦 OpenClaw detected → installing to $TARGET"
        mkdir -p "$HOME/.openclaw/workspace/skills"
        git clone "$REPO" "$TARGET"
    fi
    INSTALLED=1
fi

# Nothing detected — install to Claude Code by default
if [ $INSTALLED -eq 0 ]; then
    echo "⚠️  No known agent detected. Installing to Claude Code default path..."
    TARGET="$HOME/.claude/skills/$NAME"
    mkdir -p "$HOME/.claude/skills"
    git clone "$REPO" "$TARGET"
    echo ""
    echo "Installed to: $TARGET"
    echo "If you use a different agent, move or symlink this directory:"
    echo "  Codex:    ln -s $TARGET ~/.agents/skills/$NAME"
    echo "  OpenClaw: ln -s $TARGET ~/.openclaw/workspace/skills/$NAME"
    INSTALLED=1
fi

echo ""
echo "✅ Done! Restart your agent and try:"
echo '   "以巴菲特的视角分析英伟达"'
echo '   "Analyze NVIDIA from Buffett'\''s perspective"'
