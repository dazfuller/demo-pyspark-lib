from typing import List

from pyspark.sql.dataframe import DataFrame
from tests.PySparkTestCase import PySparkTestCase
import unittest
from pyspark.sql import Row
import dazspark.utils as u


class TestUtilsColumnNameCleaning(unittest.TestCase):
    def test_removal_of_spaces(self):
        input: str = "Example Column Name"
        expected: str = "Example_Column_Name"
        self.assertEqual(expected, u.replace_invalid_chars(input))

    def test_removal_of_special_characters(self):
        input: str = "Life; Is {beautiful}\nif you let=(it).be\tso"
        expected: str = "Life_Is_beautiful_if_you_let_it_be_so"
        self.assertEqual(expected, u.replace_invalid_chars(input))

    def test_no_changes_on_valid_string(self):
        input: str = "example_name"
        expected: str = "example_name"
        self.assertEqual(expected, u.replace_invalid_chars(input))

    def test_multiple_spaces_collapse_to_single(self):
        input: str = "example . name"
        expected: str = "example_name"
        self.assertEqual(expected, u.replace_invalid_chars(input))

    def test_alternative_replace_char(self):
        input: str = "example_name"
        expected: str = "example~name"
        self.assertEqual(expected, u.replace_invalid_chars(input, replace_char="~"))


class TestUtilsColumnNameStandardisation(unittest.TestCase):
    def test_standardising_simple_column(self):
        input: str = "EXAMPLE COLUMN NAME"
        expected: str = "Example_Column_Name"
        self.assertEqual(expected, u.standardise_name(input))

    def test_multiple_special_characters(self):
        input: str = "Life; Is {beautiful}\nif you let=(it).be\tso"
        expected: str = "Life_Is_Beautiful_If_You_Let_It_Be_So"
        self.assertEqual(expected, u.standardise_name(input))

    def test_leading_and_trailing_seperator_chars(self):
        input: str = "{weird column}"
        expected: str = "Weird_Column"
        self.assertEqual(expected, u.standardise_name(input))


class TestUtilsColumnCleaningWithPySpark(PySparkTestCase):
    def test_dataframe_column_cleaning(self):
        expected_cols: List[str] = ["Item_Id", "Item_Name", "Value_Usd"]
        data_row: Row = Row("item.id", "item.name", "value (USD)")
        data = [
            data_row(1, "item 1", 123.45),
            data_row(2, "item 2", 543.21)
        ]

        df: DataFrame = self.spark.createDataFrame(data)
        standardised_df: DataFrame = u.standardise_data_frame(df)

        self.assertListEqual(expected_cols, standardised_df.columns)
