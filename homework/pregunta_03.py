"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_03():

    ruta = os.path.join("files", "input", "tbl0.tsv")
    df = pd.read_csv(ruta, sep="\t")

    # Contar registros por cada valor en la columna 'c1'
    conteo = df['c1'].value_counts().sort_index()

    return conteo

if __name__ == "__main__":
    print(pregunta_03())


    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
