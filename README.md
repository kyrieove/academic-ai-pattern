# academic-ai-pattern

English | [简体中文](README_zh.md)

**Locate problems in academic expression and argument, with evidence and traceable revision guidance.**

`academic-ai-pattern` combines six mechanisms, sixteen rule categories, and manuscript context to review English academic writing. Its reports explain where a problem occurs, why it requires attention, which information must be preserved, and how to address it. Authors use these findings to revise individual passages while retaining control of the source manuscript.

## Key strengths

| Strength | How it works | Value for authors |
|---|---|---|
| **Connects sentence form to argument structure** | M1–M6 and S1–S16 examine enumeration, abstraction, repeated functions, paragraph continuity, and evidence alignment | Reviews local wording and identifies missing links between definitions, inferences, and evidence |
| **Judges expressions by their academic function** | Applies preservation checks to experimental conditions, results lists, repeated terms, Methods procedures, and necessary hedging | Provides explicit reasons for retaining information when assessing a stylistic change |
| **Links recommendations directly to the source** | Each finding includes a location, quotation, rationale, and action direction; supported findings also include a candidate revision | Shows which passage needs attention, why it needs attention, and how to address it |
| **Makes the review process inspectable** | Retains original candidates and individual decisions, discloses scope, and checks source, inventory, and report consistency | Shows what has been reviewed and what still requires verification, allowing authors to challenge specific decisions |
| **Preserves the author's editorial choices** | Keeps the manuscript read-only, writes recommendations separately, and records preferences such as spelling and citation form | Lets authors select recommendations according to their research aims and writing preferences and edit the source themselves |
| **Turns corpus reading into a reusable baseline** | Distills author or field corpora by section and design, retains per-paper measures and writing observations, and produces PROFILE and BASELINE files | Supports subsequent manuscript reviews, author-style reference, and comparisons of journal writing practices from the same corpus |

The six examples below illustrate individual decisions. The [complete focused-review example](examples/sample_report.md) shows how the report corresponds to its adjudication ledger.

“AI pattern” retains the terminology of the project's rule manual. The rules examine specific problems in academic expression; a rule match is not evidence of AI authorship. The project does not produce AI-generation probabilities or detector scores.

## Scope

The primary intended inputs are empirical research articles and academic theses written in English. For reviews and other academic genres, define the scope explicitly and apply the relevant disciplinary and genre conventions.

The review procedure requires the source manuscript to remain read-only. Findings and candidate revisions are written to separate files, and authors review the recommendations before editing their manuscripts. Sample groups, measures, statistical results, necessary qualifications, and technical terms are assessed by their academic function. A list, repetition, or sentence form alone does not justify deletion.

The project has two entry points:

| Entry point | Task | Main outputs |
|---|---|---|
| Manuscript review | Locate candidates, examine context, and record individual decisions | Markdown report, candidate JSON, adjudication JSON |
| Corpus distillation | Summarize writing features and their scope from author or field corpora | `DNA/PROFILE.md`, layered observations, and `corpus/BASELINE.md` |

The two workflows can be used independently. Manuscript review does not require a corpus baseline.

## Usage

### Using the skill with an agent

Obtain the repository and load the complete directory using your agent environment's skill configuration. Retain the accompanying `scripts/`, `references/`, and `assets/` directories. [SKILL.md](SKILL.md) defines the entry procedure; installation paths and invocation syntax depend on the host environment.

```bash
git clone https://github.com/kyrieove/academic-ai-pattern.git
```

Once the skill is loaded, a request can take the following form:

```text
Use academic-ai-pattern to review manuscript.docx and produce a review report.
```

Fast review is the default. To request additional detail or restrict the scope:

```text
Run a deep review of manuscript.docx and explain the individual decisions.
Review only the Discussion of manuscript.docx, focusing on S10 and S11.
```

Both fast and deep modes require decisions for candidates within scope. Deep mode adds contextual quotations and decision details. Focused review marks rules outside its scope as unreviewed. Under the current output specification, analysis and decisions are written in Chinese; source quotations and candidate revisions retain their English wording.

### Running the supporting scripts

The scripts perform extraction, formal signal scanning, and report consistency checks. An agent or reviewer supplies semantic judgments, decision rationales, and report content. Running the scanner alone does not produce a complete review.

