import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

PLOT_PATH = os.path.join("output", "plots")
REPORT_PATH = os.path.join("output", "reports")

data_path = os.path.join('data', 'processed', 'health_data_with_gaps.csv')
df = pd.read_csv(data_path)

os.makedirs(PLOT_PATH, exist_ok=True)
os.makedirs(REPORT_PATH, exist_ok=True)

death_cols = [
    "Premature_Death_AIAN",
    "Premature_Death_Asian",
    "Premature_Death_Black",
    "Premature_Death_Hispanic",
    "Premature_Death_White",
    "Premature_Death_NHOPI",
]

races = [col.split("_")[-1] for col in death_cols]

df_melted = df.melt(value_vars=death_cols, var_name="Race", value_name="DeathRate")

plt.figure(figsize=(12,6))
sns.boxplot(data=df_melted, x="Race", y="DeathRate")
plt.title("인종별 조기 사망률 분포 (Boxplot)")
plt.savefig(os.path.join(PLOT_PATH, "premature_death_by_race_boxplot.png"))
plt.close()

plt.figure(figsize=(12,6))
sns.violinplot(data=df_melted, x="Race", y="DeathRate")
plt.title("인종별 조기 사망률 분포 (Violin Plot)")
plt.savefig(os.path.join(PLOT_PATH, "premature_death_by_race_violinplot.png"))
plt.close()

for race in races:
    gap_col = f"DeathGap_{race}"
    if gap_col not in df.columns:
        print(gap_col, "is not in columns")
        continue

    df_sorted = df[["County", gap_col]].dropna().sort_values(by=gap_col, ascending=False)

    top10 = df_sorted.head(10)
    bottom10 = df_sorted.tail(10)

    plt.figure(figsize=(10,6))
    sns.barplot(data=top10, x=gap_col, y="County", palette="Reds_r")
    plt.title(f"{race} DeathGap 상위 10개 카운티")
    plt.savefig(os.path.join(PLOT_PATH, f"top10_{race.lower()}_deathgap.png"))
    plt.close()

    plt.figure(figsize=(10,6))
    sns.barplot(data=bottom10, x=gap_col, y="County", palette="Reds_r")
    plt.title(f"{race} DeathGap 하위 10개 카운티")
    plt.savefig(os.path.join(PLOT_PATH, f"bottom10_{race.lower()}_deathgap.png"))
    plt.close()

summary_cols = death_cols + [f"DeathGap_{race}" for rafce in races if f"DeathGap_{race}" in df.columns]
summary = df[summary_cols].describe()
summary.to_csv(os.path.join(REPORT_PATH, "statistics_summary.csv"))
