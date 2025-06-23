import os
import pandas as pd
from src.utils.columns import CLUSTER_FEATURE_COLUMNS

def generate_cluster_summary(
        cluster_path='output/clusters/health_clusters.csv',
        output_dir='output/reports'
):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(cluster_path)

    national_mean = df[CLUSTER_FEATURE_COLUMNS].mean()
    cluster_summary = df.groupby('Cluster')[CLUSTER_FEATURE_COLUMNS].mean().round(4)
    cluster_counts = df['Cluster'].value_counts().sort_index()
    cluster_summary['n_county'] = cluster_counts

    report_lines = []
    report_lines.append("건강 클러스터 분석 요약 리포트")
    report_lines.append(f"총 클러스터 수: {df['Cluster'].nunique()}개\n")

    for cluster_id, row in cluster_summary.iterrows():
        report_lines.append(f"▷ cluster {cluster_id} (총 {int(row['n_county'])}개 카운티)")
        diffs = (row[CLUSTER_FEATURE_COLUMNS] - national_mean).sort_values(ascending=False)

        for feat in CLUSTER_FEATURE_COLUMNS:
            val = row[feat]
            delta = val - national_mean[feat]
            arrow = '↑' if delta > 0 else '↓'
            report_lines.append(
                    f"   - {feat}: {val:.3f} ({abs(delta):.3f} {arrow} 전국 평균 {national_mean[feat]:.3f})"
            )
        
        top_risk = diffs.head(2).index.tolist()
        bottom_good = diffs.tail(2).index.tolist()

        report_lines.append("\n  ▷ 클라스터 특징 요약:")
        report_lines.append(f"     * 높은 지표: {', '.join(top_risk)}")
        report_lines.append(f"     * 낮은 지표: {', '.join(bottom_good)}")
        report_lines.append(
                    f"     → 시사점: {top_risk[0]} 등의 수치가 전국 평균보다 높아, 지역 사회 기반의 건강 정책 강화가 필요합니다.\n"
        )

    txt_path = os.path.join(output_dir, 'cluster_summary.txt')

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"[완료] 텍스트 리포트 저장: {txt_path}")
