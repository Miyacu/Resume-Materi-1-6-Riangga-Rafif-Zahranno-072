# Integrated AI & Spatial Deforestation Analysis Platform

Repositori ini merepresentasikan *pipeline* *end-to-end* untuk analisis data lingkungan, klasifikasi deforestasi berbasis Machine Learning, integrasi GIS/spasial, serta otomasi komputasi kinerja tinggi (HPC).

## 📌 Cakupan Materi Integrasi (1–6)

- **Materi 1 (`01_data_preparation.py`)**: Data Preparation & Pembersihan Anomali Aturan Bisnis.
- **Materi 2 (`02_hpc_batch_submission.sh`)**: Otomasi Eksekusi Paralel & Batch Submission SLURM untuk HPC.
- **Materi 3 (`03_spatial_processor.py`)**: Integrasi Data Spasial & Pemrosesan GIS.
- **Materi 4 (`04_model_training.py`)**: Pelatihan Model Machine Learning (*Supervised Learning*).
- **Materi 5 (`05_model_evaluation.py`)**: Evaluasi Performa Model & Metrik Klasifikasi.
- **Materi 6 (`06_data_visualization.py`)**: Visualisasi Data Interaktif & Desain Antarmuka Berbasis IMK.

---

## 🚀 Cara Penggunaan

1. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Skrip Secara Terpisah:**
   ```bash
   python 01_data_preparation.py
   python 03_spatial_processor.py
   python 04_model_training.py
   python 05_model_evaluation.py
   python 06_data_visualization.py
   ```

3. **Eksekusi di Kluster HPC (Linux/SLURM):**
   ```bash
   sbatch 02_hpc_batch_submission.sh
   ```