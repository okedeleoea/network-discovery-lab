# Elastic Detection Rules

## Blocked SMB Attempt
```kql
destination.port:445 and event.action:("DROP","BLOCK")
```
Network Scan

```Kql
network.transport:tcp and destination.port > 0
```

