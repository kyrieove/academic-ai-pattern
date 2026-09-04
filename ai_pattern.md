# AI 感模式手册 (Academic AI-Pattern Manual)

> 本手册提炼自数百篇同行评议学术实证论文的审读与改写实践，系统梳理学术英语写作中典型的 AI 生成模式与弱论证故障。
>
> 核心原则：**本手册绝非机械禁词表，而是故障代码库。** 形式匹配只能用于高召回定位候选，绝不能直接定罪；必须深入语义机制、上下文事实与学科惯例进行严格的保护测试。
> S1–S16 覆盖学术写作中最常见的 16 种表层症状与生成机制缺陷。

## 怎么用这份文档

新会话开始时，把这份文件给执行者读。它替代"凭感觉判断 AI 感"。

**入口是 §1 那一个问题，不是 §3 的清单。** §3 是被那个问题调出来的故障代码库；
从 S1 顺着跑到 S16 会把手册用成禁词表，那正是它反对的东西。

- **查文本**：先建第 4 节的语义合同 → 第 1 节的问题（作者做了什么决定？）→ 第 3 节按需取代码
- **改文本**：先过第 11 节的作者模型分类，再按第 5 节的六条硬规矩动手
- **别浪费时间**：第 7 节列出假信号和禁用做法，追它们会把文章改坏
- **写之前 / 修完之后**：第 2.5 节把症状接到上游的结构决定，指向 `write-it-up` skill
- **别扩张**：§1 末尾是新增症状的门槛。先证明 M1–M6 都解释不了，才准新设条目

---

## 1. 一句话规律

**每一处 AI 感，都是省掉了一项只有人写才会付的成本。**

人写作贵在六件事上：决定删什么、记得自己写过什么、把推理算完写下来、信任读者能自己判断、设想读者此刻知道多少、让措辞强度服从证据。AI 每一项都有省掉的默认动作，那个默认动作就是 AI 感。

### 判定方法：一个问题

对可疑的句子问：**作者在这里做了什么决定？**

如果答案是"没有决定，只是把相关的都列全了 / 换了个抽象词 / 加了句评价"——就是 AI 感。

这个测试比任何词表都准，因为它测的是生成机制，不是词汇。

### 新增症状的门槛

发现新现象时，**先证明 M1–M6 六个机制都解释不了**，才考虑新增 S 条目。顺序固定：

1. 现有某个 M 能解释 → 作为**案例**并入对应的 S，不新设条目；
2. 是同一个 M 的新表现形式 → 扩写那条 S 的判定，不新设条目；
3. 六个 M 都解释不了 → 才考虑新增 mechanism，S 条目随之产生。

不走这个顺序，手册会退化成一张越来越长的禁词表——那正是 §7 明令禁止的东西。
S14–S16 覆盖修辞夸张、自问自答与机械元话语等常见反模式。

---

## 2. 层 1 — 六个机制

| 机制 | 省掉的成本 | 对应症状 |
|---|---|---|
| **M1 穷举代替取舍** | 决定删什么 | S1 S2 S13 |
| **M2 抽象代替机制** | 把推理算完 | S3 S4 |
| **M3 替读者做评价** | 信任读者 | S8 S13 S15 |
| **M4 默认选项反复调用** | 记得自己写过什么 | S4 S5 S6 S10 |
| **M5 顺序服从作者** | 设想读者此刻知道多少 | S7 S13 S16 |
| **M6 句式与声势代替证据** | 让主张、关系和证据一一对齐 | S9 S11 S12 S13 S14 |

---

## 2.5 症状的上游：结构决定

> 参照 `write-it-up` skill（Silvia, *Write It Up*, APA 2015 的知识库综合，非原文复制）。
> 只给指针，不抄内容——书受版权，PDF 放在 gitignore 的 `writing_guides/`。

这份手册在**句子和段落**层面运作；Silvia 在**章节、稿件、研究项目**层面。两者不重叠，是**叠加**。
很多症状不是写句子写坏了，而是**上游的结构决定没做**，到句子层面才显形。

| 症状 | 上游的结构决定 | 出处 |
|---|---|---|
| S13 模板支架 | 这一节的论证目的是什么？**gap 不是论证**，文献编年史也不是 | ch04 |
| S7 段落衔接 | 先搭论证骨架：bookends-and-books（Pre-Intro 立问题 → 若干有标题的论证段 → Present Research 收口） | ch04 |
| S2 理由枚举 | 四个 Introduction engine 选了哪个（哪个对 / 机制是什么 / 分类要改 / 有新东西） | ch04 |
| S12 引用堆叠 | 引用是**筛选**出来的，不是收集来的；只引真读过的 | ch08 |
| S3 抽象缺推理 | **不带数字先写一遍**。文字讲不通，统计救不回来 | ch06 |
| S11 过度对冲 | **项目边界不自动等于局限**；局限只在具体且有用时才写 | ch07 |

**用法**：修出一个症状之后，回头问上游那一栏的问题。如果答不上来，
这个症状会在下一段重新长出来——修的是显形，不是成因。

### 机制层的映射强度（诚实标注）

| 机制 | 强度 | 说明 |
|---|---|---|
| M5 顺序服从作者 | **强** | Silvia 的核心就是论证架构 |
| M6 句式代替证据 | **强** | ch07 的局限判据、ch08 的引用纪律 |
| M1 穷举代替取舍 | 中 | `build only the necessary argument` 是节层面的同一原则 |
| M2 抽象代替机制 | 中 | numbers-stripped draft 是"推理在不在"的检验 |
| **M3 替读者做评价** | **无对应** | Silvia 没有这条。这是作者本人的标准（作者模型 P6），不是通行写作建议 |
| **M4 默认选项反复调用** | **无对应** | 术语漂移他不处理；S10 聚焦学术术语唯一性与近义词漂移 |

### 两处与本手册冲突，保留冲突不调和

**① Silvia 反对 S5。** ch02 明确说不要采纳没有理由的禁令，列举项里就有
`nearby demonstrative pronouns`——正是 S5 的 that/this。他会判为 peeve。
**本手册以领域裁决为准**，但 S5 应理解为个人标准，不是通用规则。

**② 语域方向相反。** ch02 主张学术散文保持 personal、collaborative、confident，
不该禁第一人称；M3 要求不替读者做评价。本文正文无第一人称，属作者选择。

**③ 时效**：Silvia 是 2015 年的心理学语境，投稿规则、报告标准、开放科学要求都可能已变。

---

## 3. 层 2 — 十六个症状

**这是故障代码库，不是检查清单。** 不要从 S1 顺着跑到 S16。

正确的入口是 §1 那个问题——**作者在这里做了什么决定？** 答不上来，才来这里找对应的
代码；答得上来，就不查。反着走（关键词 → S 码 → 删除）只会制造噪音：S1 一次扫出
78 条，真问题 5 条；S6 扫出 5 处，作者全判可接受；S15 唯一一处命中判为标题回扣。

每条开头的 **账** 记录这条规则在本文的实际表现。**扫描前先看这个数**——采纳率低的
条目，扫描结果的默认处置是不动，不是改。账里写“未清点”“未记录”的地方就是记录本身
的缺口，别当成零。

### S1 连续动词组 / 列表堆叠 —— M1，能机扫

> **账**：命中 78（单次扫描）｜采纳 **5**｜全文累计改 17 处｜标准裁决（砍，不是重排）

四项以上的并列动词或抽象名词，列表本身不携带信息，只是把"有很多因素"摊开。

**前**
> Evaluating an autonomous control pipeline, for example, requires calibrating sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers.

**后**
> Evaluating an autonomous pipeline nominally assesses control stability, but tracking accuracy critically depends on synchronizing telemetry data while evaluating dynamic sensor noise.

**关键：这是"砍"，不是"换个说法"。** 中间若尝试把五个动词改成三个带方向的动词依然繁冗；写作审查的通用原则是：**"没有必要将多个动词全数堆砌，只保留承载核心论证的一两个主要动作即可。"**

判断哪几项该留：**只留承载论证的那一两项**。砍掉的项通常在文章别处已经讲过，检查一下就知道不会丢信息。

**扫描**

