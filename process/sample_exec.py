import os

# The first argument is the path to the "echo" executable (usually '/bin/echo' on Unix-like systems)
# The second argument is a list of arguments, where the first element is the name of the program ('echo')
os.execv("/bin/echo", ["echo", "Hello"])

