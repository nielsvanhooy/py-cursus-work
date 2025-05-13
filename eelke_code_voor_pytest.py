# Exercise : IP Address Manager
# Create a script that manages a database of IP address assignments in a network.
# Requirements:
# Read an existing IP address database file (ip_addresses.csv)
# Allow users to:
#   View all IP addresses and their assignments
#   Add a new IP address assignment
#   Remove an existing assignment
#   Search for an IP address or hostname
#   Save the updated database back to the file
#
#
# use the following knowledge:
#
# Functions!
# the WITH statement.
# Working with Exceptions
# and everything you have learned up until now.
# use the python csv module to read and write CSV files.

import csv

def file_opener_dict():
    return_data = []
    with open("ip_addr.csv", newline='') as csvfile:
        content = csv.DictReader(csvfile)
        for things in content:
            return_data.append(things)
    return return_data

def entry_adder(db_data):
    new_ip_address = input("ip_address:")
    new_hostname = input("hostname:")
    new_department = input("department:")
    new_assigned_date = input("assigned_date:")
    new_notes = input("notes:")
    new_entry = {
        'ip_address': new_ip_address,
        'hostname': new_hostname,
        'department': new_department,
        'assigned_date': new_assigned_date,
        'notes': new_notes
    }
    print(f"adding: {new_entry}")
    db_data.append(new_entry)

def display_data(db_data):
    for data in db_data:
        print(data)

def entry_searcher(db_data, search_term):
    for data in db_data:
        if data['ip_address'] == search_term or data['hostname'] == search_term:
            print(data)
            break

    #nog iets met match ip|hst en dan case mogelijk ipv if lussie

def entry_remover(db_data, search_term):

    # Find entry index
    entry_index = None
    for i, entry in enumerate(db_data):
        if entry['ip_address'] == search_term or entry['hostname'] == search_term:
            entry_index = i
            break

    db_data.pop(entry_index)
    print(f"removing: {entry_index}")

def file_saver_old(db_data):
    with open("ip_addr.csv", "w", newline='') as csvfile:
        row_count = 0
        print("Writing to file")
        for data in db_data:
            print(".")
            if row_count == 0:
                w = csv.DictWriter(csvfile, data.keys())
                w.writeheader()
                w.writerow(data)
            else:
                w.writerow(data)
            row_count = row_count + 1
    print("Done")

def file_saver_new(db_data):
    with open("ip_addr.csv", "w", newline='') as csvfile:
        print("Writing to file")
        fieldnames = ['ip_address', 'hostname', 'department', 'assigned_date', 'notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in db_data:
            print(".")
            writer.writerow(data)
    print("Done")

def menu():
    options = """
    0. re-import form file
    1. show all
    2. search by IP or HOSTNAME (UNDER_CONSTRUCTION)
    3. add an entry
    4. remove an entry (UNDER_CONSTRUCTION)
    5. save to file oud
    6. save to file new
    7. quit
    """
    return options

def main():
    db_data = file_opener_dict()
    busy = True
    while busy:
        print(menu())
        choice = int(input('choose:'))
        match choice:
            case 0:
                db_data = file_opener_dict()
            case 1:
                display_data(db_data)
            case 2:
                search_term = input("enter ip_address or hostname to search for:")
                entry_searcher(db_data, search_term)
            case 3:
                entry_adder(db_data)
            case 4:
                search_term = input("enter ip_address or hostname to remove:")
                entry_remover(db_data, search_term)
            case 5:
                file_saver_old(db_data)
            case 6:
                file_saver_new(db_data)
            case _:
                print("\t\tBYE!")
                busy = False


if __name__ == '__main__':
    main()
