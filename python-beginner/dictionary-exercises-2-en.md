# Advanced Network Engineering Python Exercises

These exercises are designed to reinforce your understanding of Python dictionaries, loops, user input, and data processing in a network engineering context.

---

## Exercise 1: Network Device Manager

### Objective
Manage a dictionary of network devices. Each device is represented as a key (device name) with a dictionary as the value containing:
- `"ip"`: The device's IP address (string)
- `"status"`: Either `"up"` or `"down"` (string)

### Tasks
1. Create a dictionary named `devices` with at least three devices (e.g., `"Router1"`, `"Switch2"`, `"Server3"`).
2. Print the IP and status of `"Router1"`.
3. Prompt the user to add a new device by entering its name, IP, and status.
4. Ask the user for a device name to update its status. If the device exists, update it; otherwise, print an error message.
5. Print the final device inventory.

```python
# HINT: Create a dictionary with nested dictionaries for devices
# HINT: Use input() to collect new device details
# HINT: Use .get() or dictionary indexing to retrieve values

def network_device_manager():
    print("=== NETWORK DEVICE MANAGER ===")
    
    # Step 1: Create the initial dictionary
    devices = {
        "Router1": {"ip": "192.168.1.1", "status": "up"},
        "Switch2": {"ip": "192.168.1.2", "status": "down"},
        "Server3": {"ip": "192.168.1.10", "status": "up"}
    }
    
    # Step 2: Print Router1's details
    # TODO: Print Router1's IP and status
    
    # Step 3: Add a new device from user input
    # TODO: Ask user for new device details and add it to the dictionary
    
    # Step 4: Update an existing device's status
    # TODO: Ask user for a device name and update its status if it exists
    
    # Step 5: Print the final inventory
    # TODO: Loop through dictionary and print all devices and their details
    
    print("\nDone!")

# Uncomment the line below to run the function
# network_device_manager()
```

---

## Exercise 2: IP Log Analyzer

### Objective
Analyze a list of network log entries to count how many times each IP address appears, then display the counts sorted from highest to lowest.

### Tasks
1. Given a list of log strings in the format: `"timestamp device_name IP_address action"`, extract the IP address.
2. Count how many times each IP appears using a dictionary.
3. Sort the dictionary in descending order based on occurrence count.
4. Print the IPs with their counts.

```python
# HINT: Use .split() to extract the IP from each log entry
# HINT: Use a dictionary to store counts
# HINT: Use sorted() with key=lambda to sort by value

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
    
    # Step 1: Create an empty dictionary for IP counts
    # TODO: Extract IPs and count occurrences
    
    # Step 2: Sort IPs by count (descending order)
    # TODO: Use sorted() to sort dictionary by values
    
    # Step 3: Print sorted IPs and their counts
    
    print("\nDone!")

# Uncomment the line below to run the function
# ip_log_analyzer()
```

---

## Exercise 3: Network Traffic Data Analyzer

### Objective
Analyze simulated network traffic records to determine which source IPs are generating the most traffic.

### Tasks
1. Given a list of tuples `(source_ip, destination_ip, bytes_transferred)`, track the total bytes transferred per source IP.
2. Sort and print the top three source IPs by traffic.

```python
# HINT: Loop through the traffic records and accumulate traffic for each source IP
# HINT: Use sorted() to order source IPs by total bytes transferred

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
    
    # Step 1: Create a dictionary to store total bytes transferred per source IP
    # TODO: Loop through traffic records and sum bytes per source IP
    
    # Step 2: Sort the dictionary by total bytes transferred (descending order)
    # TODO: Use sorted() with key=lambda to sort by value
    
    # Step 3: Print the top 3 source IPs
    
    print("\nDone!")

# Uncomment the line below to run the function
# network_traffic_analyzer()
```
