import os
import pickle
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def train_isolation_forest(X_scaled, y_true, models_dir="models", outputs_dir="outputs"):
    """
    Trains an Isolation Forest anomaly detection model.
    """
    print("\n[*] Training Isolation Forest model...")
    # anomaly ratio ~ 0.05
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X_scaled)
    
    # Save the model
    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, 'isolation_forest.pkl'), 'wb') as f:
        pickle.dump(model, f)
    print(f"[+] Model saved to {models_dir}/isolation_forest.pkl")
    
    # Evaluate
    print("\n[*] Evaluating Model Performance...")
    # Predictions: 1 for normal, -1 for anomaly
    preds = model.predict(X_scaled)
    # Convert predictions to match our labels (0 = normal, 1 = threat)
    preds = [1 if p == -1 else 0 for p in preds]
    
    print("\nClassification Report:")
    print(classification_report(y_true, preds))
    
    # Confusion Matrix Visualization
    cm = confusion_matrix(y_true, preds)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Threat'], yticklabels=['Normal', 'Threat'])
    plt.title('Threat Detection Confusion Matrix')
    plt.ylabel('Actual Truth')
    plt.xlabel('Predicted')
    
    os.makedirs(outputs_dir, exist_ok=True)
    cm_path = os.path.join(outputs_dir, "confusion_matrix.png")
    plt.savefig(cm_path)
    plt.close()
    
    print(f"[+] Confusion matrix graph saved to {cm_path}")

if __name__ == "__main__":
    from preprocess import preprocess_data
    X_scaled, y_true = preprocess_data()
    train_isolation_forest(X_scaled, y_true)
