# Python Networking Exercises - Solutions

## Exercise 1: Network Device Inventory Manager (Easy)

```python
def load_network_devices(filename):
    """Load network devices from file and return list of dictionaries."""
    devices = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(',')
                    if len(parts) == 4:
                        device = {
                            "name": parts[0],
                            "ip": parts[1],
                            "mac": parts[2],
                            "status": parts[3]
                        }
                        devices.append(device)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return devices

def display_device_summary(devices):
    """Display a formatted summary of all devices."""
    if not devices:
        print("No devices to display.")
        return
    
    total_devices = len(devices)
    active_devices = len([d for d in devices if d["status"].lower() == "active"])
    inactive_devices = total_devices - active_devices
    
    print("=" * 50)
    print("NETWORK DEVICE SUMMARY")
    print("=" * 50)
    print(f"Total devices: {total_devices}")
    print(f"Active devices: {active_devices}")
    print(f"Inactive devices: {inactive_devices}")
    print("\nDevice List:")
    print("-" * 30)
    
    for device in devices:
        status_indicator = "✓" if device["status"].lower() == "active" else "✗"
        print(f"{status_indicator} {device['name']} ({device['status']})")

def find_devices_by_status(devices, status):
    """Return list of devices matching the given status."""
    return [device for device in devices if device["status"].lower() == status.lower()]

def get_device_by_ip(devices, ip_address):
    """Return device dictionary matching the IP address."""
    for device in devices:
        if device["ip"] == ip_address:
            return device
    return None

def validate_ip_format(ip_address):
    """Basic IPv4 format validation."""
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True

def create_device_report(devices, output_filename):
    """Create a formatted device report file."""
    try:
        with open(output_filename, 'w') as file:
            file.write("NETWORK DEVICE REPORT\n")
            file.write("=" * 50 + "\n")
            file.write(f"Total Devices: {len(devices)}\n")
            file.write(f"Generated on: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            file.write(f"{'Device Name':<15} {'IP Address':<15} {'MAC Address':<18} {'Status':<10}\n")
            file.write("-" * 65 + "\n")
            
            for device in devices:
                file.write(f"{device['name']:<15} {device['ip']:<15} {device['mac']:<18} {device['status']:<10}\n")
        
        print(f"Device report created successfully: {output_filename}")
    except Exception as e:
        print(f"Error creating report: {e}")

# Main program
if __name__ == "__main__":
    # Load devices
    devices = load_network_devices("network_devices.txt")
    if not devices:
        print("No devices loaded. Exiting.")
        exit()
    
    # Display summary
    display_device_summary(devices)
    
    # Interactive IP lookup
    print("\n" + "=" * 50)
    while True:
        ip_input = input("\nEnter an IP address to look up (or 'quit' to exit): ").strip()
        if ip_input.lower() == 'quit':
            break
        
        if not validate_ip_format(ip_input):
            print("Invalid IP format. Please use xxx.xxx.xxx.xxx format.")
            continue
        
        device = get_device_by_ip(devices, ip_input)
        if device:
            print(f"Found device: {device['name']} - Status: {device['status']} - MAC: {device['mac']}")
        else:
            print("No device found with that IP address.")
    
    # Create report
    create_device_report(devices, "device_report.txt")
```

---

## Exercise 2: Firewall Log Analyzer (Medium)

