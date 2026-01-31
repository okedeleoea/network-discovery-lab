import csv
from collections import defaultdict

LOG_FILE = "network.log"
PORT_THRESHOLD = 3
  # adjustable
TIME_WINDOW = "1 minute"  # conceptual (for documentation)

def detect_port_scans(log_file):
    """
    Detects potential TCP port scanning activity based on
    number of unique destination ports accessed by a source IP.
    """

    scan_activity = defaultdict(set)

    with open(log_file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            src_ip = row["src_ip"]
            dest_port = row["dest_port"]

            # Track unique ports per source
            scan_activity[src_ip].add(dest_port)

    print("\n=== Port Scan Detection Report ===\n")

    alerts = 0
    for src_ip, ports in scan_activity.items():
        port_count = len(ports)

        if port_count >= PORT_THRESHOLD:
            alerts += 1
            print(f"[ALERT] Possible Port Scan Detected")
            print(f" Source IP     : {src_ip}")
            print(f" Ports Scanned : {port_count}")
            print(f" Sample Ports  : {sorted(list(ports))[:10]}")
            print("-" * 40)

    if alerts == 0:
        print("No port scanning activity detected.")

if __name__ == "__main__":
    detect_port_scans(LOG_FILE)

