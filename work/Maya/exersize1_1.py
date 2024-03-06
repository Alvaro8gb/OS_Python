import os
import time
from os import wait

try:
    pid = os.fork()

    if pid > 0:
        # parent process
        print(f"parent")
        os.wait()
    elif pid == 0:
        # child process
        print(f"child")
        time.sleep(2)
        print(f"Hello")
        os._exit(0)
    else:
        # fork failed
        print("fork failed")
except OSError as e:
    print(f"fork failed: {e}")
    os._exit(1)