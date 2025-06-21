import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from src.visualization.cluster_plot import plot_pca_clusters, plot_cluster_feature_means

def run_kmeans_clustering(df: pd.DataFrame, features: list, k: int, save_dir: str):
    df = df.copy()
    df[features] = df[features].replace('Not Available', pd.NA)
    df[features] = df[features].apply(pd.to_numeric, errors='coerce')
    df_cluster = df.dropna(subset=features).copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_cluster[features])

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    df_cluster['Cluster'] = kmeans.fit_predict(X_scaled)

    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)
    df_cluster['PC1'] = components[:, 0]
    df_cluster['PC2'] = components[:, 1]

    fig_dir = os.path.join("output", "figures", "clusters")
    os.makedirs(fig_dir, exist_ok=True)

    plot_pca_clusters(df_cluster, k, os.path.join(fig_dir, f"pca_cluster_k{k}.png"))
    plot_cluster_feature_means(df_cluster, features, os.path.join(fig_dir, f"cluster_feature_averages_k{k}.png"))

    df_with_cluster = df.merge(df_cluster[['FIPS', 'Cluster']], on='FIPS', how='left')
    df_with_cluster.to_csv(os.path.join(save_dir, "health_clusters.csv"), index=False)
    print(f"[완료] 클러스터 결과 저장 완료: health_clusters.csv")
