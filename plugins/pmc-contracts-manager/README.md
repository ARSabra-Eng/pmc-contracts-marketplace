# PMC Contracts Manager — ZCode Plugin

A [ZCode](https://zcode.z.ai) plugin that turns the agent into a **professional Contracts Manager for PMC (Project Management Consultancy) work**, built on the **FIDIC 2017** suite (Red / Yellow / Silver Books). It covers the **full contract lifecycle** and always works from the **Engineer / PMC neutral-administrator perspective**.

> ⚠️ **Important:** This plugin provides contract-administration drafting and process support. It is **not legal advice**. Always verify deadlines and entitlements against your project's own Particular Conditions, Contract Data and applicable law.

---

## What's Inside — 8 Lifecycle Skills

| # | Skill | Covers |
|---|-------|--------|
| 1 | `contract-review` | Pre-award tender/contract review, Particular Conditions deviation scan, contract risk register, qualification comments, red-flag list |
| 2 | `contract-mobilization` | Award → commencement: Contract Agreement (1.6), Performance Security (4.2), insurances (18), advance payment (14.2), Commencement Date (8.1), baseline programme review (8.3), correspondence protocol (1.3) |
| 3 | `contract-administration` | Day-to-day admin: Engineer instructions (3.3), notices register, 10-register suite, Contemporary Records (20.1), meeting minutes, monthly PMC report |
| 4 | `claim-notice-management` | Clause 20 regime: 28-day Notice of Claim, time-bar math (worked examples), claims register, 42-day detailed claims & Engineer responses, 3.7 Agreement or Determination |
| 5 | `eot-delay-analysis` | EOT grounds (8.4), SCL Protocol delay methods (TIA, windows, as-planned vs as-built, collapsed as-built), criticality, concurrency & float, prolongation cost, assessment letters |
| 6 | `variation-management` | Variations (13.1–13.3), valuation (12.3), provisional sums (13.5), daywork (13.6), changes in legislation/cost (13.7/13.8), VO letters & register |
| 7 | `payment-final-account` | Payment cycle (14.3/14.6/14.7/14.8), advance payment & retention, Taking-Over (10.1), DNP & Performance Certificate (11.9), Final Statement/discharge/FCC (14.11–14.14), final account |
| 8 | `dispute-resolution` | Clause 21 escalation ladder (3.7 → NOD → DAAB → amicable → arbitration), deadlines, referral bundles, dispute avoidance |

Every skill includes: when to use, inputs to collect, step-by-step workflow, FIDIC 2017 clause reference tables, deadline math, letter/register/report templates, and a QA checklist.

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

- Skills are plain Markdown at `plugins/pmc-contracts-manager/skills/<name>/SKILL.md` — edit freely.
- Common edits: hardcode your standard Contract Data values (retention %, DNP, delay-damages cap), adjust letter skeletons to house style, add project-specific QA items.
- Want more? Add a `commands/` folder (slash commands) or `agents/` (a dedicated Contracts Manager subagent) per the ZCode plugin docs — the manifest in `.zcode-plugin/plugin.json` supports both.

## Version

1.0.0 — FIDIC 2017 baseline, PMC/Engineer perspective, English.
