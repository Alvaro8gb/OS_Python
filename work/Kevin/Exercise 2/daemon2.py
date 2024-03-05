import os
import time

def daemon():
    for i in range(5): # This would go on forever if it were a real daemon
        time.sleep(1)

os.setsid()
os.chdir("/tmp")
print(f"I am the daemon {os.getpid()} in the session {os.getsid(os.getpid())}")
daemon()