```bash
python - <<'EOF'
import re,zipfile
z=zipfile.ZipFile('essay.docx'); doc=z.read('word/document.xml').decode('utf-8')
def txt(f):
    t=''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>',f,re.S))
    for a,b in [('&lt;','<'),('&gt;','>'),('&amp;','&')]: t=t.replace(a,b)
    return t
paras=[txt(p).strip() for p in re.findall(r'<w:p[ >].*?</w:p>',doc,re.S)]
for p in paras:
    if len(p)<120: continue
    for s in re.split(r'(?<=[.?!])\s+',p):
        c=re.sub(r'\([^)]*\)','',s)          # 去掉引用里的逗号，否则全是假阳性
        if c.count(',')>=4 and re.search(r',\s*(and|or)\s',c): print(s[:200],'\n')
EOF
```

⚠️ **假阳性率超过 90%。** 一次扫出 78 条，真问题只有 5 条。必须人工过一遍，别批量替换。

---

### S2 理由枚举式、不服人 —— M1，不能机扫

> **账**：命中 未清点（不能机扫）｜采纳 1（作者当场指出的那处）｜领域裁决 未单独记录

用"有 N 个理由"代替一条论证。枚举出来的理由通常各自都很弱，加起来也不强。

**前**
> The present study evaluates multimodal feedback in human-computer interaction for two reasons: multimodal cues are prominent in interface engineering, and they have also been linked to user reaction speed.

两条理由本质上都是“它很热门”，第二条弱到近乎无实质论据。

**后**（换成一条论证，并承认更强的竞争者）
> The question has to be put to a particular mechanism. Sensory redundancy is not the sole candidate for that role: adaptive visual layout is more consistently implicated across benchmark systems, and auditory priority cues have at least as strong a claim to reduce localized interference. It is, however, the mechanism most often named as the driver behind latency reduction, and the empirical gap between how readily it is invoked and how well it holds up under sustained load is what the present study examines.

**修法**：删掉枚举框架，换成一条能推进论证的理由。承认弱点往往比堆理由更有力。

---

### S3 抽象到不知所言 —— M2，半机扫（只有 payoff 外壳能扫）

> **账**：命中 未清点（不能机扫）｜采纳 6（只覆盖 §1–§2、§4.3–§5.1）｜领域裁决 已记录（“要拆分开”），日期未记

三个诊断特征，命中任意一个就是：

1. **命名了一个区分，但从没定义**
2. **给了定义，但那定义排除不了任何东西**
3. **payoff 句（`helps to explain why…`、`their contribution is to show…`）里的推理步骤缺失**

**前**（三条全中）
> Chen et al. (2022) contrast static routing accounts with adaptive scheduling models, in which the controller plays an optimizing role, coordinating network packets in relation to a global deadline. The latter view helps to explain why throughput that appears robust in baseline benchmarks can look quite different during peak load surges.

`adaptive scheduling models` 从没定义；`coordinating network packets in relation to a global deadline` 放在任何调度定义里都成立；第二句承诺解释但没给中间那步。

**后**
> Chen et al. (2022) set an adaptive scheduling model against static routing accounts. A static account treats throughput as a fixed capacity the node maintains, so a metric obtained under idle conditions should carry over to any network state. On the adaptive view, throughput is not a static property, and what it demands depends on runtime dynamics: resolving queue contention during burst traffic is not the same operation as steady-state load balancing. This is why an idle latency benchmark need not predict the delays an operator experiences during sudden failover events.

**修法：拆，不是换词。** 核心原则：**遇到高密度空洞抽象表达，切忌用另一个抽象词去替换，而必须将推理逻辑逐层拆解开来。**

拆的顺序固定：**命名 → 具体说明是什么 → 说后果 → 给实例**。压缩的多子句一定要拆成短句，一句一件事。

**⚠️ 同一个模糊说法常常出现两次。** 这条在 §2.1 和 §4.4 各写了一遍，第一次只修了 §2.1，第二次才发现。改完一处，去搜全文有没有第二处。

**新增子型：浅层 payoff。** 一个事实句后面挂 `clarifying`、`highlighting`、
`suggesting`、`leaving unaddressed` 等 `-ing` 短语，看起来给出了意义或后果，
但没有写出**谁根据什么推出什么**。这不是 `-ing` 禁令：只有中间推理缺失时才归 S3。

判定时把 `-ing` 短语拆成独立句，再问三件事：

1. 施事是谁？
2. 它依据哪项结果或来源？
3. 它新增的关系能否被前文推出？

任一项答不上来，就是 payoff 外壳；三项都答得上来，就是正常压缩，保留。
`跨稿件实证样本` 只读复核中的 `research has examined metaphor comprehension,
clarifying how...` 是候选实例，不代表已裁决或已修改。

---

### S4 冒号 + 展开 —— M2 + M4，能机扫

> **账**：命中 31（正文冒号）｜采纳 23｜保留 8｜领域裁决 未单独记录

> 抽象断言 **:** 具体展开

这是最高频的单一构造。本文正文 31 处冒号，**至少 20 处是这一个动作**：

- `the operational lesson carries over: results from one configuration…`
- `This architecture makes the trade-off explicit: caching occurs while…`
- `Two features make the model robust: it rests on longitudinal telemetry…`
- `Chen et al. (2020) illustrate the problem: network incentives moved…`
- `What a latency difference establishes is narrow: the systems diverged…`
- `The answer is: part of the way, and unevenly`
- `The distributed model fits better because it requires none of this: it expects partial…`

**为什么它是 AI 感**：

- 对 M2：冒号向读者承诺"马上解释"，抽象断言因此能存活。没有冒号，你必须直接写具体的东西。
- 对 M4：每次要连接"断言"和"展开"，生成器都伸手拿冒号。人会换——有时句号，有时 `because`，有时把具体的东西直接提为主语。

**修法**：不是全删。留少数真正需要引出清单的，其余改掉——把展开的内容提为主语，或断成两句。

**扫描**

```bash
grep -o '.\{80\}:.\{60\}' essay.txt | grep -v 'http\|Author:\|Title:\|Date:\|Contact:'
```

---

### S5 指代滥用 that —— M4，能机扫

> **机制与习惯**：在学术英语中，刚讨论且仍在焦点的对象倾向用 this，拉开距离时用 that。部分学者和编辑更偏好使用 this / it 代替反复出现的远指 that。

**建议原则：刚提及、正在论述的焦点用 this；已经论毕、需要拉开距离的用 that。**

| 前 | 后 |
|---|---|
| `On that view the pipeline is not a set of fixed parameters` | `On this view…` |
| `That possibility cannot be evaluated` | `This possibility…` |
| `That result suggests that an unstable…` | `The result suggests…`（顺手消掉一句两个 that） |
| `That pattern is testable.` | `This pattern is testable.` |
| `However, even that literature resists` | `However, even this literature resists` |

**不要动**：真正的 that-从句（`That two routes converge is…`）、时间指代（`at that point`）。

在初稿审查中可重点关注 that/this 比例失衡与远指漂移现象。

**扫描**

```bash
grep -oE '(^|[.!?] )That\b.{0,60}' essay.txt
grep -oE 'that (view|result|pattern|literature|account|claim|difference|effect|comparison|component|framework|level|possibility|conclusion)\b.{0,50}' essay.txt
```

---

### S6 同一表述 / 同一功能槽重复出现 —— M4，半机扫

> **账**：命中 5｜采纳 **0**｜标准裁决（符合文献惯例，五处全保留）

**字面长串重复最容易被可靠定位，但“确实重复”不等于“必须修改”。** 技术术语、
标准结果表述和图注可能有意重复；本文扫出的 5 处就全部被作者保留。功能槽重复更弱，
必须同时看位置和功能，不能只凭频次。

人也重复，但人重复的是**术语**（`response latency`、`distributed consensus model`）——那是刻意的一致性。AI 重复的是**表述**：隔了几千字，同一个意思被重新生成成几乎一样的句子，作者不知道自己说过。

本文实测：

| 重复的表述 | 出现位置 |
|---|---|
| `visual, acoustic, tactile, and spatial telemetry` | §1、§3.2 |
| component vs process 那整套说法 | §2.1、§4.4 |
| `latency-related alert benefits were preserved` | §2.2、§3.2 |
| `showed a clear processing throughput bottleneck` | §2.3、§3.x |
| `feedback channels are active at the same time` | §1、§2.2 |

**扫描**

```bash
python - <<'EOF'
import re,collections
b=re.sub(r'\([^)]*\)','',open('essay.txt',encoding='utf-8').read())
w=b.split(); g=collections.Counter(' '.join(w[i:i+6]) for i in range(len(w)-6))
for k,v in sorted(g.items(),key=lambda t:-t[1]):
    if v>=2 and not re.search(r'et al|\d{4}|Section',k): print(v,k)
EOF
```

