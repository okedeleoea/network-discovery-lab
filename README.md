# network-discovery-lab
**SOC Detection Engineering | Network Reconnaissance & Prevented Lateral Movement**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows_Event_Logs-0078D6?style=flat&logo=windows&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic_SIEM-005571?style=flat&logo=elastic&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kalilinux&logoColor=white)

---

## 📌 Overview
This lab demonstrates **network discovery and defensive detection** in a controlled environment.

The focus is **not exploitation**, but:
- detecting reconnaissance activity,
- validating security controls,
- documenting *prevented* lateral movement,
- and closing incidents professionally as a SOC analyst.

This mirrors how real SOC teams operate in production environments.



## 🎯 Objectives
- Simulate internal network discovery (port scanning)
- Detect reconnaissance activity using Python logic
- Attempt credential abuse and persistence
- Validate firewall controls blocking SMB
- Write SOC-grade investigation and response documentation
- Map activity to MITRE ATT&CK with **partial success accuracy*



## 🧪 Lab Environment
| Component | Details |
|--------|---------|
| Attacker | Kali Linux |
| Target | Windows workstation |
| Logs | Windows Security Event Logs |
| SIEM | Elastic (conceptual detections) |
| Language | Python |
| Tools | Nmap, schtasks, Windows Firewall |



## 🔍 Attack Simulation Summary 
1. Internal network discovery via TCP port scanning
2. New local user account created (`svc_backup`)
3. Attempted scheduled task execution **failed**
4. SMB access attempt over TCP/445
5. Windows Firewall **blocked SMB**
6. No persistence achieved
7. No lateral movement occurred

**Final Outcome:**  
✔ Reconnaissance detected  
✔ Credential abuse attempt observed  
✔ Lateral movement **prevented**

---

## 🛡️ Detection Coverage

### Network Discovery
- High-volume TCP port scanning
- Unique destination port thresholding

**MITRE**
- TA0043 – Reconnaissance  
- T1046 – Network Service Scanning  

---

### Credential Abuse (Partial)
- Local account creation detected
- Scheduled task creation attempted but failed

**MITRE**
- TA0006 – Credential Access  
- T1053.005 – Scheduled Task (Attempted)

---

### Lateral Movement (Blocked)
- SMB access attempt detected
- Firewall enforcement confirmed

**MITRE**
- TA0008 – Lateral Movement  
- T1021.002 – SMB (Blocked)

---

## 📊 Elastic Detection (Sample)
```kql
network.transport : "tcp" and
destination.port : 445 and
event.action : ("DROP","BLOCK")
```
🚨 Incident Outcome
Severity: Low
Status: Contained
Impact: None
Reason: Security controls functioned as designed

📁 Repository Structure
.
├── port_scan_detector.py
├── elastic-detection.md
├── investigation-timeline.md
├── analysis.md
├── remediation.md
├── soar-playbook.md
└── README.md

📈 Detection Maturity
Area
Level
Recon Detection
Implemented
Credential Abuse
Partial
Lateral Movement
Prevented
Automation
Conceptual
Documentation
SOC-grade

🚧 Detection Gaps
No EDR telemetry (Sysmon)
No AD telemetry
SIEM detections are conceptual

## How to Run the Detection Script

1. Clone the repository
2. Ensure Python 3 is installed
3. Place your `network.log` file
4. Run:
   ```bash
   python3 port_scan_detector.py
```

🔮 Future Improvements
Add Sysmon + Winlogbeat
Expand to Active Directory
Automate response actions
Visualize alerts in Elastic dashboards

👤 Author
Olanrewaju Emmanuel Okedele
Aspiring SOC Analyst | Detection Engineering
Ontario-focused job search
🔗 LinkedIn: https://www.linkedin.com/in/okedeleoea
