from transform import get_transformed_data, get_velib_in_paris

velib_df = get_transformed_data()
# print(velib_df.head())
# print(velib_df.shape)

velib_in_paris = get_velib_in_paris()
print(velib_df.head())
print(velib_in_paris.shape)

