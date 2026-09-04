# 吸收 writing-dna-skill：改动方案（交给 Codex 执行）

目标仓库：`C:\Users\ASUS\Dropbox\metaphor_production\academic-ai-pattern`

**执行原则**：外科手术式改动。只动下列指定位置，不重排、不润色、不改动未提到的任何内容。每处都给出了精确锚点字符串，按锚点定位后插入或替换。

涉及文件：`SKILL.md`、`references/quick-rules.md`、`references/report-schema.md`、`scripts/validate_report.py`、`ai_pattern.md`

---

## 改动 1 — SKILL.md：给候选改法加守恒约束

**文件**：`SKILL.md`
**操作**：替换单行

锚点（Hard boundary 一节的最后一条）：

```
- **改法分离**：`需修改` 可附一个单独标记的英文候选改法；报告本身绝不修改源稿。
```

替换为：

```
- **改法分离**：`需修改` 可附一个单独标记的英文候选改法；报告本身绝不修改源稿。候选改法受信息守恒约束：每个实词都要能在原文指出出处，不得新增人名、数字、日期、来源或因果，不得删除原有限定词与让步。
```

---

## 改动 2 — quick-rules.md：新增「候选改法守恒」一节

**文件**：`references/quick-rules.md`
**操作**：在 `## 三类发现必须分开` 这一行**之前**插入新的一节（即紧接「**同一条理由不能覆盖多条候选。** 一条通用理由判 N 条，等于一条都没判。」之后，前后各留一个空行）

插入内容：

```markdown
## 候选改法守恒

候选改法是本 skill 唯一产出新文本的地方，"源稿只读"的边界保护不到它。

**每个实词都要能在触发片段或其所在区块里指出出处。** 指不出来就是新增，必须撤销或退回概括表述。

**一律不得新增**：人名、机构、地名、数字、比例、单位、样本量、日期、时间顺序、引语、引用来源、因果或动机。原文写 `improved performance`，不得改成 `improved accuracy by 12%`——哪怕 12% 出现在别的段落。

**一律不得删除**：限定词与让步（`may`、`might`、`could`、`suggest`、`appear`、`likely`、`in some cases`、`under these conditions`）、条件从句、范围限定、证据等级标记。把 `may improve` 改成 `improves` 是篡改认识强度，不是去 AI 模式。

**S11 是唯一例外**：S11 的裁决对象本来就是强度失配，改法可以上调或下调强度，但必须在 `**守恒核对**` 里写明依据稿内哪一句证据，不得默认删除对冲。

**每条带候选改法的 finding 必须写 `**守恒核对**` 字段**：一句话说明改法保持了哪些对象、方向、数量、范围、来源和证据等级；改动其中任何一项时写明依据。
```

---

## 改动 3 — quick-rules.md：惯例查询补选取算法

**文件**：`references/quick-rules.md`
**操作**：在「惯例查询：先查本地语料」一节内插入

锚点（该节三个判据的最后一条）：

```
- **同体裁文献里作为常规表述反复出现** → 受保护。判"常规"要点开几篇看上下文，确认是同一个意思，不是同形不同义。
```

在该行**之后**插入（留一个空行）：

```markdown
**"点开几篇"的选取方法**——不按这个选，就等于没查：

1. 按 **section（Introduction／Methods／Results／Discussion）＋ 研究设计（实验／观察／综述／meta）** 筛出同类文献；
2. 匹配项超过 5 篇时，取近 5 年、期刊层级与目标期刊相当的 5 篇；
3. 匹配项不足 5 篇时，用同 section 不同主题的文献补齐到 5 篇，并在报告的「外部证据」里写明补齐来源；
4. 读的目的不是数命中，是确认这 5 篇里该表述承担的是同一个语义功能。说不出这 5 篇的共同用法，记 `核查未完成`，不得记 `受保护`。
```

---

## 改动 4 — report-schema.md：候选改法与守恒核对进入 finding 模板

**文件**：`references/report-schema.md`

### 4a. 模板内加两个字段

锚点（「快速模式 finding」代码块内）：

```
**处理方向**：给出最小充分动作，不直接改稿。

**交叉规则**：S11（如无则写“无”）
```

替换为：

```
**处理方向**：给出最小充分动作，不直接改稿。

**候选改法**：仅 `需修改` 可附，保留英文；不附时省略本字段。

**守恒核对**：附 `候选改法` 时必填。说明改法保持了哪些对象、方向、数量、范围、来源和证据等级；改动任一项时写明依据。

**交叉规则**：S11（如无则写“无”）
```

### 4b. 替换候选改法的说明句

锚点：

```
只有 `需修改` 可附一个 `**候选改法**`，并说明它保持了哪些对象、方向、数量、范围、来源和证据等级。其他裁决不给完整改写。
```

替换为：

