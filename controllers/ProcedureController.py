import os

import polars as pl

from interfaces.interfaces import GET_INFO
from models.Procedure import PROCEDURE
from services.union import UNION


class PROCEDURECONTROLLER(GET_INFO):
    @staticmethod
    def getInfo(
        dir_base: str, directory: str, archive: str, df: pl.DataFrame
    ) -> pl.DataFrame:
        procedures = pl.read_csv(
            os.path.join(dir_base, directory, archive),
            schema=PROCEDURE().procedure,
        )

        procedures_df = UNION.union_dataframes(origin=procedures, total=df)

        return procedures_df
