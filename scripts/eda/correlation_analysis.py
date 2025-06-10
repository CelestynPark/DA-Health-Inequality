import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Arial'
sns.set(style='whitegrid')

DATA_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')
df = pd.read_csv(DATA_PATH)

health_columns = [
    "Premature_Death_Total",
    "Poor_or_Fair_Health",
    "Adult_Smoking",
    "Adult_Obesity",
    "Uninsured",
    "Primary_Care_Physician",
    "Some_College",
    "Unemployment",
    "Children_in_Poverty",
    "Air_Pollution_PM",
    "Severe_Housing_Problems",
]

race_mortality_columns = [
    "Premature_Death_AIAN",
    "Premature_Death_Asian",
    "Premature_Death_Black",
    "Premature_Death_Hispanic",
    "Premature_Death_White",
    "Premature_Death_NHOPI",
]

target_columns = race_mortality_columns + health_columns

df[target_columns] = df[target_columns].replace('Not Available', pd.NA)

df[target_columns] = df[target_columns].apply(pd.to_numeric, errors='coerce')

df_corr = df[target_columns].dropna()

OUTPUT_DIR = os.path.join('output', 'eda', 'figures', 'distribution')
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure(figsize=(14,10))
corr_matrix = df_corr.corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})
plt.title("Correlation Matrix: Race-based Premature Death vs Health Factors", fontsize=15)
plt.tight_layout()
heatmap_path = os.path.join(OUTPUT_DIR, "correlation_matrix_full.png")
plt.savefig(heatmap_path)
plt.close()
print(f"[저장 완료] {heatmap_path}")

race_corrs = corr_matrix.loc[race_mortality_columns, health_columns]
race_corrs_path = os.path.join(OUTPUT_DIR, "correlation_table.csv")
race_corrs.to_csv(race_corrs_path)
print(f"[저장 완료] {race_corrs_path}")