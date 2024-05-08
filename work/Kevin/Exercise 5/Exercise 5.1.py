import os
import sys
import time

if len(sys.argv) != 5:
    print("Usage: python \"Exercise 5.1.py\" command1 arg1 command2 arg2")
    sys.exit(1)

command1 = sys.argv[1]
arg1 = sys.argv[2]
command2 = sys.argv[3]
arg2 = sys.argv[4] 

r, w = os.pipe()
pid = os.fork()

if pid > 0:
    os.dup2(w, 1) # 1 is stdout
    os.close(w)

    os.execlp(command1, command1, arg1)
elif pid == 0: # child
    os.close(w)  # Close the write end in the child so stdout goes to the terminal
    os.dup2(r, 0) # 0 is stdin
    os.close(r)

    time.sleep(1) # make sure the child waits for the parent to send it info
    
    os.execlp(command2, command2, arg2)
else:
    print("Fork failed")
    sys.exit(1)