```python
from collections import Counter
import datetime

def load_firewall_logs(filename):
    """Load firewall logs from file and return list of dictionaries."""
    logs = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                log_entry = parse_log_entry(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return logs

def parse_log_entry(log_line):
    """Parse a single log line into a dictionary."""
    try:
        parts = log_line.split(',')
        if len(parts) == 5:
            return {
                "timestamp": parts[0],
                "ip": parts[1],
                "port": int(parts[2]),
                "action": parts[3],
                "protocol": parts[4]
            }
    except (ValueError, IndexError):
        print(f"Malformed log line: {log_line}")
    return None

def filter_logs_by_action(logs, action):
    """Return logs matching the specified action."""
    return [log for log in logs if log["action"].lower() == action.lower()]

def get_top_ports(logs, limit=5):
    """Return the most frequently accessed ports."""
    port_counter = Counter(log["port"] for log in logs)
    return port_counter.most_common(limit)

def analyze_ip_activity(logs, devices):
    """Cross-reference logs with device inventory."""
    ip_activity = {}
    
    # Create a lookup dictionary for devices by IP
    device_lookup = {device["ip"]: device["name"] for device in devices}
    
    for log in logs:
        ip = log["ip"]
        if ip not in ip_activity:
            ip_activity[ip] = {
                "device_name": device_lookup.get(ip, "Unknown"),
                "total_requests": 0,
                "allowed_requests": 0,
                "denied_requests": 0
            }
        
        ip_activity[ip]["total_requests"] += 1
        if log["action"].lower() == "allow":
            ip_activity[ip]["allowed_requests"] += 1
        elif log["action"].lower() == "deny":
            ip_activity[ip]["denied_requests"] += 1
    
    return ip_activity

def detect_suspicious_activity(logs, max_denied_requests=3):
    """Find IPs with excessive denied requests."""
    deny_counter = Counter(log["ip"] for log in logs if log["action"].lower() == "deny")
    
    suspicious_ips = []
    for ip, count in deny_counter.items():
        if count > max_denied_requests:
            suspicious_ips.append({"ip": ip, "deny_count": count})
    
    return sorted(suspicious_ips, key=lambda x: x["deny_count"], reverse=True)

def generate_security_report(logs, devices, output_filename):
    """Generate comprehensive security report."""
    try:
        with open(output_filename, 'w') as file:
            file.write("NETWORK SECURITY REPORT\n")
            file.write("=" * 60 + "\n")
            file.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Summary statistics
            total_logs = len(logs)
            allowed_logs = len(filter_logs_by_action(logs, "allow"))
            denied_logs = len(filter_logs_by_action(logs, "deny"))
            
            file.write("SUMMARY STATISTICS\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total log entries: {total_logs}\n")
            file.write(f"Allowed requests: {allowed_logs} ({allowed_logs/total_logs*100:.1f}%)\n")
            file.write(f"Denied requests: {denied_logs} ({denied_logs/total_logs*100:.1f}%)\n\n")
            
            # Top ports
            file.write("TOP 5 ACCESSED PORTS\n")
            file.write("-" * 30 + "\n")
            top_ports = get_top_ports(logs, 5)
            for port, count in top_ports:
                file.write(f"Port {port}: {count} requests\n")
            file.write("\n")
            
            # IP activity analysis
            file.write("IP ACTIVITY ANALYSIS\n")
            file.write("-" * 30 + "\n")
            ip_activity = analyze_ip_activity(logs, devices)
            for ip, activity in ip_activity.items():
                file.write(f"IP: {ip} ({activity['device_name']})\n")
                file.write(f"  Total: {activity['total_requests']}, ")
                file.write(f"Allowed: {activity['allowed_requests']}, ")
                file.write(f"Denied: {activity['denied_requests']}\n")
            file.write("\n")
            
            # Suspicious activity
            file.write("SUSPICIOUS ACTIVITY\n")
            file.write("-" * 30 + "\n")
            suspicious = detect_suspicious_activity(logs)
            if suspicious:
                for entry in suspicious:
                    file.write(f"⚠️  IP {entry['ip']}: {entry['deny_count']} denied requests\n")
            else:
                file.write("No suspicious activity detected.\n")
        
        print(f"Security report created: {output_filename}")
    except Exception as e:
        print(f"Error creating security report: {e}")

# Main program
if __name__ == "__main__":
    # Load data
    devices = load_network_devices("network_devices.txt")
    logs = load_firewall_logs("firewall_logs.txt")
    
    if not devices or not logs:
        print("Failed to load required data files.")
        exit()
    
    # Display summary
    print("FIREWALL LOG ANALYSIS")
    print("=" * 40)
    
    total_logs = len(logs)
    allowed = len(filter_logs_by_action(logs, "allow"))
    denied = len(filter_logs_by_action(logs, "deny"))
    
    print(f"Total log entries: {total_logs}")
    print(f"Allowed: {allowed} ({allowed/total_logs*100:.1f}%)")
    print(f"Denied: {denied} ({denied/total_logs*100:.1f}%)")
    
    # Top ports
    print(f"\nTop 5 Ports:")
    for port, count in get_top_ports(logs, 5):
        print(f"  Port {port}: {count} requests")
    
    # Suspicious activity
    suspicious = detect_suspicious_activity(logs)
    if suspicious:
        print(f"\n⚠️  Suspicious IPs detected:")
        for entry in suspicious:
            print(f"  {entry['ip']}: {entry['deny_count']} denied requests")
    
    # Generate report
    generate_security_report(logs, devices, "security_report.txt")
```

