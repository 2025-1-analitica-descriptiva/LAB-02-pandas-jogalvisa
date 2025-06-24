"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
import os

def pregunta_06():

    ruta = os.path.join("files", "input", "tbl1.tsv")
    df = pd.read_csv(ruta, sep="\t")
    
    #Retornar los valores únicos de la columna 'c4' en mayúsculas y ordenados alfabéticamente
    unique_values = df['c4'].str.upper().unique() 
    unique_values.sort()  # Ordenar alfabéticamente

    return unique_values.tolist()  # Convertir a lista

if __name__ == "__main__":
    print(pregunta_06())
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
