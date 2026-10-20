#!/bin/bash
#SBATCH --job-name=deforestation_hpc_job
#SBATCH --output=logs/hpc_job_%j.log
#SBATCH --error=logs/hpc_job_%j.err
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --time=01:30:00

echo "=== [Materi 2] Memulai Eksekusi Paralel di Kluster HPC (SLURM) ==="
module load python/3.10

# Eksekusi pipeline secara berurutan
python3 01_data_preparation.py
python3 03_spatial_processor.py
python3 04_model_training.py
python3 05_model_evaluation.py
python3 06_data_visualization.py

echo "=== Eksekusi HPC Selesai ==="