import os
import pandas as pd
from src.utils.prepare_data import preprocess_health_data
from src.utils.columns import TOTAL_COLUMNS, RACE_COLUMNS
from src.visualization.eda_plot import plot_correlation_heatmap

def run():
    df = preprocess_health_data()
    target_columns = RACE_COLUMNS + TOTAL_COLUMNS

    df[target_columns] = df[target_columns].replace('Not Available', pd.NA)
    df[target_columns] = df[target_columns].apply(pd.to_numeric, errors='coerce')

    df_corr = df[target_columns].dropna()
    corr_matrix = df_corr.corr()

    fig_dir = os.path.join("output", "figures", "eda")
    os.makedirs(fig_dir, exist_ok=True)
    heatmap_path = os.path.join(fig_dir, "correlation_matrix_full.png")
    plot_correlation_heatmap(corr_matrix, heatmap_path)

    table_dir = os.path.join("output", "tables", "eda")
    os.makedirs(table_dir, exist_ok=True)
    race_corrs = corr_matrix.loc[RACE_COLUMNS, TOTAL_COLUMNS]
    race_corrs_path = os.path.join(table_dir, "correlation_table.csv")
    race_corrs.to_csv(race_corrs_path)

    print(f"[저장 완료] {heatmap_path}")
    print(f"[저장 완료] {race_corrs_path}")

if __name__ == "__main__":
    run()

