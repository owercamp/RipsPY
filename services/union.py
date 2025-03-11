import polars as pl


class UNION:
    @staticmethod
    def union_dataframes(origin: pl.DataFrame, total: pl.DataFrame) -> pl.DataFrame:
        total = pl.concat([total, origin])
        return total
