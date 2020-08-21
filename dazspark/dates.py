from datetime import datetime, timedelta, timezone
from typing import Optional

import pandas as pd
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import TimestampType

# The Excel epoch value. Whilst the actual epoch is the 1st January 1900, this is considered day 1
# and so we need to set the epoch to the day before
EXCEL_EPOCH = datetime(1899, 12, 30, tzinfo=timezone.utc)


def from_excel_date_func(serial: float) -> Optional[datetime]:
    """Parses an Excel serial to a datetime value with precision to the second.

    Excel stores dates as a decimal value such as 43913.66528, where the integer component is the number of days
    since the Excel epoch (1st January 1900), and the decimal component is a fractional part of the day.

    For a further explanation see: https://www.excelcse.com/how-does-excel-store-dates-and-times/

    Args:
        serial (float): The Excel serial date

    Returns:
        datetime: Parsed datetime as UTC
    """
    try:
        days: int = int(serial)
        millis: int = (serial - days) * 86400000
        return (EXCEL_EPOCH + timedelta(days=days, milliseconds=millis)).replace(microsecond=0)
    except ValueError:
        return None


@pandas_udf(TimestampType())
def from_excel_date(ess: pd.Series) -> pd.Series:
    """A scalar Pandas UDF for converting Excel serial dates to datetime values

    Args:
        ess (pd.Series): A series containing the Excel serial dates

    Returns:
        pd.Series: Parsed series of datetime value
    """
    return ess.apply(from_excel_date_func)
