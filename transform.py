import pandas

from dataframe import get_velib_data


def transform():
    df = get_velib_data()
    # convert column names to snake case
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # convert "station_en_fonctionnement" to boolean
    names = {
        "OUI": True,
        "NON": False
    }
    df["station_en_fonctionnement"] = df["station_en_fonctionnement"].map(names)
    df["retour_vélib_possible"] = df["retour_vélib_possible"].map(names)
    df["borne_de_paiement_disponible"] = df["borne_de_paiement_disponible"].map(names)

    return df

