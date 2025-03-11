import os

import polars as pl

from interfaces.interfaces import GET_INFO
from models.User import USER
from services.union import UNION
from services.verified_entity import ENTITY


class USERCONTROLLER(GET_INFO):
    @staticmethod
    def getInfo(dir_base: str, directory: str, archive: str, df: pl.DataFrame):
        users = pl.read_csv(
            os.path.join(dir_base, directory, archive),
            schema=USER().user,
        )

        entity = ENTITY.entity_null(users, directory)
        df = UNION.union_dataframes(origin=entity, total=df)
        return df

    @staticmethod
    def add_facture(user_df: pl.DataFrame, facture: pl.DataFrame) -> pl.DataFrame:
        processed_facture = facture.select(
            pl.col("Numero de identificacion del usuario en el sistema").alias(
                "identificacion"
            ),
            pl.col("Numero de la factura"),
        ).unique(subset=["identificacion"])

        user_df = user_df.join(processed_facture, on="identificacion", how="left")

        user_df = user_df.with_columns(
            pl.coalesce(pl.col("Numero de la factura"), pl.lit("sin factura")).alias(
                "ingreso"
            )
        ).drop(["Numero de la factura"])

        return user_df
