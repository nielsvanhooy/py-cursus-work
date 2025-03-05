# Python Function Exercises - Solutions (For Teacher)

## Beginner Exercises

### Exercise 1: IP Address Validator

#### Solution Without Functions:
```python
# IP Address Validator without functions
ip_address = input("Enter an IP address: ")

# Split the IP address by dots
parts = ip_address.split(".")

# Check if there are exactly 4 parts
is_valid = True
if len(parts) != 4:
    is_valid = False
else:
    # Check if each part is a valid number between 0 and 255
    for part in parts:
        # Check if the part is a digit
        if not part.isdigit():
            is_valid = False
            break
            
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 255:
            is_valid = False
            break

# Display the result
if is_valid:
    print("Valid IP address!")
else:
    print("Invalid IP address!")
```

#### Solution With Functions:
```python
def is_valid_ip(ip_string):
    """
    Check if the string is a valid IPv4 address.
    Returns True if valid, False otherwise.
    """
    # Split the IP address by dots
    parts = ip_string.split(".")
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
        
    # Check if each part is a valid number between 0 and 255
    for part in parts:
        # Check if the part is a digit
        if not part.isdigit():
            return False
            
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 255:
            return False
            
    # If we got here, the IP is valid
    return True

# Main program
ip_address = input("Enter an IP address: ")

if is_valid_ip(ip_address):
    print("Valid IP address!")
else:
    print("Invalid IP address!")
```


### Exercise 2: Password Strength Checker

#### Solution Without Functions:
```python
# Password Strength Checker without functions
password = input("Enter a password: ")

# Check password length
if len(password) < 8:
    strength = "weak"
    reason = "too short"
else:
    # Check for different character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    
    # Determine strength
    if has_upper and has_lower and has_digit and has_special:
        strength = "strong"
        reason = ""
    elif has_upper and has_lower and has_digit:
        strength = "medium"
        reason = "missing special characters"
    elif has_upper and has_lower:
        strength = "weak"
        reason = "missing digits and special characters"
    else:
        strength = "weak"
        reason = "missing uppercase"
        if not has_lower:
            reason += ", lowercase"
        if not has_digit:
            reason += ", digits"
        if not has_special:
            reason += ", special characters"

# Display the result
if reason:
    print(f"Password strength: {strength} ({reason})")
else:
    print(f"Password strength: {strength}")
```

#### Solution With Functions:
```python
def check_password_strength(password):
    """
    Check the strength of a password and return a tuple with:
    (strength, reason)
    where strength is 'weak', 'medium', or 'strong'
    and reason explains why the password got that rating
    """
    # Check password length
    if len(password) < 8:
        return "weak", "too short"
        
    # Check for different character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    
    # Determine strength
    if has_upper and has_lower and has_digit and has_special:
        return "strong", ""
    elif has_upper and has_lower and has_digit:
        return "medium", "missing special characters"
    elif has_upper and has_lower:
        return "weak", "missing digits and special characters"
    else:
        reason = "missing uppercase"
        if not has_lower:
            reason += ", lowercase"
        if not has_digit:
            reason += ", digits"
        if not has_special:
            reason += ", special characters"
        return "weak", reason

# Main program
password = input("Enter a password: ")
strength, reason = check_password_strength(password)

if reason:
    print(f"Password strength: {strength} ({reason})")
else:
    print(f"Password strength: {strength}")
```

### Exercise 3: Network Latency Simulator

#### Solution Without Functions:
```python
# Network Latency Simulator without functions
import random

# Ask user for connection type
connection_type = input("Enter connection type (fiber, cable, dsl, satellite): ").lower()

# Determine latency range based on connection type
if connection_type == "fiber":
    min_latency = 5
    max_latency = 15
elif connection_type == "cable":
    min_latency = 10
    max_latency = 30
elif connection_type == "dsl":
    min_latency = 15
    max_latency = 40
elif connection_type == "satellite":
    min_latency = 500
    max_latency = 700
else:
    print("Invalid connection type!")
    min_latency = 0
    max_latency = 0

# If connection type was valid, simulate latency
if min_latency > 0:
    latency = random.randint(min_latency, max_latency)
    print(f"Simulated latency: {latency}ms")
```

