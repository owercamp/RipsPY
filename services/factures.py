import polars as pl


class FACTURE_NUMBER:
    def uniques_factures(self, *args) -> pl.DataFrame:
        unique = pl.DataFrame(
            schema={
                "Numero de la factura": pl.String,
                "Numero de identificacion del usuario en el sistema": pl.String,
            }
        )

        for item in args[0]:
            facture = item.select(
                pl.col("Numero de la factura"),
                pl.col("Numero de identificacion del usuario en el sistema"),
            ).unique(subset=["Numero de la factura"])
            unique = pl.concat([unique, facture])

        return unique.unique(subset=["Numero de la factura"])
