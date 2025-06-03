import pandas as pd


def get_velib_dispo():
    df = pd.read_csv("data/velib-disponibilite-en-temps-reel-paris-data.csv", delimiter=";")
    return df


# get types of each column
def get_velib_dispo_types():
    df = get_velib_dispo()
    return df.dtypes


# get name of columns
def get_velib_dispo_columns():
    df = get_velib_dispo()
    return df.columns

