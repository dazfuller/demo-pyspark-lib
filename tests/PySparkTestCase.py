import unittest

from pyspark.sql import SparkSession


class PySparkTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = SparkSession.builder.appName("unittests").master("local[2]").getOrCreate()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.spark.stop()
