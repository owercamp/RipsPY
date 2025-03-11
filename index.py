import os
from tkinter import filedialog, messagebox

import polars as pl
from tqdm import tqdm

from controllers.ConsultController import CONSULTCONTROLLER
from controllers.ProcedureController import PROCEDURECONTROLLER
from controllers.TransactionController import TRANSCONTROLLER
from controllers.UserController import USERCONTROLLER
from models.Consult import CONSULT
from models.Procedure import PROCEDURE
from models.Trans import TRANS
from models.User import USER
from services.factures import FACTURE_NUMBER
from services.final_date import FILTERDAYEND


def init():
    dirs = filedialog.askdirectory(title="Seleccione el directorio")
    users_df = pl.DataFrame(schema=USER().user)
    consult_df = pl.DataFrame(schema=CONSULT().consult)
    procedures_df = pl.DataFrame(schema=PROCEDURE().procedure)
    transactions_df = pl.DataFrame(schema=TRANS().transaction)

    my_dirs = len(os.listdir(dirs))

    if my_dirs != 0:
        directories = os.listdir(dirs)

        for row, directory in enumerate(
            tqdm(directories, desc="Leyendo carpeta", unit="carpeta")
        ):
            list_archives = os.listdir(os.path.join(dirs, directory))
            for row, archive in enumerate(list_archives):
                if str(archive).startswith("US"):  ## lectura de usuarios
                    users_df = USERCONTROLLER().getInfo(
                        dir_base=dirs, directory=directory, archive=archive, df=users_df
                    )

                if str(archive).startswith("AC"):  ## lectura de Consulta
                    consult_df = CONSULTCONTROLLER().getInfo(
                        dir_base=dirs,
                        directory=directory,
                        archive=archive,
                        df=consult_df,
                    )

                if str(archive).startswith("AF"):  ## lectura de Trans
                    transactions_df = TRANSCONTROLLER().getInfo(
                        dir_base=dirs,
                        directory=directory,
                        archive=archive,
                        df=transactions_df,
                    )

                if str(archive).startswith("AP"):  ## lectura de Procedimientos
                    procedures_df = PROCEDURECONTROLLER().getInfo(
                        dir_base=dirs,
                        directory=directory,
                        archive=archive,
                        df=procedures_df,
                    )

        # filters for date
        consult_df = FILTERDAYEND.filterDate(df=consult_df, col="Fecha de la consulta")
        transactions_df = FILTERDAYEND.filterDate(df=transactions_df, col="FECHA")
        procedures_df = FILTERDAYEND.filterDate(
            df=procedures_df, col="Fecha del procedimiento"
        )

        factures = FACTURE_NUMBER().uniques_factures([consult_df, procedures_df])

        facture_to_user = (
            USERCONTROLLER().add_facture(user_df=users_df, facture=factures)
        ).filter(pl.col("ingreso") != "sin factura")

        facture_validated = facture_to_user.select(pl.col("ingreso")).unique(
            subset="ingreso"
        )

        consult_df = consult_df.filter(
            pl.col("Numero de la factura") == facture_validated
        )

        print(facture_validated)

    else:
        messagebox.showinfo(title="Directorio", message="El directorio esta vacio")


if __name__ == "__main__":
    init()
