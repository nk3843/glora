import pandas as pd

def load_gdelt_csv(path: str, nrows: int = None) -> pd.DataFrame:
    df = pd.read_csv(path, nrows=nrows)
    df = df.dropna(subset=["Actor1Name", "Actor2Name", "SQLDATE"])
    df["SQLDATE"] = pd.to_datetime(df["SQLDATE"], format="%Y%m%d")
    df = df.dropna(subset=["SQLDATE"])
    return df
    
