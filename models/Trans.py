import polars as pl


class TRANS:
    def __init__(self: pl.DataFrame) -> pl.DataFrame:
        self.transaction = {
            "Codigo del Prestador": pl.String,
            "Razon Social o Apellidos y nombres del prestador": pl.String,
            "Tipo de Identificacion": pl.String,
            "Numero de Identificacion": pl.String,
            "Numero de la factura": pl.String,
            "FECHA": pl.Date,
            "Fecha de Inicio": pl.Date,
            "Fecha final": pl.Date,
            "Codigo entidad Administradora": pl.String,
            "Nombre entidad administradora": pl.String,
            "Numero del Contrato": pl.String,
            "Plan de Beneficios": pl.String,
            "Numero de la poliza": pl.String,
            "Valor total del pago compartido COPAGO": pl.Int8,
            "Valor de la comision": pl.Int8,
            "Valor total de Descuentos": pl.String,
            "Valor Neto a Pagar por la entidad Contratante": pl.String,
        }
