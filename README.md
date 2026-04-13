# AI-Powered Cybersecurity Threat Detection System 🚀🛡️

## 📌 Project Overview
This project simulates an **AI-powered Intrusion and Anomaly Detection System**. It monitors simulated network traffic, processes the log data, and uses Machine Learning (Isolation Forest) to detect unusual behavioral patterns indicative of cyber-attacks like DoS, Brute Force, and Data Exfiltration.

## 🎯 Problem Statement
Traditional rule-based cybersecurity systems struggle to detect "zero-day" and novel attack vectors. By leveraging Machine Learning anomaly detection, this system autonomously learns normal network behavior and flags deviations in real-time, significantly reducing response time for SOC (Security Operations Center) Analysts.

## 🛠 Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Isolation Forest)
* **Data Visualization:** Matplotlib, Seaborn

## 📂 Architecture
1. **Virtual Simulation:** Generates synthetic network logs with benign and malicious traffic.
2. **Preprocessing:** Standardizes features so no single network parameter dominates the model.
3. **Model:** Isolation Forest unsupervised learning to isolate threats.
4. **Alert Engine:** Flags malicious traffic and outputs security events.


