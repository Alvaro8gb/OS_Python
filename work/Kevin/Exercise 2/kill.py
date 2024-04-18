import os
import time

pid = input("Who are we killing today? (Enter PID)")

try:
    pid = int(pid)
except:
    print("It must be a number")
    exit(1)

os.system(f"kill -9 {pid}")
print(f"process {pid} killed unless it didn't exist")
print(f"I am {os.getpid()} and I killed someone")