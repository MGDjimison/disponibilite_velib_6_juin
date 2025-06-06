from transform import get_transformed_data, get_velib_in_paris, add_department

velib_df = get_transformed_data()
# print(velib_df.head())
# print(velib_df.shape)

# velib_in_paris = get_velib_in_paris()
# print(velib_in_paris["commune"].value_counts())
# print(velib_in_paris.shape)
# print(velib_in_paris["code_postal"].value_counts())

velib_df["departement"] = add_department()
print(velib_df["departement"].value_counts())

