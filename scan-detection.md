## Detection: Network Scanning Activity

### Detection Summary
Aggressive TCP SYN scan detected targeting all TCP ports from a single internal source.

### Indicators
- High-volume SYN packets to sequential ports
- Incomplete TCP handshakes
- Short scan duration (~90 seconds)
- Dynamic RPC port (49668) exposure

### Likely Tools
- Nmap (-sS -p- -T4)

### Severity
Medium

### Analyst Action
- Identify source IP and host
- Validate if scanning is authorized
- Monitor for follow-up lateral movement attempts

### SOC Notes
Presence of high dynamic ports may indicate RPC-based activity and should be correlated with authentication logs.

