import re
from typing import Optional


def replace_invalid_chars(col_name: str, replace_char: Optional[str] = "_") -> str:
    """Replace invalid characters in a string.

    These are characters which are not expected with the Parquet file format

    Args:
        col_name (str): The column name to have invalid characters removed from
        replace_char (str, optional): The character used to replace invalid characters with. Defaults to "_".

    Returns:
        str: [description]
    """
    return re.sub("[ ,;{}()\n\t=\\/.]", "_", col_name)


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
