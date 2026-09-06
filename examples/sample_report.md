# AI-pattern 审查报告：sample_paper.md

聚焦审查（S1、S13；全文作者正文） · 2026-09-06 · 规则版本 2

## 审查元数据

| 项目 | 内容 |
|---|---|
| 输入格式 | Markdown |
| 作者模型 | 作者模型不足；不使用个人偏好定罪 |
| 联网状态 | 未联网，仅审查 S1/S13 稿内论证功能 |
| 提取警告 | 参考文献与标题不进入形式扫描；本例为虚构教学稿件 |

## 执行摘要

脚本候选 8 条，语义补充 0 条，逐条裁决 8 条。通读已检查 S1 和 S13；其他规则未审查。
四条候选受保护，一条待作者判断，三条需修改合并为两个 finding。同一未来展望问题同时涉及 S1/S13，只展开一次。
本例展示范围披露和账本对应，不声称完整论文审查，也不证明 AI 来源。

## S1–S16 覆盖表

| 规则 | 状态 | 候选数 | 逐条裁决 |
|---|---|---:|---:|
| S1 列表堆叠 | 已审查 | 6 | 6 |
| S2 范围外 | 未审查 | 0 | 0 |
| S3 范围外 | 未审查 | 0 | 0 |
| S4 范围外 | 未审查 | 0 | 0 |
| S5 范围外 | 未审查 | 0 | 0 |
| S6 范围外 | 未审查 | 0 | 0 |
| S7 范围外 | 未审查 | 0 | 0 |
| S8 范围外 | 未审查 | 0 | 0 |
| S9 范围外 | 未审查 | 0 | 0 |
| S10 范围外 | 未审查 | 0 | 0 |
| S11 范围外 | 未审查 | 0 | 0 |
| S12 范围外 | 未审查 | 0 | 0 |
| S13 模板支架 | 已审查 | 2 | 2 |
| S14 范围外 | 未审查 | 0 | 0 |
| S15 范围外 | 未审查 | 0 | 0 |
| S16 范围外 | 未审查 | 0 | 0 |

## 行动清单

| ID | 症状 | 裁决 | 位置 | 处理方向 |
|---|---|---|---|---|
| AP-S01-001 | 未区分的并列能力与 gap | 需修改 | markdown-p0007 | 说明四个动作的区别及其与研究缺口的关系；确认冗余后再删。 |
| AP-S13-001 | 后续措施缺少本文依据 | 需修改 | markdown-p0021 | 将后续措施对应到本文的具体生态效度限制；不要补造新实验。 |

## 发现

### AP-S01-001

**类别**：AI 模式（可观察的论证缺口，不判断生成来源）

**位置**：markdown-p0007

**触发片段**：

> However, existing research exhibits a critical gap: multimodal interfaces can organize, coordinate, prioritize, and optimize concurrent feedback channels.

**裁决**：需修改

**理由**：四个能力动词没有分别界定，且只陈述“能做什么”，没有交代为何构成 critical gap。

**保护测试**：正文未把这些动作定义为四个实验条件或测量；需要补充其论证关系。不能据此认定哪三个动作可删。

**处理方向**：说明四个动作的区别及其与研究缺口的关系；确认冗余后再删。

**交叉规则**：无；本次未审查 S3 等其他规则。

**账本**：S1-f6ca695a5eb9

### AP-S13-001

**类别**：AI 模式（未来计划依据不足）

**位置**：markdown-p0021

**触发片段**：

> Future research should combine multiple interactive paradigms, eye tracking, neuroimaging, and diverse demographic cohorts to examine ecological validity.

**裁决**：需修改

**理由**：生态效度是明确目标，但四项措施没有分别对应本文哪一种效度限制，无法评估选择依据。

**保护测试**：未来计划允许列举多项方法；问题是缺少对应关系，不是四项结构或 future research 词组。

**处理方向**：将后续措施对应到本文的具体生态效度限制；不要补造新实验。

**交叉规则**：S1

**账本**：S1-2a267de05974、S13-9573b498b26a

## 受保护与未触发模式

四组反馈条件和 ANOVA 的因素列表保留；反馈模态清单与明确指定对象的选题开头保留。三条选题理由是否可删仍待作者判断，见账本。

## 外部证据

未联网（裁决仅依赖稿内证据）。没有验证虚构示例中的文献，不声称它们存在或支持相关主张。

## 限制

只审 S1/S13，未检查其他规则、事实、引用真实性和方法学风险。本例不提供候选改法：原文没有足够依据支持具体新机制或新研究设计。自动检查仅证明格式、溯源与账本一致，理由质量仍需作者复核。

## 源文件校验

- 源文件：sample_paper.md
- SHA-256：`992b4410a46eae09454a0dfd778ad66095807846c34399b3bd8ad389be58d644`
- 原始候选：[sample_candidates.json](sample_candidates.json)
- 裁决账：[sample_ledger.json](sample_ledger.json)

从 skill 根目录重跑（提取 JSON 放临时目录；候选输出使用新的临时路径，不覆盖演示文件）：

```bash
python scripts/extract_document.py examples/sample_paper.md --output <tmp>/extract.json
python scripts/scan_all_candidates.py <tmp>/extract.json --rules S1 S13 --output <tmp>/candidates.json
python scripts/validate_report.py examples/sample_report.md <tmp>/extract.json --source examples/sample_paper.md --candidates <tmp>/candidates.json --ledger examples/sample_ledger.json
```
