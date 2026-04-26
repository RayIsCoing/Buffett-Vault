# Buffett Perspective — Claude Code Skill

以巴菲特 70 年投资哲学为基底的分析系统。不是语录机器，而是一个能检索原文、结合实时数据、给出明确投资判断的完整认知框架。

## 数据来源

- 49 封股东信 (1977-2025) 全文
- 7 封合伙人信 (1957-1976)
- 35 场年会问答记录 (1985-2025)
- 39 篇 CNBC 采访实录
- 49 份季度 13F 持仓 CSV (2013Q4-2025Q4)
- 经典演讲、文章、播客访谈
- 结构化笔记：132 家公司持仓历史、被拒投资案例、哲学演变时间线

## 安装

```bash
# 克隆到 Claude Code skills 目录
git clone https://github.com/RayIsCoing/Buffett-Vault.git ~/.claude/skills/buffett-perspective
```

## 使用

在任意 Claude Code 会话中，以下触发词会自动激活此 Skill：

- `buffett` / `巴菲特` / `warren` / `berkshire`
- `价值投资` / `value investing`
- `buffett mode` / `ask warren` / `buffett perspective`

### 示例

```
以巴菲特的视角分析英伟达
巴菲特怎么看当前的AI泡沫？
用价值投资框架评估腾讯
```

## 工作流程

1. **实时搜索** — 先搜目标公司最新财报、新闻、股价
2. **Vault 检索** — Grep 搜索股东信/年会记录中的历史观点和类比案例
3. **六步分析引擎** — 能力圈 → 护城河 → 管理层 → 所有者收益 → 安全边际 → 行动建议
4. **明确判定** — Strong Buy / Buy / Accumulate on Weakness / Watch / Avoid

## 关于 PDF

原版 PDF 未包含在 repo 中（已提取为 .txt）。如需 PDF 原件，股东信可从 [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html) 下载。

## License

SKILL.md 和结构化笔记为原创内容，MIT License。
股东信、年会记录等原文版权属于 Berkshire Hathaway / 原始来源。
