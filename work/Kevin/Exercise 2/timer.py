import os
import signal
import time
import sys
from functools import partial

# This is what the child function does. I could do os.execl('/bin/bash', 'bash', '-c', command) but I hate exec so I wont.
def child_process(command):
    print("\nChild process is beginning the command")
    os.system(command)
    print("Child process is done")

# This tells the child that times up and that it should die
def alarm_handler(child_pid, a, b):
    print(f"\nTime's up. Telling child {child_pid}")
    os.kill(child_pid, signal.SIGTERM)
    time.sleep(1)
    print("If the child is still alive it's getting nuked")
    os.kill(child_pid, signal.SIGKILL)

# This is invoked when ctrl+C is pressed
def kill_child_ctrlC(a, b):
    print("\nctrl+C pressed. Killing child")
    os.kill(child_pid, signal.SIGKILL)



#if the command is too short, tell the user
if len(sys.argv) < 2:
    print("Usage: seconds command [args...]")
    sys.exit(1)

# if the user put a bad length in, tell them
try:
    timeout = int(sys.argv[1])
except:
    print("Timeout must be in seconds")
    sys.exit(1)

# truncate the command to be used by the child
leftover_command = sys.argv[2:]
command = ""
for word in leftover_command:
    command += str(word)
    command += " "



# set the ctrl+C signal handler
signal.signal(signal.SIGINT, kill_child_ctrlC)

# set the timer handler and length
signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(timeout)



pid = os.fork()

if pid == 0:
    child_process(command)
if pid > 0:
    child_pid = pid

    # This creates a partially made function with the first input as the child pid
    handler_with_pid = partial(alarm_handler, child_pid) 

    signal.signal(signal.SIGALRM, handler_with_pid)
    signal.alarm(timeout)

    garbage, status = os.waitpid(child_pid, 0)
    print(f"\nChild process ended with status {status}")
else:
    print("Fork Failed")