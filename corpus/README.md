# 语料目录

`/distill` 的输入。目录约定见 `references/distill.md`。

```
corpus/
├── _index.csv          # path 指向章节提取 JSON；其余字段见 distill.md
├── author/raw/         # 作者已发表论文原文
├── author/extract/     # extract_document.py 的输出
├── field/raw/          # 目标期刊同 section 论文原文
├── field/extract/
└── BASELINE.md         # 蒸馏产物，/ai-pattern 条件加载
```

**原文不入库。** `raw/` 与 `extract/` 已在 `.gitignore` 里。已发表论文有版权，不得提交到仓库，也不得上传到第三方服务。

**蒸馏产物里不得出现超过短语级的原文引用。** `BASELINE.md` 与 `DNA/PROFILE.md` 描述写法，不搬内容。
