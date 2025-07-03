import os
import matplotlib.pyplot as plt
import pandas as pd
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
            "High School Completion raw value",
            "Premature Death raw value"
        ]
    ].dropna()

def plot_scatter(df, output_path):
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df,
        x="High School Completion raw value",
        y="Premature Death raw value",
        scatter_kws={"alpha": 0.6},
        line_kws={"color": "red"}
    )
    plt.title("High School Completion vs Premature Death by County")
    plt.xlabel("High School Completion (%)")
    plt.ylabel("Premature Death (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "figures", "high_school_completion_vs_premature_death_scatter.png")

    df = load_data(data_path)
    df_selected = select_data(df)
    plot_scatter(df_selected, output_path)

    print(f"[INFO] Scatter plot saved t0: {output_path}")