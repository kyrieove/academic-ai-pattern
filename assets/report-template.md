# AI-pattern 审查报告：{{SOURCE_NAME}}

{{AUDIT_MODE}} · {{AUDIT_TIME}} · 规则版本 {{RULE_VERSION}}

## 审查元数据

| 项目 | 内容 |
|---|---|
| 输入格式 | {{INPUT_FORMAT}} |
| 作者模型 | {{AUTHOR_MODEL}} |
| 联网状态 | {{RESEARCH_STATUS}} |
| 提取警告 | {{EXTRACTION_WARNINGS}} |

## 执行摘要

{{EXECUTIVE_SUMMARY}}

## S1–S16 覆盖表

| 规则 | 状态 | 候选数 | 逐条裁决 |
|---|---|---:|---:|
| S1 连续动词组／列表堆叠 | {{STATUS}} | 0 | 0 |
| S2 理由枚举式 | {{STATUS}} | 0 | 0 |
| S3 抽象到不知所言 | {{STATUS}} | 0 | 0 |
| S4 冒号＋展开 | {{STATUS}} | 0 | 0 |
| S5 指代滥用 that | {{STATUS}} | 0 | 0 |
| S6 表述／功能槽重复 | {{STATUS}} | 0 | 0 |
| S7 衔接断裂 | {{STATUS}} | 0 | 0 |
| S8 评价式句子 | {{STATUS}} | 0 | 0 |
| S9 无根据的对立／幽灵反驳 | {{STATUS}} | 0 | 0 |
| S10 术语身份漂移 | {{STATUS}} | 0 | 0 |
| S11 认识强度失配 | {{STATUS}} | 0 | 0 |
| S12 模糊归因／引用堆叠 | {{STATUS}} | 0 | 0 |
| S13 模板支架 | {{STATUS}} | 0 | 0 |
| S14 造作比喻 | {{STATUS}} | 0 | 0 |
| S15 修辞问句／自问自答 | {{STATUS}} | 0 | 0 |
| S16 机械导航／元话语 | {{STATUS}} | 0 | 0 |

## 行动清单

全部 finding，含 `待作者判断` 与 `核查未完成`。行数等于展开的 finding 数。

| ID | 症状 | 裁决 | 位置 | 处理方向 |
|---|---|---|---|---|
{{ACTION_ROWS}}

## 发现

{{FINDINGS_OR_NONE}}

## 受保护与未触发模式

{{PROTECTED_AND_CLEAR_PATTERNS}}

## 外部证据

{{EVIDENCE_OR_LOCAL_ONLY_NOTE}}

## 限制

{{LIMITATIONS}}

## 源文件校验

| 项目 | 内容 |
|---|---|
| 源文件 | {{SOURCE_NAME}} |
| SHA-256 | `{{SOURCE_SHA256}}` |
| 裁决账 | {{LEDGER_NAME}} |
