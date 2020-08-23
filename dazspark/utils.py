import re
from functools import reduce
from typing import Optional

from pyspark.sql import DataFrame


def replace_invalid_chars(col_name: str, replace_char: Optional[str] = "_") -> str:
    """Replace invalid characters in a string.

    These are characters which are not expected with the Parquet file format

    Args:
        col_name (str): The column name to have invalid characters removed from
        replace_char (str, optional): The character used to replace invalid characters with. Defaults to "_".

    Returns:
        str: [description]
    """
    return re.sub("_+", replace_char, re.sub("[ ,;{}()\n\t=\\/.]", replace_char, col_name))


def standardise_name(col_name: str) -> str:
    """Standardise a given column name.

    Removes all invalid characters and re-joins works in the name, capitalizing each part of the name, for example
    "token id" becomes "Token_Id"

    Args:
        col_name (str): The column name to standarise

    Returns:
        str: A standardised column name
    """
    return re.sub("_+", "_", "_".join([part.capitalize() for part in re.split("[ _]", replace_invalid_chars(col_name))]).strip("_"))


def standardise_data_frame(df: DataFrame) -> DataFrame:
    """Standardises the column names of a Spark DataFrame

    Args:
        df (DataFrame): The DataFrame to standardise the column names of

    Returns:
        DataFrame: DataFrame with columns renamed and standardised
    """
    return reduce(lambda acc, col: acc.withColumnRenamed(col, standardise_name(col)), df.columns, df)