```
只有 `需修改` 可附一个 `**候选改法**`，其他裁决不给完整改写。附候选改法时必须同时写 `**守恒核对**`。守恒规则见 quick-rules.md「候选改法守恒」：候选改法中的每个实词都要能在触发片段或其所在区块指出出处，不得新增人名、数字、日期、来源或因果，不得删除原有限定词与让步（S11 除外，且须写明依据）。
```

### 4c. 「禁止项与终检」补反向条目

锚点（整节）：

```
- 不给 AI 概率、检测器分数、总分或通过阈值；
- 不虚构事实、数字、例子、文献或作者意图；
- 不把个人偏好伪装成通用错误；
- 不在任何必需步骤未完成时声称完整覆盖。

交付前运行 `scripts/validate_report.py`，核对章节、S1–S16 行、ID、裁决、区块 ID、引文和源文件 hash。
```

替换为：

```
- 不给 AI 概率、检测器分数、总分或通过阈值；
- 不虚构事实、数字、例子、文献或作者意图；
- 不把个人偏好伪装成通用错误；
- 不在任何必需步骤未完成时声称完整覆盖。

以下是反向终检，防的是改过头，逐项复查：

- 有没有只凭形式命中就定罪的 finding？保护测试必须写出这一句删掉后丢失的具体内容，写不出就降为 `待作者判断`；
- 有没有用同一条通用理由覆盖多个裁决单元？
- 候选改法里有没有触发片段和所在区块都找不到的实词、数字、日期或来源？
- 候选改法里有没有删掉原文的限定词、让步或范围限定？（S11 除外，且须在守恒核对写明依据）
- 有没有为"节奏""参差度""句长分布"建立 finding 或提出改法？句长离散度不是判据；
- 有没有把被动语态、名词化、长句、三项并列或句内同构排比本身当作 finding 依据？

交付前运行 `scripts/validate_report.py`，核对章节、S1–S16 行、ID、裁决、区块 ID、引文、候选改法守恒和源文件 hash。
```

---

## 改动 5 — validate_report.py：两条机器检查

**文件**：`scripts/validate_report.py`
**操作**：三处插入／替换，不改动其他逻辑

### 5a. 守恒核对字段的条件必填

锚点（第一个 finding 循环内，verdict 校验）：

```python
        verdict_match = re.search(r"\*\*裁决\*\*：\s*(\S+)", chunk)
        if not verdict_match or verdict_match.group(1) not in VERDICTS:
            fail(errors, f"{finding_id}: invalid verdict")
```

在该 `if` 块**之后**插入（同一缩进层级，仍在 `for chunk in finding_chunks:` 循环体内）：

```python
        # A rewrite is the only new text this tool emits; it needs its own audit line.
        if "**候选改法**" in chunk and "**守恒核对**" not in chunk:
            fail(errors, f"{finding_id}: 候选改法 present without 守恒核对")
```

### 5b. 候选改法不得引入原文没有的数字

锚点（第二个 finding 循环，此处已持有 `positions` 和 `known_blocks`）：

```python
        for quote in quotes:
            normalized = quote.rstrip()
            if not any(normalized in known_blocks.get(block_id, "") for block_id in positions):
                fail(errors, f"{finding_id}: quote not found in its referenced blocks: {normalized[:80]}")
```

在该 `for quote in quotes:` 块**之后**插入（同一缩进层级）：

```python
        # Numbers are the cheapest thing to fabricate and the most expensive to miss.
        rewrite = re.search(r"(?m)^\*\*候选改法\*\*：(.*?)(?=\n\*\*|\Z)", chunk, re.S)
        if rewrite:
            source_text = " ".join(known_blocks.get(block_id, "") for block_id in positions)
            for number in sorted(set(re.findall(r"\d+(?:\.\d+)?", rewrite.group(1)))):
                if number not in source_text:
                    fail(errors, f"{finding_id}: 候选改法 introduces number absent from its blocks: {number}")
```

**说明**：数字检查是字面匹配。改法把 `0.05` 写成 `5%` 会被拦下——这是有意的，改写不得替作者换算；确需换算时把原文写法保留在改法里。

### 5c. 输出加一个计数，便于确认闸门生效

锚点：

```python
    result = {
        "ok": not errors,
        "findings": len(ids),
        "quoted_fragments": len(re.findall(r"(?m)^> ", report)),
        "errors": errors,
    }
```

替换为：

```python
    result = {
        "ok": not errors,
        "findings": len(ids),
        "rewrites": report.count("**候选改法**"),
        "quoted_fragments": len(re.findall(r"(?m)^> ", report)),
        "errors": errors,
    }
```

---

## 改动 6 — ai_pattern.md §7：新增「方向存疑」子表

**文件**：`ai_pattern.md`
**操作**：在 §7 末尾插入一个子节

锚点（§7 结尾的禁用做法段落，其后是一行 `---`）：

