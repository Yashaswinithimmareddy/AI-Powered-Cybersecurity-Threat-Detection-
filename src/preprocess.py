import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import pickle

def preprocess_data(input_file="data/network_traffic.csv", output_dir="data", models_dir="models"):
    """
    Loads data, isolates features, and applies Standard Scaling.
    """
    print("[*] Loading dataset...")
    df = pd.read_csv(input_file)
    
    # Drop the target label (since unsupervised learning will just find outliers)
    # But keep it stored to validate our model later
    X = df.drop(columns=['is_threat'])
    y = df['is_threat']
    
    print("[*] Scaling features (Standardization)...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Save the scaler for inference
    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, 'scaler.pkl'), 'wb') as f:
        pickle.dump(scaler, f)
        
    print(f"[+] Preprocessing complete! Scaler saved to {models_dir}/scaler.pkl")
    return X_scaled, y

if __name__ == "__main__":
    preprocess_data()
