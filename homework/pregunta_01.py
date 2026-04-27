"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.
    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    import os

    import pandas as pd

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    df = df.reset_index(drop=True)

    df = df.dropna()
    df = df.drop_duplicates()

    columnas_texto = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    for columna in columnas_texto:
        df[columna] = (
            df[columna]
            .str.lower()
            .str.replace("_", " ", regex=False)
            .str.replace("-", " ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
        )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
        .astype(float)
    )

    df["estrato"] = df.estrato.astype(str).str.strip().astype(int)
    df["comuna_ciudadano"] = (
        df.comuna_ciudadano.astype(str).str.strip().astype(float).astype(int)
    )
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"].astype(str).str.strip(),
        format="mixed",
        dayfirst=True,
        errors="coerce",
    ).dt.strftime("%d/%m/%Y")

    df = df.dropna()
    df = df.drop_duplicates()

    if not os.path.exists("files/output"):
        os.makedirs("files/output")


    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)


    return df

    
    




print(pregunta_01())
