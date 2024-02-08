import signal
import time

def signal_handler(signum, frame):
    print("Printing this message every 2 seconds.")
    # Reschedule the alarm
    signal.alarm(2)

# Set the signal handler for SIGALRM
signal.signal(signal.SIGALRM, signal_handler)

# Schedule the first SIGALRM after 10 seconds
signal.alarm(5)

while True:
    time.sleep(1)

