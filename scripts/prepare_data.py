import pandas as pd
import os

RAW_DATA_PATH = os.path.join('data', 'raw', 'analytic_data2025_v2.csv')
DICT_PATH = os.path.join('data', 'raw', 'DataDictionary_2025.xlsx')
OUTPUT_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')

columns_map = {
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

df = pd.read_csv(RAW_DATA_PATH)

df_selected = df[list(columns_map.keys())].rename(columns=columns_map)

df_selected = df_selected.applymap(lambda x: x.strip() if isinstance(x, str) else x)

missing_ratio = df.isnull().mean().sort_values(ascending=False)
print("결측치 비유 ㄹ:\n", missing_ratio)

for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        if df[col].isnull().mean() > 0:
            df[col] =- df[col].fillna(df[col].median())

race_columns = [col for col in df_selected.columns if col.startswith("Premature_Death_") and col != "Premature_Death_Total"]

df_selected[race_columns] = df_selected[race_columns].fillna("Not Available")

df_selected.to_csv(OUTPUT_PATH, index=False)
print("전처리 완료")