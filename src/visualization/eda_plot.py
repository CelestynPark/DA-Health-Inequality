import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

plt.rcParams['font.family'] = 'Arial'
sns.set(style='whitegrid')

def plot_missing_value_ratio(missing_df: pd.DataFrame, save_path: str):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=missing_df, x="missing_ratio", y="column", palette="viridis")
    plt.title("Missing Value Ratio by Column")
    plt.xlabel("Missing Ratio")
    plt.ylabel("Column")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"[완료] 결측치 비율 시각화 저장: {save_path}")

def plot_correlation_heatmap(corr_matrix: pd.DataFrame, save_path: str):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(14, 10))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        square=True,
        cbar_kws={"shrink": 0.8}
    )
    plt.title("Correlation Matrix: Race-based Premature Death vs Health Factors", fontsize=15)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_distribution(df: pd.DataFrame, column_name: str, save_dir: str):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(8, 5))
    sns.histplot(df[column_name].dropna(), kde=True, bins=30, color="steelblue")
    plt.title(f"Distribution of {column_name}", fontsize=14)
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.tight_layout()

    save_path = os.path.join(save_dir, f"{column_name}_distribution.png")
    plt.savefig(save_path)
    plt.close()
    print(f"[저장 완료] {save_path}")

def plot_race_group_comparison(group_means: pd.DataFrame, race_name: str, save_path: str):
    import matplotlib.pyplot as plt

    ax = group_means.plot(
        kind='barh',
        figsize=(10, 6),
        color=['salmon', 'skyblue']
    )
    plt.title(f"{race_name} - Health & Social Factor Averages by Mortality Group", fontsize=13)
    plt.xlabel("Average Value")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
