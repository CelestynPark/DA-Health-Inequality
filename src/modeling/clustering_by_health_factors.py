import os
from src.utils.prepare_data import preprocess_health_data
from src.utils.columns import CLUSTER_FEATURE_COLUMNS
from src.modeling.kmeans_clustering import run_kmeans_clustering

def run():
    df = preprocess_health_data()
    save_dir = os.path.join("output", "clusters")
    os.makedirs(save_dir, exist_ok=True)

    run_kmeans_clustering(df, features=CLUSTER_FEATURE_COLUMNS, k=10, save_dir=save_dir)

if __name__ == "__main__":
    run()