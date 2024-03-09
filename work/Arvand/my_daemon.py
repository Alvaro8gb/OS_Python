import os
import sys

pid = os.fork()

if pid > 0:
    sys.exit(f"Parent {os.getpid()} (Child: {pid})")

elif pid == 0:
    print(f"Child {os.getpid()} (Parent: {os.getppid()})")

    # File path to the Daemon function
    with open("daemon_function.py", "r") as file:
        python_code = file.read()

    # Detach from parent process
    os.setsid()
    os.chdir('/tmp') 

    # Verify that the program is in /tmp
    print(os.listdir())

    # Execute the functionality of the Daemon process here
    exec(python_code)

else:
    print("Fork failed.")