# Beginner Network Engineering Python Exercises

These simple exercises will help you practice Python basics while introducing network engineering concepts:
- Variables and data types
- Conditional statements (if/elif/else)
- Lists and loops
- Input/output

## Exercise 1: Device Name Generator

### Instructions:
Create a program that generates network device names based on user input.
1. Ask for the device type (Router, Switch, or Firewall)
2. Ask for a location code (3 letters)
3. Ask for a number
4. Generate a device name by combining these elements
   - Example: Router + NYC + 01 = RTR-NYC-01

### Starter Code:
```python
# ===== EXERCISE 1: DEVICE NAME GENERATOR =====

def device_name_generator():
    print("=== DEVICE NAME GENERATOR ===")
    print("Generate standardized network device names")
    
    generate_another = True
    
    while generate_another:
        # Get device information from user
        print("\nDevice types:")
        print("1. Router")
        print("2. Switch")
        print("3. Firewall")
        
        device_choice = input("Enter device type (1-3): ")
        
        # TODO: Convert the choice to a device code (RTR, SWT, FWL)
        # If choice is 1, device_code should be "RTR"
        # If choice is 2, device_code should be "SWT"
        # If choice is 3, device_code should be "FWL"
        # For any other input, set device_code to "DEV"
        
        # Get location from user
        location = input("Enter location code (3 letters, e.g. NYC): ").upper()
        
        # TODO: Check if location is valid (3 letters)
        # If not valid, set it to "LOC"
        
        # Get device number
        number = input("Enter device number (2 digits, e.g. 01): ")
        
        # TODO: Check if number is valid (2 digits)
        # If not valid, set it to "00"
        
        # TODO: Create the device name by combining the three parts
        # Format should be: <device_code>-<location>-<number>
        # Example: RTR-NYC-01
        
        # TODO: Display the generated device name
        
        # Ask if user wants to generate another name
        another = input("\nGenerate another device name? (yes/no): ").lower()
        if another != "yes" and another != "y":
            generate_another = False
    
    print("Thank you for using the Device Name Generator!")

# Run this program by removing the comment symbol (#) from the line below
# device_name_generator()
```

## Exercise 2: IP Address Counter

### Instructions:
Create a program that helps network technicians count through IP addresses.
1. Ask for a starting IP address (last octet only, e.g., 192.168.1.X)
2. Ask how many addresses to count
3. Display the list of addresses in sequence

### Starter Code:
```python
# ===== EXERCISE 2: IP ADDRESS COUNTER =====

def ip_address_counter():
    print("=== IP ADDRESS COUNTER ===")
    print("Generate a sequence of IP addresses")
    
    count_again = True
    
    while count_again:
        # Get the first three octets of the IP address
        base_ip = input("\nEnter the first three octets (e.g., 192.168.1): ")
        
        # Get the starting value for the last octet
        try:
            start_octet = int(input("Enter the starting value for the last octet (0-255): "))
            
            # TODO: Validate that start_octet is between 0 and 255
            # If invalid, print an error message and continue to the next loop iteration
            
            # Get the number of addresses to generate
            count = int(input("How many addresses do you want to count? "))
            
            # TODO: Validate that count is positive
            # If invalid, print an error message and continue
            
            # TODO: Generate and display the list of IP addresses
            # Be careful not to exceed 255 for the last octet
            # Format each address as: base_ip.last_octet
            # Example: 192.168.1.10, 192.168.1.11, etc.
            
        except ValueError:
            print("Please enter valid numbers!")
            continue
            
        # Ask if user wants to count again
        another = input("\nCount another sequence? (yes/no): ").lower()
        if another != "yes" and another != "y":
            count_again = False
    
    print("Thank you for using the IP Address Counter!")

# Run this program by removing the comment symbol (#) from the line below
# ip_address_counter()
```

## Exercise 3: Network Device List Manager

### Instructions:
Create a program that manages a list of network devices.
1. Allow adding and removing devices
2. Display the complete list
3. Count how many of each type of device you have

