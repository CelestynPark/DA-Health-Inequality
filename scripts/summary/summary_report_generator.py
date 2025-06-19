import os
import pandas as pd

DATA_PATH = os.path.join('output', 'clustering', 'health_clusters.csv')
SAVE_DIR = os.path.join('output', 'summary')
os.makedirs(SAVE_DIR, exist_ok=True)

FEATURE_COLS = [
    'Poor_or_Fair_Health',
    "Adult_Smoking",
    "Adult_Obesity",
    "Uninsured",
    "Primary_Care_Physician",
    "Some_College",
    "Unemployment",
    "Children_in_Poverty",
    "Air_Pollution_PM",
    "Severe_Housing_Problems",
    "Premature_Death_AIAN",
    "Premature_Death_Asian",
    "Premature_Death_Black",
    "Premature_Death_Hispanic",
    "Premature_Death_White",
    "Premature_Death_NHOPI",
]

df = pd.read_csv(DATA_PATH)

national_mean = df[FEATURE_COLS].mean()

cluster_summary = df.groupby('Cluster')[FEATURE_COLS].mean().round(4)
cluster_counts = df['Cluster'].value_counts().sort_index()
cluster_summary['n_county'] = cluster_counts

csv_path = os.path.join(SAVE_DIR, 'cluster_summary.csv')
cluster_summary.to_csv(csv_path)
print(f'[完] 클러스터 평균값 저장 완료: {csv_path}')

report_lines = []
report_lines.append('건강 클러스터 분석 요약 리포트')
report_lines.append(f"총 클러스터 수: {df['Cluster'].nunique()}개")

for cluster_id, row in cluster_summary.iterrows():
    report_lines.append(f"▷ Cluster {cluster_id} (총 {int(row['n_county'])}개 카운티)")
    diffs = (row[FEATURE_COLS] - national_mean).sort_values(ascending=False)

    for feat in FEATURE_COLS:
        val = row[feat]
        delta = val - national_mean[feat]
        arrow = '↑' if delta > 0 else '↓'
        report_lines.append(
            f"  - {feat}: {val:.3f} ({abs(delta):.3f} {arrow} 전국 평균 {national_mean[feat]:.3f})"
        )

    top_risk = diffs.head(2).index.tolist()
    bottom_good = diffs.tail(2).index.tolist()

    report_lines.append("")
    report_lines.append("  ▷ 클러스터 특징 요약:")
    report_lines.append(f"     * 높은 지표: {', '.join(top_risk)}")
    report_lines.append(f"     * 낮은 지표: {', '.join(bottom_good)}")

    risk_msg = f"{top_risk[0]} 등의 수치가 전국 평균보다 높아, 지역 사회 기반의 건강 정책 강화가 필요합니다."
    report_lines.append(f"     → 시사점: {risk_msg}")
    report_lines.append("")

txt_path = os.path.join(SAVE_DIR, 'cluster_summary.txt')
with open(txt_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"[完] 텍스트 요약 보고서 저장 완료: {txt_path}")