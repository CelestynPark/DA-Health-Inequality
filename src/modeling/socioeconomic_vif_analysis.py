import pandas as pd
import os
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def select_variables(df):
    cols = [
        "Poor or Fair Health raw value",
        "Unemployment raw value",
        "Income Inequality raw value",
        "Children in Poverty raw value",
        "High School Completion raw value",
        "Median Household Income raw value",
        "Severe Housing Problems raw value",
        "Children in Single-Parent Households raw value",
        "% Rural raw value"
    ]
    df_selected = df[cols].dropna()
    return df_selected

def calculate_vif(df_selected):
    X = add_constant(df_selected)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data

def save_vif_report(vif_data, output_path):
    with open(output_path, 'w') as f:
        f.write(vif_data.to_string(index=False))
    print(f"[INFO] VIF report saved to: {output_path}")

if __name__ == "__main__":
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "tables", "socioeconomic_vif.txt")

    df = load_data(data_path)
    df_selected = select_variables(df)
    vif_data = calculate_vif(df_selected)
    save_vif_report(vif_data, output_path)