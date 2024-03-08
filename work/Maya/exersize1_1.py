import os
import time

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
        os.execvp("ls", ["ls", "-l"])
        print("exec failed")
        os._exit(1)
    else:
        # fork failed
        print("fork failed")
except OSError as e:
    print(f"fork failed: {e}")
    os._exit(1)