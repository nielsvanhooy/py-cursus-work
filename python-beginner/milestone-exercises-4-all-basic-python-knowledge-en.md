# Python Networking Exercises

## Overview
These exercises are designed to test your understanding of Python fundamentals while working with networking concepts. 
Each exercise builds upon the previous one, so complete them in order.

### Required Files
Before starting, create these sample files in your working directory:

**network_devices.txt**
```
Router,192.168.1.1,00:1A:2B:3C:4D:5E,active
Switch,192.168.1.2,00:1B:44:11:3A:B7,active
Laptop,192.168.1.10,00:1C:42:2E:60:4A,inactive
Phone,192.168.1.15,00:1D:33:44:55:66,active
Printer,192.168.1.20,00:1E:55:66:77:88,inactive
Server,192.168.1.100,00:1F:66:77:88:99,active
```

**firewall_logs.txt**
```
2024-06-11 08:15:23,192.168.1.10,80,ALLOW,HTTP
2024-06-11 08:16:45,10.0.0.5,22,DENY,SSH
2024-06-11 08:17:12,192.168.1.15,443,ALLOW,HTTPS
2024-06-11 08:18:33,172.16.0.100,23,DENY,Telnet
2024-06-11 08:19:55,192.168.1.10,25,ALLOW,SMTP
2024-06-11 08:20:17,203.0.113.15,3389,DENY,RDP
2024-06-11 08:21:42,192.168.1.20,80,ALLOW,HTTP
2024-06-11 08:22:58,192.168.1.100,443,ALLOW,HTTPS
2024-06-11 08:23:19,10.0.0.8,21,DENY,FTP
2024-06-11 08:24:31,192.168.1.15,993,ALLOW,IMAPS
```

---

## Exercise 1: Network Device Inventory Manager (Easy)

Create a comprehensive network device management system that reads device information from a file and provides various analysis functions.

### Requirements:

1. **Function: `load_network_devices(filename)`**
   -- Read the network_devices.txt file
   -- Return a list of dictionaries, where each dictionary represents a device with keys: "name", "ip", "mac", "status"
   -- Handle file not found errors gracefully

2. **Function: `display_device_summary(devices)`**
   -- Print a formatted summary showing:
     -- Total number of devices
     -- Number of active devices
     -- Number of inactive devices
     -- List all device names with their status

3. **Function: `find_devices_by_status(devices, status)`**
   -- Return a list of devices that match the given status ("active" or "inactive")
   -- The status parameter should be case-insensitive

4. **Function: `get_device_by_ip(devices, ip_address)`**
   -- Return the device dictionary that matches the given IP address
   -- Return None if no device is found

5. **Function: `validate_ip_format(ip_address)`**
   -- Check if the IP address follows the basic IPv4 format (xxx.xxx.xxx.xxx)
   -- Return True if valid, False otherwise
   -- Use string methods and basic validation (don't worry about valid IP ranges)

6. **Function: `create_device_report(devices, output_filename)`**
   -- Create a report file that lists all devices in a formatted way
   -- Include device name, IP, MAC address, and status
   -- Add a header with the total count of devices

### Main Program:
Write a main section that:
- Loads the devices from the file
- Displays the device summary
- Asks the user to enter an IP address and shows the corresponding device info
- Creates a device report file called "device_report.txt"

---

## Exercise 2: Firewall Log Analyzer (Medium)

Building on Exercise 1, create a firewall log analysis system that processes security logs and integrates with your device inventory.

### Requirements:

1. **Function: `load_firewall_logs(filename)`**
   -- Read the firewall_logs.txt file
   -- Return a list of dictionaries with keys: "timestamp", "ip", "port", "action", "protocol"
   -- Handle file errors appropriately

2. **Function: `parse_log_entry(log_line)`**
   -- Take a single line from the log file and convert it to a dictionary
   -- Handle any malformed lines by returning None

3. **Function: `filter_logs_by_action(logs, action)`**
   -- Return all log entries that match the specified action ("ALLOW" or "DENY")
   -- Make the search case-insensitive

4. **Function: `get_top_ports(logs, limit=5)`**
   -- Analyze all log entries and return the most frequently accessed ports
   -- Return a list of tuples: [(port, count), (port, count), ...]
   -- Sort by count in descending order

5. **Function: `analyze_ip_activity(logs, devices)`**
   -- Cross-reference firewall logs with your device inventory
   -- Return a dictionary where keys are IP addresses and values are dictionaries containing:
     -- "device_name": name from device inventory (or "Unknown" if not found)
     -- "total_requests": total number of log entries for this IP
     -- "allowed_requests": number of ALLOW entries
     -- "denied_requests": number of DENY entries

6. **Function: `detect_suspicious_activity(logs, max_denied_requests=3)`**
   -- Find IP addresses that have more than `max_denied_requests` DENY entries
   -- Return a list of dictionaries with IP address and deny count
   -- Sort by deny count in descending order

7. **Function: `generate_security_report(logs, devices, output_filename)`**
   -- Create a comprehensive security report file
   -- Include:
     -- Summary statistics (total logs, allowed vs denied)
     -- Top 5 most accessed ports
     -- IP activity analysis
     -- List of suspicious IPs
     -- Timestamp of the report

### Main Program:
Write a main section that:
- Loads both device inventory and firewall logs
- Displays summary statistics
- Shows the top 5 ports
- Lists any suspicious IP addresses
- Generates a security report file

---

### Bonus Challenges:
- Add input validation for all user inputs
- Implement a simple command-line menu system
- Add the ability to compare current analysis with previous runs
- Create a function to export data in CSV format for external analysis
---

## Testing Your Solutions

For each exercise, test your functions with:
- Valid input files
- Missing files
- Empty files
- Malformed data
- Edge cases (empty lists, invalid IP addresses, etc.)

Make sure your code handles errors gracefully and provides meaningful error messages to users.