**新增子型：重复功能槽。** AI 不一定复现同一个 6-gram，也可能在每次需要回指、
解释或总结时都调用同一种抽象主语：`The present study...`、`These findings...`、
`This interpretation...`、`The results...`。问题不是这些词出现了，而是它们反复占据
相同的**句首位置 × 段落功能**，作者没有重新决定这一句真正的主语。

扫描时除 n-gram 外，再记录：句首形式、所在段落位置、承担的功能（报告 / 解释 /
回指 / 限定 / 总结）。同一开头多次出现不自动构成问题；只有功能也重复才进入人工判定。

**保护与修法**：

- 技术对象（如 `The N400`）重复是术语一致性；Methods 中稳定使用同一主语也可能是体裁需要。
- 不能随机轮换 `study` / `analysis` / `investigation`；那会制造 S10。
- 真正的修法是让具体研究者、结果、实验限制或理论关系成为主语；若原主语最准确，零修改。

`跨稿件实证样本` 的只读复核中，`The present study` 分布在 7 个段落、
`These findings` 在 5 个段落、`This interpretation` 在 4 个段落；这些数字只是候选分布，
没有过作者模型，不能直接据以修改。

**新增子型：标题回声。** 小标题后的第一句若只是换词重说标题，然后下一句才进入内容，
就是跨标题边界的 S6。删除测试仍看信息：第一句若没有增加对象、关系、证据、范围或边界，
删掉；若它定义标题中的术语、限定适用范围或建立与上段的关系，则保留。若第一句主要在
预告本节将做什么，同时归 S16。

---

### S7 段落衔接断裂、逻辑不通 —— M5，不能机扫

> **账**：命中 未清点（不能机扫）｜采纳 2（作者当场指出的两处）｜领域裁决 未单独记录

段落开头直接抛出新概念，不承接上一段留下的问题。

**前**：上一段结尾是 `Multimodal cues may therefore influence all three performance metrics without being the primary driver of any of them`，下一段开头直接是 `The present study evaluates multimodal feedback in human-computer interaction for two reasons…`——中间少了“为什么必须落到某个具体机制上”。

**后**：`This possibility cannot be evaluated at the level of sensory feedback as a whole. Feedback is an umbrella term for distinct sensory modalities that dissociate from one another… The question has to be put to a particular mechanism.`

**同类：命名顺序。** 先解释再命名是反的。三个 process 应当**先给名称**（response inhibition / interference control / conflict monitoring），每个一句定义，再落到任务映射；而不是先描述四个操作、下一句才带出名字。

**检查方法**：只读每段的**首句和末句**，看能不能连成一条线。连不上就是断的。

---

### S8 评价式句子 —— M3，能机扫（关键词）

> **账**：命中 12｜采纳 12｜领域裁决 已记录标准准则｜`useful markers of processing stage` 判为修饰名词的常规用法，不计命中

**学者不替读者判断重要性。** 核心审稿原则：

> **"论证是否 straightforward、证据是否充分，读者能看出来；作者无需使用主观评价词替读者背书。"**
> **"在实证写作中，尽量避免滥用 useful, important, instructive 等空洞评价。"**

已删除的（典型示例）：
`The point is straightforward`、`The consequence is serious`、`the honest position is`、`hard to miss`、`not a peripheral rival`、`plainly not specific`、`the informative part`、`is instructive`、`the reason is clear`

基准版本 又抓到：`This separation is useful, because…`

**⚠️ 这类会复发。** 删过一轮之后仍有残留，基准版本 又扫出 2 处，**已在同轮修掉**
（经同行评议复核确认）：

- §1 `This measurement problem is crucial to any scalable architecture claim.`
  → `Any scalable architecture claim has to deal with this measurement problem.`（评价去掉，内容留下）
- §2.3 `Baseline heuristic algorithms nevertheless remain useful, especially when…` → 删

（`useful markers of processing stage` 这种修饰名词的常规用法不算，保留。）

**修法**：删掉评价，留下内容。
`This separation is useful, because sensory overflow is not always a bandwidth problem.` → `Sensory overflow is not always a bandwidth problem.`

**证据等级不是评价。** `strongest evidence`、`clearest evidence` 只有在全文事先建立了
primary / secondary / exploratory 的证据层级，而且该句准确回指这个层级时，才是信息，
不是替读者喝彩。反过来，`important evidence`、`particularly suitable`、`useful insight`
若删掉形容词后命题完全不变，仍按 S8 处理。不要按词判，要问评价是否改变证据排序。

**新增子型：系词回避 / 谓语膨胀。** `serves as`、`stands as`、`represents`、
`functions as a testament to` 有时只是绕开简单的 `is` / `has`，顺便制造重要性。
替换成系词后若对象、关系和证据等级完全不变，改用字面谓语；若 `functions as` 表示真实
功能、`represents` 表示抽样或表征关系，则不是膨胀，必须保留。

**同族：造作的比喻** —— 见 S14。判定标准不同，不要混在这里查。

**扫描**

```bash
grep -oniE '\b(is|are|remains?|seems?) (useful|instructive|important|crucial|clear|striking|notable|telling|revealing|essential|straightforward|obvious)\b|\bit is (important|worth|clear|notable) \b|\b(crucially|notably|importantly|strikingly|tellingly)\b' essay.txt
```

---

### S9 没有根据的对立 / 幽灵反驳 —— M6，半机扫

> **账**：命中 18｜采纳 3｜保留 14｜**1 处去向未记录**｜裁决标准（对立两边都要有正文支撑）

句子摆出 `not X but Y`、`rather than`、`although`、`despite`、`while` 或 `whether X or Y`，但正文并未建立 X、没有证据支持 Y，或者两边根本不是互斥项。形式制造了判断力，论证却没有付出相应成本。

**裁决标准（规则保留）**：判定标准是**对立两边是否都有正文支撑**。
支撑齐全的不动——本文 18 处里有 14 处属此类，因为"不是单一机制，而是多重风险"
本身就是全文论点。**修法是把 `rather than` 之后的内容整个删掉，不是改写它。**
裁决逻辑：**若对比的对立项并无正文或文献依据，判定为幽灵反驳，应直接删去修饰从句。**

已删的三处：

| 位置 | 删掉的部分 | 为什么 |
|---|---|---|
| §1 | `…active at the same time, ~~which is a precondition for crossmodal integration rather than an instance of it~~` | `precondition` vs `instance` 这组对立此处没解释，§2.2 才展开 |
| §4.1 | `…reported in Section 3.2, ~~rather than a separate argument against them~~` | "预期的理由"和"反对的独立论据"不互斥，一个东西可以两者都是 |
| §3.2 | `…system-level throughput and channel-specific demands ~~rather than in a general weakness of feedback processing~~` | 对立的方向和证据的方向相反：前半是推测，后半反而有文献 |

还包括两类残留：

- **幽灵反驳**：`It is not simply...`、`This does not mean...`，但前文没人提出被否定的说法。
- **拆分式揭晓**：先写一个否定句，下一句才用 `Instead` 给出本来可以直接说的主张。

**新增子型：防御式幽灵反驳。** `This paper does not claim...`、`We do not attempt...`、
`This should not be taken to mean...`、`We are not arguing...` 有时不是在回应真实争议，而是在预演
一个正文和文献都没有提出的审稿意见。先问：被否定的解释是否出现在文献、研究设计或前文？
若没有，它就是想象出来的防御对象；若同义地改成正面范围不会改变真假条件，直接说明本文
**实际研究、估计或覆盖什么**。若否定会改变主张的真值，或澄清一个真实竞争解释，则必须保留。

**新增子型：假范围。** `from X to Y`、`ranging from X to Y`、`across X and Y` 会把并列对象
包装成连续谱。先问 X 与 Y 是否位于同一比较维度，中间是否存在可解释的顺序，以及正文是否
真的覆盖这个范围；任一项不成立，就直接列出实际讨论的对象。真实的时间范围、剂量梯度、
发展阶段或同一量纲上的区间受保护。

**假选项补充测试**：一个被否定的备选方案是否真会被目标读者考虑，是否改变后续决策，
后文是否继续比较它？三项都否时，它只是草稿中的防御动作；直接写真正的约束条件。

**四问测试**：X 从哪里来？读者为什么会相信 X？Y 有什么独立证据？去掉对立框架后还剩多少实质内容？有一问答不上，就直接陈述有证据支持的关系。