```
以下方法明确禁用：故意加入语法错误或碎片句、随机替换同义词、按固定句长制造 burstiness、
按主观商业检测器分数设通过线、强行改变作者语域、为了通过检测器而改事实、承诺“无法被 AI 检测”。
这些方法优化的是表面统计或个人偏好，不是文章。
```

在该段落**之后**、`---` 之前插入：

```markdown
### 方向存疑：可能反向的信号（尚未在英文学术语料验证）

上表每条的处置是"不作为单独信号"。下面这一类不同：在中文非虚构语料（300 篇、5 个模型、约 118 万字）的实测里，**人类作者用得比模型更多**。删改这类特征不是降 AI 感，是把稿件推向更像模型输出的方向。

| 特征 | 中文语料方向 | 本手册处置 |
|---|---|---|
| 反复重复同一名词全称、少用代词 | 人类多于 AI | 名词复现本身不构成 S6，S6 要成立须是同一功能槽反复调用；术语复现另受 S10 的一致性要求保护 |
| 比喻本身、比喻独立成段 | 人类约为 AI 的 2.4 倍 | S14 只处理抽象物被赋予戏剧动作的喻体，不得扩大到比喻本身 |
| 正文问句、设问 | 人类远多于 AI | S15 只处理临时提问后自己回答，不得扩大到研究问题与标题回扣 |
| 句内同构排比（`faster, cheaper, and more robust`） | 人类不少于 AI | 不得作为 S1 依据；S1 只管多项不形成取舍的堆叠 |
| 句长与段长的离散度不足 | 无差异 | 不得为"制造节奏"改写，也不得据此建立 finding |

**这些数字来自中文自媒体语料，不能直接迁移到英文实证论文。** 在英文学术语料上重测之前，本子表只承担一个作用：禁止把这五类特征单独作为 finding 依据。测出英文方向后再决定是升级为规则、还是并入上面的假信号表。

来源：`writing-dna-skill` / `lieflat-less-ai-tone`（研究仓库 https://github.com/larashero3-dotcom/lieflat-less-ai-tone）。
```

---

## 不要做的事

- 不要把 lieflat 的中文规则（破折号、顿号罗列、序数词小标题、翻译腔五式、"说白了"起手式）搬进 S1–S16。语言和体裁都不匹配。
- 不要把任何中文语料的频率数字（`x.xx/千字`）写成本手册的判定门槛。改动 6 里的数字只出现在明确标注来源的子表内。
- 不要给本 skill 增加"直接改写稿件"的能力。源稿只读是设计边界。
- 不要新增 S17 及以后的条目。新现象先走 §1「新增症状的门槛」的三步。
- 不要动 `scan_all_candidates.py`、`extract_document.py`、`slice_author_prose.py`、`next_report_path.py`。
- 不要改动 README、README_zh、examples 或已有报告样例。

---

## 验收

改完依次跑：

```bash
cd "C:/Users/ASUS/Dropbox/metaphor_production/academic-ai-pattern"
python -c "import ast,pathlib; ast.parse(pathlib.Path('scripts/validate_report.py').read_text(encoding='utf-8'))"
python scripts/validate_report.py --help
git diff --stat
```

预期：

1. `validate_report.py` 语法通过，`--help` 正常输出；
2. `git diff --stat` 只列出 5 个文件：`SKILL.md`、`references/quick-rules.md`、`references/report-schema.md`、`scripts/validate_report.py`、`ai_pattern.md`；
3. 逐行看 `git diff`，确认没有任何未在本方案中指定的改动，包括空格、标点和换行的顺手调整。

另需一条端到端验证：造一个最小报告片段，`**候选改法**` 里写一个原文没有的数字，跑 `validate_report.py` 确认报出 `introduces number absent from its blocks`；再补上 `**守恒核对**` 并把数字改回原文写法，确认通过。验证用的临时文件不要提交。

---

## 本轮不做：作者指纹自动蒸馏（另开一轮）

`author_profile.template.yaml` 现在是手填的声明式配置，作者不可能知道自己的 `long_sentence_tolerance` 是多少，所以 C 类指纹实际上永远降级为 `待作者判断`。

writing-dna-skill 的 L1 层（脚本统计句长分布、标点习惯、高频词）正好补这个洞。目标接口：

```bash
python scripts/distill_author_profile.py <作者已发表论文目录> --output author_profile.yaml
```

输入 10–20 篇该作者已发表的 DOCX/PDF，输出填好数值的 `author_profile.yaml`，每个字段附样本量与分布区间。做完之后 C 类从"不可裁决"变成"有语料证据可裁决"，配套改 §11.3 的裁决逻辑：**语料实测的作者习惯与 S1–S16 冲突时以语料为准——那是作者的真实写法，不是 AI 模式**。

新建脚本 + 改 §11.3，工作量半天到一天，不要和上面 6 处文档改动混在一轮里做。