#### Solution With Functions:
```python
import random

def simulate_latency(connection_type):
    """
    Simulates network latency for different connection types.
    Returns the latency in milliseconds or None if invalid connection type.
    """
    connection_type = connection_type.lower()
    
    # Determine latency range based on connection type
    if connection_type == "fiber":
        min_latency = 5
        max_latency = 15
    elif connection_type == "cable":
        min_latency = 10
        max_latency = 30
    elif connection_type == "dsl":
        min_latency = 15
        max_latency = 40
    elif connection_type == "satellite":
        min_latency = 500
        max_latency = 700
    else:
        return None
    
    # Generate random latency within the range
    return random.randint(min_latency, max_latency)

# Main program
connection_type = input("Enter connection type (fiber, cable, dsl, satellite): ")
latency = simulate_latency(connection_type)

if latency is not None:
    print(f"Simulated latency: {latency}ms")
else:
    print("Invalid connection type!")
```

### Exercise 4: Data Usage Calculator

#### Solution Without Functions:
```python
# Data Usage Calculator without functions

# Ask for activity and duration
activity = input("Select activity (video, audio, browsing, gaming): ").lower()
hours = float(input("How many hours? "))

# Calculate data usage based on activity
if activity == "video":
    # 3.5 MB per minute
    usage_mb = 3.5 * 60 * hours
elif activity == "audio":
    # 1 MB per minute
    usage_mb = 1 * 60 * hours
elif activity == "browsing":
    # 0.5 MB per minute
    usage_mb = 0.5 * 60 * hours
elif activity == "gaming":
    # 40 MB per hour
    usage_mb = 40 * hours
else:
    print("Invalid activity!")
    usage_mb = 0

# Display the result
if usage_mb > 0:
    if usage_mb >= 1000:
        usage_gb = usage_mb / 1000
        print(f"Total data usage: {usage_gb:.2f} GB")
    else:
        print(f"Total data usage: {usage_mb:.0f} MB")
```

#### Solution With Functions:
```python
def calculate_data_usage(activity, hours):
    """
    Calculate data usage in MB for a given activity and duration.
    Returns usage in MB or 0 if invalid activity.
    """
    activity = activity.lower()
    
    if activity == "video":
        # 3.5 MB per minute
        return 3.5 * 60 * hours
    elif activity == "audio":
        # 1 MB per minute
        return 1 * 60 * hours
    elif activity == "browsing":
        # 0.5 MB per minute
        return 0.5 * 60 * hours
    elif activity == "gaming":
        # 40 MB per hour
        return 40 * hours
    else:
        return 0

def format_data_usage(mb):
    """Format data usage in MB or GB for display"""
    if mb >= 1000:
        return f"{mb/1000:.2f} GB"
    else:
        return f"{mb:.0f} MB"

# Main program
activity = input("Select activity (video, audio, browsing, gaming): ")
hours = float(input("How many hours? "))

usage_mb = calculate_data_usage(activity, hours)

if usage_mb > 0:
    formatted_usage = format_data_usage(usage_mb)
    print(f"Total data usage: {formatted_usage}")
else:
    print("Invalid activity!")
```

## Advanced Exercises

### Exercise 5: Network Packet Analyzer

