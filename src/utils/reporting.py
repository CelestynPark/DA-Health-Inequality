import pandas as pd

def summarize_missing_values(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    missing_df = df[columns].isna().mean().sort_values(ascending=False).reset_index()
    missing_df.columns = ["column", "missing_ratio"]
    return missing_df
