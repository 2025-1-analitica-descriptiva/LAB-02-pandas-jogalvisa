"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_04():

    ruta = os.path.join("files", "input", "tbl0.tsv")
    df = pd.read_csv(ruta, sep="\t")

    # Calcular el promedio de 'c2' por cada letra de 'c1'
    conteo = df.groupby('c1')['c2'].mean().sort_index()
    return conteo

if __name__ == "__main__":
    print(pregunta_04())
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
