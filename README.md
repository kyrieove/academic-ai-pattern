# academic-ai-pattern

<p align="right">
  <b>English</b> | <a href="README_zh.md"><b>简体中文</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Supported Agents](https://img.shields.io/badge/Agents-Codex%20%7C%20Claude%20Code%20%7C%20DeepSeek%20%7C%20Antigravity-brightgreen.svg)](#-installation--usage)

> **Evidence-backed, non-destructive AI-writing pattern auditor for academic English.**  
> Built for peer-reviewed empirical papers. Surfaces structural generation flaws with high recall, natively eliminates AI defensive writing (preemptive hedging and disclaimers), and provides transparent read-only diagnostic reports while strictly safeguarding experimental designs, statistical facts, and disciplinary terminology. Native support for OpenAI Codex, Claude Code, DeepSeek / Harness, and Google Antigravity.

---

### 🚀 Installation & Quickstart (立即安装与调用)

The standard way to install AI Agent skills across modern ecosystems is via the universal [skills.sh](https://skills.sh) CLI (`npx skills add`). It automatically detects your agent environment and routes files to the appropriate directory.

#### Quick Install (Universal)
```bash
npx skills add kyrieove/academic-ai-pattern
```

---

#### Agent-Specific Commands (Ordered)

#### 1. OpenAI Codex
Install for Codex via CLI:
```bash
npx skills add kyrieove/academic-ai-pattern --agent codex
```
Prompt in Codex:
```text
Run $academic-ai-pattern on manuscript.docx and generate a versioned audit report.
```

#### 2. Claude Code
Install directly into Claude Code's skills directory:
```bash
npx skills add kyrieove/academic-ai-pattern --agent claude-code
```
Invoke in Claude Code:
```text
/academic-ai-pattern audit manuscript.docx
```

#### 3. DeepSeek / Harness
Install into your DeepSeek workspace or Agent Harness:
```bash
npx skills add kyrieove/academic-ai-pattern
```
Or manually symlink `SKILL.md` and `references/` into your harness prompt directory.

#### 4. Google Antigravity
**Recommended Project-Level Install** (Run at the root of your manuscript directory; select Universal / General Agent to install into `.agents/skills/`):
```bash
npx skills add kyrieove/academic-ai-pattern
```
> 💡 **Note**: Google Antigravity natively scans and mounts `.agents/skills/` from the workspace root. If installing globally (`-g`), select **Universal / General Agent** at the interactive prompt.

Invoke in Antigravity chat:
```text
Use $academic-ai-pattern to audit manuscript.docx.
```

#### 5. Standalone CLI (Python, Zero-Node Fallback)
If you don't use Node.js or an Agent framework, run directly with Python:
```bash
git clone https://github.com/kyrieove/academic-ai-pattern.git
cd academic-ai-pattern

# Extract and scan
python scripts/extract_document.py examples/sample_paper.md --output temp_extract.json
python scripts/scan_all_candidates.py temp_extract.json --output temp_candidates.json --markdown temp_ledger.md
python scripts/validate_report.py examples/sample_report.md temp_extract.json --source examples/sample_paper.md
```
---

### 🎯 The Problem & Three Core Principles (痛点与三大铁律)

Commercial "AI paraphrasers" and "AI detectors" actively damage academic manuscripts, while mainstream LLMs (especially Codex and Claude) suffer from innate generation defects:
- **Mechanical Synonyms Destroy Precision**: General tools blindly replace essential domain terminology with strange synonyms or invert causal claims, leading peer reviewers to criticize *"poor English and unnatural phrasing"*.
- **Opaque Probabilistic Scores**: Flagging a manuscript as *"74% AI-generated"* gives authors zero actionable guidance on which specific sentence or cognitive mechanism failed.
- **Punishing Disciplinary Conventions**: 4-group experimental designs, APA standard passive voice in Methods, and authorized literature phrases are routinely misflagged as "unnatural redundancy".
- **Pervasive LLM "Defensive Writing" Dilutes Authority**: Trained to evade accountability, commercial LLMs obsessively open with self-limiting disclaimers (*"While this study does not claim to offer a complete theory..."*), stack timid modal hedges (*"might tentatively suggest that X could potentially..."*), and frame arguments negatively (*"We do not argue that..."*), squandering valuable introductory space on apologetic caveats and gutting the manuscript's scholarly authority.

**Our Non-Negotiable Boundaries:**
1. **Zero-Tampering (Read-Only)**: We audit, diagnose, and provide evidence; we never modify your original text, formatting, or citations.
2. **Form Locates, Mechanism Convicts**: A colon, a list, or a transition only locates a candidate. A verdict requires proving an underlying cost-saving generation failure (M1–M6).
3. **Empirical Fact Protection**: Experimental conditions, numerical contrasts, construct boundaries, and literature phrases enjoy genre-protected immunity.

> 🛡️ **Core Defensive Philosophy: High-Recall Priority — Zero Tolerance for Slop Leakage (宁误判不漏检)**  
> Why do we strictly enforce a *"prefer false alarms over missing AI slop"* audit policy?  
> In rigorous peer-reviewed international journals (SCI/SSCI), expert reviewers treat AI writing artifacts with **zero tolerance**. If an audit tool misses even one or two glaring AI clichés (such as ungrounded phantom contrasts `not X but rather Y`, inflated hollow praise `plays a pivotal role`, or theatrical rhetorical questions), the reviewer's confidence in the paper's intellectual honesty, experimental rigor, and original contribution collapses immediately.  
> Therefore, `academic-ai-pattern` enforces an **aggressive High-Recall First** architecture: we would rather flag an author's ambitious compound sentence or stylistic flourish for conscious author review (classified under `⚖️ Author Discretion`) than risk letting a single commercial LLM shortcut slip through to a critical referee. You, the human author, always retain the final decision.

---

### 🎯 Deep Integration: Detecting & Eliminating AI "Defensive Writing" (Eliminating Defensive Writing)

Modern large language models (particularly OpenAI Codex, Claude, and heavily aligned RLHF models) have an innate tendency toward **Defensive Writing** when polishing scientific prose. Trained to evade accountability and negative feedback, models frequently bury core findings under layers of apologetic hedging, preemptive disclaimers, and timid qualifications:

- **Opening with Preemptive Disclaimers**: Disparaging one's own contribution before stating it (*"While this study does not claim to offer a comprehensive theory..."*);
- **Stacked Modal Hedging**: Multiplying timid modals (*"might tentatively suggest that X could potentially influence Y"*), crippling the manuscript's analytical authority;
- **Negative Framing**: Obsessively explaining what the paper **does not** do (*"We do not argue that..."*) rather than positively articulating what it contributes;
- **Scattering Caveats Preemptively**: Littering abstracts and introductions with defensive disclaimers before presenting empirical evidence.

`academic-ai-pattern` directly integrates **Eliminating Defensive Writing** principles into its audit engine:
1. **Dismantles Negative Framing (S9 Phantom Contrasts & Defensive Antitheses)**: Strips gratuitous *"not X but rather Y"* formulas, steering authors toward **Positive Analytical Scope**;
2. **Prunes Stacked Hedging (S11 Epistemic Stance & Excessive Hedging)**: Purges timid clusters (*"might cautiously suggest that X could potentially..."*), ensuring that uncertainty is calibrated through empirical confidence intervals rather than apologetic prose;
3. **Restores Claim-Forward Precision**: Keeps legitimate methodological limits properly placed in Methods and Limitations, restoring authoritative, confident, and direct scholarly prose.

---

### 🏛️ Theoretical Foundation & Editorial Standards (理论与16大规则)

This project is built upon empirical publishing standards across international journals and computational linguistics research into large language model generation:

- **Scientific Editorial Foundations**:
  - **Semantic Contracts & Immutable Zones**: Grounded in scientific publication integrity (ICMJE, APA 7th ed.), enforcing strict non-modification boundaries for empirical data, sample sizes, and established construct names.
  - **Distributional Fault Code Architecture**: Rather than superficial keyword bans, evaluating structural patterns across paragraph boundaries (e.g., recursive functional slots, empty payoff clauses, and phantom contrasts).
  - **Evidence Hierarchy & Claim Alignment**: Ensuring claim strength matches experimental design (preventing ungrounded causal leaps or excessive defensive hedging).
- **Core Principles**:
  - ❌ **No AI Detector Evasion**: We reject superficial paraphrasing aimed at gaming commercial detectors; our goal is genuine academic rigor and peer-review acceptance.
  - ❌ **No Arbitrary Stylistic Bans**: We reject dogma like "eliminate all passive voice" or "ban all semicolons"—passive voice in Methods and precise semicolons in citations serve crucial scientific functions.
  - ❌ **Zero Hallucination / Zero Tampering**: Strictly forbidding the injection of ungrounded numbers, personal anecdotes, or fake specificity.

---

### 🧠 The 6 Cost-Saving Mechanisms (Why AI Feels Like AI)

> **Every true AI pattern stems from bypassing an intellectual cost that only human researchers pay:**

- **M1. Exhaustion Instead of Selection**: Using 4-verb chains or list stacking instead of making a conceptual decision on what to prune.
- **M2. Abstraction Instead of Mechanism**: Using vague placeholders (`plays a crucial role in`, `fosters integration`) instead of calculating the inferential steps.
- **M3. Evaluating for the Reader**: Overusing subjective hype (`important`, `crucial`, `fascinating`) instead of trusting readers with empirical data.
- **M4. Routine Loops**: Recursively calling the same structural template (e.g., "abstract claim : concrete expansion").
- **M5. Cohesion Breakdowns**: Ordering ideas only for the writer, leaving paragraph boundaries disconnected.
- **M6. Rhetorical Posture Over Evidence**: Over-hedging (`it may potentially seem...`) or inventing ungrounded phantom contrasts (`not X, but Y`).

---

### 📋 S1–S16 Fault Code Overview

| Code | Pattern Name | Core Symptom | Key Protection Test |
|---|---|---|---|
| **S1** | Verb Chains / List Stacking | Multiple verbs or nouns only conveying "volume" without selection | Experimental sample groups, conditions, outcome inventories |
| **S2** | Enumerated Justification | Substituting N weak reasons for a single moving argument | Each reason independently alters the thesis |
| **S3** | Hollow Abstraction | Naming a distinction without definition; shallow payoff | Surrounding context already provides agency and logic |
| **S4** | Colon + Expansion | Recurrent "abstract assertion : concrete breakdown" | Genuine definitions or standalone emphasis |
| **S5** | Demonstrative Drift (`that`) | Distancing an active referent currently in focal discussion | Grammatical that-clauses; time indexicals |
| **S6** | Template Repetition | Recycling identical argumentative slots across sections | Standardized Methods genre; core term consistency |
| **S7** | Broken Cohesion | Paragraph opening fails to resolve previous paragraph's tension | Headings or explicit discourse markers already connect |
| **S8** | Evaluative Adjectives | Telling the reader how to feel (`crucial`, `useful`, `notable`) | Cross-study empirical rankings (`strongest`, `clearest`) |
| **S9** | Phantom Contrasts | `not X but Y` or `rather than` without literature grounding | Genuine theoretical debates; condition comparisons |
| **S10** | Terminology Drift | Cycling synonyms for a single measured construct | Disciplinary construct distinction; cited author terms |
| **S11** | Epistemic Mismatch | Verbs or modal strength exceeding experimental design | Necessary design-coupled hedging |
| **S12** | Vague Attribution | Dense end-of-sentence citations without claim alignment | Multi-source consensus on a single macro-claim |
| **S13** | Portability Scaffolds | Plug-and-play openings, conclusions, or generic future work | Proposing domain-specific empirical consequences |
| **S14** | Strained Metaphors | Giving abstract constructs dramatic personified agency | Stable disciplinary metaphors (e.g., cognitive bottleneck) |
| **S15** | Rhetorical Questions | Posing questions in authorial prose and answering them | Official Research Questions; explicit title recalls |
| **S16** | Mechanical Navigation | Signposting roadmap sentences that add zero new boundaries | Long dissertation roadmaps; necessary cross-references |

---

---

## 🔍 6 Practical Examples: Before vs. After (6大实战前后对比)

Rather than superficial synonym swapping, `academic-ai-pattern` evaluates cognitive cost-saving mechanisms (M1–M6) alongside disciplinary protection tests. Below are five of the most prominent, unmistakable patterns:

---

### 1. S1 Consecutive Gerund Chains / List Stacking (连续动名词堆叠)
- **Before (AI Pattern)**:
  > *"Evaluating the autonomous control pipeline requires calibrating visual sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers."*
- **Mechanism Diagnosis (M1 Exhaustion Instead of Selection)**: Four consecutive `-ing` phrases mechanically enumerate every possible engineering step. Stacking creates an illusion of thoroughness while obscuring which specific operation actually bears the empirical argument.
- **Protection Test**: If this were the Methods section reporting 4 actual measured modules or conditions, it would be protected. In theoretical framing, it merely inflates text.
- **Scholarly Revision (After)**:
  > *"The evaluation nominally assesses control stability, but tracking accuracy critically depends on synchronizing telemetry data while evaluating dynamic sensor noise."*  
  *(Prunes non-essential steps; retains only the two operations that carry the actual inferential weight.)*

---

### 2. S4 Colon + Expansion (冒号＋展开)
- **Before (AI Pattern)**:
  > *"The distributed architecture fits real-time operations better because it requires none of this: it inherently expects packet loss, asynchronous node updates, and variable network latency."*
- **Mechanism Diagnosis (M2 Abstraction + M4 Routine Loop)**: The single most frequent AI pattern (*"abstract assertion : concrete breakdown"*). The colon promises the reader an "instant payoff", allowing vague assertions to survive. Human scholars integrate concrete mechanics directly.
- **Scholarly Revision (After)**:
  > *"The distributed architecture fits real-time operations better because it inherently accommodates asynchronous node updates and variable network latency."*  
  *(Removes the colon crutch; elevates the concrete mechanism directly into the predicate.)*

---

### 3. S8 Evaluative Sentences (评价式句子)
- **Before (AI Pattern)**:
  > *"This algorithmic trade-off is crucial to any scalable deployment, and the rationale is straightforward."*
- **Mechanism Diagnosis (M3 Evaluating for the Reader)**: Telling the reader how to feel (*"crucial"*, *"useful"*, *"straightforward"*, *"notable"*) instead of demonstrating significance through empirical facts. Reviewers consistently flag this as defensive or promotional rhetoric.
- **Scholarly Revision (After)**:
  > *"Any scalable deployment must directly resolve this algorithmic trade-off."*  
  *(Strips the subjective cheerleader adjectives; allows the methodological constraint to speak for itself.)*

---

### 4. S14 Strained / Theatrical Metaphors (造作比喻)
- **Before (AI Pattern)**:
  > *"The attention mechanism acts as an omniscient digital conductor, furiously orchestrating the chaotic symphony of multi-source sensory tokens."*
- **Mechanism Diagnosis (M6 Theatrical Posture Over Evidence)**: Fabricating dramatic, personified imagery (*"digital conductor"*, *"chaotic symphony"*) to simulate depth. Reviewers instantly spot this as synthetic and ungrounded.
- **Protection Test**: Standard disciplinary technical metaphors (*"attention bottleneck"*, *"gradient decay"*, *"computational pipeline"*) are strictly protected.
- **Scholarly Revision (After)**:
  > *"The attention mechanism applies dynamic weight matrices to prioritize high-saliency token embeddings across multimodal inputs."*  
  *(Replaces melodrama with precise, literal scientific mechanics.)*

---

### 5. S10 Terminology Drift / Synonym Cycling (术语身份漂移)
- **Before (AI Pattern)**:
  > *Paragraph 1: "The benchmark evaluated **response latency** across query batches..."*  
  > *Paragraph 2: "Reductions in **processing delay** improved overall throughput..."*  
  > *Paragraph 3: "These results demonstrate lower **execution lag** under peak load..."*
- **Mechanism Diagnosis (M4 Reckless Synonymization)**: Paraphrasers indiscriminately cycle synonyms to avoid repetition, causing readers and reviewers to mistake a single measured construct for three distinct performance variables.
- **Protection Test**: Distinct constructs must never be merged. However, for a single measured construct, lexical repetition represents scientific precision, not stylistic redundancy!
- **Scholarly Revision (After)**:
  > Standardize on the single, highest-frequency literature consensus term across the entire manuscript: **`response latency`**.

---

> 📄 **Looking for the complete end-to-end example?**  
> Browse the full synthetic empirical manuscript in [examples/sample_paper.md](examples/sample_paper.md) and its complete 37-candidate audit report in [examples/sample_report.md](examples/sample_report.md).


---

---

### 6. Eliminating AI Defensive Writing: From Apologetic Caveats to Claim-Forward Authority (破除AI防御性写作)
- **Before (Typical AI / Codex Defensive Slop)**:
  > *"While this study does not claim to offer a comprehensive theory of distributed caching, and although our evaluation is inherently restricted to synthetic benchmarks, our findings might tentatively suggest that adaptive scheduling could potentially mitigate transient queue congestion."*
- **Mechanism Diagnosis (Defensive Writing: Preemptive Apologies + Stacked Hedging + Negative Framing)**:  
  To evade accountability, commercial LLMs dilute prose with nested disclaimers (`While we do not claim...`) and stacked modal hedges (`might tentatively suggest that ... could potentially`). This apologetic tone squanders precious introductory real estate explaining what the paper *refuses to do*, obscuring its core contribution.
- **Claim-Forward Academic Reconstruction (After)**:
  > *"In 64-node benchmark evaluations, the adaptive scheduling policy reduced peak queue latency by 23.4% ($p < .001$), demonstrating that dynamic cache reallocation directly mitigates transient node congestion under high-throughput workloads."*  
  *(Revision Strategy: **Lead with the claim and evidence**; replace timid hedges with empirical data; keep necessary benchmark constraints in the Methods section, restoring direct, confident, and authoritative scholarly prose.)*

## 📊 Output & How to Use the Report (产出报告怎么读怎么改)

What exactly does `/academic-ai-pattern` output when auditing a paper? How should you read the report, and how should you process the findings?

### 1. Output Artifacts (产出产物)
Upon completing an audit, **your original manuscript remains strictly read-only and is never modified**. Instead, the skill generates structured companion diagnostic files in the same directory:
- 📑 `<stem>-ai-pattern-report.md`: **Main Audit Report** (Executive summary, S1–S16 coverage matrix, actionable checklist, detailed findings with minimal sufficient actions).
- 📑 `<stem>-ai-pattern-ledger.md`: **Full Adjudication Ledger** (Complete audit trail tracking every single candidate signal, rationale, and exact source quote).

---

### 2. How to Read the Report: Three-Tier Verdicts (怎么看)
This tool **never generates arbitrary "AI probability percentages"**. Instead, it delivers a **three-tier structured adjudication** aligned with rigorous peer-review standards:

| Verdict Flag | Meaning | Author Action |
|---|---|---|
| 🚨 **Needs Revision** (`需修改`) | Confirmed M1–M6 lazy generation shortcut that failed empirical protection tests (e.g., 4-verb chains, boilerplate future outlook, phantom contrasts). | **Action Recommended**: Apply surgical trimming following the provided direction and suggested rewrite. |
| ⚖️ **Author Discretion** (`待作者判断`) | Borderline stylistic choices or personal preferences (e.g., colon expansion, evaluative adjectives). | **Author Decision**: Keep if conceptually necessary; streamline if redundant. |
| 🛡️ **Protected** (`受保护`) | Matches a surface pattern but serves legitimate empirical functions (e.g., 4 experimental conditions, Methods passive voice, standard terminology). | **Preserve Intact**: Zero tampering. Protects your empirical rigor and facts. |

---

### 3. How to Process Findings: Practical Walkthrough (怎么处理)

Each finding is presented in a self-contained, actionable card. Below is an authentic finding entry from the report:

#### Authentic Finding Card Example:
> ### AP-S01-001
> **Category**: AI Pattern (S1 Consecutive Gerund Chain / List Stacking)  
> **Location**: `markdown-p0012`  
> **Trigger Snippet**:  
> `> Evaluating the autonomous control pipeline requires calibrating visual sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers.`  
> **Verdict**: 🚨 Needs Revision (`需修改`)  
> **Rationale**: Stacks four consecutive `-ing` gerund clauses to display process steps rather than making a selective argument (M1 Exhaustion over Selection).  
> **Protection Test**: Context is introduction rather than Methods design; trimming secondary operational steps preserves empirical facts.  
> **Action Direction**: Trim non-essential procedural steps; retain only the one or two actions carrying the core argument.  
> **Candidate Rewrite**:  
> `Evaluating an autonomous pipeline nominally assesses control stability, but tracking accuracy critically depends on synchronizing telemetry data while evaluating dynamic sensor noise.`

#### 4-Step Practical Workflow for Authors:
1. **Check the Action List**: Review the `## 行动清单` table at the top of the report to see the total number of action items.
2. **Execute Surgical Trimming**: For each `Needs Revision` item, locate the paragraph in your manuscript, consult the concise "Action Direction", and streamline the sentence (typically taking less than 30 seconds per item).
3. **Exercise Author Discretion**: For `Author Discretion` items, decide whether to simplify based on target journal guidelines.
4. **Preserve Protected Zones**: Leave all `Protected` items untouched, confident that your empirical design and terminology are justified.

---

### 💡 Experimental Exploration: Author Profile & Style Fingerprint (实验性文风探索)

Academic writing is never an assembly-line commodity. Seasoned researchers develop their own authentic "Authorial Voice" and argumentative rhythm over years of scholarship. Conventional de-AI tools typically enforce a rigid "one-size-fits-all" mold, mechanically penalizing complex, nuanced compound sentences or legitimate personal style as "AI-like".

`academic-ai-pattern` introduces the **Author Profile** mechanism, cleanly decoupling universal peer-review standards from an author's unique voice:
- **A Style Protection Compact**: Rather than an arbitrary constraint, it serves as a protective compact between the author and the audit tool. By declaring personal style tolerances and domain-specific terminology whitelists, your authentic academic voice is safeguarded against mechanical homogenization.
- **Quick Configuration (Ready to Use)**:
  Copy the configuration template to get started:
  ```bash
  cp author_profile.template.yaml author_profile.yaml
  ```
  Customizable dimensions include:
  - **Domain Whitelist**: Exclude your core variables and technical terminology from S1/S6/S10 false alarms;
  - **Syntactic Tolerances**: Threshold for long sentences (default 12%), semicolon preference, rhetorical question policies;
  - **Argumentation & Voice**: Preferences for narrative subject-verb citations (e.g., `Smith et al. argued that...`), first-person stance (`I / We`);
  - **Language Variants**: American (`american`) vs. British (`british`) conventions.

> 🚧 **Preliminary Construction Notice & Call for Community Ideas (初步建设阶段说明)**:  
> **Frankly, the Author Profile system is currently in its early experimental stage.**  
> Accurately defining and defending a researcher's individual style is a profound interdisciplinary challenge spanning computational linguistics, publishing ethics, and software design. Our ongoing exploratory roadmap includes:
> 1. **Auto-Profiling via Past Publications**: Exploring direct ingestion of 2–3 pre-LLM peer-reviewed papers by an author to automatically infer their authentic sentence-length distributions, connective preferences, and citation gestures;
> 2. **Domain & Journal Presets**: Exploring standardized profile baselines for distinct disciplines (e.g., theoretical mathematics vs. systems engineering vs. experimental cognitive science) or research groups.
> 
> **How should this system evolve to be more intuitive and powerful? We warmly invite your ideas!**  
> If you have thoughts, practical pain points, or suggestions from your own research, laboratory management, or peer-review workflows, please share your perspective in [GitHub Issues](https://github.com/kyrieove/academic-ai-pattern/issues)!

---

---

### 📂 Examples & Demonstration (样例与演示)

- [examples/sample_paper.md](examples/sample_paper.md): Full synthetic empirical manuscript evaluating multimodal cognitive load.
- [examples/sample_report.md](examples/sample_report.md): Validated audit report illustrating 37-candidate review decisions, action lists, and empirical protection rationale.

---

## ⚠️ Limitations & Beta Status (局限性与测试版说明)

> **Current Status**: Public Beta v0.9.x. Community feedback and contributions are warmly welcome!

While `academic-ai-pattern` adheres to a strict non-destructive, evidence-first audit philosophy, users should keep in mind the following boundaries:

1. **Target Genre**: Tailored specifically for **empirical research articles (SCI/SSCI), literature reviews, and academic theses**. It is not suited for creative writing, journalism, or advertising prose where subjective hyperbole is standard.
2. **Human-in-the-Loop Adjudication**: Syntactic patterns serve solely as diagnostic cues; **the author remains the ultimate decision-maker**. Frontier or interdisciplinary fields may have unique conventions that authors should evaluate in context.
3. **Citation Verification**: The tool audits internal logical coherence and claims-evidence fit locally. Whether cited literature is quoted out of context requires author domain expertise or web lookup.
4. **Community-Driven Refinement**: Writing conventions vary across disciplines (e.g., pure mathematics vs. experimental cognitive neuroscience). We invite researchers to test the skill on diverse manuscripts and suggest edge cases or improvements via [GitHub Issues](https://github.com/kyrieove/academic-ai-pattern/issues) to help refine the S1–S16 rulebook!

---

### 📄 License (开源许可证)

This project is licensed under the [MIT License](LICENSE).
