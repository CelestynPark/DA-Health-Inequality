from src.eda.overview import run as run_overview
from src.eda.correlation import run as run_correlation
from src.eda.distribution import run as run_distribution
from src.eda.groupby_race_mean import run as run_groupby_race_mean
from src.eda.map_by_variable import run as run_map_by_variable

if __name__ == "__main__":
    print("▶ EDA Overview 실행")
    run_overview()
    
    print("▶ Correlation Analysis  실행")
    run_correlation()
    
    print("▶ Distribution Plotting 실행")
    run_distribution()

    print("▶ Race Group Comparision 실행")
    run_groupby_race_mean()

    print("▶ Map Plotting 실행")
    run_map_by_variable()