#### Solution Without Functions:
```python
# Network Packet Analyzer without functions

# Sample packets
packets = [
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 640, "time": 1.24},
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.2", "protocol": "UDP", "size": 320, "time": 1.45},
    {"source_ip": "10.0.0.1", "destination_ip": "192.168.1.2", "protocol": "TCP", "size": 480, "time": 1.86},
    {"source_ip": "192.168.1.2", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 560, "time": 2.12},
    {"source_ip": "192.168.1.3", "destination_ip": "10.0.0.3", "protocol": "ICMP", "size": 256, "time": 2.34},
    {"source_ip": "10.0.0.2", "destination_ip": "192.168.1.1", "protocol": "UDP", "size": 384, "time": 2.56},
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 720, "time": 2.78},
    {"source_ip": "192.168.1.3", "destination_ip": "10.0.0.4", "protocol": "TCP", "size": 512, "time": 3.01},
    {"source_ip": "192.168.1.2", "destination_ip": "10.0.0.2", "protocol": "UDP", "size": 448, "time": 3.25},
    {"source_ip": "10.0.0.1", "destination_ip": "192.168.1.1", "protocol": "TCP", "size": 688, "time": 3.48}
]

# Calculate statistics
total_packets = len(packets)

# Average packet size
total_size = 0
for packet in packets:
    total_size += packet["size"]
average_size = total_size / total_packets

# Packets per protocol
tcp_count = 0
udp_count = 0
icmp_count = 0
for packet in packets:
    if packet["protocol"] == "TCP":
        tcp_count += 1
    elif packet["protocol"] == "UDP":
        udp_count += 1
    elif packet["protocol"] == "ICMP":
        icmp_count += 1

# Total data transferred
total_data_kb = total_size / 1024

# Unique source and destination IPs
source_ips = set()
dest_ips = set()
for packet in packets:
    source_ips.add(packet["source_ip"])
    dest_ips.add(packet["destination_ip"])
unique_source_ips = len(source_ips)
unique_dest_ips = len(dest_ips)

# Display results
print("Network Packet Analysis")
print("----------------------")
print(f"Total packets: {total_packets}")
print(f"Average packet size: {average_size:.0f} bytes")
print("Protocol distribution:")
print(f"  - TCP: {tcp_count} packets")
print(f"  - UDP: {udp_count} packets")
print(f"  - ICMP: {icmp_count} packets")
print(f"Total data transferred: {total_data_kb:.2f} KB")
print(f"Unique source IPs: {unique_source_ips}")
print(f"Unique destination IPs: {unique_dest_ips}")
```

#### Solution With Functions:
```python
def get_packet_count(packets):
    """Return the total number of packets"""
    return len(packets)

def calculate_average_size(packets):
    """Calculate the average packet size in bytes"""
    if not packets:
        return 0
        
    total_size = sum(packet["size"] for packet in packets)
    return total_size / len(packets)

def count_protocols(packets):
    """
    Count packets by protocol type
    Returns a dictionary with protocol counts
    """
    protocol_counts = {}
    
    for packet in packets:
        protocol = packet["protocol"]
        if protocol in protocol_counts:
            protocol_counts[protocol] += 1
        else:
            protocol_counts[protocol] = 1
            
    return protocol_counts

def calculate_total_data(packets):
    """Calculate total data transferred in KB"""
    total_bytes = sum(packet["size"] for packet in packets)
    return total_bytes / 1024

def get_unique_ips(packets):
    """
    Get counts of unique source and destination IPs
    Returns a tuple of (unique_source_count, unique_dest_count)
    """
    source_ips = set(packet["source_ip"] for packet in packets)
    dest_ips = set(packet["destination_ip"] for packet in packets)
    
    return len(source_ips), len(dest_ips)

def display_packet_analysis(packets):
    """Display the analysis of packet data"""
    total_packets = get_packet_count(packets)
    avg_size = calculate_average_size(packets)
    protocol_counts = count_protocols(packets)
    total_data_kb = calculate_total_data(packets)
    unique_sources, unique_dests = get_unique_ips(packets)
    
    print("Network Packet Analysis")
    print("----------------------")
    print(f"Total packets: {total_packets}")
    print(f"Average packet size: {avg_size:.0f} bytes")
    
    print("Protocol distribution:")
    for protocol, count in protocol_counts.items():
        print(f"  - {protocol}: {count} packets")
        
    print(f"Total data transferred: {total_data_kb:.2f} KB")
    print(f"Unique source IPs: {unique_sources}")
    print(f"Unique destination IPs: {unique_dests}")

# Main program
# Sample packets
packets = [
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 640, "time": 1.24},
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.2", "protocol": "UDP", "size": 320, "time": 1.45},
    {"source_ip": "10.0.0.1", "destination_ip": "192.168.1.2", "protocol": "TCP", "size": 480, "time": 1.86},
    {"source_ip": "192.168.1.2", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 560, "time": 2.12},
    {"source_ip": "192.168.1.3", "destination_ip": "10.0.0.3", "protocol": "ICMP", "size": 256, "time": 2.34},
    {"source_ip": "10.0.0.2", "destination_ip": "192.168.1.1", "protocol": "UDP", "size": 384, "time": 2.56},
    {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1", "protocol": "TCP", "size": 720, "time": 2.78},
    {"source_ip": "192.168.1.3", "destination_ip": "10.0.0.4", "protocol": "TCP", "size": 512, "time": 3.01},
    {"source_ip": "192.168.1.2", "destination_ip": "10.0.0.2", "protocol": "UDP", "size": 448, "time": 3.25},
    {"source_ip": "10.0.0.1", "destination_ip": "192.168.1.1", "protocol": "TCP", "size": 688, "time": 3.48}
]

# Run the analysis
display_packet_analysis(packets)
```

