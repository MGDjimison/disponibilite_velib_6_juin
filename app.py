from transform import get_transformed_data, get_station_by_departement, get_station_by_commune

transformed_velib_df = get_transformed_data()

station_by_departement = get_station_by_departement()
print(station_by_departement)

station_by_commune = get_station_by_commune()
print(station_by_commune)