**不要误杀**：理论之间的真实竞争、实验条件比较、承认限制后的转折、以及文献中明确存在的争议都应保留。对立词不是问题；**没有来源的对立**才是。

---

### S10 同义词轮换 / 术语身份漂移 —— M4，能机扫但必须人工判定

> **账**：命中 4 个词族｜采纳 3 个词族（共改 12 处）｜保留 1 个词族｜裁决标准（取文献里命中最多的叫法）

为避免重复，把同一构念轮换成多个近义词，读者会误以为它们是不同变量。学术写作中，术语重复通常是精确性，不是文风缺陷。

**判断顺序**：

1. 先建立术语表：标准名、允许缩写、允许语法变体、明确禁止的近义替换。
2. 查标题、摘要、正文、表图说明、附录是否指向同一身份。
3. 只有表述性重复可以改；概念身份的重复必须保留。
4. 无法确认两项是否同一构念时，标记给作者，不能擅自合并。

这条与 S6 相反但不冲突：**S6 查重复的说法，S10 保护重复的术语。**

**裁决标准（规则保留）**：**修法是采用相关文献里出现最多的叫法**，不是自己挑一个。落笔前用 R2 的 Europe PMC 查询逐个比命中数，取最高的那个。

本文四组实测与处置：

| 词族 | 各项 hits | 处置 |
|---|---|---|
| 延迟 | `response latency` / `processing delay` / `execution lag` | 统一为 `response latency`（改 4 处） |
| 精度 | `recognition accuracy` / `detection precision` / `classification rate` | 统一为 `recognition accuracy`（改 3 处） |
| 冗余 | `sensory redundancy` / `multimodal overlap` | 两者都可用，保留（作者判为可接受） |

**三条边界**：

1. **构念不同就不是漂移。** `sensory prioritization` 和 `crossmodal gating` 是两个独立机制，统一它们会毁掉论证。只统一**指同一构念**的说法。
2. **被引用的作者用词不动。** 经典文献里对该特性的标准定义就是 `response latency`（Smith & Johnson, 2021），此处必须原样保留；改它会改变被引来源的主张，违反 R3。
3. **词频最高不总是赢。** `shared mechanism`（6825）虽被作者初判为要删，但它是 §4.4 `Shared susceptibility need not mean a shared mechanism` 的论证转折点，且命中数是 `generic bottleneck`（607）的 11 倍。**规则与论证冲突时，论证优先**；作者复核后保留。

---

### S11 认识强度与证据不匹配 —— M6，半机扫

> **账**：命中 4｜采纳 4（3 处过弱 / 1 处过强）｜标准裁决

主张的动词、限定词和因果方向必须与证据类型相称。两端都会产生 AI 感：

- **过强**：相关或横断研究写成 `proves`、`demonstrates`、`establishes`、`confirms`；有限结果被抬成 `fundamental`、`transformative`、`definitive`。
- **过弱**：`may potentially perhaps suggest` 一类叠加缓和；修改后留下 `may can`、`appears to suggest` 等 hedge debris。
- **边界丢失**：删掉样本、任务、时间、比较对象、条件或否定范围，让局部发现看起来普遍成立。

**证据强度测试**：为每条经验主张写下证据来源和证据类型，再问这个动词能否由该设计支持。观察性结果通常支持 `was associated with`，不自动支持因果；空泛地加 `may` 也不能修复缺失的证据。

**限制来源—位置测试**：遇到叠加对冲，先指出不确定性究竟来自样本、设计、测量、
外部效度还是竞争解释。找不到具体来源的限定可能只是防御性语气；找得到时，不得把它换成
更强的动词，而应保留使主张成立所需的最小边界。必要限制应放在它会改变解释的位置；
同一句式若在摘要、引言、讨论和结论反复出现，则再按 S13 检查分布性模板。

**保护**：与证据绑定的 hedging 不能为了“更有力”而删。被动语态、第一人称复数和正式定义也不是天然 AI 痕迹。

**裁决标准（规则保留）**：这条在本文里**过弱的问题远多于过强**——
4 处待判里 3 处是过度对冲，只有 1 处过强。修法分两种：

| 类型 | 修法 |
|---|---|
| **过强** | 把情态动词换成**该设计支持的报告式动词** |
| **过弱** | 删掉叠加的第二重限定，或**把程度副词换成具体说不出口的那件事** |

已改的四处：

| 位置 | 前 | 后 |
|---|---|---|
| §3.3 过强 | `Their conclusion is that sensory feedback **cannot be regarded as** a universal driver` | `They conclude that sensory feedback **did not function as** a universal driver`（情态断言过强，而结论只来自一个测试基准、一套材料） |
| §4.4 过弱 | `weigh against a universal model **without establishing its absence**` | `weigh against a universal model.`（两重限定叠加；`weigh against` 本身已经足够弱，测试规模小也已在同句说明） |
| §5.2 过弱 | `and **much less** informative about whether the architecture is the right one` | `It **cannot test** whether the architecture is the right one.`（程度副词换成具体做不到的事，并拆成两句） |
| §2.2 过弱 | `Their strongest claim **remains debatable**.` | `**Whether monitoring accounts for most of that demand** is not settled.`（原句没说谁在争、争什么；改后点名争的是"most"这个量） |

**过弱的判定问题**：这个限定词删掉之后，主张会变成假的吗？不会，就是叠加对冲。
**过强的判定问题**：这个动词，该研究的设计支持得起吗？

---

### S12 模糊归因 / 引用堆叠 —— M6，半机扫

> **账**：命中 5｜采纳 4｜保留 1（多来源支持同一件事）｜标准裁决

`researchers argue`、`studies show`、`it is widely believed`、`the literature suggests` 如果没有紧邻来源、范围和具体发现，就是借“文献”制造权威。另一种表现是句末堆很多引用，却不说明各文献分别支持什么。

**新增子型：引用存在，施事仍缺席。** 句末有 citation 不等于归因清楚。
`Previous studies suggest... (A; B; C)`、`X has been identified as...`、
`It was found that...` 可能仍把三件事藏起来：哪位研究者、哪种设计、哪条发现。
判断单位是**主张—来源对应关系**，不是“有没有括号”。

这也不是被动语态禁令。Methods 中程序、材料和处理步骤的被动语态通常有体裁功能；
只有已有具体来源、改成叙述式引用能让证据归属更清楚时，才进入 S12。

**修法**：

- 能署名就署名；不能署名就说明证据集合的范围。
- 把“谁发现了什么、用什么设计、支持到什么程度”写清楚。
- related-work 段按主题、分歧或证据链组织，不按“作者 A 做了……作者 B 做了……”点名册组织。
- `Table/Figure X shows...` 后面必须有与论点相关的解释；只报“显示”不算分析。

**引用不是装饰。** 每条经验性主张应能回到数字、图表、表格或准确引用；引用数量不能替代证据对应关系。

**裁决标准（规则保留）**：**拆法灵活，仿照文献里此类描写的通行做法**，不套固定模板。
操作上分成一个判断：

> **堆叠里的来源是支持同一件事，还是各支持一件不同的事？**
>
> - **同一件事** → 堆叠是文献通行写法，保留。
> - **各支持不同的事** → 必须逐条挂上去，`X 发现…（引用），Y 则…（引用）`。

已改的四处：

| 位置 | 前 | 后 |
|---|---|---|
| §1 模糊归因 | `engineering accounts **increasingly** describe…` | 删掉 `increasingly`——趋势主张没有时间范围也没有证据 |
| §3.1 模糊归因 | `previous evaluations have **consistently** reported…` | 删掉 `consistently`——只有两个来源，撑不起“一致” |
| §6 堆叠 | uffer capacity, scheduling strategy, computational bandwidth, and cache topology all scale (Alvarez et al.; Brooks; Davies) | 三个来源各支持一项，逐条挂：uffer capacity scales with core count (Alvarez et al.), scheduling efficiency changes under peak load (Brooks), and cache latency scales non-linearly (Davies) |
| §7 堆叠 | `depends on sensory load and bandwidth, and part of it disappears once baseline latency is controlled (Chen et al.; Miller & Davis; Smith & Johnson)` | 同上，并修掉一处**孤儿引用**：先前删掉通道从句后某文献仍挂在句尾，却没有对应主张 |

**保留的一处堆叠**：§6 `Systemic bottlenecks must be distinguished from transient sensor noise (Alvarez et al.; Brooks; Davies; Evans)` —— 四个来源支持同一个方法学要点，属通行写法。

