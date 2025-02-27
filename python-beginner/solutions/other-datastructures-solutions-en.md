# Beginner Network Engineering Exercises: Tuples & Sets - Solutions

These are the full solutions for the beginner-level network engineering exercises using tuples and sets.

---

## Solution 1: Storing Network Device Information (Tuples)

```python
def router_tuple():
    print("=== NETWORK DEVICE INFORMATION ===")
    
    # Step 1: Create a tuple with router name, IP address, and MAC address
    router_info = ("RouterA", "192.168.1.1", "AA:BB:CC:DD:EE:FF")
    
    # Step 2: Print each element separately
    print("Router Name:", router_info[0])
    print("IP Address:", router_info[1])
    print("MAC Address:", router_info[2])
    
    # Step 3: Try modifying the IP address (This will cause an error)
    # router_info[1] = "192.168.1.2"  # Uncomment to see the error
    
    print("\nDone!")
```

---

## Solution 2: Unique Connected Devices (Sets)

```python
def unique_connected_devices():
    print("=== UNIQUE CONNECTED DEVICES ===")
    
    # Step 1: Create an empty set
    connected_devices = set()
    
    # Step 2: Add multiple IPs, including duplicates
    connected_devices.update(["192.168.1.10", "192.168.1.11", "192.168.1.10", "192.168.1.12"])
    
    # Step 3: Print the set and observe if duplicates exist
    print("Connected Devices:", connected_devices)
    
    # Step 4: Remove an IP and print the set again
    connected_devices.discard("192.168.1.11")
    print("Updated Devices:", connected_devices)
    
    print("\nDone!")
```

---

## Solution 3: Comparing Network Segments (Sets)

```python
def compare_network_segments():
    print("=== COMPARING NETWORK SEGMENTS ===")
    
    # Step 1: Create two sets with overlapping IPs
    network_A = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
    network_B = {"192.168.1.3", "192.168.1.4", "192.168.1.5"}
    
    # Step 2: Print devices common in both networks
    print("Common Devices:", network_A & network_B)
    
    # Step 3: Print devices unique to network_A
    print("Devices only in Network A:", network_A - network_B)
    
    # Step 4: Print devices unique to network_B
    print("Devices only in Network B:", network_B - network_A)
    
    print("\nDone!")
```

---

## Solution 4: Immutable Network Configuration (Tuples)

```python
def immutable_network_config():
    print("=== NETWORK CONFIGURATION ===")
    
    # Step 1: Create a tuple with subnet mask, default gateway, and DNS server
    network_config = ("255.255.255.0", "192.168.1.1", "8.8.8.8")
    
    # Step 2: Print all values
    print("Subnet Mask:", network_config[0])
    print("Default Gateway:", network_config[1])
    print("Primary DNS Server:", network_config[2])
    
    # Step 3: Attempt to modify the DNS server (This will cause an error)
    # network_config[2] = "8.8.4.4"  # Uncomment to see the error
    
    print("\nDone!")
```

---

These solutions demonstrate how to work with tuples and sets in practical networking applications. Review them after completing the exercises!

