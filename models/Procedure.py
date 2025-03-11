import polars as pl


class PROCEDURE:
    def __init__(self: pl.DataFrame) -> pl.DataFrame:
        self.procedure = {
            "Numero de la factura": pl.String,
            "Codigo del prestador de servicios de salud": pl.String,
            "Tipo de Identificacion del Usuario": pl.String,
            "Numero de identificacion del usuario en el sistema": pl.String,
            "Fecha del procedimiento": pl.Date,
            "Numero de Autorizacion": pl.String,
            "Codigo del procedimiento": pl.String,
            "Ambito de realizacion del procedimiento": pl.Int8,
            "Finalidad del procedimiento": pl.Int8,
            "Personal que atiende": pl.String,
            "Diagnostico principal": pl.String,
            "Codigo del diagnostico relacionado": pl.String,
            "Codigo del diagnostico de la Complicacion": pl.String,
            "Forma de realizacion del acto quirurgico": pl.String,
            "Valor del Procedimiento": pl.String,
        }