**与 作者模型 P2 的边界**：P2 禁止把叙述式引用压平成无主语被动句（上一轮压平 21 处后全部回退）。
S12 的方向相反——**把堆叠展开成叙述式**。两条规则同向，不冲突：都要求引用挂在它支持的主张上。

**孤儿引用是本条的副产品**：任何删改都可能让某个来源失去对应主张。改完句子要回头看句尾引用是否还都有着落。

---

### S13 模板支架 / 论证动作模板 —— M1 + M3 + M4 + M5 + M6，半机扫

> **账**：命中 4（50 个段末句跑过可移植性测试）｜采纳 4（3 删 / 1 补）｜标准裁决

以下结构只能作为候选信号，不能单独定罪：

- `Recent advances in...`，但没有时间范围或具体进展。
- `To the best of our knowledge...`，但没有可核查的检索边界。
- `Further research is needed...`，但没有指出下一项研究要区分什么解释。
- `This paper makes three contributions...`，后面只是目录或同义改写。
- `Despite these limitations...`，却没有说明限制如何约束结论。
- 通用开头、段末总结、未来叙事或“这为未来铺平道路”的结尾，换到另一主题仍成立。

**可移植性测试**：把学科名和变量名替换掉，句子是否仍能原样放进另一篇论文？如果能，它多半是支架。修复时补上本文特有的对象、关系、边界或后果；如果补不出来，就删。

**段落交换测试**：相邻段落能否互换而几乎不影响论证？若能，说明段落在并列展示材料，没有形成读者必须按此顺序经过的推理链。这同时是 S7 的全文级检查。

**新增子型：每句都有内容，但论证动作是模板。** 多个相邻段落可能反复执行同一个序列：

> 报告结果 → `may reflect / may indicate` → `compatible with` 某文献 →
> `cannot determine / remains indirect` 收回

单段看每句话都合理，放到全文却暴露出同一默认动作被连续调用。把变量名和成分名遮住，
只标每句话的功能；如果几个段落的功能序列相同，而且换位置仍基本成立，就是分布性 S13。

**修法不是删对冲。** `may`、`compatible with`、`cannot determine` 可能是 S11 要保护的
认识边界。应重新决定每段究竟需要报告、比较两种解释、排除什么，还是保留开放；
不能把这些词批量删除或换成同义词来制造变化。

**新增子型：限制分布模板。** 真实限制也会因位置和重复方式变成防御性支架：每个主张后
都接同一类退让，或同一 caveat 在摘要、引言、讨论和结论逐字回放。诊断时把每段的工作
单独标成主张、证据、比较、限制或推进；一个段落原则上只承担一个主要工作，不要默认把
主张、道歉、例外和澄清塞在同一段。限制仍应留在它改变解释的位置，不能为了“集中处理”
而移走会改变当前句真假条件的边界。负面免责声明若能等义改成研究实际覆盖的正面范围，
按 S9 删除防御支架；不能等义改写就保留。

`跨稿件实证样本` 的只读复核发现 `compatible with` 8 次，并在 Discussion 连续出现
“结果—解释—文献—限制”序列。这是跨稿件候选实例，未修改，也不计入本条的“账”。

**同族：贡献 / 依据支架。** `provide a basis`、`provide evidence`、`provide constraints`、
`offer a useful starting point` 如果只说“这项文献或本文有用”，却没有说明它具体允许推出
什么，也归本条。诊断问题是：**这项来源究竟允许本文多说哪一句？** 答得出就直接写那句；
答不出就删支架。稳定的理论名称可以重复，完整的贡献评价框架不必随之重复。

**裁决标准（规则保留）**：本文命中率很低——可移植性测试跑遍全部 50 个段末句，
只有 4 处不通过。**规则保留不是因为本文问题多，而是因为它管的是以后新起草的段落。**

四处全部判为问题，处置分两种：

| 位置 | 原句 | 处置 |
|---|---|---|
| §4.2 | `The role of ambient operating temperature remains largely unexplored in this literature, although latency develops in a wider hardware context.` | **删**。标了个空白就走，没有来源，也没说这个空白如何影响本文论证 |
| §6 | `Preregistration and out-of-sample validation are needed before these methods can support firm conclusions.` | **补具体后果**：`Until those choices are preregistered, an exploratory benchmark reflects the pipeline as much as the data.` |
| Discussion | `Future research should combine multiple tasks... to evaluate these alternative models across diverse samples...` | **删**。属于通用的空洞未来展望模板，换到任何领域都原样成立（S13 模板支架）。 |
| §7 | `Far transfer from generic interface training should not be assumed either.` | **删**。该方案在全文从未被讨论，是凭空出现的“实践启示”手势 |

**处置分岔的判据**（就是 S13 原有的修法，这里给出实例）：**补得出本文特有的后果就补，补不出就删。**
§6 那句补得出（微状态分析的自由度问题在前一句已经建立），其余三句补不出。

**两个副产品**：删掉 §7 那句同时消掉了一个五项列表（S1）；删掉 §4.2 末句后，
该段落回到以实质主张收尾（`unstable adaptive filtering may meet increased contention under peak network load`）。

---

### S14 造作的比喻 —— M6，不能机扫

> **账**：命中 7｜采纳 7｜裁决标准（造作拟人化比喻判定为太假，予以删除或替换为字面表述）

> 核心机制：聚焦修辞层面的造作拟人化比喻，剔除伪造画面的非学术戏剧性表述。

为了让句子有画面而造的比喻或拟人。作者的判词是**"太假"**。

**已删除的**：`a uniformly weak digital brake`、`not in an isolated hardware vacuum`、
`swallow the protocol`、`background noise`、`speed measured under another name`、
`closeness to the metal`、`processing is not a quantity but a job`

**边界**：普通技术词汇不算，换掉标准术语是相反方向的错误。
保留的：`causal chain`、`watershed` model、`architecture`。

**新增测试：主语—动词资格。** 问主语是否能在字面上或本学科惯例中执行该动词。
`the decision emerges`、`data tell us`、`culture shifts` 只有在遮住研究者、参与者、制度或机制时
才进入候选；`results show`、`the model predicts`、`the data constrain`、`the analysis estimates`
是常规学术转喻，不因主语非人就改。缺的是经验来源或证据施事时归 S12；为制造画面而赋予
抽象物行动时归 S14。

**新增子型：格言式压缩 / 戏剧性短句串。** `X is the language of Y`、
`X is not a tool but a mirror`、`X becomes a trap` 一类可移植金句，可能把普通关系压成
看似深刻的结论；连续几个极短句若都只承担 punchline，也属于分布性候选。单个短句、
领域内稳定隐喻和作者有证据支撑的概念定义不动。修法是写出具体对象、关系或机制，
不是把短句机械合成长句。

**和 S8 的区别**：S8 是替读者判断重要性（`is useful`），S14 是替读者制造画面。
两者都属"不让内容自己说话"，但一个改的是评价词，一个改的是意象。

**修法**：换成该领域的字面说法，然后按 R2 查头搭配。
`processing is not a quantity but a job` → `processing throughput is not a fixed parameter`
（`fixed parameter` 1240 hits）。

---

### S15 修辞问句 / 自问自答 —— M3，能机扫

> **账**：命中 1｜采纳 **0**｜裁决标准（标题已立过的问题，正文回扣不算自问自答）

> 核心机制：聚焦正文中突兀出现的修辞问句与自问自答，推动论证回归客观陈述。

提一个没人问的问题，然后自己答。表演的是"读者的参与"。

**本文命中**（§8 开头）
> How far, then, can multimodal architectures optimize operational throughput under
> conflicting sensory streams? **The answer is part of the way, and unevenly.**

⚠️ 语料库实测 记了一条实测：**作者本人从不用修辞问句**。语料里的问号全是研究问题列表
和以 `?` 结尾的参考文献标题。所以这条在本文里是高置信信号。

**受保护，不要动**：§1 的三个研究问题（`Accordingly, three questions are addressed
here: …`）、标题里的问句、参考文献标题里的问号。

**裁决标准（规则保留；该处命中判为合规保留）**：

这条针对的是**没人问就自己问**。如果问题**在标题里已经立过**，正文回扣同一个问题
不算修辞问句，是收尾结构。

本文 §8 开头就是这种情况，保留原样：

> 标题：`How Far Can Multimodal Architectures Optimize Operational Throughput Under
> Conflicting Sensory Streams?`
>
> §8 开头：`How far, then, can multimodal architectures optimize operational throughput under
> conflicting sensory streams? The answer is part of the way, and unevenly.`

