import os
import pandas as pd
import statsmodels.api as sm

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

def interpret_coefficient(model):
    summary = model.summary2().tables[1]
    interpretations = []
    for variables, row in summary.iterrows():
        if variables == 'const':
            continue
        coef = row["Coef."]
        pval = row["P>|t|"]
        if pval < 0.05:
            effect = '증가' if coef > 0 else '감소'
            interpretations.append(
                f"{variables}의 1단위 증가가 Poor or Fair Health raw value에 {effect}하는 효과는 {abs(coef):.4f}입니다. (p-value: {pval:.4f})"
            )
        else:
            interpretations.append(
                f"{variables}의 1단위 변화는 Poor or Fair Health raw value에 유의미한 영향을 미치기 않습니다 (p-value: {pval:.4f}"
            )
    return interpretations

def save_summary(interpretations, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("회귀 분석 결과 해석:\n\n")
        for line in interpretations:
            f.write(line + '\n')
        print(f"[INFO] Regression summary saved to: {output_path}")

if __name__ == '__main__':
    data_path = os.path.join("data", "raw", "analytic_data2025_v2.csv")
    output_path = os.path.join("output", "tables", "socioeconomic_regression_summary.txt")

    df = load_data(data_path)
    df_selected = select_variables(df)
    model = fit_model(df_selected)
    interpretations = interpret_coefficient(model)
    save_summary(interpretations, output_path)