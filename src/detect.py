import pandas as pd
import numpy as np
import pickle
import os

def detect_threats(new_data_path="data/network_traffic.csv", models_dir="models", outputs_dir="outputs"):
    """
    Loads saved model and scaler to detect threats in incoming network data.
    """
    print("\n[*] Starting Threat Detection Pipeline...")
    
    # Load model and scaler
    try:
        with open(os.path.join(models_dir, 'scaler.pkl'), 'rb') as f:
            scaler = pickle.load(f)
        with open(os.path.join(models_dir, 'isolation_forest.pkl'), 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        print("[-] Error: Model or scaler not found. Please train the model first.")
        return
        
    print("[*] Loading new network traffic logs...")
    df = pd.read_csv(new_data_path)
    
    # Simulate receiving "unseen" features without the label
    X_new = df.drop(columns=['is_threat'], errors='ignore')
    
    # Preprocess
    print("[*] Scaling data...")
    X_scaled = scaler.transform(X_new)
    
    # Predict
    print("[*] Running AI anomaly detection...")
    preds = model.predict(X_scaled)
    preds_binary = [1 if p == -1 else 0 for p in preds]
    
    df['threat_alert'] = preds_binary
    
    # Filter and display anomalies
    anomalies = df[df['threat_alert'] == 1]
    
    print(f"\n[!!!] ALERT: Detected {len(anomalies)} potential cyber threats out of {len(df)} records!")
    if len(anomalies) > 0:
        print("\n--- SAMPLE THREAT LOGS ---")
        print(anomalies[['packet_size', 'connection_rate', 'login_attempts', 'bytes_sent']].head())
    
    # Save alerts
    os.makedirs(outputs_dir, exist_ok=True)
    alerts_file = os.path.join(outputs_dir, 'threat_alerts.csv')
    anomalies.to_csv(alerts_file, index=False)
    print(f"\n[+] Detailed alert logs saved to: {alerts_file}")

if __name__ == "__main__":
    detect_threats()
