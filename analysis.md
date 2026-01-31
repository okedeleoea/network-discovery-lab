## Network Discovery & Service Enumeration

### Target
Windows host on internal network

### Tools Used
- Nmap

### Findings
- Port 135 (MSRPC)
- Port 139 (NetBIOS)
- Port 445 (SMB)

### Risk Analysis
These services can be abused for:
- Lateral movement
- Credential harvesting
- Remote code execution

### Recommendations
- Restrict SMB access via firewall
- Disable NetBIOS if not required
- Monitor Windows Event IDs related to SMB activity

