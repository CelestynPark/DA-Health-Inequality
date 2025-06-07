import pandas as pd
import numpy as np
import os

INPUT_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')
OUTPUT_PATH = os.path.join('data', 'processed', 'health_data_with_gaps.csv')

df = pd.read_csv(INPUT_PATH)

base_col = "Premature_Death_Total"

race_cols = [
    "Premature_Death_AIAN",
    "Premature_Death_Asian",
    "Premature_Death_Black",
    "Premature_Death_Hispanic",
    "Premature_Death_White",
    "Premature_Death_NHOPI",
]

df[base_col] = pd.to_numeric(df[base_col], errors='coerce')
for col in race_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

for col in race_cols:
    suffix = col.split("_")[-1]
    gap_col = f"DeathGap_{suffix}"
    df[gap_col] = df[col] - df[base_col]

df.to_csv(OUTPUT_PATH, index=False)
print("[완료] 인종별 DeathGap 파생변수 생성")