---

## Exercise 3: Network Security Dashboard (Hard)

```python
import datetime
from collections import Counter, defaultdict
import os

class NetworkMonitor:
    def __init__(self):
        self.devices = []
        self.logs = []
        self.topology = {}
        self.config = {}
        self.health_score = 0
        self.anomalies = []

def load_all_data(device_file, log_file, topology_file=None):
    """Load and validate all data sources."""
    monitor = NetworkMonitor()
    
    # Load devices
    monitor.devices = load_network_devices(device_file)
    if not monitor.devices:
        print("Warning: No devices loaded.")
    
    # Load logs
    monitor.logs = load_firewall_logs(log_file)
    if not monitor.logs:
        print("Warning: No logs loaded.")
    
    # Create topology
    monitor.topology = create_network_topology(monitor.devices)
    
    return monitor

def create_network_topology(devices):
    """Create network topology grouped by subnet."""
    topology = defaultdict(list)
    
    for device in devices:
        # Extract subnet (first 3 octets)
        ip_parts = device["ip"].split('.')
        if len(ip_parts) == 4:
            subnet = '.'.join(ip_parts[:3]) + '.0/24'
            topology[subnet].append(device)
    
    return dict(topology)

def calculate_network_health(devices, logs):
    """Calculate overall network health score (0-100)."""
    if not devices or not logs:
        return 0
    
    score = 0
    
    # Factor 1: Active device percentage (0-30 points)
    active_devices = len([d for d in devices if d["status"].lower() == "active"])
    device_health = (active_devices / len(devices)) * 30
    score += device_health
    
    # Factor 2: Allow/Deny ratio (0-25 points)
    allowed = len([l for l in logs if l["action"].lower() == "allow"])
    if logs:
        allow_ratio = (allowed / len(logs)) * 25
        score += allow_ratio
    
    # Factor 3: Protocol diversity (0-20 points)
    unique_protocols = len(set(log["protocol"] for log in logs))
    protocol_score = min(unique_protocols * 4, 20)  # Max 20 points
    score += protocol_score
    
    # Factor 4: Traffic distribution (0-25 points)
    if logs:
        ip_counter = Counter(log["ip"] for log in logs)
        # Check if traffic is well distributed (no single IP dominates)
        max_requests = max(ip_counter.values()) if ip_counter else 0
        total_requests = len(logs)
        if total_requests > 0:
            distribution_score = max(0, 25 - (max_requests / total_requests * 50))
            score += distribution_score
    
    return min(100, max(0, score))

def detect_anomalies(logs, devices):
    """Advanced anomaly detection."""
    anomalies = []
    
    if not logs:
        return anomalies
    
    # Anomaly 1: High volume from single IP
    ip_counter = Counter(log["ip"] for log in logs)
    avg_requests = len(logs) / len(ip_counter) if ip_counter else 0
    
    for ip, count in ip_counter.items():
        if count > avg_requests * 3:  # More than 3x average
            anomalies.append({
                "type": "High Volume",
                "description": f"IP {ip} has {count} requests (avg: {avg_requests:.1f})",
                "severity": "Medium"
            })
    
    # Anomaly 2: Unusual port access
    common_ports = {80, 443, 22, 25, 53, 993}
    unusual_ports = []
    
    for log in logs:
        if log["port"] not in common_ports and log["port"] > 1024:
            unusual_ports.append(log["port"])
    
    if unusual_ports:
        port_counter = Counter(unusual_ports)
        for port, count in port_counter.most_common(3):
            anomalies.append({
                "type": "Unusual Port",
                "description": f"High activity on uncommon port {port} ({count} requests)",
                "severity": "Low"
            })
    
    # Anomaly 3: Access to inactive devices
    inactive_ips = {d["ip"] for d in devices if d["status"].lower() == "inactive"}
    
    for log in logs:
        if log["ip"] in inactive_ips:
            anomalies.append({
                "type": "Inactive Device Access",
                "description": f"Traffic to inactive device {log['ip']}",
                "severity": "High"
            })
    
    # Anomaly 4: High deny rate for specific IPs
    ip_denies = defaultdict(int)
    ip_totals = defaultdict(int)
    
    for log in logs:
        ip_totals[log["ip"]] += 1
        if log["action"].lower() == "deny":
            ip_denies[log["ip"]] += 1
    
    for ip in ip_totals:
        if ip_totals[ip] >= 3:  # Only consider IPs with multiple requests
            deny_rate = ip_denies[ip] / ip_totals[ip]
            if deny_rate > 0.7:  # More than 70% denied
                anomalies.append({
                    "type": "High Deny Rate",
                    "description": f"IP {ip} has {deny_rate:.1%} requests denied",
                    "severity": "High"
                })
    
    return anomalies

def generate_network_map(topology, output_filename):
    """Create a text-based network map."""
    try:
        with open(output_filename, 'w') as file:
            file.write("NETWORK TOPOLOGY MAP\n")
            file.write("=" * 50 + "\n\n")
            
            for subnet, devices in topology.items():
                file.write(f"📁 {subnet}\n")
                file.write("  ├─ Devices:\n")
                
                for i, device in enumerate(devices):
                    connector = "└─" if i == len(devices) - 1 else "├─"
                    status_icon = "🟢" if device["status"].lower() == "active" else "🔴"
                    
                    file.write(f"  {connector} {status_icon} {device['name']} ({device['ip']})\n")
                    file.write(f"     MAC: {device['mac']}\n")
                
                file.write("\n")
        
        print(f"Network map created: {output_filename}")
    except Exception as e:
        print(f"Error creating network map: {e}")

def create_dashboard_summary(devices, logs, topology, health_score, anomalies):
    """Generate comprehensive dashboard summary."""
    print("\n" + "="*80)
    print("🖥️  NETWORK SECURITY DASHBOARD")
    print("="*80)
    
    # Health Score
    health_color = "🟢" if health_score >= 80 else "🟡" if health_score >= 60 else "🔴"
    print(f"\n📊 NETWORK HEALTH SCORE: {health_color} {health_score:.1f}/100")
    
    # Quick Stats
    print(f"\n📈 QUICK STATISTICS:")
    print(f"├─ Total Devices: {len(devices)}")
    print(f"├─ Active Devices: {len([d for d in devices if d['status'].lower() == 'active'])}")
    print(f"├─ Network Subnets: {len(topology)}")
    print(f"├─ Total Log Entries: {len(logs)}")
    print(f"└─ Security Anomalies: {len(anomalies)}")
    
    # Anomalies
    if anomalies:
        print(f"\n⚠️  SECURITY ALERTS:")
        high_severity = [a for a in anomalies if a["severity"] == "High"]
        medium_severity = [a for a in anomalies if a["severity"] == "Medium"]
        low_severity = [a for a in anomalies if a["severity"] == "Low"]
        
        if high_severity:
            print(f"🚨 HIGH PRIORITY ({len(high_severity)}):")
            for anomaly in high_severity[:3]:  # Show top 3
                print(f"   • {anomaly['description']}")
        
        if medium_severity:
            print(f"🟡 MEDIUM PRIORITY ({len(