Python 3.10 or later is recommended. DOCX, Markdown, and TXT extraction use the Python standard library; PDF extraction additionally requires `pypdf` or `PyPDF2`. Check PDF extraction against the original pages to verify layout and paragraph boundaries. The bundled extractor does not perform OCR. DOCX extraction also has scope limits: headers, footers, comments, and text boxes are not extracted. Warnings should be disclosed in the report.

The commands below reproduce the supplied S1/S13 focused example from the repository root. Replace `<TMP_DIR>` with an existing temporary directory; retain the quotes for paths containing spaces.

```bash
python -X utf8 scripts/extract_document.py examples/sample_paper.md --output "<TMP_DIR>/extract.json"
python -X utf8 scripts/scan_all_candidates.py "<TMP_DIR>/extract.json" --rules S1 S13 --output "<TMP_DIR>/candidates.json"
python -X utf8 scripts/validate_report.py examples/sample_report.md "<TMP_DIR>/extract.json" --source examples/sample_paper.md --candidates "<TMP_DIR>/candidates.json" --ledger examples/sample_ledger.json
```

This example uses an existing report and adjudication ledger. For a new manuscript, complete the decisions and report before running validation. Changes to candidate IDs or source content require corresponding outputs to be regenerated.

## Review procedure

1. **Extract and delimit the text.** Record source SHA-256, block locations, extraction warnings, and the actual scanning scope.
2. **Establish manuscript context.** Identify the research objects, main claims, terms, directions, conditions, and evidence levels.
3. **Generate candidates.** Scan implemented formal signals and add semantic candidates found during reading, such as uncertain term identity or missing inferential relations. Zero scanner matches do not establish completion of a rule's review.
4. **Adjudicate individually.** Assess whether each candidate serves a necessary academic function. Specify an observable gap or a reason for preservation, and consult external sources when a decision depends on external facts.
5. **Report and verify.** Produce the report and ledger, run consistency checks, and separately assess whether candidate revisions preserve facts, scope, and evidential strength.

## Six mechanisms (M1–M6)

The six mechanisms organize the project's analysis around selection, inference, evaluation, control of repetition, the reader's perspective, and evidential constraints. M1–M6 explain how a problem appears in the text; S1–S16 locate and record its specific manifestations.

### M1 Enumeration in place of selection

**Writing task: decide what to retain and what to remove.** Verbs, reasons, or future directions are listed without explaining how each advances the argument. Review each item's independent function to distinguish necessary inventories from redundant enumeration.

Related rules: S1, S2, S13.

### M2 Abstraction in place of mechanism

**Writing task: make the inference explicit.** Abstract concepts or summary conclusions replace specific relations. A phrase such as `plays a crucial role in` names a role without stating its object, conditions, or evidential basis. Identify who infers what, from which evidence, through which intermediate step.

Related rules: S3, S4.

### M3 Evaluating on the reader's behalf

**Writing task: present the basis for evaluation.** Words such as `important`, `crucial`, and `fascinating` substitute for an account of the research's significance. Check whether the evaluation rests on an explicit comparison dimension or ordering of evidence. Remove evaluation that adds no information.

Related rules: S8, S13, S15.

### M4 Repeated use of default moves

**Writing task: track what earlier text has already established.** Repeated openings, colon expansions, or paragraph endings perform argumentative work already completed. Synonym changes for the same construct are also examined here. Assess functional redundancy and identity drift while retaining necessary repetition of technical terms.

Related rules: S4, S5, S6, S10.

### M5 Ordering solely from the writer's perspective

**Writing task: account for what the reader knows at this point.** Paragraphs follow the writer's arrangement of material without connecting to the questions, objects, or relations established in preceding text. Examine the link between each paragraph ending and the next opening, and whether signposting identifies an actual argumentative progression.

Related rules: S7, S13, S16.

### M6 Rhetorical form in place of evidence

**Writing task: align claims with evidence.** Contrasts, emphatic assertions, vague attribution, or rhetorical metaphors advance conclusions without corresponding support. Check the object, direction, conditions, and evidential strength of each claim. Apply the same requirement when adding or removing hedges.

Related rules: S9, S11, S12, S13, S14.

The six mechanisms support explanation and adjudication of textual problems, not identification of authorship or actual generation provenance.

## S1–S16 rule coverage

