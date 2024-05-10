
import os
import sys


def main(command):
    create_daemon(command)


def create_daemon(command=None, loop=True):

    # Fork an initial child process
    pid = os.fork()

    # Initial Parent Process
    if pid > 0:
        # Exit normally from the initial parent process
        print(f"Initial parent process (PID {os.getpid()}) with child process (PID {pid}).")
        sys.exit(0)

    # Initial Child Process (Daemon Process)
    elif pid == 0:

        # Create a new session and process group (+ reset the umask) to detach the daemon from the parent environment
        os.setsid()
        os.umask(0)

        # Fork a secondary child process to ensure it is not the session leader and can successfully execute the logic
        pid = os.fork()

        # Secondary Parent Process
        if pid > 0:
            # Exit normally from the secondary parent process
            print(f"Secondary parent process (PID {os.getpid()}) with child process (PID {pid}).")
            sys.exit(0)

        # Secondary Child Process
        elif pid == 0:

            # Change the working directory of the daemon to /tmp
            print(f"Child process (PID {os.getpid()}).")
            os.chdir('/tmp')

            # Create and run a bash command if provided
            if command is not None:
                print(f"Executing command: {command}")
                os.execvp(command[0], command)
            else:
                print("No command provided in argument.")
                # Enter an optional infinite loop to keep the daemon running
                if loop:
                    print(f"Daemon entering infinite loop!")
                while loop:
                    pass

        else:
            print("Second fork failed!")

    # Error
    else:
        print("First fork failed!")


if __name__ == '__main__':
    cmd = None
    if len(sys.argv) > 1:
        cmd = sys.argv[1:]
    main(cmd)
