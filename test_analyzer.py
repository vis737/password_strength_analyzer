import unittest
from analyzer import analyze_password

class TestPasswordStrengthAnalyzer(unittest.TestCase):

    def test_empty_string(self):
        res = analyze_password("")
        self.assertEqual(res["score"], 0)
        self.assertEqual(res["label"], "Weak")
        self.assertFalse(res["checks"]["length"])
        self.assertFalse(res["checks"]["uppercase"])
        self.assertFalse(res["checks"]["lowercase"])
        self.assertFalse(res["checks"]["digit"])
        self.assertFalse(res["checks"]["special"])
        self.assertEqual(len(res["feedback"]), 5)

    def test_none_input(self):
        res = analyze_password(None)
        self.assertEqual(res["score"], 0)
        self.assertEqual(res["label"], "Weak")

    def test_all_digits(self):
        # 8 digits -> length=True, digit=True -> score 2 -> Weak
        res = analyze_password("12345678")
        self.assertEqual(res["score"], 2)
        self.assertEqual(res["label"], "Weak")
        self.assertTrue(res["checks"]["length"])
        self.assertTrue(res["checks"]["digit"])
        self.assertFalse(res["checks"]["uppercase"])
        self.assertFalse(res["checks"]["lowercase"])
        self.assertFalse(res["checks"]["special"])
        self.assertEqual(len(res["feedback"]), 3)

    def test_all_lowercase_short(self):
        # 5 lower chars -> length=False, lowercase=True -> score 1 -> Weak
        res = analyze_password("hello")
        self.assertEqual(res["score"], 1)
        self.assertEqual(res["label"], "Weak")

    def test_medium_password(self):
        # Length 8+, Upper, Lower, Digit, No special -> score 4 -> Medium
        res = analyze_password("Password123")
        self.assertEqual(res["score"], 4)
        self.assertEqual(res["label"], "Medium")
        self.assertFalse(res["checks"]["special"])
        self.assertEqual(len(res["feedback"]), 1)
        self.assertIn("Include at least one special character", res["feedback"][0])

    def test_strong_password(self):
        # All 5 pass -> score 5 -> Strong
        res = analyze_password("S3cur3P@ssw0rd!")
        self.assertEqual(res["score"], 5)
        self.assertEqual(res["label"], "Strong")
        self.assertEqual(len(res["feedback"]), 0)

    def test_spaces_and_unicode(self):
        # Spaces count as special characters
        res = analyze_password("Pass 123 ⚡")
        self.assertTrue(res["checks"]["special"])
        self.assertTrue(res["checks"]["uppercase"])
        self.assertTrue(res["checks"]["lowercase"])
        self.assertTrue(res["checks"]["digit"])
        self.assertTrue(res["checks"]["length"])
        self.assertEqual(res["score"], 5)
        self.assertEqual(res["label"], "Strong")

    def test_very_long_password(self):
        # 10,000 characters
        long_pass = "A" * 5000 + "a" * 5000 + "1" + "!"
        res = analyze_password(long_pass)
        self.assertEqual(res["score"], 5)
        self.assertEqual(res["label"], "Strong")

if __name__ == "__main__":
    unittest.main()
