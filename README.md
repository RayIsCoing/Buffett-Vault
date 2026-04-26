# Buffett Perspective

以巴菲特 70 年投资哲学为基底的 AI 分析系统。不是语录机器，而是一个能检索原文、结合实时数据、给出明确投资判断的完整认知框架。

An AI investment analysis system built on Warren Buffett's 70 years of investment philosophy. Not a quote machine — a complete cognitive framework that searches primary sources, combines real-time data, and delivers clear investment verdicts.

---

## 安装 / Installation

### 一行安装（自动检测平台）

```bash
curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash
```

脚本自动检测你安装了哪些 Agent（Claude Code / Codex / OpenClaw），clone 到对应目录。已安装则自动更新。

### 或者让你的 Agent 自己安装

直接对你的 Agent 说：

> 帮我安装这个 Skill：https://github.com/RayIsCoing/Buffett-Vault
>
> 安装方法：运行 `curl -sSL https://raw.githubusercontent.com/RayIsCoing/Buffett-Vault/master/install.sh | bash`

### 手动安装（按平台）

<details>
<summary>点击展开各平台命令</summary>

**Claude Code (Anthropic)**

```bash
git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.claude/skills/buffett-perspective
```

Agent 读取 `SKILL.md`（人格 prompt）+ `CLAUDE.md`（操作手册）。

**Codex CLI (OpenAI)**

```bash
git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.agents/skills/buffett-perspective
```

Agent 读取 `SKILL.md`（人格 prompt）+ `AGENTS.md`（操作手册）。

**OpenClaw**

```bash
git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.openclaw/workspace/skills/buffett-perspective
```

Agent 读取 `SKILL.md`（人格 prompt）+ `AGENTS.md`（操作手册）。

**Cursor**

```bash
git clone https://github.com/RayIsCoing/Buffett-Vault.git .cursor/skills/buffett-perspective
```

在 Cursor Settings > Rules for AI 中添加：

```
Read and follow instructions in .cursor/skills/buffett-perspective/AGENTS.md and .cursor/skills/buffett-perspective/SKILL.md
```

**其他 Agent**

本项目兼容任何能读取 Markdown 指令文件的 AI agent。将 repo clone 到 agent 可访问的路径，然后在 agent 的指令配置中引用 `SKILL.md` 和 `AGENTS.md`。

</details>

---

## 文件说明 / File Guide

| 文件 | 读者 | 作用 |
|------|------|------|
| `SKILL.md` | 所有 Agent | 巴菲特人格 prompt：声音、框架、六步分析引擎、历史案例、反拒绝规则 |
| `CLAUDE.md` | Claude Code | Agent 操作手册（中文）：工作流、检索方法、路径约定、输出格式 |
| `AGENTS.md` | Codex / OpenClaw / Cursor / 其他 | Agent 操作手册（英文）：同 CLAUDE.md 内容，适配 AGENTS.md 协议 |
| `README.md` | 人类用户 | 你正在读的这个文件 |

---

## 数据来源 / Data Sources

| 类型 | 数量 | 格式 | 路径 |
|------|------|------|------|
| 股东信 Shareholder Letters | 49 封 (1977-2025) | .txt | `Attachments/shareholder-letters/` |
| 合伙人信 Partnership Letters | 7 封 (1957-1976) | .txt | `Attachments/partnership-letters/` |
| 年会问答 Annual Meetings | 35 场 (1985-2025) | .txt | `Attachments/annual-meetings/` |
| CNBC 采访 | 39 篇 (2008-2026) | .txt | `Attachments/interviews/cnbc/` |
| 播客访谈 Podcasts | 26 篇 | .txt | `Attachments/interviews/podcasts/` |
| 其他访谈 Other Interviews | 3 篇 | .txt | `Attachments/interviews/other/` |
| 经典演讲 Speeches | 1 篇 | .txt | `Attachments/speeches/` |
| 13F 季度持仓 SEC Filings | 49 份 (2013Q4-2025Q4) | .csv | `Attachments/sec-filings/` |
| 结构化笔记 Notes | 4 篇 | .md | `Notes/` |
| 投资主题 Topics | 5 篇 | .md | `Topics/` |
| 人物档案 People | 3 篇 | .md | `People/` |

所有 .txt / .csv / .md 文件均可被 Agent 通过 Grep/Read 工具直接检索。

---

## 触发词 / Triggers

在支持 skill trigger 的平台（Claude Code、Codex、OpenClaw）中，以下关键词自动激活此 Skill：

`buffett` · `巴菲特` · `warren buffett` · `berkshire` · `伯克希尔` · `价值投资` · `value investing` · `护城河` · `moat analysis` · `股东信` · `buffett mode` · `ask warren` · `buffett perspective`

---

## 工作流程 / Workflow

```
用户提问 → 实时搜索（财报/新闻/股价）→ Vault 检索（股东信/年会/持仓）→ 六步分析 → 明确判定
```

1. **实时搜索** — 先搜目标公司最新财报、新闻、股价
2. **Vault 检索** — Grep 搜索股东信/年会记录中的历史观点和类比案例
3. **六步分析引擎** — 能力圈 → 护城河 → 管理层 → 所有者收益 → 安全边际 → 行动建议
4. **明确判定** — 五档之一：

| 判定 | 含义 |
|------|------|
| **Strong Buy** | 优秀企业 + 合理价格，重仓 |
| **Buy** | 好企业 + 合理价格，建仓 |
| **Accumulate on Weakness** | 优秀企业但价格偏高，回调时买入 |
| **Watch** | 有意思但待确认，需注明等什么催化剂 |
| **Avoid** | 业务有根本性问题 |

---

## 示例 / Examples

```
以巴菲特的视角分析英伟达
巴菲特怎么看当前的AI泡沫？
用价值投资框架评估腾讯
Analyze NVIDIA from Buffett's perspective
What would Buffett think about the current AI bubble?
```

---

## 关于 PDF / About PDFs

原版 PDF 未包含在 repo 中（已提取为 .txt）。如需 PDF 原件，股东信可从 [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html) 下载。

---

## License

`SKILL.md`、`CLAUDE.md`、`AGENTS.md` 和 `Notes/` 目录下的结构化笔记为原创内容，MIT License。
股东信、年会记录、采访实录等原文版权属于 Berkshire Hathaway / 原始来源方。
