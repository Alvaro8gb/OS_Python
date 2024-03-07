import os

pid = os.fork()

if pid == 0:
    print(f"child with pid {os.getpid()}")
else:
    print(pid)