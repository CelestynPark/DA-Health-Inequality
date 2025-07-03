import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def select_data(df):
    return df[
        [   
            "Name",
            "5-digit FIPS Code",
            "State Abbreviation",
            "Children in Poverty raw value",
            "Poor or Fair Health raw value"
        ]
    ].dropna()

def plot_scatter(df, output_path):
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df,
        x="Children in Poverty raw value",
        y="Poor or Fair Health raw value",
        scatter_kws={"alpha": 0.6},
        line_kws={"color": "red"}
    )
    plt.title("Children in Poverty vs Poor or Fair Health by County")
    plt.xlabel("Children in Poverty (%)")
    plt.ylabel("Poor or Fair Health (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "figures", "poverty_vs_health_scatter.png")

    df = load_data(data_path)
    df_selected = select_data(df)
    plot_scatter(df_selected, output_path)

    print(f"[INFO] Scatter plot saved t0: {output_path}")