**所以本条的判定问题是**：这个问题此前有没有被立过？立过就是回扣，没立过才是自问自答。

⚠️ 别把低命中数当成"已经改过了"。本文只有 1 处命中，是因为全文本来只有这一处
——另外三类问号本就受保护。规则的价值在以后新起草的段落。

**修法**：把问句改成陈述，或删掉问句只留答案。

```bash
grep -oE '[^.?!]{0,120}\?' essay.txt
```

命中数很少，逐条看即可。

---

### S16 机械导航 / 元话语 —— M5，半机扫

> **账**：命中 11｜采纳 **0（未处理）**｜领域裁决 未裁决

> 核心机制：聚焦不提供实质信息边界的机械导航与空洞元话语。

用章节路标代替真实的论证衔接。读者被告知"去看第几节"，而不是被带过去。

**本文 11 处**章节交叉引用：

- `The interpretation of this result also depends on the evidence for alternative architectural trade-offs, which is taken up in Section 4.5.`
- `A further qualification follows from Section 4.5, where …`
- `A further limitation becomes visible once Section 4.5 is taken into account, because …`
- `Whether the more recent benchmarking suite adds anything to that answer is taken up in Section 5.`

**判定**：删掉这个路标，论证还站得住吗？站得住就是赘余。
真正需要指路的短引（`see Section 3.3`）可以留。

**新增子型：微型导航。** 不写 `Section` 也可能只是预告下一步：
`A further question is...`、`This is where X becomes relevant.`、
`The next issue concerns...`、`The discussion below is organized...`。
如果下一句或小标题已经直接表达同一内容，导航句没有新增对象、关系或边界，就按 S16。

判定仍是删除测试：删掉后下一句是否自然、信息是否完全不减。真实的逻辑桥梁必须保留；
不能因为一句话位于段末或包含 `question` 就自动删除。

**同族：版本元评论。** `the improved version`、`we now provide`、`unlike the previous
approach` 若只是在记录写作或修改过程，不说明当前研究对象、方法差异及其后果，就属于元话语。
论文正文应描述当前方法实际做什么；只有真实版本比较、方法比较、勘误、变更日志或迁移说明
才需要保留旧版本。标题后的复述句则与 S6 的“标题回声”交叉判定。

**注意**：`Section 4.5` 出现 5 次以上，本身也是 S6（重复表述）的一个变体。

```bash
grep -oE '[^.]{0,110}Section [0-9]+(\.[0-9]+)?[^.]{0,60}\.' essay.txt
```

---

## 4. 动笔前：先建立语义合同

去 AI 味不是自由改写。先锁定“什么绝不能被风格编辑改变”，再判断哪里值得改。

### 4.1 主张—证据账本

对高风险句至少记录以下字段：

| 字段 | 要锁定的内容 |
|---|---|
| 对象 | 谁 / 什么变量 / 哪一组 |
| 关系 | 相关、预测、比较、调节、因果或解释 |
| 方向与极性 | 正 / 负；存在 / 不存在；支持 / 不支持 |
| 数量 | 样本量、效应、区间、阈值、时间点 |
| 边界 | 人群、任务、条件、时间和比较对象 |
| 强度 | `may`、`suggests`、`supports`、`demonstrates` 等认识强度 |
| 来源 | 引用、表、图、数据或作者自己的推理 |
| 状态 | 已核实、待核实、仅为解释、存在冲突 |

**禁止的变换**：新增事实、删除关键限定、改变因果方向、把相关写成因果、扩大适用范围、改变数字或引文、把不确定写成确定、合并原本有意区分的构念。

### 4.2 锁定区与术语表

默认锁定：原文引语、数字、公式、代码、表格、参考文献字段、专名、量表 / 任务 / 指标名，以及作者要求原样保留的句段。修改锁定区必须另有事实核查理由，不能借“humanize”顺手改。

为核心构念建立术语表。权威顺序是：作者明确指定 > 本文定义和方法 > 被引文献的标准用法 > 学科惯例 > 一般词典。术语身份不确定时，保持原样并标记。

### 4.3 先分类，再处理

每个候选只能进入四类之一：

1. **局部缺陷**：单句自身就损害意义或可读性。
2. **分布性缺陷**：单次合理，但在全文反复占据相同位置和功能。
3. **受保护结构**：承担逻辑、术语、证据或体裁功能，应保留。
4. **不确定**：需要作者或原文确认，不改。

分布性缺陷不能只凭次数判断。至少记录：出现次数、分布距离、所在位置（段首 / 段末等）、承担的功能，以及是否与其他弱信号聚集。**重复且功能冗余**才构成问题；功能性的重复不是问题。

分布图的单位不能只到词和标点，还要包括三层：

- **句首功能槽**：谁在反复承担报告、回指、解释或总结的主语；
- **段落动作序列**：每句话分别在报告结果、提出解释、挂文献、加限定还是推进结论。
- **段末功能槽**：段落是否总以结论、评价、限制、未来方向或 punchline 中的同一种动作收尾。

可以把学科名、变量名和硬件模块名暂时遮住，只看功能标签。若相邻段落仍呈现同一序列，
或遮住内容后可以互换，就是结构模板候选；随后仍须过作者模型和受保护结构检查。
段末功能相同也只构成候选：先看它是否来自章节任务或学科惯例，再判断是否功能冗余。

---

## 5. 改的时候的六条硬规矩

### R1 砍，不要重排

把五项列表改成三项列表、把并列动词换成带方向的动词——**都不算修好**。只留承载论证的一两项，其余删掉。

例外只有两种：
- **枚举本身就是论证**（如"横断数据分不清因、果、第三方相关"这个三分，砍到两项论证就塌了）
- **项目是数据**（样本量、任务名、核心参数名）

### R2 表述照文献惯例，不能自己编

核心原则：**学术表达应遵循领域文献的通行搭配与惯例，切忌脱离学科语境自行生造或由 AI 随意抽象替换。**

替换用的措辞落笔前查 Europe PMC：

```bash
curl -sS -G "https://www.ebi.ac.uk/europepmc/webservices/rest/search" \
  --data-urlencode 'query="fixed capacity"' \
  --data-urlencode format=json --data-urlencode pageSize=1 | grep -o '"hitCount":[0-9]*'
```

**只查头搭配，不查整串。** 未改动的原文也有 50% 的 4-gram 落在 ≤2 hits——几乎每个 4-gram 的英语都罕见。

检索实测对比：

| 我写的 | 整串 | 头搭配 | 判定 |
|---|---|---|---|
| `carry over to any task` | 0 | `carry over to` 38189 | 安全 |
| `has been read as conflict` | 0 | `has been read as` 7432 | 安全 |
| `suppresses competing network packets` | 0 | `suppress competing` 548 | 安全 |
| `shows up in behavior` | 1 | `shows up in behaviour` **0** | **生造，换掉** |

---

### R3 主张不漂移：修改前后逐项对账

每次改写后，对照第 4 节的主张—证据账本。最少检查：对象、关系、方向、数量、边界、
强度、来源、排序和证据等级是否完全保留。排序包括比较项的先后、证据层级、优先级与
“最强 / 次要 / 探索性”等相对位置；把列表重排得更顺也可能改变论证。

尤其警惕“更自然”的句子悄悄做到这些事：

- 补了原文没有的机制、例子、动机或评价；
- 为了具体而编造数字、地点、人物、研究设计或引文；
- 把作者的解释写成文献结论；
- 把 `may`、`in this task`、`in this sample` 之类关键限制删掉；
- 为了流畅而合并方向不同的两项主张。

**删除安全测试**：删掉一个短语后，是否改变真假条件、适用范围、比较对象或证据强度？会改变就不能当作赘词删。

### R4 最小充分修改，并尊重锁定区

先定位具体缺陷，再做能消除该缺陷的最小连贯修改。允许不改；“零修改”是合法结果。

- 局部问题局部修，不为了让整段“更像人”而重写整段。
- 只有当问题跨句（如推理缺口、段落顺序、术语漂移）时，才扩大编辑范围。
- 引语、数字、引用、技术术语和表格默认锁定。
- 多个弱信号在同一处聚集时，把它们视为一个结构问题一次修好，不按词表逐个刮掉。

### R5 保留关系，不保留过渡词外壳

删 `Moreover`、`However`、`This suggests` 或冒号时，先问它承担的逻辑关系是什么。若关系真实，必须通过 `because`、`although`、`whereas`、关键词回指、合句或句序恢复；不能把连接词删掉后留下两句并排事实。

