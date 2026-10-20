"""
Materi 6: Data Visualization & Human-Computer Interaction (IMK)
Membuat visualisasi data bersih tanpa 'chartjunk' berdasarkan prinsip kognitif.
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

def generate_clean_visualization(df: pd.DataFrame):
    print("[Materi 6] Membuat Visualisasi Data Bersih (Prinsip IMK)...")
    
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    gdf.plot(column='deforestation_driver', ax=ax, legend=True,
             cmap='Set2', markersize=gdf['area_hectares'] * 12, alpha=0.8)
    
    plt.title("Peta Sebaran Driver Deforestasi (Clean Data-Ink Ratio)", fontsize=11)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig("output_visualization.png")
    print("[Materi 6] Visualisasi disimpan ke 'output_visualization.png'.")

if __name__ == "__main__":
    dummy_data = pd.DataFrame({
        'latitude': [-3.80, -3.81, -3.82],
        'longitude': [102.26, 102.27, 102.28],
        'area_hectares': [15.0, 1.2, 0.8],
        'deforestation_driver': ['Large-scale', 'Small-scale', 'Fire']
    })
    generate_clean_visualization(dummy_data)