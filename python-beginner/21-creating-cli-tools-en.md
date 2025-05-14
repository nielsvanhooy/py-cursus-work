# Creating python programs for the CLI.

There are 3 packages that are populair to create CLI tooling

1: Argparse (built-in)
2: Click - https://click.palletsprojects.com/en/stable/
3: Typer - https://typer.tiangolo.com/

in our projects we will be using Click. but if you create native tooling for python we use Argparse.

# Introduction to the argparse Module and Its Benefits
The argparse module is part of Python's standard library. 
Therefore, it can be used without installing any additional
packages. It offers a straightforward and consistent interface for parsing command line inputs. 
Some of the advantages
of utilizing argparse are:

 - Automatic help generation: It generates help and usage messages based on the code's arguments.
 - Error handling: It displays helpful error messages when users enter invalid arguments.
 - Type conversion: It can automatically convert parameter strings to the appropriate data type.
 - It supports both necessary positional arguments and optional arguments with simplicity.
 - Default values: It allows you to provide default values for parameters that the user does not supply.

# Setting Up argparse and Basic Usage

```python
import argparse
```

This line loads the argparse module into your script, allowing you to use its functionality to parse command-line
arguments.


The first step in utilizing argparse is to generate a parser object. This object will store information about the
arguments your program accepts and parse command-line input.


```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
```

Powered By
In this example, we create an ArgumentParser() object and describe the program. When the user selects the help option (
-h or --help), this description will be displayed.

Now that we've developed the parser, we can specify the arguments our program will accept.

Positional arguments are essential and must be presented in a precise order. For example, a script that adds
two numbers. We can define two positional arguments for the numbers:

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('num1', type=int, help='The first number to add.')
parser.add_argument('num2', type=int, help='The second number to add.')
```
In this code, num1 and num2 refer to the positional parameters.

type=int indicates that the parameters should be converted to integers. The help argument specifies a description that
will appear in the help message.

Adding optional arguments
Optional arguments are not necessary and typically provide additional options or change the behavior of the program.
They are usually prefixed with one or two dashes. We'll add an optional argument to enable verbose output:

```python
parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity.')
```

The short option is -v (for example, -v). --verbose is a lengthy option.
action='store_true' indicates that if the option is selected, the verbose attribute will be set to True; 
otherwise, it will be `False`.
The help argument specifies a description for the help message.
Parsing arguments and accessing their values
After specifying all of the arguments, we need to parse the command-line input. Use the .parse_args() method to achieve
this.

```python
args = parser.parse_args()
```

The parsed parameters are now stored in the args variable as attributes. 
We can access them using dot notation.

```python
result = args.num1 + args.num2
print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))
if args.verbose:
print('Verbose mode is enabled.')
```
Putting everything together, here's a complete script that adds two numbers and includes an optional verbose mode:

```python
import argparse

parser = argparse.ArgumentParser(description='Add two integers.')

parser.add_argument('num1', type=int, help='The first number to add.')
parser.add_argument('num2', type=int, help='The second number to add.')
parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity.')

args = parser.parse_args()
result = args.num1 + args.num2

print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))
if args.verbose:
    print('Calculation completed successfully.')
```

You can run this script from the command line and provide the required positional arguments:

```bash
python add_numbers.py 3 5
The sum of 3 and 5 is 8
```
If you include the -v or --verbose option, the script will print the additional verbose message:

```bash
python add_numbers.py 3 5 --verbose
The sum of 3 and 5 is 8
Calculation completed successfully.
```

If the user runs the script with the -h or --help option, argparse will display an automatically generated help message:

```bash
python add_numbers.py -h

usage: add_numbers.py [-h] [-v] num1 num2

Add two integers.
positional arguments:
num1 The first number to add.
num2 The second number to add.
optional arguments:
-h, --help show this help message and exit
-v, --verbose Increase output verbosity.
```
This feature makes your program more user-friendly by providing clear instructions on how to use it.

# Advanced Argument Handling
When developing command-line programs in Python, you may encounter scenarios requiring more complex argument parsing.
Python's argparse module includes several features to address these complex requirements, allowing you to develop
flexible and user-friendly interfaces.

# Using nargs for multiple arguments
There are situations when your application needs to accept numerous values for the same argument. For example, assume
you wish to create a script that processes multiple files at once. The nargs parameter in argparse allows you to specify
how many command-line arguments should be read.

Here's how to use nargs to accept multiple filenames:

```python
import argparse

parser = argparse.ArgumentParser(description='Process multiple files.')

parser.add_argument('filenames', nargs='+', help='List of files to process.')

args = parser.parse_args()
for filename in args.filenames:
    print(f'Processing file: {filename}')
    # Add your file processing code here
```
In this case, nargs='+' instructs the parser to expect one or more arguments in filenames. The user can provide as many
file names as necessary, and they will be saved in a list called args.filenames.

If you want to accept a certain amount of arguments, set nargs to that number. For example, nargs=2 requires exactly two
parameters.

# Implementing choices to limit argument values
Sometimes, you want to limit an argument to a specified range of valid values. This guarantees that the user offers
valid input, hence avoiding mistakes or unexpected actions. The options parameter lets you specify the allowable values
for an argument.

Consider a script that executes multiple activities depending on a mode selected by the user.

```python
import argparse

