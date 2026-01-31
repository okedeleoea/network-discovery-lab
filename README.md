# Network Discovery, Detection & Automated Response Lab (Elastic + SOAR)

## Overview
This project demonstrates practical **Security Operations (SOC)** and **Security Automation (SOAR)** skills by simulating internal reconnaissance, detecting malicious behavior, and automating response workflows using industry-aligned methods.

The lab is designed to reflect real-world SOC activities commonly used by organizations in Canada, particularly in environments leveraging **Elastic Security**.

---

## Objectives
- Perform internal network discovery and service enumeration
- Detect TCP port scanning using time-window correlation
- Identify post-scan lateral movement over SMB/RPC
- Translate detection logic into Elastic Security rules
- Design a SOAR-style automated response playbook
- Document analyst investigation workflows

---

## Lab Environment
- **Host OS:** Windows
- **Attacker / Analyst:** Kali Linux
- **Target:** Internal Windows host
- **Tools:**
  - Nmap
  - Python
  - Elastic Security (KQL / EQL – conceptual)
  - Git

---

## Detection Capabilities

### 1. Port Scan Detection
- Detects high-volume TCP port scanning from a single source
- Uses **time-window correlation** and **unique port counting**
- Logic mirrors SIEM threshold-based detections

**MITRE ATT&CK**
- TA0043 – Reconnaissance  
- T1046 – Network Service Scanning

---

### 2. Post-Scan Lateral Movement Detection
- Identifies SMB/RPC connections following reconnaissance
- Correlates scanning activity with lateral movement attempts
- Focuses on ports 135, 139, and 445

**MITRE ATT&CK**
- TA0008 – Lateral Movement  
- T1021.002 – SMB / Windows Admin Shares  

---

## Automation & SOAR Design
A SOAR-style playbook was designed to:
- Enrich source IP and asset context
- Automatically contain suspicious hosts
- Escalate high-risk activity to analysts
- Create incidents with supporting evidence

This aligns with **Security Automation and Detection Engineering** practices used in modern SOCs.

---

## Analyst Investigation Workflow
Elastic Timeline-style investigation steps are documented, including:
- Pivoting on source IPs
- Time-based event expansion
- Focused analysis of SMB/RPC activity
- Incident outcome classification

---

## Repository Structure
```text
network-discovery-lab/
├── port_scan_detector.py        # Python detection engine
├── elastic-detection.md         # Elastic KQL & EQL detection rules
├── soar-playbook.md             # Automated response design
├── investigation-timeline.md   # SOC analyst investigation steps
├── analysis.md                  # Scan findings & risk analysis
├── remediation.md               # Hardening recommendations
└── README.md

