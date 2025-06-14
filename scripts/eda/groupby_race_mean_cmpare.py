import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['font.family'] = 'Arial'
sns.set(style='whitegrid')

DATA_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')
df = pd.read_csv(DATA_PATH)

health_columns = [
    'Poor_or_Fair_Health',
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

OUTPUT_DIR = os.path.join('output', 'eda', 'figures', 'race_group_comparison')
os.makedirs(OUTPUT_DIR, exist_ok=True)

for col in race_columns:
    df[col] = pd.to_numeric(df[col].replace('Not Available', np.nan), errors='coerce')

for race in race_columns:
    temp_df = df[[race] + health_columns].dropna()

    median_val = temp_df[race].median()
    temp_df['Group'] = temp_df[race].apply(lambda x: 'High Mortality' if x > median_val else 'Low Mortality')

    group_means = temp_df.groupby('Group')[health_columns].mean().T
    group_means.columns = ['High Mortality', 'Low Mortality']

    ax = group_means.plot(kind='barh', figsize=(10, 6), color=['salmon', 'skyblue'])
    plt.title(f'{race} - Health & Social Factor Averages by Mortality Group', fontsize=13)
    plt.xlabel('Average Value')
    plt.tight_layout()

    fig_path = os.path.join(OUTPUT_DIR, f'group_compare_{race}.png')
    plt.savefig(fig_path)
    plt.close()

    print(f"[저장 완료] {fig_path}")