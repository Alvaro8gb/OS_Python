
import os
import sys
import signal


def main():

    # Get the PID to kill as input from the user
    pid_input = input("Enter the Process ID (PID): ")
    terminate_process(pid_input)


def terminate_process(pid_input):

    # Convert the input to integer
    pid = int(pid_input)
    # Kill the process with the given PID
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Process with PID {pid} killed successfully.")
    except Exception as e:
        # By this way we can know about the type of error occurring
        print(f"Error to kill process {pid}: {e}")

    return


if __name__ == '__main__':
    sys.exit(main())