段内优先走**旧信息 → 新信息**：句首接住上一句已经激活的对象，句末放推动下一句的新内容。句法应写出真实关系；需要因果、让步或条件时，复杂句本身不是缺点。

### R6 先修高影响问题，最后才修节奏

优先级固定：

1. 事实、引文和主张—证据对应；
2. 推理缺口、段落顺序和术语身份；
3. 删除空支架、虚假对立和无内容评价；
4. 局部措辞、重复和节奏。

句长、三项结构、破折号、分号、被动语态、名词化或第一人称本身都不是问题。节奏应服从信息结构，不能按“长短长”配额或统计阈值改写。
最后检查节奏时，可以记录段末分别在做结论、评价、限制、未来方向还是强调；只有它们在
全文机械复用同一功能、且不由作者模型或章节任务解释时才改。不得用主观风格分数或固定
“两拍优于三拍”之类节奏公式作为完成标准。

---

## 6. 不属于这个体系的四条

这四条常被混进 AI 感清单，但性质不同，混在一起会导致查不到。

**① 表述自己编** —— 不是生成模式，是"没去查"。查了就没有。→ 见 R2

**② 违背文献得出的事实** —— 是错误，不是文风。**注意和 S11 区分**：S11 是校准漂移
（系统性地把主张写得比证据强），是可预期的生成模式；这一条是一次性的事实说反，
没有规律可循。例：把 inhibition 写成 `strongest candidate`，而实际上 working memory 才是跨三种障碍最一致的候选，且文章自己的 §7 就是这么说的。改的是内容不是措辞，只能逐条核。

**③ 不为了指标强行改文字** —— 这是给执行者的工作规则，不是文本缺陷。作者的判准是 **"我本人肯定不会那么写"**，不是相似度分数。

**④ 工具残留 / 伪造引用** —— 这是生成过程或校对失败的硬证据，不是文风。应单独扫描并修复来源链：`turn0search0`、`oaicite`、`utm_source=chatgpt.com`、`grok_card`、`attached_file`、占位日期（如 `2025-XX-XX`）、无效 DOI / ISBN、文中未使用或参考文献表缺失的条目。发现后不能“润色掉”，必须核对真实来源。

---

## 7. 假信号与禁用做法：别追

追这些会把文章改坏。表中前六条由本文实测；各项保护条目严格遵循实证同行评议规范与学术体裁惯例。

| 看起来像问题 | 实际 |
|---|---|
| 三项列表 | 正常英文。`latency, throughput, and error rate` 是论证骨架不是堆砌 |
| 分号过多 | 多来源 APA 引用中包含分号属于体裁格式，不能粗暴计入正文分号文风统计 |
| 长句过多 | 学术实证论文中包含必要从句限定的长句（>35词）常见且合理，不可人为机械拆碎导致论证离散 |
| 短语在语料库罕见 | 未改动的原文也有 50% 落在 ≤2 hits。只有头搭配有信号 |
| 作者写英式英语 | 拼写检测易出现正则误报（如将 organism 误判为 organis）。应依据 author_profile 配置与目标期刊指南统一规范 |
| 重复 4-gram ×11 | 那个 4-gram 是 `van de voorde et`，一个被引 11 次的作者名 |
| 看到 `however` / `moreover` 就删 | 连接词可能承担真实的让步或递进；应检查关系是否成立 |
| 被动语态、名词化、第一人称复数 | 都可能是学科和体裁需要，不能作为单独信号 |
| 破折号、冒号或三段式本身 | 标点和结构只有在反复承担空洞功能时才有问题 |
| 单个“AI 高频词” | 单词没有作者身份；要看语义功能、分布和信号聚集 |
| `may` / `compatible with` / `cannot determine` 重复 | 可能在保护证据边界。查段落动作模板，不要靠删对冲制造变化 |
| `-ing` 短语或被动句本身 | 只有隐藏施事、来源或推理步骤时才有问题；方法描述和真实压缩应保留 |
| 副词、非人主语或 `results show` 本身 | 先查证据强度和主语—动词资格；常规学术转喻不是假施事 |
| Wh-开头、破折号、三项并列或“三拍”本身 | 形式没有固定的人类 / AI 身份；只查它是否反复承担空功能 |
| 每段以限制或结论收尾 | 只提示检查段末功能分布；章节任务和作者习惯可以合法地产生重复 |
| Title Case、弯引号等排版形式 | 常由期刊、Word 或模板控制，不是作者身份或生成机制的证据 |

**动手前先看清指标在数什么。**

以下方法明确禁用：故意加入语法错误或碎片句、随机替换同义词、按固定句长制造 burstiness、
按主观商业检测器分数设通过线、强行改变作者语域、为了通过检测器而改事实、承诺“无法被 AI 检测”。
这些方法优化的是表面统计或个人偏好，不是文章。

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

---

## 8. 规则审计覆盖与裁决基准

在对学术稿件进行完整审计时，S1–S16 必须保证全面的候选扫描覆盖：

| 规则族 | 典型审查重点 | 判定核心与保护机制 |
|---|---|---|
| **S1–S2 结构冗余** | 连续动词串、多项名词列表、枚举式展开 | 保护：样本组、比较条件、分类清单；若删除任一项不影响论证成立，则精简至 1–2 项 |
| **S3–S4 抽象与空转** | 未定义抽象概念、浅层 payoff、频繁冒号展开 | 保护：真正的概念界定与一次性清单；若内容可直接作主语，避免“空断言 + 冒号展开” |
| **S5–S7 篇章衔接** | 指代词漂移、功能槽重复、段落间断裂 | 保护：学科术语一致性、Methods 规范、研究问题回扣；审查段末与下段段首的逻辑递进 |
| **S8–S10 评价与构念** | 替读者主观评价（important/crucial）、无据对立（not X but Y）、近义词轮换 | 保护：由全文建立的比较排序（clearest/strongest）、真实理论竞争；同一构念严禁更换近义词 |
| **S11–S14 证据与强度** | 认识强度失配（过度对冲或夸大）、引用堆叠、模板支架、造作比喻 | 保护：实证设计绑定的必要限定、多来源共同支持综合命题；剔除可移植的空话模板 |
| **S15–S16 提问与路标** | 修辞自问自答、机械元话语与空路标 | 保护：正式研究问题（Research Questions）、学位论文必要路线图；删除不提供新信息的路标 |

---

## 9. 一次完整审计怎么走

### 9.1 诊断顺序

1. **读全文，不先替换。** 写下目标读者、体裁、作者的核心判断和不可丢失的限定。
2. **建两张表。** 主张—证据账本和术语表；锁定引语、数字、引用、专名、技术对象。
3. **扫硬残留。** 工具标签、占位符、无效标识符、引文与参考文献不对应。
4. **读论证骨架。** 只读标题、各段首尾句和结论，查 S7、S9、S13。
5. **逐段查机制。** 查 S1–S16；记录候选的准确位置、功能和证据，不按词表自动改。
6. **画分布图。** 对冒号、评价句、模板段首、同义轮换、句首功能槽和段落动作序列
   记录次数、位置和功能；区分局部缺陷与分布性缺陷。必要时遮住变量名，只比较
   “结果—解释—引用—限定”等功能标签。
7. **过作者模型。** 对每个还活着的候选再问一次：**即使学术上没错，这个作者会这么写吗？**
   对照 §11 的三类约束——A 类违反必改；B 类违反照文献惯例改；C 类只在来源标为
   “语料实测”或“领域裁决”时才据以修改，标 **推断** 的不能单独动手。§11 里查不到
   对应行的，按 §11.4“还没量过的”处理：标记，不改。
8. **按 R1–R6 修改。** 先事实和关系，后措辞和节奏；使用最小充分改动。
9. **逐项过终检闸门。** 任一项失败就撤回、缩小修改或标记待核。

### 9.2 每处修改的十问闸门

1. 改写前后的事实和命题相同吗？
2. 对象、关系、方向、数量、边界和比较对象都保留了吗？
3. 认识强度是否仍与证据类型相称？
4. 引文、数字、引用和技术术语是否原样或经核实？
5. 是否新增了原文没有的机制、例子、动机或评价？
6. 术语是否仍指向同一构念，而不是为了变换措辞而漂移？
7. 删除过渡或句式后，原有逻辑关系还清楚吗？
8. 这处问题是单句缺陷，还是只有放在全文分布里才成立？
9. 修改是否直接修复了已说明的缺陷，而非泛泛“更像人”？
10. 句子现在是否增加判断、证据、机制、边界或推进？若都没有，能否直接删？

