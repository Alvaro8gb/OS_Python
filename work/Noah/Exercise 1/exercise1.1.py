
import os
import time


def main():

    # Fork a child process
    pid = os.fork()

    # Parent Process
    if pid > 0:
        print(f"Parent process (PID {os.getpid()}) with child process (PID {pid})")
        os.waitpid(pid, 0)
    # Child Process
    elif pid == 0:
        print(f"Child process (PID {os.getpid()})")
        # Simulate the bash command "(sleep 2; echo "Hello")" in Python
        time.sleep(2)
        print("Hello")
    # Error
    else:
        print("Fork failed!")


if __name__ == '__main__':
    main()
