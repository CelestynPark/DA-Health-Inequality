import os
import pandas as pd

def get_data_paths():
    raw_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    dict_path = os.path.join("data", "raw", "DataDictionary_2025.xlsx")
    output_path = os.path.join("data", "processed", "health_data_cleaned.csv")
    return raw_path, dict_path, output_path

COLUMN_RENAME_MAP = {
    "State FIPS Code": "FIPS",
    "State Abbreviation": "State",
    "Name": "County",
    "Premature Death raw value": "Premature_Death_Total",
    "Poor or Fair Health raw value": "Poor_or_Fair_Health",
    "Adult Smoking raw value": "Adult_Smoking",
    "Adult Obesity raw value": "Adult_Obesity",
    "Uninsured raw value": "Uninsured",
    "Primary Care Physicians raw value": "Primary_Care_Physician",
    "Some College raw value": "Some_College",
    "Unemployment raw value": "Unemployment",
    "Children in Poverty raw value": "Children_in_Poverty",
    "Air Pollution: Particulate Matter raw value": "Air_Pollution_PM",
    "Severe Housing Problems raw value": "Severe_Housing_Problems",
    "Premature Death (AIAN)": "Premature_Death_AIAN",
    "Premature Death (Asian)": "Premature_Death_Asian",
    "Premature Death (Black)": "Premature_Death_Black",
    "Premature Death (Hispanic)": "Premature_Death_Hispanic",
    "Premature Death (White)": "Premature_Death_White",
    "Premature Death (NHOPI)": "Premature_Death_NHOPI",
}

def preprocess_health_data(save_path: str = None) -> pd.DataFrame:
    raw_path, _, default_output_path = get_data_paths()
    df = pd.read_csv(raw_path)

    df_selected = df[list(COLUMN_RENAME_MAP.keys())].rename(columns=COLUMN_RENAME_MAP)

    df_selected = df_selected.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    for col in df_selected.select_dtypes(include=['float64', 'int64']).columns:
        if df_selected[col].isnull().mean() > 0:
            median = df_selected[col].median()
            df_selected[col] = df_selected[col].fillna(median)

    race_columns = [col for col in df_selected.columns if col.startswith("Premature_Death_") and col != "Premature_Death_Total"]
    df_selected[race_columns] = df_selected[race_columns].fillna("Not Available")

    if save_path is None:
        save_path = default_output_path
    df_selected.to_csv(save_path, index=False)
    print(f"[INFO] Preprocessed data saved to: {save_path}")

    return df_selected

def print_missing_report(df: pd.DataFrame):
    missing_ratio = df.isnull().mean().sort_values(ascending=False)
    print("[INFO] Missing value ratio:\n", missing_ratio)
