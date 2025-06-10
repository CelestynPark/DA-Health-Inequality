import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Arial'
sns.set(style='whitegrid')

DATA_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')
df = pd.read_csv(DATA_PATH)

total_columns = [
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

race_columns = [
    "Premature_Death_AIAN",
    "Premature_Death_Asian",
    "Premature_Death_Black",
    "Premature_Death_Hispanic",
    "Premature_Death_White",
    "Premature_Death_NHOPI",
]

target_columns = total_columns + race_columns

OUTPUT_DIR = os.path.join('output', 'eda', 'figures', 'distribution')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_distribution(column_name, save_dir):
    plt.figure(figsize=(8,5))
    sns.histplot(df[column_name].dropna(), kde=True, bins=30, color="steelblue")
    plt.title(f"Distribution of {column_name}", fontsize=14)
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.tight_layout()
    save_path = os.path.join(save_dir, f"{column_name}_distribution.png")
    plt.savefig(save_path)
    print(f"[저장 완료] {save_path}")

for col in target_columns:
    plot_distribution(col, OUTPUT_DIR)