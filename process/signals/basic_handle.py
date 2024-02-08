import signal
import time 
import inspect

def signal_handler(signum, frame): # It's mandatory to specify two arguments.
    print(f"Señal {signum} capturada.")

    # Inspect the call stack
    for info in reversed(inspect.getouterframes(frame)):
        print(info)
    
    print("Continue")
    
signal.signal(signal.SIGINT, signal_handler)

time.sleep(10)