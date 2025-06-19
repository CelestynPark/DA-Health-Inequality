import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

DATA_PATH = os.path.join('data','processed', 'health_data_cleaned.csv')
SAVE_DIR = os.path.join('output', 'clustering')
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


df[FEATURE_COLS] = df[FEATURE_COLS].replace('Not Available', pd.NA)

df[FEATURE_COLS] = df[FEATURE_COLS].apply(pd.to_numeric, errors='coerce')

df_cluster = df.dropna(subset=FEATURE_COLS).copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster[FEATURE_COLS])

k = 10
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df_cluster['Cluster'] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
df_cluster['PC1'] = components[:, 0]
df_cluster['PC2'] = components[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cluster, x='PC1', y='PC2', hue='Cluster', palette='Set2', s=60)
plt.title(f'PCA Clustering (k={k})')
plt.savefig(os.path.join(SAVE_DIR, f'pca_clustger_k{k}.png'))
plt.close()
print(f'[完] PCA 클러스터 시각화 저장 완료')

cluster_means = df_cluster.groupby('Cluster')[FEATURE_COLS].mean()

plt.figure(figsize=(10, 6))
cluster_means.T.plot(kind='bar', figsize=(12, 6))
plt.title('Cluster-wise Feature Averages')
plt.ylabel('Average (Standardized)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(SAVE_DIR, f'cluster_feature_averages_k{k}.png'))
plt.close()
print(f'[完] 클러스터 평균 비교 시각화 저장 완료')

df_with_cluster = df.merge(df_cluster[['FIPS', 'Cluster']], on='FIPS', how='left')
df_with_cluster.to_csv(os.path.join(SAVE_DIR, 'health_clusters.csv'), index=False)
print(f'[完] 클러스터 결과 저장 완료')