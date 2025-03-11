import polars as pl


class USER:
    def __init__(self: pl.DataFrame) -> pl.DataFrame:
        self.user = {
            "tipo_identificacion": pl.String,
            "identificacion": pl.String,
            "entidad_administradora": pl.String,
            "tipo_usuario": pl.Int8,
            "primerapellido": pl.String,
            "segundoapellido": pl.String,
            "primernombre": pl.String,
            "segundonombre": pl.String,
            "edad": pl.Int64,
            "unidad_medida": pl.Int8,
            "sexo": pl.String,
            "cod_dto": pl.Int64,
            "cod_municipio": pl.String,
            "zona_residencia": pl.Enum(["U", "R"]),
        }
