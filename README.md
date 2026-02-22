# 🚀 Infrastructure Security Scanner  
### Python-Based Network Risk Assessment Tool

## 📌 Project Overview

Infrastructure Security Scanner is a Python-based tool that analyzes open TCP ports on a target host, identifies exposed services, evaluates security risk levels, and generates structured audit reports.

This project simulates basic vulnerability assessment techniques used in real-world DevOps and infrastructure security environments.

---

## 🎯 Problem Statement

In IT and DevOps environments, exposed network ports can increase security risks and create potential attack surfaces. Engineers must regularly audit systems to detect open services and evaluate infrastructure risk levels.

This tool automates basic security auditing by scanning commonly used service ports and generating risk-based compliance reports.

---

## ⚙️ Features

- Scans common TCP service ports (FTP, SSH, HTTP, HTTPS, MySQL, RDP, etc.)
- Detects open and closed ports using socket-based TCP connection attempts
- Classifies overall security risk (LOW / LOW-MEDIUM / MEDIUM / HIGH)
- Generates timestamped security audit report
- Accepts custom target host input
- Fully offline (No AWS account required)

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- File Handling
- Networking Concepts
- Risk Classification Logic

---

## 🧠 How It Works

1. User enters target host (default: 127.0.0.1).
2. The program attempts TCP connections to predefined ports.
3. If connection succeeds → Port is marked OPEN.
4. Open ports are stored and analyzed.
5. Risk level is calculated based on predefined high-risk ports.
6. A structured security report file is generated.

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository

git clone https://github.com/rushikeshgokhe/infrastructure-security-scanner.git

cd infrastructure-security-scanner

### 2️⃣ Run the Program

python security_scanner.py

### 3️⃣ Enter Target Host

Press Enter to scan localhost  
OR  
Enter any reachable IP address

---

## 📄 Example Console Output

==== Local Infrastructure Security Scanner ====

Enter target host (default: 127.0.0.1):

Starting Security Scan on 127.0.0.1...

Port 21 (FTP) is closed  
Port 80 (HTTP) is OPEN  
Port 443 (HTTPS) is closed  

Scan Completed  
Risk Level: LOW-MEDIUM  

---

## 📄 Generated Report

The program automatically creates:

security_scan_report.txt

Example content:

===== INFRASTRUCTURE SECURITY SCAN REPORT =====
Scan Time: 2026-02-21 22:00:15
Target Host: 127.0.0.1

Open Ports Detected:
- Port 80 (HTTP)

Overall Risk Level: LOW-MEDIUM

---

## 🔐 Risk Classification Logic

- HIGH → High-risk ports exposed (FTP, Telnet, MySQL, RDP)
- MEDIUM → Multiple services exposed
- LOW-MEDIUM → Few non-critical ports open
- LOW → No exposed services detected

---

## 🚀 Future Improvements

- Scan custom port ranges (1–1024)
- Add multithreading for faster scanning
- Maintain scan history logs
- Integrate with AWS using boto3 for cloud security auditing
- Develop a web-based dashboard

---

## 👨‍💻 Author

Rushikesh Gokhe  
Aspiring Cloud & DevOps Engineer