### Exercise 6: Network Traffic Simulator

#### Solution Without Functions:
```python
# Network Traffic Simulator without functions
import random

# Create devices
devices = [
    {"name": "Router", "ip": "192.168.1.1", "sent": 0, "received": 0},
    {"name": "Laptop", "ip": "192.168.1.101", "sent": 0, "received": 0},
    {"name": "Smartphone", "ip": "192.168.1.102", "sent": 0, "received": 0},
    {"name": "Server", "ip": "192.168.1.200", "sent": 0, "received": 0},
    {"name": "SmartTV", "ip": "192.168.1.103", "sent": 0, "received": 0}
]

# Protocols to simulate
protocols = ["HTTP", "FTP", "SMTP"]
protocol_counts = {"HTTP": 0, "FTP": 0, "SMTP": 0}

# Simulate traffic for 10 cycles
simulation_cycles = 10
for cycle in range(simulation_cycles):
    # Each device sends data to 1-3 random other devices
    for sender_idx, sender in enumerate(devices):
        # How many devices to send to (1-3)
        num_recipients = random.randint(1, 3)
        
        # Get recipient indices (excluding self)
        possible_recipients = list(range(len(devices)))
        possible_recipients.remove(sender_idx)
        recipient_indices = random.sample(possible_recipients, min(num_recipients, len(possible_recipients)))
        
        for recipient_idx in recipient_indices:
            # Generate random data size (10KB to 1MB)
            data_size_kb = random.randint(10, 1000)
            
            # Choose random protocol
            protocol = random.choice(protocols)
            protocol_counts[protocol] += data_size_kb
            
            # Update sent and received counts
            devices[sender_idx]["sent"] += data_size_kb
            devices[recipient_idx]["received"] += data_size_kb

# Find most active device
most_active_device = None
most_active_amount = -1
for device in devices:
    total_data = device["sent"] + device["received"]
    if total_data > most_active_amount:
        most_active_amount = total_data
        most_active_device = device

# Find most popular protocol
most_popular_protocol = None
most_popular_amount = -1
for protocol, amount in protocol_counts.items():
    if amount > most_popular_amount:
        most_popular_amount = amount
        most_popular_protocol = protocol

# Calculate total traffic
total_traffic = sum(protocol_counts.values())

# Display results
print("Network Traffic Simulation")
print("-------------------------")
print(f"Simulation period: {simulation_cycles} cycles\n")

print("Device Statistics:")
for device in devices:
    sent_mb = device["sent"] / 1000
    received_mb = device["received"] / 1000
    print(f"  - {device['name']} ({device['ip']}):")
    print(f"    Sent: {sent_mb:.1f} MB, Received: {received_mb:.1f} MB\n")

print("Analysis:")
print(f"  - Most active device: {most_active_device['name']} ({most_active_amount/1000:.1f} MB total)")
most_popular_percentage = (most_popular_amount / total_traffic) * 100
print(f"  - Most popular protocol: {most_popular_protocol} ({most_popular_percentage:.0f}% of traffic)")
```

