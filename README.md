⚠️ This repository has been archived.

This project evolved into:
➡️ soc-detection-engineering-lifecycle-lab

# network-discovery-lab
**SOC Detection Engineering | Network Reconnaissance & Prevented Lateral Movement**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows_Event_Logs-0078D6?style=flat&logo=windows&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic_SIEM-005571?style=flat&logo=elastic&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kalilinux&logoColor=white)

---

📖 Overview

This lab simulates internal network discovery activity and documents how a security analyst can observe, validate, and assess reconnaissance behavior before any successful exploitation or lateral movement occurs.

The goal is not to break into systems, but to understand:

What reconnaissance looks like on a network

What information an attacker attempts to gather

What defenders should expect to see in logs and scans

Where detection and prevention controls succeed or fail

This project represents the early phase of the attack lifecycle, and serves as a foundation for later detection engineering and SIEM-focused labs.

🎯 Objectives

Perform controlled internal network reconnaissance

Identify exposed services and open ports

Validate host reachability and network segmentation

Document reconnaissance artifacts and observations

Assess security posture based on discovery results

Prepare inputs for downstream detection engineering

🧪 Lab Environment
Component	Details
Analyst / Attacker Host	Kali Linux
Target Host	Windows workstation
Network Type	Internal / lab network
Tools Used	Nmap, Ping, SMB client (enumeration only)
Focus	Visibility, documentation, analysis

⚠️ No exploitation or privilege escalation is performed in this lab.

🔍 Activities Performed
1️⃣ Host Reachability Testing

ICMP probing to assess whether hosts respond to pings

Observation of blocked vs allowed ICMP traffic

Purpose:
Determine network visibility and firewall behavior.

2️⃣ Port & Service Discovery

Targeted port scanning (including TCP/445)

Identification of filtered, closed, and open ports

Purpose:
Understand which services are exposed internally and which are protected by firewall rules.

3️⃣ Service Enumeration (Non-Exploitive)

Attempted SMB service discovery

No authentication success

No share access achieved

Purpose:
Validate that file sharing controls and firewall rules prevent enumeration and access.

🧠 Key Findings

Target host was reachable but selectively filtered

SMB (TCP/445) was blocked / filtered

No successful authentication or resource access occurred

Network segmentation and host firewall controls were effective

🛡️ Defensive Interpretation (SOC Perspective)

From a SOC analyst viewpoint, this activity represents:

Pre-attack reconnaissance

An opportunity for:

Early detection

Threat hunting

Alert tuning

Evidence that preventive controls are working as designed

This lab intentionally stops before detection logic, which is handled in the separate:

➡️ network-detection-lab

🧩 Relationship to Other Labs
Lab	Purpose
network-discovery-lab	Reconnaissance & visibility
network-detection-lab	SIEM alerts & detection rules
AD attack labs	Credential abuse & lateral movement
Automation labs	Python-based detection & enrichment

This separation mirrors real SOC workflows and improves portfolio clarity.

📚 MITRE ATT&CK Mapping (Discovery Only)

TA0043 – Reconnaissance

T1046 – Network Service Scanning

No lateral movement, credential access, or persistence techniques are executed in this lab.

📂 Repository Structure
network-discovery-lab/
├── README.md
├── analysis.md                # Scan results & observations
├── screenshots/               # Evidence of scans & outputs
└── notes.md                   # Analyst interpretation & lessons learned

👤 Author
Olanrewaju Emmanuel Okedele
Aspiring SOC Analyst | Detection Engineering
Ontario-focused job search
🔗 LinkedIn: https://www.linkedin.com/in/olanrewajuemmanuelokedele
