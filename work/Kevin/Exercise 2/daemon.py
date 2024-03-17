import os
import time

pid = os.fork()

if pid == 0:
    # get the filepath of this program and edit it to be daemon2.py
    cwd = os.path.abspath(__file__)
    cwd = cwd[:-3]
    path_to_daemon2 = cwd + "2.py"

    # I hate os.execl()
    os.execl("/usr/bin/python3", "python3", path_to_daemon2, '0')
if pid > 0:
    os.wait() #probably not needed if it was a real daemon
    print(f"A daemon has been created by me, the father {os.getpid()} in session {os.getsid(os.getpid())}")
else:
    print("Fork Failed")