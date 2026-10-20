"""
Materi 1: Data Preparation & Business Anomaly Cleaning
Menangani data kotor, menghapus missing values, dan mencegah Data Leakage.
"""

import pandas as pd
import numpy as np

def clean_environmental_data(df: pd.DataFrame) -> pd.DataFrame:
    print("[Materi 1] Memulai Data Preparation...")
    
    # 1. Menghapus nilai kosong pada kolom kunci
    initial_len = len(df)
    df = df.dropna(subset=['latitude', 'longitude', 'deforestation_driver'])
    
    # 2. Cek anomali aturan bisnis (misal: luas lahan tidak boleh negatif)
    df = df[df['area_hectares'] > 0]
    
    # 3. Mencegah Data Leakage (Hapus kolom inspeksi masa depan)
    leakage_cols = ['future_inspection_date', 'inspector_notes']
    df = df.drop(columns=[c for c in leakage_cols if c in df.columns])
    
    print(f"[Materi 1] Data dibersihkan: {initial_len} -> {len(df)} baris.")
    return df

if __name__ == "__main__":
    dummy_data = pd.DataFrame({
        'latitude': [-3.80, -3.81, np.nan, -3.82],
        'longitude': [102.26, 102.27, 102.28, 102.29],
        'area_hectares': [12.5, -2.0, 5.0, 1.2],
        'deforestation_driver': ['Large-scale', 'Fire', 'Small-scale', 'Fire'],
        'future_inspection_date': ['2026-12-01', '2026-12-02', '2026-12-03', '2026-12-04']
    })
    clean_environmental_data(dummy_data)