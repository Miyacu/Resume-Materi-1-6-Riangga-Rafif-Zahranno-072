"""
Materi 5: Model Evaluation & Performance Metrics
Mengevaluasi akurasi, precision, recall, dan f1-score model Machine Learning.
"""

from sklearn.metrics import classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def evaluate_model():
    print("[Materi 5] Menjalankan Evaluasi Performa Model...")
    
    # Dataset sampel untuk pengujian evaluasi
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
    
    predictions = model.predict(X_test)
    
    print("\n[Laporan Evaluasi Performa Model]:")
    print(classification_report(y_test, predictions, zero_division=0))

if __name__ == "__main__":
    evaluate_model()