import os
import time
from os import wait


pid = os.fork()

if pid > 0:
    print(f"parent")
    os.wait()
elif pid == 0:
    print(f"child")
    time.sleep(2)
    print(f"Hello")