| Rule | Review target | Relevant distinction |
|---|---|---|
| S1 | Verb chains and lists | Redundant enumeration versus necessary conditions, procedures, or results |
| S2 | Enumerated reasons | Numbering conventions versus independently supported reasons |
| S3 | Abstract expression | Missing information versus concepts defined in context |
| S4 | Colon expansion | Repetitive scaffolding versus explicit definitions or lists |
| S5 | Demonstrative `that` | Confirmed personal preferences versus ordinary grammatical usage |
| S6 | Repeated wording or paragraph functions | Redundancy versus consistent terminology or necessary reference back |
| S7 | Paragraph continuity | Inferential gaps versus relations established by headings or context |
| S8 | Evaluative expression | Unsupported evaluation versus comparisons with explicit evidence dimensions |
| S9 | Contrast and negation | Unsupported opposition versus theoretical alternatives or scope restrictions |
| S10 | Term identity | Naming drift within a construct versus distinct measured objects |
| S11 | Epistemic strength | Claims exceeding evidence versus necessary uncertainty |
| S12 | Attribution and citation groups | Unclear support versus multiple sources supporting a synthesis |
| S13 | Argumentative scaffolding | Generic statements versus manuscript-specific functions |
| S14 | Metaphorical expression | Unclear rhetorical relations versus established technical usage |
| S15 | Questions and self-answering | Questions without argumentative development versus formal research questions |
| S16 | Navigation and metadiscourse | Redundant signposting versus necessary guidance |

See [quick-rules.md](references/quick-rules.md) for operational rules and [ai_pattern.md](ai_pattern.md) for detailed discussion. These categories are not a diagnostic scale validated across disciplines. Match counts describe candidates for review, not manuscript quality or detection accuracy.

## Six review examples

These synthetic teaching fragments illustrate reviews of lists, colons, evaluation, metaphor, terminology, and hedging. Each example states the source text, decision rationale, and action.

### 1. S1 Consecutive gerunds and lists

**Source:**

> Evaluating the autonomous control pipeline requires calibrating visual sensor feeds, synchronizing telemetry data packets, computing steering vectors, and validating fail-safe triggers.

**Decision: author judgment required.** The sentence names four distinct procedures: sensor calibration, telemetry synchronization, steering computation, and fail-safe validation. Four gerunds alone do not establish redundancy. Placement in an Introduction does not justify deleting technical facts.

**Action:** Check each procedure's argumentative function against the design and surrounding text. Remove confirmed duplication; retain procedures with distinct functions.

**Conservation check:** Introduce no claims about control stability, tracking accuracy, or causal relations absent from the source.

### 2. S4 Colons and expansion

**Source:**

> The architecture expects the following: packet loss, asynchronous node updates, and variable network latency.

**Decision: protected.** The colon introduces three explicit operating conditions. The sentence does not demonstrate repetitive, empty scaffolding.

**Action:** Retain the sentence. To assess repeated scaffolding across the manuscript, examine the function of each occurrence.

**Conservation check:** Retain packet loss, asynchronous node updates, and variable network latency.

### 3. S8 Unsupported evaluation

**Before:**

> The algorithm reduced response latency in this sample. These results are fascinating.

**Decision: needs revision.** The first sentence reports a result and its scope. The second expresses praise without adding a fact, comparison dimension, or inference.

**Candidate revision:**

> The algorithm reduced response latency in this sample.

**Conservation check:** Preserve the algorithm, outcome direction, and restriction to this sample. Add no sample size, effect size, or mechanism.

### 4. S14 Metaphor in place of an explicit relation

**Source:**

> The attention mechanism acts as an omniscient digital conductor, furiously orchestrating the chaotic symphony of multi-source sensory tokens.

**Decision: needs revision.** Conductor and symphony provide imagery without specifying how the attention mechanism processes sensory tokens.

**Action:** Ask the author to state the objects, operations, and relations defined by the actual method. The fragment supplies insufficient method information for a specific replacement sentence.

**Conservation check:** Do not introduce dynamic weight matrices, high-saliency embeddings, or other mechanisms absent from the source. Assess established technical metaphors by their definitions and usage.

### 5. S10 Term identity and related expressions

**Source:**

> The benchmark evaluated response latency. Processing delay was measured separately.

**Decision: protected.** Separately explicitly distinguishes the two measurements. Lexical similarity between latency and delay does not justify merging their names.

**Action:** Retain the two measurement names. Where other passages alternate among response latency, processing delay, and execution lag, compare their operational definitions: standardize names for the same measure and preserve distinctions between different measures.

**Conservation check:** Base terminology decisions on measurement identity, not frequency or surface similarity.

### 6. S11 Stacked hedges and claim strength

**Source:**

