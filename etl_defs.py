
def clean_null(df, columns):
    for column in columns:
        if column in df.columns:
            null_ids = df[column].isnull().sum()
            if null_ids > 0:
                print(f"{null_ids} valores nulos na coluna {column} serão removidos.")
                df = df.dropna(subset=[column])
    return df

def clean_dataframes(dataframes, id_columns):
    cleaned_dfs = []
    for i, df in enumerate(dataframes):
        df = clean_null(df, id_columns)
        cleaned_dfs.append(df)
    return cleaned_dfs