import polars as pl


class ENTITY:
    def entity_null(df: pl.DataFrame, directory: str) -> pl.DataFrame:
        if directory == "ZONA INDUSTRIAL" or directory == "CALLE 103":
            return df.with_columns(pl.col("entidad_administradora").fill_null("SDS001"))

        if directory == "BUCARAMANGA":
            return df.with_columns(pl.col("entidad_administradora").fill_null("68001"))

        if directory == "MEDELLIN":
            return df.with_columns(pl.col("entidad_administradora").fill_null("EAS016"))

        if directory == "PEREIRA":
            return df.with_columns(pl.col("entidad_administradora").fill_null("66000"))

        if directory == "IBAGUE":
            return df.with_columns(pl.col("entidad_administradora").fill_null("73000"))

        if directory == "CALI":
            return df.with_columns(pl.col("entidad_administradora").fill_null("EPS012"))
