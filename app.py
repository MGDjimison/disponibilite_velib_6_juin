import pandas as pd

velib_dispo_df = pd.read_csv("data/velib-disponibilite-en-temps-reel-paris-data.csv", delimiter=";")
print(velib_dispo_df.head())