parser = argparse.ArgumentParser(description='Perform actions in different modes.')

parser.add_argument('--mode', choices=['backup', 'restore', 'delete'], required=True, help='Mode of operation.')

args = parser.parse_args()

if args.mode == 'backup':
    print('Backing up data...')
# Backup code here
elif args.mode == 'restore':
    print('Restoring data...')
# Restore code here
elif args.mode == 'delete':
    print('Deleting data...')
# Delete code here
```
In this script, the --mode argument must be one of the options. If the user enters a value that is not in the list,
argparse will return an error message.

# Handling boolean flags and toggles
Boolean flags are choices that enable or disable specific functionalities in your application. They are typically
defined without a value, merely by including the flag in the command. You can handle these flags in argparse with the
action parameter.


```python
import argparse

parser = argparse.ArgumentParser(description='A script with debug mode.')

parser.add_argument('--debug', action='store_true', help='Enable debug output.')

args = parser.parse_args()

if args.debug:
    print('Debug mode is enabled.')
    # Additional debug information here
else:
    print('Debug mode is disabled.')
```
By using action='store_true', the --debug flag will set args.debug to True when present and False otherwise.

# Setting default values and required arguments
Optional arguments frequently include sensible default values. This signifies that if the user does not specify the
argument, the application will use the default. The default argument allows you to specify a default value.

Here's an example:

```python
import argparse

parser = argparse.ArgumentParser(description='Adjust program settings.')

parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds.')

args = parser.parse_args()

print(f'Timeout is set to {args.timeout} seconds.')
```
In this scenario, if the user does not specify --timeout, the default is 30 seconds.

To make an optional argument mandatory, set required=True.

```python
import argparse

parser = argparse.ArgumentParser(description='Send a message.')

parser.add_argument('--recipient', required=True, help='Recipient of the message.')

args = parser.parse_args()

print(f'Sending message to {args.recipient}.')
```
The script will now require the --recipient argument.

# Customizing Help and Error Messages
Providing clear and helpful messages to users is an essential component of developing an effective command-line program.
Python's argparse module automatically creates help messages, but you can modify these messages to better suit your
needs.

Generating automatic help messages
By default, argparse generates a help message, which may be accessed using the -h or --help options. This message
contains the program's usage, a description, and information about each argument.

For example:

```python
import argparse
parser = argparse.ArgumentParser(description='Calculate factorial of a number.')
parser.add_argument('number', type=int, help='The number to calculate the factorial for.')
args = parser.parse_args()
```

When a user runs the script with -h, they will see:

```bash
usage: script.py [-h] number
Calculate factorial of a number.
positional arguments:
number The number to calculate the factorial for.
optional arguments:
-h, --help show this help message and exit
```
This automatic help message gives useful information without requiring any additional effort.

Customizing help descriptions and usage messages
While the default help messages are useful, you may want to alter them to provide extra information or to fit a specific
structure. You can change the description, epilog, and usage text in the ArgumentParser.

For example, to include an epilog and personalize the usage message:

```python
import argparse

parser = argparse.ArgumentParser(
    description='Convert temperatures between Celsius and Fahrenheit.',
    epilog='Enjoy using the temperature converter!',
    usage='%(prog)s [options] temperature'
)

parser.add_argument('temperature', type=float, help='Temperature value to convert.')
parser.add_argument('--to-fahrenheit', action='store_true', help='Convert Celsius to Fahrenheit.')
parser.add_argument('--to-celsius', action='store_true', help='Convert Fahrenheit to Celsius.')

args = parser.parse_args()
```
Now, when the user checks the help message, it will include the customized description, usage, and epilog:

```bash
python file.py --help

usage: p.py [options] temperature

Convert temperatures between Celsius and Fahrenheit.

positional arguments:
temperature Temperature value to convert.

options:
-h, --help show this help message and exit
--to-fahrenheit Convert Celsius to Fahrenheit.
--to-celsius Convert Fahrenheit to Celsius.
```

# Managing error handling and user feedback
If a user enters invalid arguments, argparse will display an error message and exit the program. You can modify this
behavior to provide more useful feedback or to handle failures differently.

One approach is to override the error method in a subclass of ArgumentParser:

```python
import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f'Error: {message}')
        self.print_help()
        sys.exit(2)
        
parser = CustomArgumentParser(description='Divide two numbers.')

parser.add_argument('numerator', type=float, help='The numerator.')
parser.add_argument('denominator', type=float, help='The denominator.')

args = parser.parse_args()

if args.denominator == 0:
    parser.error('Denominator cannot be zero.')
    
result = args.numerator / args.denominator
print(f'Result: {result}')
```
If the user attempts to divide by zero in this script, the application will display an error warning and help text,
directing the user to provide valid data.

```bash
Python file.py 6 0
Error: Denominator cannot be zero.
usage: file.py [-h] numerator denominator
Divide two numbers.
positional arguments:
numerator The numerator.
denominator The denominator.
options:
-h, --help show this help message and exit
```
You can also include custom error handling in your script. For instance, to manage invalid file paths:

```python
import argparse
import os

