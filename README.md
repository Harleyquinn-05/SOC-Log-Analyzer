
# 🔐 SOC Log Analyzer (Brute Force Detection)

A beginner-friendly Security Operations Center (SOC) log analysis tool built using Python.

This project simulates real-world SOC tasks by analyzing login logs and detecting potential brute-force attacks based on multiple failed login attempts.

---

## 📖 Project Overview

In a real SOC environment, analysts monitor system logs to detect suspicious activities.

This tool:
- Reads login log files
- Identifies failed login attempts
- Counts repeated failures per user
- Flags possible brute-force attacks

---

## 🛠 Technologies Used

- Python 3
- Collections module (Counter)
- Kali Linux (Development Environment)
- Git & GitHub

---

## 📂 Project Structure
SOC-Log-Analyzer/
│
├── detector.py # Python script for log analysis
├── login_logs.txt # Sample log file
└── README.md


---

## 🚀 How It Works

1. The script reads the `login_logs.txt` file.
2. It filters lines containing `LOGIN FAILED`.
3. Counts failed attempts per user.
4. If failed attempts ≥ 5, it flags:


Possible brute force attack on <username>


---

## ▶️ How to Run

Open terminal in project directory and run:

```
<img width="720" height="323" alt="flameshot gui" src="https://github.com/user-attachments/assets/18ac878d-fe28-4cb2-8f2e-6ba9bcfa7fc7" />




👩‍💻 Author

Mahima Singh
Aspiring Cybersecurity & SOC Analyst
