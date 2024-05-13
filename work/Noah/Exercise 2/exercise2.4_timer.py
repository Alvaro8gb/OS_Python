
import os
import sys
import time
import signal
import errno


def main():

    if len(sys.argv) < 3:
        print("Usage: python", sys.argv[0], "<seconds> <command> [args...]")
        return 1

    seconds = int(sys.argv[1])
    command = sys.argv[2:]

    # Fork a child process
    pid = os.fork()

    # Parent Process
    if pid > 0:

        # Set up the timer and CTRL+C signal handlers
        signal.signal(signal.SIGALRM, lambda signum, frame: handle_timer_limit(pid))
        signal.signal(signal.SIGINT, lambda signum, frame: handle_ctrl_c(pid))
        # Set up the alarm with the time limit
        signal.alarm(seconds)

        # Wait for the child process to finish and handle its termination
        try:
            pid, status = os.wait()
            if os.WIFSIGNALED(status):
                print(f"Child process {pid} was terminated by signal {os.WTERMSIG(status)}!")
            elif os.WIFEXITED(status):
                print(f"Child process {pid} exited with status {os.WEXITSTATUS(status)}!")
        # Clean up the child process if it is still running
        finally:
            try:
                os.kill(pid, 0)
            except OSError:
                return
            os.kill(pid, signal.SIGKILL)
            print(f"SIGKILL successfully terminated child process {pid} during clean up.")

    # Child Process
    elif pid == 0:
        # Execute the command in the child process
        print(f"Child process (PID {os.getpid()}).")
        os.execvp(command[0], command)

    # Error
    else:
        print("Fork failed!")


def handle_timer_limit(child_pid):

    # Warn the child process that the time limit has been reached by sending it a SIGTERM signal
    print(f"WARNING: Time limit for child process {child_pid} reached. Sending SIGTERM signal.")
    os.kill(child_pid, signal.SIGTERM)

    # Wait 1 second and check if the child process is still alive
    time.sleep(1)
    try:
        os.kill(child_pid, 0)
    except OSError as e:
        if e.errno == errno.ESRCH:
            print(f"SIGTERM successfully terminated child process {child_pid}.")
            return

    # If the child process is still alive, send a SIGKILL signal
    print(f"WARNING: Child process {child_pid} still alive. Sending SIGKILL signal.")
    os.kill(child_pid, signal.SIGKILL)
    print(f"SIGKILL successfully terminated child process {child_pid}.")

    return


def handle_ctrl_c(child_pid):
    print(f"User input CTRL+C detected. Sending SIGKILL signal to child process {child_pid}.")
    os.kill(child_pid, signal.SIGKILL)
    print(f"SIGKILL successfully terminated child process {child_pid}.")

    return


if __name__ == '__main__':
    main()
