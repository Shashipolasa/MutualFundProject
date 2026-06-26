import unittest
from src.etl.normalizer import normalize_year, normalize_ticker


class TestNormalizer(unittest.TestCase):

    def test_year_string(self):
        self.assertEqual(normalize_year("2023"), 2023)

    def test_year_spaces(self):
        self.assertEqual(normalize_year(" 2022 "), 2022)

    def test_year_int(self):
        self.assertEqual(normalize_year(2021), 2021)

    def test_invalid_year(self):
        self.assertIsNone(normalize_year("abcd"))

    def test_ticker_lower(self):
        self.assertEqual(normalize_ticker("tcs"), "TCS")

    def test_ticker_spaces(self):
        self.assertEqual(normalize_ticker(" infy "), "INFY")

    def test_ticker_none(self):
        self.assertIsNone(normalize_ticker(None))


if __name__ == "__main__":
    unittest.main()
