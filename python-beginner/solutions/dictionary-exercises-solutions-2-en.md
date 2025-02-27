# Advanced Network Engineering Python Exercises - Solutions

These are the full solutions for the advanced network engineering exercises.

---

## Solution 1: Network Device Manager

```python
def network_device_manager():
    print("=== NETWORK DEVICE MANAGER ===")
    
    # Step 1: Create the initial dictionary
    devices = {
        "Router1": {"ip": "192.168.1.1", "status": "up"},
        "Switch2": {"ip": "192.168.1.2", "status": "down"},
        "Server3": {"ip": "192.168.1.10", "status": "up"}
    }
    
    # Step 2: Print Router1's details
    print("Router1 details:", devices.get("Router1"))
    
    # Step 3: Add a new device from user input
    new_device = input("Enter new device name: ")
    new_ip = input("Enter IP address for {}: ".format(new_device))
    new_status = input("Enter status (up/down) for {}: ".format(new_device))
    devices[new_device] = {"ip": new_ip, "status": new_status}
    
    # Step 4: Update an existing device's status
    update_device = input("Enter the device name to update its status: ")
    if update_device in devices:
        new_stat = input("Enter new status (up/down) for {}: ".format(update_device))
        devices[update_device]["status"] = new_stat
    else:
        print("Device not found!")
    
    # Step 5: Print the final inventory
    print("\nFinal Device Inventory:")
    for device, info in devices.items():
        print(f"{device}: IP = {info['ip']}, Status = {info['status']}")
    
    print("\nDone!")
```

---

## Solution 2: IP Log Analyzer

```python
def ip_log_analyzer():
    print("=== IP LOG ANALYZER ===")
    
    logs = [
        "2025-02-27 10:00:00 Router1 192.168.1.1 connected",
        "2025-02-27 10:05:00 Switch2 192.168.1.2 connected",
        "2025-02-27 10:10:00 Router1 192.168.1.1 disconnected",
        "2025-02-27 10:15:00 Server3 192.168.1.10 connected",
        "2025-02-27 10:20:00 Router1 192.168.1.1 connected",
        "2025-02-27 10:25:00 Switch2 192.168.1.2 disconnected"
    ]
    
    # Count occurrences of each IP address
    ip_counts = {}
    for entry in logs:
        parts = entry.split()
        ip = parts[3]
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1
    
    # Sort IPs by count (descending order)
    sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Print sorted IPs and their counts
    print("IP Address Counts (highest to lowest):")
    for ip, count in sorted_ips:
        print(f"{ip}: {count}")
    
    print("\nDone!")
```

---

## Solution 3: Network Traffic Data Analyzer

```python
def network_traffic_analyzer():
    print("=== NETWORK TRAFFIC ANALYZER ===")
    
    traffic_records = [
        ("192.168.1.1", "10.0.0.5", 500),
        ("192.168.1.2", "10.0.0.6", 1500),
        ("192.168.1.1", "10.0.0.7", 700),
        ("192.168.1.3", "10.0.0.8", 200),
        ("192.168.1.2", "10.0.0.9", 800),
        ("192.168.1.1", "10.0.0.10", 600),
        ("192.168.1.4", "10.0.0.11", 1200)
    ]
    
    # Accumulate total bytes for each source IP
    traffic_totals = {}
    for record in traffic_records:
        source_ip, _, bytes_transferred = record
        if source_ip in traffic_totals:
            traffic_totals[source_ip] += bytes_transferred
        else:
            traffic_totals[source_ip] = bytes_transferred
    
    # Sort the dictionary by total bytes transferred (descending order)
    sorted_traffic = sorted(traffic_totals.items(), key=lambda item: item[1], reverse=True)
    
    # Print the top 3 source IPs
    print("Top 3 Source IPs by Traffic:")
    for ip, total in sorted_traffic[:3]:
        print(f"{ip}: {total} bytes")
    
    print("\nDone!")
```

---

These solutions demonstrate how to manipulate dictionaries, process logs, and analyze network data efficiently. Use them to check your work or gain insights into optimizing Python scripts for network engineering tasks.

