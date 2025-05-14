# 🧠 `argparse` Exercises – Solutions

### ✅ Solution 1: Basic Math Operations CLI
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple calculator.")
    parser.add_argument("number1", type=float, help="First number")
    parser.add_argument("number2", type=float, help="Second number")
    parser.add_argument("--operation", choices=["add", "subtract", "multiply", "divide"], required=True)

    args = parser.parse_args()

    if args.operation == "add":
        print(args.number1 + args.number2)
    elif args.operation == "subtract":
        print(args.number1 - args.number2)
    elif args.operation == "multiply":
        print(args.number1 * args.number2)
    elif args.operation == "divide":
        if args.number2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(args.number1 / args.number2)

if __name__ == "__main__":
    main()
```

---

### ✅ Solution 2: Word Counter CLI
```python
import argparse

def count_word(filename, word, ignore_case=False):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            if ignore_case:
                count = text.lower().count(word.lower())
            else:
                count = text.count(word)
        print(f"The word '{word}' appears {count} times.")
    except FileNotFoundError:
        print(f"File not found: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Count word occurrences in a file.")
    parser.add_argument("filename", help="File to scan")
    parser.add_argument("--word", required=True, help="Word to count")
    parser.add_argument("--ignore-case", action="store_true", help="Ignore case sensitivity")

    args = parser.parse_args()
    count_word(args.filename, args.word, args.ignore_case)

if __name__ == "__main__":
    main()
```

---

### ✅ Solution 3: Network Configuration Manager CLI
```python
import argparse
import os

def backup_config(devices, location):
    if not os.path.exists(location):
        os.makedirs(location)

    for device in devices:
        filename = os.path.join(location, f"{device}_backup.cfg")
        with open(filename, 'w') as f:
            f.write(f"! Simulated config for {device}\n")
        print(f"Backed up {device} to {filename}")

def restore_config(device, config_file):
    try:
        with open(config_file, 'r') as f:
            print(f"Restoring {device} from {config_file}")
    except FileNotFoundError:
        print(f"{config_file} not found")

def compare_configs(config1, config2, output):
    with open(config1) as f1, open(config2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    diffs = [line for line in lines2 if line not in lines1]
    with open(output, 'w') as out:
        out.writelines(diffs)
    print(f"Differences written to {output}")

def list_backups(location, device=None):
    for fname in os.listdir(location):
        if device is None or device in fname:
            print(fname)

def main():
    parser = argparse.ArgumentParser(description="Network Config Manager")
    subparsers = parser.add_subparsers(dest="command")

    parser_backup = subparsers.add_parser("backup")
    parser_backup.add_argument("--devices", required=True)
    parser_backup.add_argument("--location", default="./backups")

    parser_restore = subparsers.add_parser("restore")
    parser_restore.add_argument("--device", required=True)
    parser_restore.add_argument("--config", required=True)

    parser_compare = subparsers.add_parser("compare")
    parser_compare.add_argument("--config1", required=True)
    parser_compare.add_argument("--config2", required=True)
    parser_compare.add_argument("--output", required=True)

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("--location", default="./backups")
    parser_list.add_argument("--device")

    args = parser.parse_args()

    if args.command == "backup":
        devices = args.devices.split(",")
        backup_config(devices, args.location)
    elif args.command == "restore":
        restore_config(args.device, args.config)
    elif args.command == "compare":
        compare_configs(args.config1, args.config2, args.output)
    elif args.command == "list":
        list_backups(args.location, args.device)

if __name__ == "__main__":
    main()
```