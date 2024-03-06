import os
import sys
import signal
import time

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Successfully killed process {pid}")
    except OSError as e:
        print(f"Failed to kill process {pid}: {e}")
    except TypeError as e:
        print(f"Invalid PID type: {e}")

if __name__ == "__main__":
    pid = os.fork()
    if pid < 0:
        print("Error forking")
        sys.exit(1)

    elif pid == 0:  # Child process
        print(f"Parent pid: {os.getppid()}")
        print(f"Child pid: {os.getpid()}")
        while True: 
            time.sleep(1)

    else:  # Parent process
        time.sleep(1)
        pid_to_delete = input("Select pid to delete: ")
        try:
            pid_to_delete = int(pid_to_delete)
        except ValueError:
            print("pid must be a number")
            sys.exit(1)

        if pid_to_delete == os.getpid():
            print("killing parent process...")
            kill_process(pid_to_delete)

        elif pid_to_delete == pid:
            print("killing child process...")
            kill_process(pid_to_delete)
            os.wait()

        else:
            print("pid does not match any process")
            sys.exit(1)
