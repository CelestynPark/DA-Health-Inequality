import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

DATA_PATH = os.path.join('data', 'processed', 'health_data_cleaned.csv')
SHAPEFILE_PATH = os.path.join('data', 'cb_2018_us_county_20m.shp')
SAVE_DIR = os.path.join('output', 'map')

os.makedirs(SAVE_DIR, exist_ok=True)

TARGET_COLUMN = 'Premature_Death_Total'

df = pd.read_csv(DATA_PATH)

df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)

df = df[df[TARGET_COLUMN] != 'Not Available']
df[TARGET_COLUMN] = pd.to_numeric(df[TARGET_COLUMN], errors='coerce')
df = df.dropna(subset=[TARGET_COLUMN])

gdf = gpd.read_file(SHAPEFILE_PATH)

if gdf.crs is None:
    gdf.set_crs('EPSG:4269', inplace=True)

gdf['GEOID'] = gdf['GEOID'].astype(str)

df['County_clean'] = df['County'].str.replace(' County', '', regex=False).str.strip().str.lower()

gdf['NAME_clean'] = gdf['NAME'].str.strip().str.lower()


merged = gdf.merge(df, left_on='NAME_clean', right_on='County_clean')

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.plot(
    column=TARGET_COLUMN,
    cmap='OrRd',
    linewidth=0.1,
    edgecolor='gray',
    figsize=(12, 8),
    legend=True,
    ax=ax,
    missing_kwds={'color': 'lightgray', 'label': 'No Data'}
)

ax.set_title(f'{TARGET_COLUMN} by County', fontsize=16)
ax.axis('off')

save_path = os.path.join(SAVE_DIR, f'map_{TARGET_COLUMN}.png')
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f'[지도 저장 완료] {save_path}')