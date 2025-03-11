import os

import polars as pl

from interfaces.interfaces import GET_INFO
from models.Trans import TRANS
from services.union import UNION


class TRANSCONTROLLER(GET_INFO):
    @staticmethod
    def getInfo(
        dir_base: str, directory: str, archive: str, df: pl.DataFrame
    ) -> pl.DataFrame:
        trans = pl.read_csv(
            os.path.join(dir_base, directory, archive),
            schema=TRANS().transaction,
        )

        transactions_df = UNION.union_dataframes(origin=trans, total=df)

        return transactions_df
