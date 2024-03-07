import os
import sys
import signal

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Successfully killed process {pid}")
    except OSError as e:
        print(f"Failed to kill process {pid}: {e}")
    except TypeError as e:
        print(f"Invalid PID type: {e}")

if __name__ == "__main__":

    pid_to_delete = input("Select pid to delete: ")
    try:
        pid_to_delete = int(pid_to_delete)
    except ValueError:
        print("pid does not match any process")
        sys.exit(1)

    kill_process(pid_to_delete)
    sys.exit(0)