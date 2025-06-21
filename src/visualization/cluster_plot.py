import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_pca_clusters(df: pd.DataFrame, k: int, save_path: str):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='PC1', y='PC2', hue='Cluster', palette='Set2', s=60)
    plt.title(f'PCA Clustering (k={k})')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[완료] PCA 클러스터 시각화 저장: {save_path}")

def plot_cluster_feature_means(df: pd.DataFrame, features: list, save_path: str):
    cluster_means = df.groupby('Cluster')[features].mean()
    cluster_means.T.plot(kind='bar', figsize=(12, 6))
    plt.title('Cluster-wise Feature Averages')
    plt.ylabel('Average (Standardized)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[완료] 클러스터 평균 시각화 저장: {save_path}")
