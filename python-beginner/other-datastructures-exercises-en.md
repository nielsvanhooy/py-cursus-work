# Beginner Network Engineering Exercises: Tuples & Sets

These exercises introduce tuples and sets, focusing on how they can be applied in network engineering.

---

## Exercise 1: Storing Network Device Information (Tuples)

### Objective:
Understand how tuples can store immutable network device information.

### Tasks:
1. Create a tuple named `router_info` containing:
   - Router name (string)
   - IP address (string)
   - MAC address (string)
2. Print each element of the tuple.
3. Try modifying the IP address and observe what happens.

```python
# HINT: Tuples are immutable. Trying to modify them will cause an error.

def router_tuple():
    print("=== NETWORK DEVICE INFORMATION ===")
    
    # TODO: Create a tuple with router name, IP address, and MAC address
    
    # TODO: Print each element separately
    
    # TODO: Try modifying the IP address and observe the result
    
    print("\nDone!")

# Uncomment the line below to run the function
# router_tuple()
```

---

## Exercise 2: Unique Connected Devices (Sets)

### Objective:
Use a set to store unique connected device IPs.

### Tasks:
1. Create an empty set named `connected_devices`.
2. Add the following IPs: `192.168.1.10`, `192.168.1.11`, `192.168.1.10`, `192.168.1.12`.
3. Print the set and observe duplicate handling.
4. Remove an IP and print the updated set.

```python
# HINT: Sets automatically remove duplicates.

def unique_connected_devices():
    print("=== UNIQUE CONNECTED DEVICES ===")
    
    # TODO: Create an empty set
    
    # TODO: Add multiple IPs, including duplicates
    
    # TODO: Print the set and observe if duplicates exist
    
    # TODO: Remove an IP and print the set again
    
    print("\nDone!")

# Uncomment the line below to run the function
# unique_connected_devices()
```

---

## Exercise 3: Comparing Network Segments (Sets)

### Objective:
Use sets to find common and unique devices in two network segments.

### Tasks:
1. Create two sets: `network_A` and `network_B`, containing some overlapping device IPs.
2. Print devices common to both networks.
3. Print devices unique to `network_A`.
4. Print devices unique to `network_B`.

```python
# HINT: Use set operations like intersection() and difference().

def compare_network_segments():
    print("=== COMPARING NETWORK SEGMENTS ===")
    
    # TODO: Create two sets with overlapping IPs
    
    # TODO: Print devices common in both networks
    
    # TODO: Print devices unique to network_A
    
    # TODO: Print devices unique to network_B
    
    print("\nDone!")

# Uncomment the line below to run the function
# compare_network_segments()
```

---

## Exercise 4: Immutable Network Configuration (Tuples)

### Objective:
Use a tuple to store a read-only network configuration.

### Tasks:
1. Define a tuple named `network_config` containing:
   - Subnet mask
   - Default gateway
   - Primary DNS server
2. Print all values.
3. Attempt to change the DNS server and observe the result.

```python
# HINT: Tuples cannot be modified after creation.

def immutable_network_config():
    print("=== NETWORK CONFIGURATION ===")
    
    # TODO: Create a tuple with subnet mask, default gateway, and DNS server
    
    # TODO: Print all values
    
    # TODO: Attempt to modify the DNS server and observe what happens
    
    print("\nDone!")

# Uncomment the line below to run the function
# immutable_network_config()
```
