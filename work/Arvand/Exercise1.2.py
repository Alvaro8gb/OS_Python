import sys
import os

pid = os.fork()

if pid == 0:
    inp = ' '.join(sys.argv[1:])
    os.system(inp)
elif pid <= 0:
    # An error occurred​
    print("Fork failed.")