### Starter Code:
```python
# ===== EXERCISE 3: NETWORK DEVICE LIST MANAGER =====

def device_list_manager():
    # Initialize an empty list to store devices
    devices = []
    
    print("=== NETWORK DEVICE LIST MANAGER ===")
    print("Keep track of your network devices")
    
    while True:
        # Display menu
        print("\nWhat would you like to do?")
        print("1. Add a device")
        print("2. Remove a device")
        print("3. View all devices")
        print("4. Count devices by type")
        print("5. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Add a device
            device_name = input("Enter device name: ")
            
            print("Device types:")
            print("1. Router")
            print("2. Switch")
            print("3. Firewall")
            print("4. Server")
            print("5. Other")
            
            type_choice = input("Enter device type (1-5): ")
            
            # TODO: Convert type_choice to a device type string
            # Add the device name and type as a list to the devices list
            # Example: devices.append([device_name, device_type])
            
            # TODO: Print a confirmation message
            
        elif choice == "2":
            # Remove a device
            if len(devices) == 0:
                print("No devices to remove!")
                continue
                
            # TODO: Display devices with numbers
            # Ask user which one to remove
            # Remove the selected device
            # Print a confirmation message
            
        elif choice == "3":
            # View all devices
            if len(devices) == 0:
                print("No devices in the list!")
            else:
                # TODO: Display all devices in a formatted way
                # Example: 1. Router-1 (Router)
                pass
                
        elif choice == "4":
            # Count devices by type
            if len(devices) == 0:
                print("No devices in the list!")
            else:
                # TODO: Count how many of each type of device
                # Display the counts
                pass
                
        elif choice == "5":
            # Exit
            print("Thank you for using the Network Device List Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run this program by removing the comment symbol (#) from the line below
# device_list_manager()
```

## Exercise 4: Simple Port Scanner Simulator

### Instructions:
Create a program that simulates checking which ports are open on a device.
1. Generate a list of common ports (e.g., 22, 80, 443)
2. Randomly decide which ports are "open" and which are "closed"
3. Display the results in a formatted way

### Starter Code:
```python
# ===== EXERCISE 4: SIMPLE PORT SCANNER SIMULATOR =====

def port_scanner():
    # Import random module for simulating port status
    import random
    
    # List of common network ports and their services
    common_ports = [
        [20, "FTP Data"],
        [21, "FTP Control"],
        [22, "SSH"],
        [23, "Telnet"],
        [25, "SMTP"],
        [53, "DNS"],
        [80, "HTTP"],
        [110, "POP3"],
        [143, "IMAP"],
        [443, "HTTPS"],
        [3389, "RDP"]
    ]
    
    print("=== SIMPLE PORT SCANNER SIMULATOR ===")
    print("Simulate checking which ports are open on a device")
    
    scan_again = True
    
    while scan_again:
        # Get device to scan
        device_ip = input("\nEnter IP address to scan: ")
        
        print(f"\nScanning {device_ip} for open ports...")
        print("PORT\tSTATUS\tSERVICE")
        print("-" * 30)
        
        # TODO: For each port in common_ports:
        # 1. Randomly decide if the port is open (about 30% should be open)
        # 2. Display the port, its status (OPEN or CLOSED), and service name
        # Example output: 80     OPEN    HTTP
        
        # Count open ports
        # TODO: Count how many ports were found open
        # Display the total number and percentage of open ports
        
        # Ask to scan again
        another = input("\nScan another device? (yes/no): ").lower()
        if another != "yes" and another != "y":
            scan_again = False
    
    print("Thank you for using the Simple Port Scanner Simulator!")

# Run this program by removing the comment symbol (#) from the line below
# port_scanner()
```

## Challenge Ideas

Once you've completed the basic exercises, try these simple extensions:

1. **Device Name Generator**: Add validation for input and a feature to generate multiple names at once.

2. **IP Address Counter**: Enhance to support counting across subnet boundaries (e.g., from 192.168.1.255 to 192.168.2.0).

3. **Network Device List Manager**: Add the ability to save and load the device list from a file.

4. **Port Scanner Simulator**: Add more realistic behaviors, like scan timing or custom port lists.