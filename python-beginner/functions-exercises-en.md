# Python Function Exercises (Networking Theme)

These exercises focus on converting regular code into functions. Each exercise has two parts:
1. First, write the code to solve the problem
2. Then, refactor your code to use functions for better organization

## Beginner Exercises

### Exercise 1: IP Address Validator

**Task:** Create a program that validates whether a string is a valid IPv4 address.

**Requirements:**
- An IPv4 address consists of four numbers separated by dots (e.g., "192.168.1.1")
- Each number must be between 0 and 255
- The program should ask the user for an IP address and tell them if it's valid
- Then refactor your code to use a function called `is_valid_ip(ip_string)` that returns True or False

**Example:**
```
Enter an IP address: 192.168.1.1
Valid IP address!

Enter an IP address: 256.0.0.1
Invalid IP address!
```

### Exercise 2: Password Strength Checker

**Task:** Create a program that checks the strength of a password.

**Requirements:**
- A password should be at least 8 characters long
- A strong password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character
- The program should tell the user if their password is "weak", "medium", or "strong"
- Then refactor your code to use a function called `check_password_strength(password)` that returns the strength

**Example:**
```
Enter a password: password123
Password strength: weak (missing uppercase and special characters)

Enter a password: Password123!
Password strength: strong
```

### Exercise 3: Network Latency Simulator

**Task:** Create a program that simulates network latency for different types of connections.

**Requirements:**
- Ask the user what type of connection they want to simulate ("fiber", "cable", "dsl", or "satellite")
- Generate a random latency time based on the connection type:
  - Fiber: 5-15ms
  - Cable: 10-30ms
  - DSL: 15-40ms
  - Satellite: 500-700ms
- Display the simulated latency
- Then refactor your code to use a function called `simulate_latency(connection_type)` that returns the latency

**Example:**
```
Enter connection type (fiber, cable, dsl, satellite): fiber
Simulated latency: 8ms

Enter connection type (fiber, cable, dsl, satellite): satellite
Simulated latency: 650ms
```

### Exercise 4: Data Usage Calculator

**Task:** Create a program that calculates how much data different activities would use.

**Requirements:**
- Ask the user what activity they want to calculate data usage for:
  - "video" (3.5 MB per minute)
  - "audio" (1 MB per minute)
  - "browsing" (0.5 MB per minute)
  - "gaming" (40 MB per hour)
- Ask for how many hours they plan to do the activity
- Calculate and display the total data usage in MB or GB (if over 1000 MB)
- Then refactor your code to use a function called `calculate_data_usage(activity, hours)` that returns the usage

**Example:**
```
Select activity (video, audio, browsing, gaming): video
How many hours? 2
Total data usage: 420 MB

Select activity (video, audio, browsing, gaming): gaming
How many hours? 5
Total data usage: 200 MB
```

## Advanced Exercises Very difficult for the die hards

### Exercise 5: Network Packet Analyzer

**Task:** Create a program that analyzes a list of network packets and provides statistics.

**Requirements:**
- Create a dictionary for each packet with keys:
  - "source_ip" (string)
  - "destination_ip" (string)
  - "protocol" (string: "TCP", "UDP", or "ICMP")
  - "size" (integer: bytes)
  - "time" (float: seconds)
- Create a list of at least 10 sample packet dictionaries
- Calculate and display:
  - Total number of packets
  - Average packet size
  - Number of packets per protocol
  - Total data transferred
  - Unique source and destination IPs
- Then refactor your code to use at least 4 different functions to perform the calculations

**Example Output:**
```
Network Packet Analysis
----------------------
Total packets: 10
Average packet size: 512 bytes
Protocol distribution:
  - TCP: 6 packets
  - UDP: 3 packets
  - ICMP: 1 packet
Total data transferred: 5.12 KB
Unique source IPs: 3
Unique destination IPs: 4
```

### Exercise 6: Network Traffic Simulator

**Task:** Create a program that simulates network traffic between different devices.

**Requirements:**
- Create a set of "devices" (at least 5) with names and IP addresses
- Simulate random traffic between devices:
  - Each device should send data to 1-3 random other devices
  - The amount of data should be random (10KB to 1MB)
  - Each device can use different protocols (HTTP, FTP, SMTP)
- Track and display:
  - Total data sent by each device
  - Total data received by each device
  - Most active device (most data transferred)
  - Most popular protocol
- Then refactor your code to use at least 5 different functions for simulation and analysis

**Example Output:**
```
Network Traffic Simulation
-------------------------
Simulation period: 10 cycles

Device Statistics:
  - Router (192.168.1.1):
    Sent: 2.3 MB, Received: 1.5 MB
    
  - Laptop (192.168.1.101):
    Sent: 3.1 MB, Received: 0.8 MB
    
  - Smartphone (192.168.1.102):
    Sent: 1.2 MB, Received: 2.5 MB
    
  - Server (192.168.1.200):
    Sent: 5.6 MB, Received: 7.4 MB
    
  - SmartTV (192.168.1.103):
    Sent: 0.4 MB, Received: 0.4 MB

Analysis:
  - Most active device: Server (13.0 MB total)
  - Most popular protocol: HTTP (65% of traffic)
```