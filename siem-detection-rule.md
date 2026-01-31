## SIEM Detection Rule: Internal Network Scanning

### Objective
Detect TCP port scanning behavior within the internal network.

### Data Sources
- Network traffic logs
- Firewall logs
- Windows Defender Firewall logs

### Detection Logic
Trigger when a single source IP attempts connections to a high number of unique destination ports within a short time window.

### Pseudo-SPL
index=network
| where tcp_flags="SYN"
| bucket _time span=1m
| stats distinct_count(dest_port) AS port_count by src_ip, dest_ip
| where port_count > 30

### Severity
Medium

### Response
- Identify scanning host
- Verify authorization
- Monitor for lateral movement

