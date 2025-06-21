import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

def plot_variable_on_map(df: pd.DataFrame, shapefile_path: str, target_column: str, save_path: str):
    df = df.copy()
    df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)

    df = df[df[target_column] != 'Not Available']
    df[target_column] = pd.to_numeric(df[target_column], errors='coerce')
    df = df.dropna(subset=[target_column])

    gdf = gpd.read_file(shapefile_path)
    if gdf.crs is None:
        gdf.set_crs('EPSG:4269', inplace=True)

    gdf['GEOID'] = gdf['GEOID'].astype(str)
    df['County_clean'] = df['County'].str.replace(' County', '', regex=False).str.strip().str.lower()
    gdf['NAME_clean'] = gdf['NAME'].str.strip().str.lower()

    merged = gdf.merge(df, left_on='NAME_clean', right_on='County_clean')

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(
        column=target_column,
        cmap='OrRd',
        linewidth=0.1,
        edgecolor='gray',
        figsize=(12, 8),
        legend=True,
        ax=ax,
        missing_kwds={'color': 'lightgray', 'label': 'No Data'}
    )
    ax.set_title(f'{target_column} by County', fontsize=16)
    ax.axis('off')

    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f'[지도 저장 완료] {save_path}')