> Although our evaluation is restricted to synthetic benchmarks, our findings might tentatively suggest that adaptive scheduling could potentially mitigate transient queue congestion.

**Decision: author judgment required.** The sentence contains stacked hedges but supplies neither the design nor the results needed to determine evidential strength. Synthetic benchmarks explicitly limits its scope.

**Action:** Establish the warranted claim strength from the research design, measured results, and uncertainty evidence, then simplify the hedges. Retain the study scope and qualifications required by the evidence.

**Conservation check:** Add no node counts, percentages, p-values, or mechanisms. Do not turn a conclusion restricted to synthetic benchmarks into a general claim.

See [sample_report.md](examples/sample_report.md) for a manuscript review example and [sample_ledger.json](examples/sample_ledger.json) for individual decisions.

## Reports and decisions

Reports distinguish writing and argument patterns (`AP-Sxx`), internal factual inconsistencies (`AP-H`), and methodological risks (`AP-M`). Each candidate receives one of four decisions:

| Decision | Meaning |
|---|---|
| Needs revision (`需修改`) | The reviewer identifies a specific problem and provides evidence and an action direction |
| Author judgment required (`待作者判断`) | Context, author intent, or confirmed preferences are insufficient for a definite decision |
| Protected (`受保护`) | The expression serves a necessary academic function in this context and is retained |
| Verification incomplete (`核查未完成`) | A source or factual check required for the decision remains incomplete |

“Protected” concerns the expression's function in the current candidate. It does not certify the underlying data, references, or methods. All revision recommendations remain subject to author review.

For file inputs, the main outputs are listed below. A new version number is selected when a corresponding output already exists.

| File | Contents |
|---|---|
| `<stem>-ai-pattern-report.md` | Scope, coverage table, action list, findings, and limitations |
| `<stem>-ai-pattern-candidates.json` | Original scanner candidates, locations, counts, and scope |
| `<stem>-ai-pattern-ledger.json` | Individual decisions, semantic additions, and finding links |

Candidate revisions are restricted to “needs revision” findings and must explain preservation of facts and argumentative relations. If the source does not support a specific revision, the report identifies the information the author needs to supply.

The output specification is in [report-schema.md](references/report-schema.md). The [sample report](examples/sample_report.md) and its [ledger](examples/sample_ledger.json) demonstrate an eight-candidate S1/S13 focused review of a synthetic teaching manuscript. References in that manuscript have not been verified.

## Author preferences and corpus baselines

The [author profile template](author_profile.template.yaml) records preferences such as spelling and citation form. Personal preferences require user confirmation and cannot override constraints on facts, construct identity, or evidential strength.

Corpus distillation starts only on explicit request; its procedure is described in [distill.md](references/distill.md). The L1 script selects indexed extracts by section and research design, computes per-paper language measures, and summarizes them. Structure, evidence strategies, and argumentative relations still require reading and interpretation.

`DNA/PROFILE.md` records writing features and their scope. `corpus/BASELINE.md` records preservation evidence traceable to specific papers. A usage found in a corpus establishes its occurrence, but does not by itself establish appropriateness in the current manuscript. Failure to find a usage likewise does not establish an error.

Baseline calibration requires independent annotations and checks both false alarms on legitimate expressions and missed substantive problems. A reduction in the number of “needs revision” decisions alone does not establish effectiveness.

## Validation and limitations

The repository includes regression checks for extraction, candidate–decision correspondence, numerical checks, and corpus selection:

```bash
python -m unittest discover -s tests -v
```

The validator checks report structure, source hashes, quotation locations, and ledger consistency. It also rescans the source extraction to verify the original candidate inventory. Passing tests establishes expected behavior for the tested cases, not the correctness of semantic judgments.

The repository does not currently provide independently annotated cross-disciplinary evaluation results from which accuracy, recall, or false-positive rates could be reported. Decisions depend on the model, available context, extraction quality, domain knowledge, and source accessibility. Check each candidate revision against the source for preservation of qualifications and argumentative relations.

The project is intended to support author self-review and documented manuscript reading. Its outputs do not establish AI authorship, research validity, or publication outcomes.

## Feedback and license

Reproducible issues can be submitted through [Issues](https://github.com/kyrieove/academic-ai-pattern/issues). Useful reports include the rule, necessary context, actual and expected decisions, and reasons for the expected judgment. Use authorized or anonymized excerpts when working with unpublished manuscripts.

Code and documentation are distributed under the [MIT License](LICENSE). This license does not extend to manuscript corpora supplied by users.
