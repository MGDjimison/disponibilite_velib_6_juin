from transform import get_transformed_data, add_department, get_average_of_numerical_columns_by_departement

transformed_velib_df = get_transformed_data()
print("commune" in transformed_velib_df.columns)
transformed_velib_df["departement"] = add_department()

average_numerical_data_df_by_departement = get_average_of_numerical_columns_by_departement()
print(average_numerical_data_df_by_departement)

