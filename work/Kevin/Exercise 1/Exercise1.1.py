import os

#Exercise 1.1
pid = os.fork()
if pid == 0:
    print("background process executing")
    pid = os.getpid()
    print(f"I am a child and my pid is {pid}")
    os.system("(sleep 2; echo 'Hello') &")
if pid > 0:
    os.wait()
    print("Main process continues")
else:
    print("Fork failed")