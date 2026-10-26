# PMC Contracts Manager — ZCode Plugin

A [ZCode](https://zcode.z.ai) plugin for **professional Contracts Manager support in PMC (Project Management Consultancy) work**, covering the full contract lifecycle from an Engineer/PMC administration perspective. Its detailed contractual rules use the **FIDIC Red Book 2017 General Conditions baseline**; always confirm the book, edition, Particular Conditions, Special Provisions, and Contract Data before applying them.

> ⚠️ **Important:** This plugin provides contract-administration drafting and process support. It is **not legal advice**. Always verify deadlines and entitlements against your project's own Particular Conditions, Contract Data and applicable law.

---

## What's Inside — 8 Lifecycle Skills

| # | Skill | Covers |
|---|-------|--------|
| 1 | `contract-review` | Pre-award review, Particular Conditions deviation scan, risk register, qualification comments, escalation triggers |
| 2 | `contract-mobilization` | Contract Agreement (1.6), Performance Security (4.2), Insurances (19), advance payment (14.2), Commencement Date (8.1), initial programme (8.3), correspondence (1.3) |
| 3 | `contract-administration` | Engineer instructions (3.5), Notices and registers, Contemporary Records (20.2.3), meeting minutes, monthly PMC reporting |
| 4 | `claim-notice-management` | Clause 20 regime: 28-day Notice, 84-day fully detailed Claim, late-Notice response, claims register, 3.7 Agreement or Determination |
| 5 | `eot-delay-analysis` | EOT under 8.5, delay-analysis methods, criticality, concurrency under Special Provisions, separate time/payment entitlement, assessment letters |
| 6 | `variation-management` | Variations (13.1–13.7), valuation (12.3), Provisional Sums (13.4), Daywork (13.5), Changes in Laws/Cost (13.6/13.7), instruction notices and register |
| 7 | `payment-final-account` | Statements, IPCs and payment (14.3/14.6/14.7/14.8), advance and retention, Taking-Over (10.1), Performance Certificate (11.9), Final Statement/discharge/FPC (14.11–14.14) |
| 8 | `dispute-resolution` | Clause 21 escalation (3.7 → NOD → DAAB → amicable settlement → arbitration), deadlines, referral bundles, dispute avoidance |

Each skill provides trigger conditions, structured workflows, verified Red Book 2017 references, practical controls or templates, and a QA checklist.

---

## Install (Local Marketplace — Recommended)

1. Unzip `pmc-contracts-manager-plugin.zip` to any folder on your machine.
2. In ZCode: **open any workspace** (the Plugins page requires one).
3. Go to **Settings → Plugins**, click **Create → Add marketplace** (top-right).
4. Point it at the unzipped folder (the one containing `marketplace.json`), or paste its path. ZCode validates it.
5. Find **pmc-contracts-manager** under the **Personal** segment → click **Install** → keep it **enabled**.
6. Done — the 8 skills are now live. View them under **Settings → Skills → Plugin skills**.

> After editing any `SKILL.md`, open **Marketplace sources** (gear icon) → **Refresh this marketplace**, and restart the conversation so skills reload.

## Install (Manual Skills Copy — Alternative)

Copy each `plugins/pmc-contracts-manager/skills/<skill-name>/` folder into your user skills directory, e.g. `~/.claude/skills/` (the location ZCode uses for user skills). Then restart the session and verify under **Settings → Skills**. The marketplace route is preferred because the plugin stays updatable as one unit.

---

## Using The Plugin

Skills trigger **automatically** when your request matches them. You can also invoke deliberately: type `$` in the ZCode input box and pick a skill, or just ask. Examples:

- *"Review the attached Particular Conditions and produce a contract risk register"* → `contract-review`
- *"We received a Notice of Claim from the Contractor dated 12 March for delayed drawings — check time-bar validity and draft the Engineer's acknowledgment"* → `claim-notice-management`
- *"The Contractor claims 45 days EOT for employer-caused delay — assess it using TIA on the accepted programme"* → `eot-delay-analysis`
- *"Draft a Variation Instruction for the additional pile caps and set out the 12.3 valuation basis"* → `variation-management`
- *"Review this monthly statement and draft the Interim Payment Certificate with reasoned deductions"* → `payment-final-account`
- *"The Employer is dissatisfied with my determination — set out the Clause 21 escalation path and deadlines"* → `dispute-resolution`

**Pro tip:** at the start of a project, run *"Summarize the Contract Particulars from the attached Contract Data and set up the mobilization checklist"* (`contract-mobilization`) — then tell the agent those particulars in later sessions so deadline math is project-accurate.

## Customizing

- Skills are plain Markdown at `plugins/pmc-contracts-manager/skills/<skill-name>/SKILL.md` — edit freely.
- Common edits: hardcode your standard Contract Data values (retention %, DNP, delay-damages cap), adjust letter skeletons to house style, add project-specific QA items.
- Want more? Add a `commands/` folder (slash commands) or `agents/` (a dedicated Contracts Manager subagent) per the ZCode plugin docs — the manifest in `.zcode-plugin/plugin.json` supports both.

## Version

1.0.1 — Corrected FIDIC Red Book 2017 guidance across all eight skills, with expanded regression coverage.
