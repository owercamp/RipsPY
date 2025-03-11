import calendar
from datetime import datetime

import polars as pl


class DAYEND:
    @staticmethod
    def getDayEnd():
        today = datetime.today()
        # Ajustar al mes anterior
        if today.month == 1:
            before_month = 12
            year = today.year - 1
        else:
            before_month = today.month - 1
            year = today.year

        # Obtener el último día del mes anterior
        _, end_day = calendar.monthrange(year, before_month)
        return datetime.strptime(
            f"{str(end_day).rjust(2, '0')}/{str(before_month).rjust(2, '0')}/{year}",
            "%d/%m/%Y",
        )


class FILTERDAYEND:
    @staticmethod
    def filterDate(df: pl.DataFrame, col: str) -> pl.DataFrame:
        return df.filter(pl.col(col) <= DAYEND.getDayEnd())
