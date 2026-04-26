# Buffett Perspective

中文 | **[English](README.md)**

基于巴菲特 70 年投资哲学的 AI 分析系统。不是语录机器，而是一个能检索原文、结合实时数据、给出明确投资判断的完整认知框架。

## 它能做什么

你问任何一家公司，Agent 会：

1. **搜实时数据** — 最新财报、新闻、股价
2. **搜 Vault 原文** — 49 封股东信、35 场年会记录、68 篇采访、49 份季度 13F 持仓
3. **跑六步分析** — 能力圈 → 护城河 → 管理层 → 所有者收益 → 安全边际 → 行动判定
4. **给出明确建议** — Strong Buy / Buy / Accumulate on Weakness / Watch / Avoid

每次分析必须引用具体的 Vault 来源。没有引用 = 无效输出。

## 安装

**一行命令（自动检测平台）：**

```bash
curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash
```

**或者让你的 Agent 自己装：**

> 帮我安装这个 Skill：https://github.com/RayIsCoing/Buffett-Vault
>
> 安装方法：运行 `curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash`

<details>
<summary>手动安装（按平台）</summary>

| 平台 | 命令 |
|------|------|
| Claude Code | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.claude/skills/buffett-perspective` |
| Codex CLI | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.agents/skills/buffett-perspective` |
| OpenClaw | `git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.openclaw/workspace/skills/buffett-perspective` |
| Cursor | `git clone https://github.com/RayIsCoing/Buffett-Vault.git .cursor/skills/buffett-perspective` 然后在 Rules for AI 中引用 |

</details>

## 试试看

```
以巴菲特的视角分析英伟达
巴菲特怎么看当前的AI泡沫？
用价值投资框架评估腾讯
Costco 在今天的价格算不算好生意？
```

## 数据来源

| 来源 | 数量 | 覆盖范围 |
|------|------|----------|
| 股东信 | 49 封 | 1977–2025 |
| 合伙人信 | 7 封 | 1957–1976 |
| 年会问答记录 | 35 场 | 1985–2025 |
| CNBC 采访 | 39 篇 | 2008–2026 |
| 播客访谈 | 26 篇 | 各年份 |
| 13F 季度持仓 | 49 份 | 2013 Q4–2025 Q4 |
| 结构化笔记 | 4 篇 | 持仓历史、被拒投资、哲学演变 |

所有文件均为纯文本（.txt / .csv / .md），Agent 可通过 Grep/Read 工具直接检索。

## 工作原理

```
用户提问 → 实时搜索 → Vault 检索 → 六步分析 → 带来源的判定
```

Agent 读取 `SKILL.md`（巴菲特人格、认知框架、反拒绝规则）和对应平台的操作手册（Claude Code 读 `CLAUDE.md`，Codex/OpenClaw 读 `AGENTS.md`）。`INDEX.md` 提供主题→文件映射，让 Agent 精准定位搜索目标。

| 文件 | 读者 | 作用 |
|------|------|------|
| `SKILL.md` | 所有 Agent | 巴菲特人格 prompt：声音、框架、六步引擎、案例库 |
| `CLAUDE.md` | Claude Code | 操作手册（中文）：工作流、检索方法、输出格式 |
| `AGENTS.md` | Codex / OpenClaw / Cursor | 操作手册（英文）：同上，适配 AGENTS.md 协议 |
| `INDEX.md` | 所有 Agent | 主题→文件搜索地图，消除猜测 |

## 触发词

在支持 Skill 触发的平台（Claude Code、Codex、OpenClaw）中：

`buffett` · `巴菲特` · `warren buffett` · `berkshire` · `伯克希尔` · `价值投资` · `value investing` · `护城河` · `moat analysis` · `股东信` · `buffett mode` · `ask warren` · `buffett perspective`

## 关于 PDF

原版 PDF 未包含在仓库中（已提取为 .txt）。如需 PDF 原件，股东信可从 [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html) 下载。

## 许可证

`SKILL.md`、`CLAUDE.md`、`AGENTS.md` 和 `Notes/` 目录下的结构化笔记为原创内容，MIT License。
股东信、年会记录、采访实录等原文版权属于 Berkshire Hathaway / 原始来源方。
