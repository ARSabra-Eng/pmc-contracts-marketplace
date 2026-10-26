from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = (ROOT / "plugins/pmc-contracts-manager/skills/claim-notice-management/SKILL.md").read_text(encoding="utf-8")
DISPUTES = (ROOT / "plugins/pmc-contracts-manager/skills/dispute-resolution/SKILL.md").read_text(encoding="utf-8")


class ClaimNoticeManagementTests(unittest.TestCase):
    def test_fully_detailed_claim_uses_84_day_baseline(self):
        self.assertIn("Within **84 days**", CLAIMS)
        self.assertNotIn("Within **42 days** of awareness", CLAIMS)
        self.assertIn("25 May", CLAIMS)

    def test_late_notice_initial_response_and_deemed_validity_are_present(self):
        self.assertIn("20.2.2", CLAIMS)
        self.assertIn("14 days after receiving the Notice of Claim", CLAIMS)
        self.assertIn("deemed to be a valid Notice", CLAIMS)

    def test_time_bar_consequence_has_no_payment_survival_exception(self):
        self.assertNotIn("payment survives", CLAIMS.lower())
        self.assertNotIn("EOT and Cost die", CLAIMS)
        self.assertIn("not be entitled to any additional payment", CLAIMS)

    def test_contemporary_records_and_employer_claims_use_2017_references(self):
        self.assertIn("20.2.3", CLAIMS)
        self.assertNotIn("Employer's Financial Claims (2.5)", CLAIMS)
        self.assertNotIn("(2.5 / Clause 20 employer claims)", CLAIMS)

    def test_determination_nod_uses_28_days(self):
        self.assertIn("Within **28 days** after receiving the Engineer's determination", CLAIMS)
        self.assertNotIn("14-day NOD", CLAIMS)

    def test_claim_agreement_and_determination_clocks_are_distinguished(self):
        self.assertIn("3.7.3", CLAIMS)
        self.assertIn("further **42 days**", CLAIMS)
        self.assertIn("deemed to have rejected the Claim", CLAIMS)
        self.assertNotIn("Interim response notice", CLAIMS)

    def test_continuing_effect_claims_are_covered(self):
        self.assertIn("20.2.6", CLAIMS)
        self.assertIn("monthly intervals", CLAIMS)
        self.assertIn("within **28 days** after the end of the effects", CLAIMS)


class DisputeResolutionTests(unittest.TestCase):
    def test_engineer_nod_and_daab_referral_use_2017_periods(self):
        self.assertIn("Within **28 days** after receiving the Engineer's determination", DISPUTES)
        self.assertIn("Within **42 days** after giving or receiving the 3.7.5 NOD", DISPUTES)
        self.assertNotIn("Within **14 days**", DISPUTES)

    def test_amicable_settlement_uses_28_day_window(self):
        self.assertIn("on or after the **28th day**", DISPUTES)
        self.assertNotIn("amicable settlement (56 days)", DISPUTES)
        self.assertNotIn("Attempts within **56 days**", DISPUTES)

    def test_nod_templates_use_prescribed_titles_and_periods(self):
        self.assertIn("Notice of Dissatisfaction with the Engineer’s Determination", DISPUTES)
        self.assertIn("Notice of Dissatisfaction with the DAAB’s Decision", DISPUTES)
        self.assertNotIn("within 14 / 28 days", DISPUTES)
        self.assertIn("within **42 days**", DISPUTES)

    def test_missed_daab_referral_invalidates_nod(self):
        self.assertIn("NOD shall be deemed to have lapsed", DISPUTES)

    def test_no_daab_route_is_covered(self):
        self.assertIn("21.8", DISPUTES)


if __name__ == "__main__":
    unittest.main()
