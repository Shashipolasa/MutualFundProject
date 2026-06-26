import unittest
import pandas as pd

from src.etl.validator import (
    check_null_primary_key,
    check_duplicate_primary_key,
    check_duplicate_company_year,
)


class TestValidator(unittest.TestCase):

    def test_null_pk(self):
        df = pd.DataFrame({"id": [1, 2, None]})
        self.assertEqual(len(check_null_primary_key(df, "id")), 1)

    def test_duplicate_pk(self):
        df = pd.DataFrame({"id": [1, 2, 2, 3]})
        self.assertEqual(len(check_duplicate_primary_key(df, "id")), 2)

    def test_duplicate_company_year(self):
        df = pd.DataFrame({
            "company_id": [1, 1, 2],
            "year": [2023, 2023, 2022]
        })
        self.assertEqual(len(check_duplicate_company_year(df)), 2)


if __name__ == "__main__":
    unittest.main()
