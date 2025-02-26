# Beginner Network Engineering Python Exercises - Solutions

## Exercise 1: Device Name Generator

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
        
        # Convert the choice to a device code
        if device_choice == "1":
            device_code = "RTR"
        elif device_choice == "2":
            device_code = "SWT"
        elif device_choice == "3":
            device_code = "FWL"
        else:
            device_code = "DEV"
            print("Invalid device type! Using DEV as default.")
        
        # Get location from user
        location = input("Enter location code (3 letters, e.g. NYC): ").upper()
        
        # Check if location is valid (3 letters)
        if len(location) != 3 or not location.isalpha():
            location = "LOC"
            print("Invalid location code! Using LOC as default.")
        
        # Get device number
        number = input("Enter device number (2 digits, e.g. 01): ")
        
        # Check if number is valid (2 digits)
        if len(number) != 2 or not number.isdigit():
            number = "00"
            print("Invalid device number! Using 00 as default.")
        
        # Create the device name by combining the three parts
        device_name = f"{device_code}-{location}-{number}"
        
        # Display the generated device name
        print(f"\nGenerated device name: {device_name}")
        
        # Ask if user wants to generate another name
        another = input("\nGenerate another device name? (yes/no): ").lower()
        if another != "yes" and another != "y":
            generate_another = False
    
    print("Thank you for using the Device Name Generator!")
```

## Exercise 2: IP Address Counter

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
            
            # Validate that start_octet is between 0 and 255
            if start_octet < 0 or start_octet > 255:
                print("Error: Last octet must be between 0 and 255!")
                continue
            
            # Get the number of addresses to generate
            count = int(input("How many addresses do you want to count? "))
            
            # Validate that count is positive
            if count <= 0:
                print("Error: Count must be a positive number!")
                continue
            
            # Generate and display the list of IP addresses
            print("\nIP Address Sequence:")
            
            current_octet = start_octet
            addresses_generated = 0
            
            while addresses_generated < count and current_octet <= 255:
                print(f"{base_ip}.{current_octet}")
                current_octet += 1
                addresses_generated += 1
            
            # Notify if we couldn't generate all requested addresses
            if addresses_generated < count:
                print(f"\nNote: Could only generate {addresses_generated} addresses before reaching 255.")
            
        except ValueError:
            print("Please enter valid numbers!")
            continue
            
        # Ask if user wants to count again
        another = input("\nCount another sequence? (yes/no): ").lower()
        if another != "yes" and another != "y":
            count_again = False
    
    print("Thank you for using the IP Address Counter!")
```

## Exercise 3: Network Device List Manager

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
            
            # Convert type_choice to a device type string
            if type_choice == "1":
                device_type = "Router"
            elif type_choice == "2":
                device_type = "Switch"
            elif type_choice == "3":
                device_type = "Firewall"
            elif type_choice == "4":
                device_type = "Server"
            else:
                device_type = "Other"
            
            # Add the device to the list
            devices.append([device_name, device_type])
            
            # Print confirmation
            print(f"Added: {device_name} ({device_type})")
            
        elif choice == "2":
            # Remove a device
            if len(devices) == 0:
                print("No devices to remove!")
                continue
                
            # Display devices with numbers
            print("\nCurrent devices:")
            for i in range(len(devices)):
                print(f"{i+1}. {devices[i][0]} ({devices[i][1]})")
                
            # Ask which device to remove
            try:
                remove_num = int(input("\nEnter the number of the device to remove: "))
                
                if 1 <= remove_num <= len(devices):
                    removed_device = devices.pop(remove_num-1)
                    print(f"Removed: {removed_device[0]} ({removed_device[1]})")
                else:
                    print("Invalid device number!")
            except ValueError:
                print("Please enter a valid number!")
            
        elif choice == "3":
            # View all devices
            if len(devices) == 0:
                print("No devices in the list!")
            else:
                print("\nAll devices:")
                for i in range(len(devices)):
                    print(f"{i+1}. {devices[i][0]} ({devices[i][1]})")
                
        elif choice == "4":
            # Count devices by type
            if len(devices) == 0:
                print("No devices in the list!")
            else:
                # Initialize counters for each type
                router_count = 0
                switch_count = 0
                firewall_count = 0
                server_count = 0
                other_count = 0
                
                # Count devices by type
                for device in devices:
                    if device[1] == "Router":
                        router_count += 1
                    elif device[1] == "Switch":
                        switch_count += 1
                    elif device[1] == "Firewall":
                        firewall_count += 1
                    elif device[1] == "Server":
                        server_count += 1
                    else:
                        other_count += 1
                
                # Display counts
                print("\nDevice Counts:")
                print(f"Routers: {router_count}")
                print(f"Switches: {switch_count}")
                print(f"Firewalls: {firewall_count}")
                print(f"Servers: {server_count}")
                print(f"Other devices: {other_count}")
                print(f"Total devices: {len(devices)}")
                
        elif choice == "5":
            # Exit
            print("Thank you for using the Network Device List Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
```

## Exercise 4: Simple Port Scanner Simulator

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
        
        # Count open ports
        open_ports = 0
        
        # Scan each port
        for port in common_ports:
            port_number = port[0]
            service_name = port[1]
            
            # Randomly decide if port is open (about 30% chance)
            is_open = random.random() < 0.3
            
            # Display result
            status = "OPEN" if is_open else "CLOSED"
            print(f"{port_number}\t{status}\t{service_name}")
            
            # Count open ports
            if is_open:
                open_ports += 1
        
        # Display summary
        open_percentage = (open_ports / len(common_ports)) * 100
        print(f"\nScan complete: {open_ports} out of {len(common_ports)} ports open ({open_percentage:.1f}%)")
        
        # Ask to scan again
        another = input("\nScan another device? (yes/no): ").lower()
        if another != "yes" and another != "y":
            scan_again = False
    
    print("Thank you for using the Simple Port Scanner Simulator!")
```