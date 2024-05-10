
import os
import sys
import time
import random
import subprocess


def main():

    # Fork a child process
    pid = os.fork()

    # Parent Process
    if pid > 0:

        # Sleep for a random time between 15 and 30 seconds
        print(f"Parent process (PID {os.getpid()}) with child process (PID {pid}).")
        seconds = random.randrange(15, 30, 1)
        print(f"Parent process sleeping for {seconds} seconds.")
        time.sleep(seconds)

        # Exit the parent process
        print("Parent process exiting.")
        sys.exit(0)

    # Child Process
    elif pid == 0:

        # Output the initial zombie processes
        initial_zombies = ps_grep()
        zombie_pid = os.getpid()
        print(f"Child process (PID {zombie_pid}).")
        print("\n[INITIAL ZOMBIE PROCESSES:]")
        print(initial_zombies)

        # Fork a grandchild process to get the final zombie processes
        pid = os.fork()

        # Grandchild Process
        if pid == 0:

            # Sleep for 5 seconds and then output the final zombie processes
            time.sleep(5)
            print(f"Grandchild process (PID {os.getpid()}).")
            final_zombies = ps_grep()
            print("\n[FINAL ZOMBIE PROCESSES:]")
            print(final_zombies)

            # Check if the child process is a zombie
            child_is_zombie = False
            print("[NEW ZOMBIE PROCESSES:]")
            new_zombies = set(final_zombies.splitlines()) - set(initial_zombies.splitlines())
            for zombie in new_zombies:
                print(zombie)
                if str(zombie_pid) in zombie:
                    child_is_zombie = True

            if child_is_zombie:
                print(f"\nRESULT: Child process (PID {zombie_pid}) is a zombie!\n")
            else:
                print(f"\nRESULT: Child process (PID {zombie_pid}) is not a zombie!\n")

            # Exit the grandchild process
            print("Grandchild process exiting.")
            sys.exit(0)

        # Child Process
        if pid > 0:
            # Exit the child process
            print("Child process exiting.")
            sys.exit(0)

        # Error
        else:
            print("Second fork failed!")

    # Error
    else:
        print("First fork failed!")


# Use the subprocess module to get zombie processes
def ps_grep():
    ps_aux = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    grep_z = subprocess.Popen(['grep', 'Z'], stdin=ps_aux.stdout, stdout=subprocess.PIPE)
    ps_aux.stdout.close()
    output = grep_z.communicate()[0]
    return output.decode('utf-8')


if __name__ == '__main__':
    main()
