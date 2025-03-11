from abc import ABC

import polars as pl


class GET_INFO(ABC):
    @staticmethod
    def getInfo(
        dir_base: str, directory: str, archive: str, df: pl.DataFrame
    ) -> pl.DataFrame:
        pass
