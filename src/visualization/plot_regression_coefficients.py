import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

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

def fit_model(df_selected):
    y = df_selected['Poor or Fair Health raw value']
    X = df_selected.drop(columns=['Poor or Fair Health raw value'])
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    return model

def plot_coefficient(model, output_path):
    coef = model.params.drop('const')
    errors = model.bse.drop('const')

    plt.figure(figsize=(10, 6))
    coef.plot(kind='barh', yerr=errors, color='skyblue', edgecolor='black')
    plt.axvline(0, color='red', linestyle='--')
    plt.title('Regression Coefficients (95% CI)')
    plt.xlabel("Coefficient Value")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == '__main__':
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "figures", "socioeconomic_coefficients.png")

    df = load_data(data_path)
    df_selected = select_variables(df)
    model = fit_model(df_selected)
    plot_coefficient(model, output_path)

    print(f"[INFO] Regression coefficients plot saved to: {output_path}")