parser = argparse.ArgumentParser(description='Read a file and display its contents.')

parser.add_argument('filepath', help='Path to the file.')

args = parser.parse_args()

if not os.path.exists(args.filepath):
    parser.error(f"The file {args.filepath} does not exist.")
    
with open(args.filepath, 'r') as file:
    contents = file.read()
    print(contents)
```
Running the script with an invalid path will display the error below:

```bash
python app..py file
usage: p.py [-h] filepath
app.py: error: The file file does not exist.
```

# Real-World Examples and Use Cases
Understanding how to use the argparse module in real-world settings will make its functionality clearer. Let's look at
some instances of how to use argparse in real-world applications.

Building a command-line calculator
Assume you need to develop a simple calculator that can do basic arithmetic operations from the command line. This
calculator should accept two numbers and an operator to execute the requested computation.

Here's how to approach this task:

```python
import argparse

parser = argparse.ArgumentParser(description='Simple command-line calculator.')

parser.add_argument('num1', type=float, help='First number.')
parser.add_argument('operator', choices=['+', '-', '*', '/'], help='Operation to perform.')
parser.add_argument('num2', type=float, help='Second number.')

args = parser.parse_args()

if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':  
    if args.num2 == 0:
        print('Error: Division by zero is not allowed.')
        exit(1)
    result = args.num1 / args.num2
print(f'The result is: {result}')
```
In this script, the argparse module is used to define three positional arguments: two numbers and an operator. The
choices argument limits the operator to valid arithmetic symbols. When the user runs the script, they can perform these
calculations:

```bash
python calculator.py 10 + 5
The result is: 15.0
```
This basic calculator shows how command-line options can enhance a program's flexibility and interactivity.

Creating a file-processing script with multiple options
Assume you require a script that processes text files and provides choices such as designating an output file, selecting
a processing mode, and enabling verbose output.

Here's an example of how you could set it up:

```python
import argparse

parser = argparse.ArgumentParser(description='Process text files.')

parser.add_argument('input_file', help='Path to the input file.')
parser.add_argument('-o', '--output', help='Path to the output file.')
parser.add_argument('-m', '--mode', choices=['uppercase', 'lowercase'], default='uppercase', help='Processing mode.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')

args = parser.parse_args()

# Read the input file
with open(args.input_file, 'r') as file:
    content = file.read()
if args.verbose:
    print(f'Reading from {args.input_file}')
    
# Process the content
if args.mode == 'uppercase':
    processed_content = content.upper()
else:
    processed_content = content.lower()
if args.verbose:
    print('Processing content')
    
# Write to the output file or print to console
if args.output:
    with open(args.output, 'w') as file:
        file.write(processed_content)
    if args.verbose:
        print(f'Writing output to {args.output}')
else:
    print(processed_content)
```
This script accepts an input file and has options for the output file, processing mode, and verbose output. Users can
modify how the script behaves without altering the code.

```bash
python text_processor.py input.txt -o output.txt --mode lowercase -v
Reading from input.txt
Processing content
Writing output to output.txt
```

Developing a CLI tool with subcommands
In more complicated applications, subcommands may be required, similar to how git works using commands such as git
commit and git push. The argparse module provides subparsers for this purpose.

Here's how to make a CLI tool with subcommands:

```python
import argparse

parser = argparse.ArgumentParser(description='Manage tasks.')

subparsers = parser.add_subparsers(dest='command', required=True)

# Subcommand 'add'
parser_add = subparsers.add_parser('add', help='Add a new task.')
parser_add.add_argument('name', help='Name of the task.')
parser_add.add_argument('-p', '--priority', type=int, choices=range(1, 6), default=3, help='Priority of the task.')

# Subcommand 'list'
parser_list = subparsers.add_parser('list', help='List all tasks.')
parser_list.add_argument('-a', '--all', action='store_true', help='List all tasks, including completed ones.')

# Subcommand 'complete'
parser_complete = subparsers.add_parser('complete', help='Mark a task as completed.')
parser_complete.add_argument('task_id', type=int, help='ID of the task to complete.')
args = parser.parse_args()

if args.command == 'add':
    print(f"Adding task '{args.name}' with priority {args.priority}")
    # Code to add the task
elif args.command == 'list':
    print('Listing tasks')
    if args.all:
        print('Including completed tasks')
    # Code to list tasks
elif args.command == 'complete':
    print(f'Marking task {args.task_id} as completed')
    # Code to complete the task
```
In this example, the script has three subcommands: add, list, and complete. Each subcommand has its arguments. When
users run the script, they enter the subcommand and any other parameters.

For example:

```bash
python task_manager.py add "Write report" -p 2
Adding task 'Write report' with priority 2
```
Listing tasks

```bash
python task_manager.py list
Listing tasks
```
Marking tasks as completed:

```bash
python task_manager.py complete 3
Marking task 3 as completed
```
subparsers enable you to create complex command line tools that are well organized and easy to extend, allowing you to
build applications that can do multiple things in a single interface. 