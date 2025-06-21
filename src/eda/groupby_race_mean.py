import os
import numpy as np
import pandas as pd
from src.utils.prepare_data import preprocess_health_data
from src.utils.columns import HEALTH_COLUMNS, RACE_COLUMNS
from src.visualization.eda_plot import plot_race_group_comparison

def run():
    df = preprocess_health_data()

    # race 컬럼 수치형 변환
    df[RACE_COLUMNS] = df[RACE_COLUMNS].replace('Not Available', np.nan)
    df[RACE_COLUMNS] = df[RACE_COLUMNS].apply(pd.to_numeric, errors='coerce')

    save_dir = os.path.join("output", "figures", "eda", "race_group_comparison")
    os.makedirs(save_dir, exist_ok=True)

    for race in RACE_COLUMNS:
        temp_df = df[[race] + HEALTH_COLUMNS].dropna()
        if temp_df.empty:
            print(f"[경고] {race}에 대한 유효한 데이터 없음, 건너뜀")
            continue

        median_val = temp_df[race].median()
        temp_df['Group'] = temp_df[race].apply(lambda x: 'High Mortality' if x > median_val else 'Low Mortality')

        group_means = temp_df.groupby('Group')[HEALTH_COLUMNS].mean().T
        group_means.columns = ['High Mortality', 'Low Mortality']

        fig_path = os.path.join(save_dir, f"group_compare_{race}.png")
        plot_race_group_comparison(group_means, race, fig_path)
        print(f"[저장 완료] {fig_path}")

if __name__ == "__main__":
    run()
