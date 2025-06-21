import os
from src.utils.prepare_data import preprocess_health_data
from src.visualization.map_plot import plot_variable_on_map

def run():
    column = 'Premature_Death_Total'
    df = preprocess_health_data()

    shapefile_path = os.path.join('data', 'external', 'cb_2018_us_county_20m.shp')
    output_path = os.path.join('output', 'maps', f'map_{column}.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plot_variable_on_map(df, shapefile_path, column, output_path)

if __name__ == "__main__":
    run()
