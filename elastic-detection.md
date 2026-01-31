## Elastic Security Detection – Port Scan to Lateral Movement

### Detection Overview
This detection identifies internal reconnaissance followed by lateral movement using SMB/RPC.

### Detection Logic
- Threshold-based port scan detection (Elastic KQL)
- Event correlation using EQL

### MITRE ATT&CK Mapping
- TA0043 – Reconnaissance
- TA0008 – Lateral Movement

### Tools
- Elastic Security
- KQL
- EQL

