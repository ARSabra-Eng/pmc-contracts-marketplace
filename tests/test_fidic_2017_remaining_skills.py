from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/pmc-contracts-manager/skills"


def skill(name):
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


class MobilizationTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("contract-mobilization")

    def test_commencement_uses_2017_rule(self):
        self.assertIn("not less than **14 days** before the Commencement Date", self.text)
        self.assertIn("within **42 days** after the Contractor receives the Letter of Acceptance", self.text)
        self.assertNotIn("28 days after the Engineer receives full performance security compliance", self.text)

    def test_initial_programme_clock_and_review_terms_are_correct(self):
        self.assertIn("within **28 days** after receiving the Notice under Sub-Clause 8.1", self.text)
        self.assertIn("Notice of No-objection", self.text)
        self.assertIn("14 days after receiving a revised programme", self.text)

    def test_clause_references_are_corrected(self):
        self.assertIn("Insurances (Clause 19)", self.text)
        self.assertIn("20.2.3", self.text)
        self.assertIn("8.8", self.text)


class AdministrationTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("contract-administration")

    def test_engineer_instruction_procedure_uses_3_5(self):
        self.assertIn("Engineer Instructions Discipline (Sub-Clause 3.5)", self.text)
        self.assertIn("deemed to have revoked the instruction", self.text)
        self.assertIn("7 days", self.text)

    def test_registers_use_2017_references(self):
        self.assertIn("Subcontractors (5.1/5.2)", self.text)
        self.assertIn("Key personnel (6.12)", self.text)
        self.assertIn("20.2.3", self.text)


class EotTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("eot-delay-analysis")

    def test_eot_and_advance_warning_are_distinguished(self):
        self.assertIn("EOT entitlement under Sub-Clause 8.5", self.text)
        self.assertIn("8.4 [Advance Warning]", self.text)
        self.assertIn("8.6 [Delays Caused by Authorities]", self.text)
        self.assertIn("8.7 [Rate of Progress]", self.text)

    def test_grounds_and_concurrency_follow_2017(self):
        self.assertIn("Clause 18 [Exceptional Events]", self.text)
        self.assertIn("Special Provisions", self.text)
        self.assertIn("13.3.1", self.text)

    def test_cost_and_nod_are_not_automatic(self):
        self.assertIn("EOT does not itself create an automatic entitlement to Cost or profit", self.text)
        self.assertIn("28-day NOD", self.text)


class VariationTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("variation-management")

    def test_instruction_and_request_for_proposal_are_distinguished(self):
        self.assertIn("13.3.1 — Variation by Instruction", self.text)
        self.assertIn("within **28 days**", self.text)
        self.assertIn("13.3.2 — Variation by Request for Proposal", self.text)

    def test_adjustment_references_are_corrected(self):
        for ref in ("13.4 [Provisional Sums]", "13.5 [Daywork]", "13.6 [Adjustments for Changes in Laws]", "13.7 [Adjustments for Changes in Cost]", "14.15 [Currencies of Payment]"):
            self.assertIn(ref, self.text)

    def test_valuation_thresholds_and_nod_are_corrected(self):
        self.assertIn("0.01% of the Accepted Contract Amount", self.text)
        self.assertIn("Cost per unit quantity", self.text)
        self.assertIn("28-day NOD", self.text)
        self.assertIn("3.5", self.text)


class PaymentTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("payment-final-account")

    def test_payment_and_interest_rules_are_corrected(self):
        self.assertIn("56 days", self.text)
        self.assertIn("after the Engineer receives the Statement and supporting documents", self.text)
        self.assertIn("three percent (3%)", self.text)

    def test_taking_over_trigger_and_deemed_date_are_corrected(self):
        self.assertIn("after receiving the Contractor’s Notice of application", self.text)
        self.assertIn("fourteenth day after the Engineer receives the Contractor’s Notice of application", self.text)

    def test_final_account_procedure_is_corrected(self):
        self.assertIn("Draft Final Statement", self.text)
        self.assertIn("Partially Agreed Final Statement", self.text)
        self.assertIn("within **56 days** of receiving a copy of the FPC", self.text)
        self.assertIn("within 21 days after the issue of the Performance Certificate", self.text)


class ContractReviewTests(unittest.TestCase):
    def setUp(self):
        self.text = skill("contract-review")

    def test_delay_payment_and_closeout_references_are_corrected(self):
        self.assertIn("8.5, 8.6, 8.8", self.text)
        self.assertIn("14.1–14.15", self.text)
        self.assertIn("1.15", self.text)

    def test_exceptional_events_insurance_and_claims_are_corrected(self):
        self.assertIn("Exceptional Events | 18", self.text)
        self.assertIn("Insurance | 19", self.text)
        self.assertIn("28-day Notice / 84-day fully detailed Claim", self.text)


class VersionTests(unittest.TestCase):
    def test_manifest_versions_are_1_0_1(self):
        marketplace = json.loads((ROOT / "marketplace.json").read_text(encoding="utf-8"))
        plugin = json.loads((ROOT / "plugins/pmc-contracts-manager/.zcode-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual("1.0.1", marketplace["plugins"][0]["version"])
        self.assertEqual("1.0.1", plugin["version"])

    def test_all_skill_and_readme_versions_are_1_0_1(self):
        for path in SKILLS.glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                self.assertRegex(path.read_text(encoding="utf-8"), r'version:\s*"1\.0\.1"')
        self.assertIn("1.0.1", (ROOT / "plugins/pmc-contracts-manager/README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
