import polars as pl


class CONSULT:
    def __init__(self: pl.DataFrame) -> pl.DataFrame:
        self.consult = {
            "Numero de la factura": pl.String,
            "Codigo del prestador de servicios de salud": pl.String,
            "Tipo de Identificacion del Usuario": pl.String,
            "Numero de identificacion del usuario en el sistema": pl.String,
            "Fecha de la consulta": pl.Date,
            "Numero de Autorizacion": pl.String,
            "Codigo de consulta": pl.String,
            "Finalidad de la consulta": pl.String,
            "Causa externa": pl.String,
            "Codigo del Diagnostico principal": pl.String,
            "Codigo del diagnostico relacionado Nº 1": pl.String,
            "Codigo del diagnostico relacionado Nº 2": pl.String,
            "Codigo del diagnostico relacionado Nº 3": pl.String,
            "Tipo de diagnostico principal": pl.Int8,
            "Valor de la consulta": pl.String,
            "Valor de la cuota moderadora": pl.Int8,
            "Valor neto a pagar": pl.String,
        }