七个补充测试：

- **强调来源测试**：把节奏、破折号、排比和强调副词拿掉，主张仍然站得住吗？站不住，说明声势在代替证据。
- **句法关系测试**：能否用 `because`、`although`、`whereas`、`if` 等明确复述句间关系？若不补写新事实就做不到，原句可能在用句法假装存在关系。
- **论证动作序列测试**：遮住变量、成分和学科名后，相邻段落是否仍使用同一功能序列，
  而且可以互换？若是，按 S13 查结构模板；必要的对冲按 S11 保护。
- **施事—来源测试**：句末即使有引用，能否指出谁用什么证据支持哪条主张？不能就按
  S12 查“引用存在但施事缺席”；Methods 的程序性被动语态除外。
- **正面范围测试**：负面免责声明能否在不改变真假条件的前提下，改成本文实际研究、估计或
  覆盖的范围？能则按 S9 / S13 查防御支架；不能则保留必要否定。
- **限制来源—位置测试**：这个 caveat 由哪项样本、设计、测量、外部效度或竞争解释约束触发，
  而且是否放在它会改变解释的位置？没有具体来源，或在全文重复同一功能，分别查 S11 / S13。
- **主语—动词资格测试**：主语能否在字面上或学科惯例中执行该动词？不能时，检查是否用
  假施事遮住来源（S12）或用拟人制造画面（S14）；常规学术转喻受保护。

---

## 10. 学术写作规范与常见反模式审查准则

### 10.1 审查边界

学术英语写作具有高度严格的实证与体裁规范。本手册的审查边界严格限定于**实证学术论文（Empirical Academic Papers）、文献综述（Literature Reviews）与学位论文（Theses/Dissertations）**，明确与以下体裁区分：
- 营销宣传、新闻通稿或公关文案（强调情感煽动与修辞夸张，与学术中立原则相悖）；
- 虚构文学创作或个人博客（鼓励个人经验与自由句式，与学术客观证据链相悖）。

审查严格聚焦于**论证机制、证据支持与学术体裁合规性**，而非主观文风好恶。

### 10.2 核心审查原则与实证保护

学术论文体检应当坚持以下六项基本原则：

| 审查原则 | 核心规范要求 |
|---|---|
| **语义合同与锁定区** | 严格锁定源文事实、样本规模、量表名、核心专名、数据单元与参考文献，禁止任何非授权篡改（§4.2） |
| **最小充分修改** | 只有证实存在生成缺陷或逻辑断裂时才建议修改；零修改同样是完全合法的审查结论（R4） |
| **分布性缺陷优先** | 关注篇章级的空洞功能槽循环、模板化段落推进与浅层 payoff 句，而非孤立抓取单个词汇（§4.3） |
| **术语身份唯一性** | 同一核心构念全文保持唯一标准称谓；术语重复代表学术精确性，受体裁最高保护（S10） |
| **认识强度与证据对齐** | 结论推断动词（demonstrates, suggests, indicates）必须严格服从实验设计（S11、R3） |
| **学术体裁语态保护** | Methods 部分的规范被动语态、多来源综合引用中的标准分号等，享有学术共同体通行保护（§7） |

### 10.3 明确排斥的非学术做法

在学术论文审查与修改中，以下做法明确予以排除和禁止：

| 违规做法 | 排除理由与风险 |
|---|---|
| **以商业检测器分数作为编辑目标** | 商业检测器缺乏对学术事实与专业术语的理解，盲目刷分极易诱导语法混乱与术语畸变 |
| **故意注入语法碎片或口语俚语** | 试图通过注入拼写错误或口语化表达伪造“人味”，会严重破坏学术语域并招致拒稿 |
| **机械长短句交替或硬性字数阈值** | 将一般统计特征误作为编辑目标，会破坏长从句所承担的严谨逻辑限定 |
| **极端形式禁令（如消灭所有被动语态）** | 被动语态在实验程序与客观事实陈述中具有不可替代的学术功能 |
| **强行同义替换以规避重复** | 频繁更换学术构念近义词会直接造成概念混淆与理论漂移（S10） |
| **为了“具体化”擅自虚构数据或例子** | 严禁 AI 凭空补充未测变量、虚构文献出处或编造实验参数（违反学术诚信红线） |
| **承诺所谓“100% 避开 AI 检测”** | 目标错误且不可验证；学术审查的唯一准则是学术质量、论证严谨度与同行评审规范 |

---

## 11. 作者模型与个性化配置

在学术审稿中，三种约束若混为一谈，执行力度就会错配：
- **A 类违反了是硬错误**（虚构事实、改动因果、改错数据）；
- **B 类违反了是外行**（破坏领域标准术语、破坏 Methods 体裁习惯）；
- **C 类违反了只是个人习惯差异**（长句偏好、叙述式引用偏好、拼写体系）。

本手册与配套 Agent 严格区分这三类约束，并将 C 类作者指纹解耦为独立的配置文件 `author_profile.template.yaml`。

### 11.1 A 类 — 通用学术硬约束

任何作者、任何学科稿件均强制适用。违反了即为学术硬伤，与文风和个人偏好无关。

| 约束项 | 说明与依据 |
|---|---|
| **严禁凭空新增材料** | 不新增原文没有的事实、例子、机制、动机或主观评价（§4.1 禁止的变换） |
| **严禁颠倒因果关系** | 不改动因果方向，不得将相关关系擅自改写为因果结论（R3） |
| **严禁改动锁定专名** | 不改数字、引文年份/作者、专有名词、量表名、实验任务名、专业构念缩写（§4.2 锁定区） |
| **严禁擅删必要限定** | 不删关键对冲与限定词（如 `in this sample`, `under these conditions`, `may`）（R3 删除安全测试） |
| **严禁擅自合并构念** | 不得扩大适用范围，不得将研究者有意区分的细分构念合并为宽泛概念（S10） |
| **引用关系严格对应** | 引用必须紧跟其直接支持的论点；改写后必须清理孤儿引用（S12） |
| **伪造/残留引用零容忍** | 工具残留或来源不清的引用必须回溯核查真实来源，严禁“润色掩盖”（§6） |

### 11.2 B 类 — 学科通行惯例

非特定个人习惯，而是学术共同体的通行规范。换由其他领域学者撰写仍需遵守。

| 惯例项 | 规范内容 |
|---|---|
| **术语身份严格唯一** | 同一核心构念在全文始终保持唯一名称；术语重复是学术精确性的体现，绝非文风冗余（S10、§4.2） |
| **权威搭配检索** | 词汇搭配以权威文献数据库（如 Europe PMC, PubMed, Web of Science）的客观搭配为准，不自行生造（R2） |
| **被引文献用词尊重** | 描述前人研究时，沿用被引文献的标准术语与指标名称（S10 边界②） |
| **多来源综合引用** | 多个来源共同支持同一宏观命题属于学术通行写法，予以保留；仅在各文献分别支持不同子项时才拆解（S12） |
| **标准体裁与语态保护** | Methods 部分的规范被动语态享有体裁保护；统计结果汇报遵循 APA/领域标准标点格式（§7） |
| **构念细分不可合并** | 领域内具有独立测量维度的构念（如 `response inhibition` 与 `interference control`）不得粗暴统一 |
| **学术论证最高优先** | 当规则修改与作者论证意图冲突时，论证优先 |

### 11.3 C 类 — 作者指纹（个性化配置）

针对作者个人文风习惯，本项目已提供解耦的配置文件模板：
`author_profile.template.yaml`。

作者可复制该文件为 `author_profile.yaml`，按需配置：
1. **语言与拼写体系**：美式英语（`american`）或英式英语（`british`）；是否允许引言与路线图使用第一人称。
2. **句法节奏容忍度**：长句（>35词）比例容忍度（默认 12%）；正文分号保留策略；修辞问句严格禁止或按需保留。
3. **论证与引用偏好**：保留叙述式引用（Narrative Citations）还是偏好括号引用；是否主动剪裁非必要列表与幽灵对立；认识强度谨慎度。
4. **学科白名单**：自定义免检构念与核心术语。

**执行规则**：
- 未提供 `author_profile.yaml` 时，系统仅执行 A 类与 B 类约束；任何纯文风特征最多判定为 `待作者判断`，绝不擅自输出 `需修改`。
- 当且仅当作者提供了配置文件或在会话中明确了个人偏好时，相关指纹规则才可升级为 `需修改` 裁决。
