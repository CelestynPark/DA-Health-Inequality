import os
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

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

def plot_diagnostics(model, output_path):
    fitted_vals = model.fittedvalues
    residuals = model.resid
    standarized_residuals = model.get_influence().resid_studentized_internal
    sqrt_std_residuals = np.sqrt(np.abs(standarized_residuals))

    plt.figure(figsize=(7, 5))
    plt.scatter(fitted_vals, residuals, edgecolors="k", alpha=0.7)
    plt.axhline(0, color='red', linestyle="--")
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Fitted')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'residuals_vs_fitted.png'))
    plt.close()

    sm.qqplot(residuals, line='45', fit=True)
    plt.title('Q-Q Plot')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'qq_plot.png'))
    plt.close()

    plt.figure(figsize=(7, 5))
    plt.scatter(fitted_vals, sqrt_std_residuals, edgecolors='k', alpha=0.7)
    plt.axhline(np.mean(sqrt_std_residuals), color='red', linestyle='--')
    plt.xlabel('Fitted values')
    plt.ylabel('Sqrt of Standarized Residuals')
    plt.title('Scale-Location Plot')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'scale_location.png'))
    plt.close()

    fig, ax = plt.subplots(figsize=(8, 6))
    sm.graphics.influence_plot(model, ax=ax, criterion='cooks')
    plt.title("Influence Plot(Cook's Distance)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'influence_plot.png'))
    plt.close()

if __name__ == '__main__':
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_dir = os.path.join("output", "figures")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = load_data(data_path)
    df_selected = select_variables(df)
    model = fit_model(df_selected)
    plot_diagnostics(model, output_dir)

    print(f"[INFO] Regression diagnostics plots saved to: {output_dir}")