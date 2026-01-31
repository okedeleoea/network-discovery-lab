## Remediation Recommendations

### SMB (Port 445)
- Restrict access to trusted internal subnets only
- Disable SMBv1
- Enforce strong authentication and account lockout policies

### NetBIOS (Port 139)
- Disable NetBIOS over TCP/IP if not required
- Block NetBIOS at network boundaries

### Monitoring & Detection
- Monitor Windows Event IDs 4624 and 4625 for abnormal logins
- Alert on unusual SMB connection patterns
- Enable centralized logging for Windows hosts

