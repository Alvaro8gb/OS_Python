import os
import signal
import time
from functools import partial

def child_process(time_child):
    print("Child Process Begins")
    time.sleep(time_child)
    print("Child Process End")

def alarm_handler(child_pid, signum, frame):
    print(f"Alarm signal (SIGALRM) received. Finishing the process son (PID {child_pid}).")
    os.kill(child_pid, signal.SIGTERM)

timeout = 10 
time_child = 5

#timeout, time_child = time_child, timeout uncoment to see how the parent kill the child

pid = os.fork()

if pid == 0:
    # This is the child process
    child_process(time_child)
else:
    # This is the parent process
    child_pid = pid  # Capture the child process ID
    print(f"Parent: Child Process with PID {child_pid} Started")
    
    # Use functools.partial to pass child_pid to alarm_handler
    handler_with_pid = partial(alarm_handler, child_pid)
    
    signal.signal(signal.SIGALRM, handler_with_pid)
    signal.alarm(timeout)

    _, status = os.waitpid(child_pid, 0)
    print(f"Child process ended with status {status}")
