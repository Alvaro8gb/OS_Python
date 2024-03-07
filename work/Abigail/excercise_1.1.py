import os

pid = os.fork()

if pid < 0:
    print("Error in fork")
elif pid == 0: #child process
    exit()
else: # parent process taking place 
    print("Parent process taking place")
    command = ["python3", "-c", "import time; time.sleep(2); print('Hello')"]
    os.execvp("python3", command)