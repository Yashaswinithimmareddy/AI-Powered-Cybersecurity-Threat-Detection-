import pandas as pd
import numpy as np
import os

def generate_network_traffic(num_samples=5000, anomaly_ratio=0.05, output_dir="data"):
    """
    Generates synthetic network traffic data and introduces cyber threat anomalies.
    """
    np.random.seed(42)
    
    # Normal network traffic simulation
    data = {
        'packet_size': np.random.normal(loc=500, scale=100, size=num_samples),
        'duration': np.random.exponential(scale=1.5, size=num_samples),
        'bytes_sent': np.random.normal(loc=2000, scale=500, size=num_samples),
        'bytes_received': np.random.normal(loc=3000, scale=800, size=num_samples),
        'login_attempts': np.random.poisson(lam=1, size=num_samples),
        'connection_rate': np.random.normal(loc=10, scale=2, size=num_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Label normal traffic as 0
    df['is_threat'] = 0
    
    # Introduce anomalies (simulating DoS, Brute Force, Data Exfiltration)
    num_anomalies = int(num_samples * anomaly_ratio)
    anomaly_indices = np.random.choice(df.index, num_anomalies, replace=False)
    
    for idx in anomaly_indices:
        attack_type = np.random.choice(['dos', 'brute_force', 'data_exfiltration'])
        
        if attack_type == 'dos':
            # High connection rate, very small packet size
            df.loc[idx, 'connection_rate'] *= np.random.uniform(10, 20)
            df.loc[idx, 'packet_size'] = np.random.uniform(20, 50)
            
        elif attack_type == 'brute_force':
            # High login attempts
            df.loc[idx, 'login_attempts'] = np.random.randint(15, 50)
            df.loc[idx, 'duration'] *= 5
            
        elif attack_type == 'data_exfiltration':
            # Huge bytes sent
            df.loc[idx, 'bytes_sent'] *= np.random.uniform(20, 50)
            df.loc[idx, 'duration'] *= 3

        df.loc[idx, 'is_threat'] = 1

    # Save to CSV
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "network_traffic.csv")
    df.to_csv(file_path, index=False)
    print(f"[+] Successfully generated artificial network traffic data: {file_path}")
    print(f"[+] Total Records: {len(df)} | Anomalies Created: {df['is_threat'].sum()}")

if __name__ == "__main__":
    generate_network_traffic()
