import os
import pandas as pd
from src.utils.prepare_data import preprocess_health_data
from src.utils.columns import TOTAL_COLUMNS, RACE_COLUMNS
from src.visualization.eda_plot import plot_missing_value_ratio
from src.utils.reporting import summarize_missing_values

def run():
    df = preprocess_health_data()
    target_columns = TOTAL_COLUMNS + RACE_COLUMNS

    print("전체 데이터 shape:", df.shape)
    print("사용할 주요 지표 컬럼 개수:", len(target_columns))
    print("결측치 개수 요약:")
    print(df[target_columns].isna().sum().sort_values(ascending=False))

    # 결측치 요약 데이터프레임 생성
    missing_df = summarize_missing_values(df, target_columns)
    print(missing_df)
    save_dir = os.path.join("output", "figures", "eda")
    os.makedirs(save_dir, exist_ok=True)
    plot_missing_value_ratio(missing_df, os.path.join(save_dir, "missing_ratio_by_column.png"))

if __name__ == "__main__":
    run()
