import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Arial'
sns.set(style='whitegrid')
pd.set_option('display.max_columns', None)

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

print("전체 데이터 shape:", df.shape)
print("사용할 주요 지표 컬럼 개수:", len(target_columns))
print("결측치 개수 요약:")
print(df[target_columns].isna().sum().sort_values(ascending=False))

missing_df = df[target_columns].isna().mean().sort_values(ascending=False).reset_index()
missing_df.columns = ["column", "missing_ratio"]
print(missing_df)

plt.figure(figsize=(12,6))
sns.barplot(data=missing_df, x="missing_ratio", y="column", palette="viridis")
plt.title("Missing Value Ratio by Column")
plt.xlabel("Missing Ratio")
plt.ylabel("Column")
plt.tight_layout()

OUTPUT_DIR = os.path.join("output", "eda", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.savefig(os.path.join(OUTPUT_DIR, "missing_ratio_by_column.png"))

print("[완료] 결측치 비율 시각화 저장:", os.path.join(OUTPUT_DIR, "missing_ratio_by_column.png"))