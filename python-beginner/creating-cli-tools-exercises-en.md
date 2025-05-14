### Exercise 1: Basic Math Operations CLI

Create a Python script that accepts two numbers and an operation (`add`, `subtract`, `multiply`, `divide`) as command-line arguments and prints the result.

**Requirements:**
- Use `argparse` to parse arguments.
- Positional arguments: `number1`, `number2`
- Required flag: `--operation` with choices: `add`, `subtract`, `multiply`, `divide`.

**Example Usage:**
```bash
python calculator.py 5 3 --operation add
# Output: 8
```

---

### Exercise 2: Word Counter CLI

Write a command-line tool that counts how many times a specific word appears in a text file.

**Requirements:**
- Use `argparse` to parse arguments.
- Required positional argument: `filename`
- Required flag: `--word` to specify the word to count.
- Optional flag: `--ignore-case` to make the match case-insensitive.

**Behavior:**
- Read the contents of the file and count how many times the word appears.
- Print the result.

**Example Usage:**
```bash
python word_counter.py sample.txt --word hello
python word_counter.py sample.txt --word hello --ignore-case
```

---

### Exercise 3: Network Configuration Manager CLI (Advanced)

Create a command-line tool that helps manage network device configurations, with features for backup, restore, and comparison.

**Requirements:**
- Support multiple subcommands:
  - `backup`: Backup configs from device(s)
  - `restore`: Restore a config to a device
  - `compare`: Compare two configuration files
  - `list`: List available backups
- Each subcommand has relevant arguments
- Support specifying multiple devices
- Option to specify backup location
- Ability to encrypt sensitive data (`--encrypt`) (ceasar cipher for example google it) -- OPTIONAL

**Example Usage:**
```bash
python config_manager.py backup --devices router1,router2 --location ./backups
python config_manager.py restore --device router1 --config backups/router1_20230515.cfg
python config_manager.py compare --config1 router1_old.cfg --config2 router1_new.cfg --output diff.txt
python config_manager.py list --location ./backups --device router1
```