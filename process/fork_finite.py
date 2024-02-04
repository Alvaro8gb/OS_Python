from os import wait, fork, getpid
import sys

def create_process_tree(depth):

    for i in range(depth):
        pid = fork()

        if pid < 0:
            print("Error fork")
        elif pid == 0:  # the created child process
            pass
        else:  # pid greater than 0 represents the parent process
            print("Parent Process ID:", getpid(), "---->", "Child's process ID:", pid)
            wait()

if __name__ == "__main__":
    deep = int(sys.argv[1])
    create_process_tree(deep)