import pandas

from dataframe import get_velib_data


def transform():
    df = get_velib_data()
    # convert column names to snake case
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

