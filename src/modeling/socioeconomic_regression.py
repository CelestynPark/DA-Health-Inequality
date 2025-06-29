import pandas as pd
import statsmodels.api as sm
import os

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

def run_regression(df_selected):
    y = df_selected["Poor or Fair Health raw value"]
    X = df_selected.drop(columns=["Poor or Fair Health raw value"])
    x = sm.add_constant(X)

    model = sm.OLS(y, x).fit()
    return model

def save_summary(model, output_path):
    with open(output_path, 'w') as f:
        f.write(model.summary().as_text())
    print(f"[INFO] Regression summary saved to: {output_path}")

if __name__ == "__main__":
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "tables", "socioeconomic_regression_summary.txt")

    df = load_data(data_path)
    df_selected = select_variables(df)
    model = run_regression(df_selected)
    save_summary(model, output_path)