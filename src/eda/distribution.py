import os
from src.utils.prepare_data import preprocess_health_data
from src.utils.columns import TOTAL_COLUMNS, RACE_COLUMNS
from src.visualization.eda_plot import plot_distribution

def run():
    df = preprocess_health_data()
    target_columns = TOTAL_COLUMNS + RACE_COLUMNS

    save_dir = os.path.join("output", "figures", "eda", "distribution")
    os.makedirs(save_dir, exist_ok=True)

    for col in target_columns:
        plot_distribution(df, col, save_dir)

if __name__ == "__main__":
    run()
