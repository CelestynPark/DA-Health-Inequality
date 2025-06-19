import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

CLUSTER_PATH = os.path.join('output', 'clustering', 'health_clusters.csv')
SHAPEFILE_PATH = os.path.join('data', 'cb_2018_us_county_20m.shp')
SAVE_DIR = os.path.join('output', 'map')

os.makedirs(SAVE_DIR, exist_ok=True)

df = pd.read_csv(CLUSTER_PATH)
df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)

gdf = gpd.read_file(SHAPEFILE_PATH)
gdf['GEOID'] = gdf['GEOID'].astype(str)

df['County_clean'] = df['County'].str.replace(' County', '', regex=False).str.strip().str.lower()

gdf['NAME_clean'] = gdf['NAME'].str.strip().str.lower()

merged = gdf.merge(df, left_on='NAME_clean', right_on='County_clean')

merged = merged[~merged['Cluster'].isna()]

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.plot(
    column='Cluster',
    cmap='Set2',
    linewidth=0.1,
    ax=ax,
    edgecolor='gray',
    legend=True,
    categorical=True
)

ax.set_title('Health Clusters by County', fontsize=16)
ax.axis('off')

save_path = os.path.join(SAVE_DIR, 'map_health_clusters.png')
plt.savefig(save_path)
print(f'[完] 클러스터 지도 저장 완료: {save_path}')