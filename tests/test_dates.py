import unittest
from datetime import datetime, timezone

import pandas as pd
from pandas.testing import assert_frame_equal

from dazspark.dates import from_excel_date, from_excel_date_func
from tests.PySparkTestCase import PySparkTestCase


class TestExcelDateParsing(unittest.TestCase):
    def test_conversion_simple_date(self):
        excel_serial: float = 43913.66528
        parsed_dt: datetime = from_excel_date_func(excel_serial)

        self.assertEqual(parsed_dt, datetime(2020, 3, 23, 15, 58, tzinfo=timezone.utc))

    def test_leap_year_conversion(self):
        excel_serial: float = 43890.781400463
        parsed_dt: datetime = from_excel_date_func(excel_serial)

        self.assertEqual(parsed_dt, datetime(2020, 2, 29, 18, 45, 13, tzinfo=timezone.utc))

    def test_invalid_value_returns_none(self):
        self.assertIsNone(from_excel_date_func("INVALID"))

    def test_integer_value_returns_midnight(self):
        excel_serial: int = 43890
        parsed_dt: datetime = from_excel_date_func(excel_serial)

        self.assertEqual(parsed_dt, datetime(2020, 2, 29, tzinfo=timezone.utc))


class TestExcelDateParsingWithPySpark(PySparkTestCase):
    def run_spark_test(self, excel_values: pd.Series, expected_dts: pd.Series) -> None:
        excel_values.name = "excel_serial"
        expected_dts.name = "parsed_dt"
        expected_df = pd.concat([excel_values, expected_dts], axis=1)

        df = (self.spark
              .createDataFrame(pd.DataFrame(excel_values))
              .withColumn("parsed_dt", from_excel_date("excel_serial"))
              .toPandas())

        try:
            assert_frame_equal(expected_df, df)
        except AssertionError as e:
            raise self.failureException("DataFrame objects are not the same") from e

    def test_simple_parsing(self):
        data = pd.Series([43913.66528, 43890.781400463])
        parsed = pd.Series([datetime(2020, 3, 23, 15, 58), datetime(2020, 2, 29, 18, 45, 13)])
        self.run_spark_test(data, parsed)

    def test_null_value_handling(self):
        data = pd.Series([43913.66528, None])
        parsed = pd.Series([datetime(2020, 3, 23, 15, 58), None])
        self.run_spark_test(data, parsed)
