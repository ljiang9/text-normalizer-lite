import unittest

from text_normalizer import normalize, to_halfwidth


class TestHalfwidth(unittest.TestCase):
    def test_fullwidth_letters(self):
        self.assertEqual(to_halfwidth("Ｈｅｌｌｏ"), "Hello")
        self.assertEqual(to_halfwidth("ＡＢＣ１２３"), "ABC123")

    def test_fullwidth_space(self):
        self.assertEqual(to_halfwidth("ａ　ｂ"), "a b")


class TestNormalize(unittest.TestCase):
    def test_nfkc(self):
        self.assertIn("1", normalize("①"))

    def test_collapse_ws(self):
        self.assertEqual(normalize("a   b\tc\nd"), "a b c d")

    def test_case_lower(self):
        self.assertEqual(normalize("HELLO World", case="lower"), "hello world")

    def test_case_upper(self):
        self.assertEqual(normalize("hello", case="upper"), "HELLO")

    def test_fullwidth_to_half(self):
        out = normalize("价格：１００元！")
        self.assertIn("100", out)

    def test_pipeline(self):
        out = normalize("Ｈｅｌｌｏ　世界！！  你好  ", case="lower")
        self.assertEqual(out, "hello 世界!! 你好")

    def test_strip(self):
        self.assertEqual(normalize("   hi   "), "hi")


if __name__ == "__main__":
    unittest.main()
