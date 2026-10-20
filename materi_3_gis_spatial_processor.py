"""
Materi 3: GIS & Spatial Data Integration
Mengonversi tabel data mentah menjadi format spasial GeoDataFrame.
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def process_spatial_data(df: pd.DataFrame) -> gpd.GeoDataFrame:
    print("[Materi 3] Memproses Integrasi Data Spasial...")
    
    # Konversi koordinat ke objek Point Shapely dan bentuk GeoDataFrame
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    
    print(f"[Materi 3] Berhasil membuat GeoDataFrame dengan {len(gdf)} titik spasial.")
    return gdf

if __name__ == "__main__":
    dummy_data = pd.DataFrame({
        'latitude': [-3.80, -3.81, -3.82],
        'longitude': [102.26, 102.27, 102.28],
        'area_hectares': [15.0, 1.2, 0.8],
        'deforestation_driver': ['Large-scale', 'Small-scale', 'Fire']
    })
    process_spatial_data(dummy_data)