from transform import *

velib_df = transform()
# print(velib_df.head())
# print(velib_df.dtypes["actualisation_de_la_donnée"])
# print(velib_df.dtypes["code_insee_communes_équipées"])
print(velib_df["station_opening_hours"].isna().sum())
print(velib_df.shape)
velib_df = velib_df.drop("station_opening_hours", axis=1)
print(velib_df.shape)
