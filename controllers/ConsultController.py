import os

import polars as pl

from interfaces.interfaces import GET_INFO
from models.Consult import CONSULT
from services.union import UNION


class CONSULTCONTROLLER(GET_INFO):
    @staticmethod
    def getInfo(
        dir_base: str, directory: str, archive: str, df: pl.DataFrame
    ) -> pl.DataFrame:
        consults = pl.read_csv(
            os.path.join(dir_base, directory, archive), schema=CONSULT().consult
        )

        df = UNION.union_dataframes(origin=consults, total=df)
        return df
