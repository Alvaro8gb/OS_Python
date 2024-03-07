import os
import sys
import time
import signal

def signal_handler():
    # parent warns the child
    os.kill(pid, signal.SIGTERM) 
    # gives a one-second leighway
    time.sleep(1)
    # forcibly terminates the child process
    os.kill(pid, signal.SIGKILL)

if len(sys.argv) < 3:
    print("Insufficient number of arguments")

command = " ".join([str(word) for word in sys.argv[2:]])

signal.signal(signal.SIGINT, signal_handler)
signal.alarm(int(sys.argv[1]))

# fork a child process
pid = os.fork()

# parent process
if pid > 0:
    while True:
        try:
            __, status = os.waitpid(pid, 0)
            if os.WIFEXITED(status): # graceful
                print(f"EXITED {os.WEXITSTATUS(status)}")
            elif os.WIFSIGNALED(status): # forcibly
                print(f"TERMINATED {os.WTERMSIG(status)}") 
        except ChildProcessError:
            break
    signal.alarm(0)

# child process
elif pid == 0:
    os.system(command)

# error
else:
    print("Fork failed.")