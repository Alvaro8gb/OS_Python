import sys
import os

print(sys.stdout)

print(sys.stderr)

sys.stdout = open('/dev/tty', 'w')
sys.stderr = open('/dev/tty', 'w')


import os

# Defining constants for readability
STDIN = 0
STDOUT = 1
STDERR = 2


message = "Hello, this is a message to standard output.\n"
os.write(STDOUT, message.encode())

error_message = "This is an error message to standard error.\n"
os.write(STDERR, error_message.encode())