#### Solution With Functions:
```python
import random

def create_devices():
    """Create and return a list of network devices"""
    return [
        {"name": "Router", "ip": "192.168.1.1", "sent": 0, "received": 0},
        {"name": "Laptop", "ip": "192.168.1.101", "sent": 0, "received": 0},
        {"name": "Smartphone", "ip": "192.168.1.102", "sent": 0, "received": 0},
        {"name": "Server", "ip": "192.168.1.200", "sent": 0, "received": 0},
        {"name": "SmartTV", "ip": "192.168.1.103", "sent": 0, "received": 0}
    ]

def simulate_traffic(devices, cycles):
    """
    Simulate network traffic between devices for a number of cycles.
    Returns a dictionary of protocol usage counts.
    """
    protocols = ["HTTP", "FTP", "SMTP"]
    protocol_counts = {"HTTP": 0, "FTP": 0, "SMTP": 0}
    
    for cycle in range(cycles):
        # Each device sends data to 1-3 random other devices
        for sender_idx, sender in enumerate(devices):
            # How many devices to send to (1-3)
            num_recipients = random.randint(1, 3)
            
            # Get recipient indices (excluding self)
            possible_recipients = list(range(len(devices)))
            possible_recipients.remove(sender_idx)
            recipient_indices = random.sample(possible_recipients, min(num_recipients, len(possible_recipients)))
            
            for recipient_idx in recipient_indices:
                # Generate random data size (10KB to 1MB)
                data_size_kb = random.randint(10, 1000)
                
                # Choose random protocol
                protocol = random.choice(protocols)
                protocol_counts[protocol] += data_size_kb
                
                # Update sent and received counts
                devices[sender_idx]["sent"] += data_size_kb
                devices[recipient_idx]["received"] += data_size_kb
    
    return protocol_counts

def find_most_active_device(devices):
    """Find and return the most active device and total data"""
    most_active_device = None
    most_active_amount = -1
    
    for device in devices:
        total_data = device["sent"] + device["received"]
        if total_data > most_active_amount:
            most_active_amount = total_data
            most_active_device = device
            
    return most_active_device, most_active_amount

def find_most_popular_protocol(protocol_counts):
    """Find and return the most popular protocol and amount"""
    most_popular_protocol = None
    most_popular_amount = -1
    
    for protocol, amount in protocol_counts.items():
        if amount > most_popular_amount:
            most_popular_amount = amount
            most_popular_protocol = protocol
            
    return most_popular_protocol, most_popular_amount

def display_simulation_results(devices, protocol_counts, cycles):
    """Display the simulation results"""
    most_active_device, most_active_amount = find_most_active_device(devices)
    most_popular_protocol, most_popular_amount = find_most_popular_protocol(protocol_counts)
    
    # Calculate total traffic
    total_traffic = sum(protocol_counts.values())
    
    # Display results
    print("Network Traffic Simulation")
    print("-------------------------")
    print(f"Simulation period: {cycles} cycles\n")
    
    print("Device Statistics:")
    for device in devices:
        sent_mb = device["sent"] / 1000
        received_mb = device["received"] / 1000
        print(f"  - {device['name']} ({device['ip']}):")
        print(f"    Sent: {sent_mb:.1f} MB, Received: {received_mb:.1f} MB\n")
    
    print("Analysis:")
    print(f"  - Most active device: {most_active_device['name']} ({most_active_amount/1000:.1f} MB total)")
    most_popular_percentage = (most_popular_amount / total_traffic) * 100
    print(f"  - Most popular protocol: {most_popular_protocol} ({most_popular_percentage:.0f}% of traffic)")
```