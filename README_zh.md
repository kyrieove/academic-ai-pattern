# academic-ai-pattern

<p align="right">
  <a href="README.md"><b>English</b></a> | <b>简体中文</b>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![支持的智能体](https://img.shields.io/badge/Agents-Codex%20%7C%20Claude%20Code%20%7C%20DeepSeek%20%7C%20Antigravity-brightgreen.svg)](#-安装与使用-installation--quickstart)

> **基于证据的非侵入式学术英语 AI 写作模式审计工具。**  
> 专为实证学术论文设计。高召回全量扫描 16 大结构性生成缺陷，深度集成去防御性写作（消除怯懦对冲与免责辩解）；坚持源稿只读输出透明诊断报告，严格保护实验设计、统计事实与学科术语。原生适配 OpenAI Codex、Claude Code、DeepSeek / Harness 与 Google Antigravity。

---

### 🚀 立即安装与调用 (Installation & Quickstart)

在现代 AI Agent 生态（涵盖 Claude Code、Codex、Cursor 等）中，Skill 的行业通用标准安装工具是基于 [skills.sh](https://skills.sh) 的 `npx skills add` 命令，它会自动探测你当前的 Agent 环境并放置到对应的规范路径中。

#### 通用一键安装
```bash
npx skills add kyrieove/academic-ai-pattern
```

---

#### 针对各 Agent 的指定安装命令（按序）：

#### 1. OpenAI Codex
为 Codex 环境指定安装：
```bash
npx skills add kyrieove/academic-ai-pattern --agent codex
```
在 Codex 对话中调用：
```text
使用 $academic-ai-pattern 审查这篇论文 manuscript.docx，生成版本化审查报告。
```

#### 2. Claude Code
直接安装至 Claude Code 的 Skill 目录：
```bash
npx skills add kyrieove/academic-ai-pattern --agent claude-code
```
在 Claude Code 会话中调用：
```text
/academic-ai-pattern 审查 manuscript.docx
```

#### 3. DeepSeek / Harness
一键安装至你的 DeepSeek 工作区或脚手架环境：
```bash
npx skills add kyrieove/academic-ai-pattern
```
并在 Prompt 中指引 DeepSeek 读取 `SKILL.md` 与 `references/quick-rules.md` 执行全流程审计。

#### 4. Google Antigravity
**推荐项目级安装**（在论文项目根目录下运行，选择通用智能体或直接回车，安装至 `.agents/skills/`）：
```bash
npx skills add kyrieove/academic-ai-pattern
```
> 💡 **提示**：Antigravity 原生自动扫描并加载当前工作区根目录的 `.agents/skills/` 目录。若执行全局安装（`-g`），CLI 提示选择智能体时请选择 **Universal / General Agent** 即可。

在 Antigravity 中直接唤起：
```text
调用 $academic-ai-pattern 针对 manuscript.docx 进行学术审查。
```

#### 5. 独立 Python 命令行模式 (免 Node/无 Agent 兜底方案)
如果不使用 Node.js，普通 Python 环境同样可以直接运行底层脚本：
```bash
git clone https://github.com/kyrieove/academic-ai-pattern.git
cd academic-ai-pattern

# 提取与扫描
python scripts/extract_document.py examples/sample_paper.md --output temp_extract.json
python scripts/scan_all_candidates.py temp_extract.json --output temp_candidates.json --markdown temp_ledger.md

# 报告校验
python scripts/validate_report.py examples/sample_report.md temp_extract.json --source examples/sample_paper.md
```

---

### 🎯 痛点与三大铁律

市面上的“降重/去 AI 工具”与商业检测器正在误导学术写作，而大模型（尤其是 Codex、Claude 等）本身又自带严重的生成恶习：
- **同义词盲改毁论文**：机械地将专业术语替换为生僻近义词，破坏概念唯一性，甚至颠倒因果，被审稿人批为 *“poor English and unnatural phrasing”*。
- **概率百分比无法指导修改**：只给一个冷冰冰的“78% AI 生成概率”，却指不出到底是哪一处逻辑缺陷、哪一处语病。
- **误伤学术规范与实证事实**：四组实验条件、Methods 的规范被动句、权威文献的标准叫法，常被当作“机械重复”而惨遭误杀。
- **大模型“防御性写作”让论证卑微怯懦（Defensive Writing）**：AI 为了逃避绝对断言责任，开篇先来一句 *“While this paper does not claim to solve...”* 自我矮化创新；正文层叠堆砌 *“might tentatively suggest that ... could potentially”* 等怯懦犹豫词；频繁花大篇幅解释文章**不是**什么（*“We do not argue that...”* 虚假对立），却迟迟不直陈提出了什么，把宝贵的篇幅浪费在消极免责上，严重削弱论文的学术说服力与期刊录用率。

**我们的铁律：**
1. **源稿只读，绝不篡改（Zero-Tampering）**：只提供证据链体检报告，绝不动你原文一字一句。
2. **形式只能定位，绝不定罪（Mechanism-Driven）**：排比、冒号或转折只作为候选定位线索；定罪必须证明背后的“偷懒生成机制”（M1–M6）。
3. **学术事实最高豁免（Empirical Protection）**：样本组、测量指标、理论争鸣、文献惯例享有免检保护。

> 🛡️ **核心防御哲学：高召回优先，宁可过度预警，绝不放过任何 AI 痕迹（High-Recall Defense）**  
> 为什么我们坚持“宁可误判好的，也绝不漏掉 AI”？  
> 在真正的顶级学术同行评议（SCI/SSCI）中，审稿专家对 AI 痕迹是**“一票信任危机”**。只要正文里漏掉了一两处极其油腻的 AI 腔调（如无据对立 `not X but rather Y`、毫无数据的空洞赞美 `plays a pivotal role`、造作的顶针设问），审稿人就会立刻对全文的原创性、实验严谨度与科研诚信产生断崖式的信任崩塌！  
> 因此，`academic-ai-pattern` 在初筛中坚持**激进的高召回策略（High Recall First）**：宁可把学者精心构思的复杂复合句或个性化表达圈选出来提醒你复核（标记为“⚖️ 待作者判断”），也坚决不为了片面追求虚假的“零误报”而放过哪怕一处潜在的 AI 生成漏洞！最终的修改权与定夺权，100% 牢牢掌握在作者手中。

---

### 🎯 深度整合：识别并破除 AI 的“防御性写作”（Eliminating AI Defensive Writing）

现代大语言模型（尤其是 Codex、Claude 等经过强指令微调与对齐的模型）在润色学术论文时，普遍存在极其严重的**“防御性写作（Defensive Writing）”**生成恶习——由于模型被训练为“避免犯错”和“避免绝对责任”，它们极其喜欢在学术论文中堆砌层层免责与软弱辩解：

- **以自我矮化开篇（Preemptive Disclaimers）**：在汇报创新前先来一句 *“While this paper does not claim to solve...”*，未陈贡献先急于免责；
- **层叠模糊犹豫词（Stacked Modal Hedging）**：一句话里塞满 *“might tentatively suggest that X could potentially influence Y”*，导致论证气势极其怯懦、模糊软弱；
- **消极否定式阐述（Negative Framing）**：频繁花篇幅解释文章**不是**什么（*“We do not argue that...”*），而不是直接正面界定研究**提出**了什么；
- **过早过度堆叠局限性**：还没有拿出核心实证数据，就在摘要或引言开头慌慌张张罗列样本限制。

`academic-ai-pattern` 深度集成了**反防御性写作（Eliminating AI Defensive Writing）**审计逻辑，精准揪出并协助学者破除这种典型的“AI 塑料防卫感”：
1. **破除消极否定（S9 幽灵反驳与虚假对立）**：剔除毫无必要的 *“not X but rather Y”* 辩解框架，引导作者采用“正面界定范围（Positive Scope）”直陈核心主张；
2. **破除怯懦对冲（S11 过度对冲与认识姿态失衡）**：剥除层叠的 *“might / perhaps / potentially”*，让证据定标，以扎实的数据与置信区间说话，而非以卑微的道歉减压；
3. **归位必要精度**：帮助作者将真正的样本约束与实验边界客观归位至 Methods 或 Limitations 章节，恢复引言与讨论的高学术权威感与清晰自信。

---

### 🏛️ 理论基础与审稿规范

本项目脱胎于高水平同行评议实证论文的实际审读与精修实践，建立在科学出版道德规范与大语言模型生成机制分析的基础之上：

- **实证审稿规范底座**：
  - **语义合同与不可动锁定区**：严格遵循学术出版规范（如 APA 第七版、ICMJE 规范），对实测数据、样本规模、量表名称与领域核心术语设立不可篡改的法定保护区。
  - **分布性缺陷与机制级诊断**：超越简单粗暴的禁词表，在篇章与段落维度诊断结构性生成缺陷（如空洞功能槽循环、浅层 payoff 句式、缺乏文献支撑的幽灵对立 `not X but Y`）。
  - **证据等级与主张对齐**：确保论断措辞的认识强度与实验设计严格对齐（杜绝因果倒置，纠正无据外推与过度对冲）。
- **坚守的学术底线**：
  - ❌ **绝不搞欺骗式逃避检测**：拒绝为商业检测器刷分而牺牲论文严谨性；我们的目标是真实提高学术说服力与同行评审通过率。
  - ❌ **绝不搞教条主义形式禁令**：不搞“消灭所有被动语态、消灭所有分号或副词”——Methods 的规范被动句与专业引用格式享有最高体裁保护。
  - ❌ **零幻觉与零篡改**：坚决禁止为了“显得更像人类”而由 AI 擅自新增数据、捏造文献或添加无关个人轶事。

---

### 🧠 核心机制：六大偷懒成本 (M1–M6)

> **每一处 AI 感，都是大模型省掉了一项只有人类学者写作才会付出的思考成本：**

- **M1 穷举代替取舍**（决定删什么）：用四个动词排比、多项列表代替清晰的论据取舍。
- **M2 抽象代替机制**（把推理算完）：遇到复杂因果，用 `plays a crucial role in` 等套话一笔带过。
- **M3 替读者做评价**（信任读者判断）：滥用 `important`, `crucial`, `fascinating` 等主观赞美词。
- **M4 默认动作反复调用**（记得自己写过什么）：段落反复调用“抽象断言：具体展开”冒号套路。
- **M5 顺序只服从作者**（设想读者此刻知道多少）：段首与上段段末完全脱节，逻辑链条断裂。
- **M6 句式声势代替证据**（让措辞强度服从证据）：过度对冲（`it may potentially seem...`）或凭空制造无根据反驳（`not X but Y`）。

---

### 📋 S1–S16 故障代码表

| 代码 | 症状名称 | 核心表现 | 主要学术保护条件 |
|---|---|---|---|
| **S1** | 连续动词组 / 列表堆叠 | 多项并列只表示“很多”，无实质推进 | 样本组、自变量条件、实测结果清单 |
| **S2** | 理由枚举式 | 用“N 个弱理由”代替一条有力论证 | 每个理由独立改变结论 |
| **S3** | 抽象到不知所言 | 命名了区分却未定义；浅层 payoff 句 | 相邻句已给出施事、来源和严谨推理 |
| **S4** | 冒号＋展开 | 反复使用“空洞断言：具体展开”句式 | 真正的概念界定或一次性强调 |
| **S5** | 指代滥用 that | 对当前焦点无故拉远距离 | 合法 that-从句或特定语境限定 |
| **S6** | 表述／功能槽重复 | 同一学术套路或论证动作循环调用 | 核心术语一致性、Methods 体裁需要 |
| **S7** | 衔接断裂 | 段首未承接上段末尾留下的问题 | 章节标题或明确逻辑词已完成过渡 |
| **S8** | 评价式句子 | 替读者主观下结论（important / useful） | 跨研究的客观证据排序（strongest / clearest） |
| **S9** | 无根据对立／幽灵反驳 | `not X but Y`, `rather than` 缺乏出处 | 真实理论竞争、条件限定否定 |
| **S10** | 术语身份漂移 | 同一构念轮换近义词 | 构念本来不同、被引来源的标准用词 |
| **S11** | 认识强度失配 | 动词、方向或范围过度夸大或过度对冲 | 与实证设计严格绑定的必要限定 |
| **S12** | 模糊归因／引用堆叠 | 句末堆砌引用，谁说了什么模糊不清 | 多来源共同支持同一宏观综合判断 |
| **S13** | 模板支架 | 万能开头、结尾或空洞未来展望 | 能写出本文特有实证后果的展望 |
| **S14** | 造作比喻 | 抽象学术概念被赋予戏剧化动作 | 领域公认的标准隐喻（如认知瓶颈） |
| **S15** | 修辞问句／自问自答 | 正文突兀提问自答以推进段落 | 研究问题列表（RQ）、标题正式回扣 |
| **S16** | 机械导航／元话语 | 空洞路标句（“本节将探讨…”） | 长篇学位论文必要路线图、必要交叉引用 |

---

---

## 🔍 6 大实战修改示例：修改前 vs 修改后 (Before vs. After)

与市面上盲目同义词乱换的工具不同，`academic-ai-pattern` 严格诊断大模型背后的“偷懒生成机制（M1–M6）”，并结合学科体裁保护做判定。以下是最典型、最明显的 5 组实战案例：

---

### 1. S1 连续动名词组／列表堆叠 (Consecutive Gerund Chains)
- **修改前（典型 AI 生成句）**：
  > *"Evaluating the autonomous control pipeline requires calibrating visual sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers."*
- **机制诊断（M1 穷举代替取舍）**：一连串堆砌四个 `-ing` 动名词短语，试图把所有工程细节全数摊开，制造“工作量很大”的虚假充实感，却没有聚焦到底哪个环节承载核心论证。
- **保护测试**：如果四项是 Methods 里必须汇报的 4 组测量指标或实验条件，享有最高保护；但在理论引言中，堆砌动名词掩盖了核心因果。
- **学者改法（修改后）**：
  > *"The evaluation nominally assesses control stability, but tracking accuracy critically depends on synchronizing telemetry data while evaluating dynamic sensor noise."*  
  *（砍掉次要步骤，只保留真正承载论证的两个核心动作。）*

---

### 2. S4 冒号＋展开 (Colon + Expansion)
- **修改前（典型 AI 生成句）**：
  > *"The distributed architecture fits real-time operations better because it requires none of this: it inherently expects packet loss, asynchronous node updates, and variable network latency."*
- **机制诊断（M2 抽象代替机制 + M4 默认动作循环）**：大模型最高频的单一套路（“抽象断言 : 具体展开”）。冒号向读者承诺“我马上解释”，让前面那句空洞无物的断言得以存活。
- **学者改法（修改后）**：
  > *"The distributed architecture fits real-time operations better because it inherently accommodates asynchronous node updates and variable network latency."*  
  *（删掉多余冒号，把具体的作用机制直接提为主干谓语，逻辑更加紧凑。）*

---

### 3. S8 评价式句子 (Evaluative Sentences)
- **修改前（典型 AI 生成句）**：
  > *"This algorithmic trade-off is crucial to any scalable deployment, and the rationale is straightforward."*
- **机制诊断（M3 替读者做评价）**：作者滥用 `crucial`、`useful`、`straightforward`、`notable` 等修饰词替读者下结论，掩盖实证推导的单薄。审稿人极易将其批为“不客观的修辞空话”。
- **学者改法（修改后）**：
  > *"Any scalable deployment must directly resolve this algorithmic trade-off."*  
  *（剥除主观吹捧词汇，留下客观约束事实，让实证逻辑自己说服读者。）*

---

### 4. S14 造作比喻 (Strained / Theatrical Metaphors)
- **修改前（典型 AI 生成句）**：
  > *"The attention mechanism acts as an omniscient digital conductor, furiously orchestrating the chaotic symphony of multi-source sensory tokens."*
- **机制诊断（M6 句式声势代替证据）**：为了强行制造生动的“画面感”，给抽象学术构念赋予戏剧化、拟人化动作（如 “digital conductor”、“chaotic symphony”），审稿人的直观感受往往是“太假”、“戏精”。
- **保护测试**：领域内公认的标准隐喻（如 `attention bottleneck`、`gradient decay`、`computational pipeline`）严格豁免保护。
- **学者改法（修改后）**：
  > *"The attention mechanism applies dynamic weight matrices to prioritize high-saliency token embeddings across multimodal inputs."*  
  *（用严谨字面的学术机制与操作定义，替代戏精式比喻。）*

---

### 5. S10 术语身份漂移／近义词轮换 (Terminology Drift)
- **修改前（典型 AI 生成句）**：
  > *第 1 段：“The benchmark evaluated **response latency** across query batches...”*  
  > *第 2 段：“Reductions in **processing delay** improved overall throughput...”*  
  > *第 3 段：“These results demonstrate lower **execution lag** under peak load...”*
- **机制诊断（M4 同义替换导致概念混乱）**：市面上的去重润色工具常盲目轮换近义词以降低重复率，导致读者和审稿人误以为这是三个不同的自变量或测量指标。
- **保护测试**：本质不同的构念绝不能合并；但在指代同一测量指标时，**术语的重复是学术严谨性的体现，受最高体裁保护**。
- **学者改法（修改后）**：
  > 全文严格统一采用文献权威度最高、出现频次最稳定的唯一术语：**`response latency`**。

---

> 📄 **想查看完整论文与全量体检报告？**  
> 请点击查阅完整的虚构测试论文 [examples/sample_paper.md](examples/sample_paper.md) 以及包含 37 个候选裁决的完整报告 [examples/sample_report.md](examples/sample_report.md)。


---

---

### 6. 破除 AI 防御性写作实战：从怯懦免责到自信直陈 (Eliminating AI Defensive Writing)
- **修改前（典型 AI / Codex 防御性弱化句）**：
  > *"While this study does not claim to offer a comprehensive theory of distributed caching, and although our evaluation is inherently restricted to synthetic benchmarks, our findings might tentatively suggest that adaptive scheduling could potentially mitigate transient queue congestion."*
- **机制诊断（典型 AI 防御性写作：预设辩解 + 层叠犹豫对冲 + 消极开篇）**：  
  大语言模型为了规避“断言责任”，在正文中层叠堆砌防卫性弱化词（`While we do not claim...`, `might tentatively suggest that ... could potentially`）。这种写法语气怯懦、重点模糊，把宝贵的引言篇幅浪费在解释“我们没做什么”上，严重削弱了论文的学术贡献感。
- **去防御性学术重构（修改后）**：
  > *"In 64-node benchmark evaluations, the adaptive scheduling policy reduced peak queue latency by 23.4% ($p < .001$), demonstrating that dynamic cache reallocation directly mitigates transient node congestion under high-throughput workloads."*  
  *（改写方向：**论点与证据先行**——直接用实证数据支撑核心贡献；删掉怯懦的多重犹豫词（`might tentatively / could potentially`）；客观的样本限制留在方法章节中交代，恢复学术文稿的直接、精准与自信。）*

## 📊 运行产出与报告解读指南 (产出报告怎么读怎么改)

运行 `/academic-ai-pattern` 审查论文后，工具究竟会产出什么？如何解读？作者应当如何根据报告处理修改论文？

### 1. 产出产物 (Artifacts)
审查完成后，**源稿件绝对保持只读，工具绝不直接修改你的原文**，而是在同目录下生成对应的版本化伴生体检文件：
- 📑 `<stem>-ai-pattern-report.md`：**主审查报告**（含执行摘要、S1–S16 覆盖表、行动清单、结构化 Finding 详情与最小修改方向）。
- 📑 `<stem>-ai-pattern-ledger.md`：**完整裁决账本**（记录全量高召回候选的逐条判定依据与原始触发文本，供深度溯源）。

---

### 2. 怎么看：拒绝概率评分，看懂三档裁决 (How to Read)
本工具**绝不给出任何虚无缥缈的“AI 生成概率百分比”**，而是提供对齐同行评审标准的**三档结构化裁决**：

| 裁决标识 | 含义说明 | 作者应对建议 |
|---|---|---|
| 🚨 **需修改** (*Needs Revision*) | 确凿命中 M1–M6 偷懒生成机制，且未通过学术保护测试（如 4 动词堆叠、空洞未来展望、无根据幽灵反驳）。 | **建议采纳**：对照报告给出的“处理方向”与“候选改法”进行微创精简。 |
| ⚖️ **待作者判断** (*Author Discretion*) | 属于学术文风边界或特定个人偏好（如冒号展开、修饰性评价词）。 | **自主裁量**：若该句属于特定理论强调可保留；若非必要则建议简化。 |
| 🛡️ **受保护** (*Protected*) | 虽命中表面形式，但实质承担合法学术功能（如 4 组自变量条件、Methods 被动句、被引作者标准命名）。 | **保留原文，严禁误伤**！工具会明确给出保护理由，打消作者顾虑。 |

---

### 3. 怎么处理：实战报告样例与四步修改法 (How to Process)

报告中的每一个核心缺陷（Finding）都以结构化卡片呈现。以下是一个真实的报告条目样例：

#### 报告卡片真实样例：
> ### AP-S01-001
> **类别**：AI 模式 (S1 连续动词组／列表堆叠)  
> **位置**：`markdown-p0012`  
> **触发片段**：  
> `> Evaluating the autonomous control pipeline requires calibrating visual sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers.`  
> **裁决**：🚨 需修改  
> **理由**：一连串堆砌四个 `-ing` 动名词短语，用全流程工序列表代替核心论据取舍，属于典型的 M1 穷举偷懒机制。  
> **保护测试**：经上下文核查，该段为引言论述而非 Methods 实验步骤说明，删除次要工序不影响实证事实。  
> **处理方向**：砍掉不承载论证的次要动作，仅保留承载核心因果的一到两个主动动词。  
> **候选改法**：  
> `Evaluating an autonomous pipeline nominally assesses control stability, but tracking accuracy critically depends on synchronizing telemetry data while evaluating dynamic sensor noise.`

#### 作者实操处理四步工作流：
1. **第一步·先看行动清单**：打开报告顶部的 `## 行动清单`，快速掌握全文共有多少处“需修改”与“待作者判断”，做到心中有数。
2. **第二步·逐项微创修改**：对标为 `需修改` 的条目，直接在原稿（.docx 或 .md）中定位对应段落，参考报告给出的“处理方向”进行外科手术式精简（通常是“砍掉次要动词”或“提炼实质机制”，每处修改耗时不到半分钟）。
3. **第三步·审视待定条目**：对 `待作者判断` 的条目，根据目标期刊审稿要求与个人文风决定是否采纳。
4. **第四步·放心保留受保护区**：对于工具判定为 `受保护` 的实测数据和标准术语，无需做任何改动，彻底打消被商业检测器误伤的顾虑。

---

### 💡 实验性文风探索：作者模型与文风指纹 (Author Profile)

学术写作绝不是流水线打螺丝。优秀的学者历经多年研究与发表，往往拥有自己独特的“学术声音”（Authorial Voice）与论证节奏。市面上传统的去 AI 工具往往“千人一面”，机械地把富有学术深度的长复合句或个性化表达误判为“AI 腔调”。

`academic-ai-pattern` 独创了 **Author Profile（作者指纹模型）** 机制，旨在将“通用学术规范”与“学者个人风格”彻底解耦：
- **文风保护契约**：它不是冷冰冰的限制，而是作者与审查工具之间的“免伤协议”。通过声明个性化偏好与专有名词白名单，确保你的个人学术风格受到最高级别的保护，绝不被机械算法抹平。
- **快速配置（当前可用）**：
  复制根目录下的配置模板即可启用：
  ```bash
  cp author_profile.template.yaml author_profile.yaml
  ```
  在其中可自由界定：
  - **学科专属白名单**：输入本课题专有的核心术语与变量名，免受 S1/S6/S10 误伤；
  - **句法与节奏容忍度**：长句容忍上限（默认 12%）、分号使用倾向、修辞问句策略；
  - **论证与引用偏好**：是否保留叙述式主谓引用（如 `Smith et al. argued that...`）、幽灵对立删改偏好；
  - **语言标准**：美式英语 (`american`) 或英式英语 (`british`)；引言是否允许第一人称 (`I / We`)。

> 🚧 **建设初期说明与社区共建邀请 (Under Active Development & Open for Ideas)**：  
> **坦诚而言，Author Profile 目前仍处于初步建设与探索阶段。**  
> 我们深知“如何精准定义与保护一位学者的独特文风”是一项跨越计算语言学、审稿伦理与软件工程的长期课题。我们正在探索的方向包括：
> 1. **历史代表作逆向指纹提取 (Auto-Profiler)**：探索直接输入作者在 LLM 诞生前独立发表的 2~3 篇代表作，自动提取其真实的句长分布、高频转折手势与引文习惯，免去手动配置；
> 2. **学科与顶刊预设库 (Journal Presets)**：探索建立适用于不同学科（如纯理论数学、系统工科、实验认知科学）或课题组的标准化 Profile 模板。
> 
> **这套机制该如何进化得更实用、更优雅？我们非常期待听取你的声音！**  
> 如果你在日常写作、实验室规范或论文审读中有任何痛点、设想或改进方案，真诚欢迎在 [GitHub Issues](https://github.com/kyrieove/academic-ai-pattern/issues) 中留下你的见解，与我们一同探索属于学者的文风守卫体系！

---

---

### 📂 样例与演示 (Examples)

- [examples/sample_paper.md](examples/sample_paper.md)：虚构的多模态认知负荷学术实验样例论文。
- [examples/sample_report.md](examples/sample_report.md)：通过全量自动化闸门校验的标准版本化 Markdown 体检报告。

---

## ⚠️ 局限性与测试版说明 (Limitations & Beta Status)

> **当前状态**：公开测试版（Public Beta v0.9.x）。真诚期待大家的试用与反馈！

尽管 `academic-ai-pattern` 坚持非侵入式只读审查与实证保护，但在使用中请注意以下边界与局限：

1. **适用体裁范围**：本工具专为**实证学术论文（SCI/SSCI）、文献综述与硕博学位论文**量身定制；对于文学创作、新闻特写或公关文案等允许主观情感夸张的体裁，本工具的严苛标准并不适用。
2. **人机协同裁决**：形式匹配只能作为定位候选的线索，**作者本人始终是最终裁判**。特定前沿交叉学科可能有其特有的行文惯例，请结合实际研究设计做出最终裁决。
3. **外部引用真实性核实**：本工具主要在本地对主张与引用的逻辑对齐度进行自洽性审查。文献出处是否存在断章取义，仍需作者结合专业知识或按需联网核验。
4. **欢迎学术共同体共建**：不同学科（如纯理论数学 vs 实验认知神经科学）在行文习惯上存在细微差异。我们真诚欢迎广大学者、审稿人与开发者在不同学科稿件上试用，通过 [GitHub Issues](https://github.com/kyrieove/academic-ai-pattern/issues) 反馈长尾特例与改进建议，共同完善 S1–S16 规则库！

---

### 📄 开源许可证 (License)

本项目基于 [MIT License](LICENSE) 协议完全开源。欢迎学者与开发者提交 PR 与 Issue！
