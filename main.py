import os
from src.data_generator import generate_network_traffic
from src.preprocess import preprocess_data
from src.train import train_isolation_forest
from src.detect import detect_threats

def main():
    print("="*60)
    print(" [~] AI-POWERED CYBERSECURITY THREAT DETECTION SYSTEM ")
    print("="*60)
    
    # Step 1: Generate Data (Virtual Simulation of Traffic)
    print("\n--- PHASE 1: DATA INGESTION ---")
    data_path = 'data/network_traffic.csv'
    if not os.path.exists(data_path):
        generate_network_traffic(num_samples=5000, anomaly_ratio=0.05)
    else:
        print("[+] Existing network traffic logs found. Skipping generation.")
        
    # Step 2 & 3: Preprocess and Train
    print("\n--- PHASE 2: MODEL TRAINING ---")
    X_scaled, y_true = preprocess_data(data_path)
    train_isolation_forest(X_scaled, y_true)
    
    # Step 4: Threat Detection & Alerting
    print("\n--- PHASE 3: THREAT DETECTION SIMULATION ---")
    detect_threats(data_path)
    
    print("\n" + "="*60)
    print(" [~] SYSTEM RUN COMPLETE ")
    print("="*60)

if __name__ == "__main__":
    main()
