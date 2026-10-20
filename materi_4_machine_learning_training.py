"""
Materi 4: Machine Learning Workflow (Supervised Learning - Training)
Fokus pada pelatihan model klasifikasi driver deforestasi.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    print("[Materi 4] Memulai Pelatihan Model Machine Learning...")
    
    df = pd.DataFrame({
        'latitude': [-3.80, -3.81, -3.82, -3.83, -3.84, -3.85] * 5,
        'longitude': [102.26, 102.27, 102.28, 102.29, 102.30, 102.31] * 5,
        'area_hectares': [15.0, 1.2, 0.8, 25.0, 1.5, 30.0] * 5,
        'deforestation_driver': ['Large-scale', 'Small-scale', 'Small-scale', 'Large-scale', 'Small-scale', 'Large-scale'] * 5
    })
    
    X = df[['latitude', 'longitude', 'area_hectares']]
    y = df['deforestation_driver']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("[Materi 4] Model Random Forest berhasil dilatih.")
    return model, X_test, y_test

if __name__ == "__main__":
    train_model()