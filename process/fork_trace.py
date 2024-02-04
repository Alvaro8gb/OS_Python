from os import wait, fork, getpid
from time import sleep

a_global = 10

def main():
    global a_global

    b_local = 10

    pid = fork()

    if pid < 0:
        print("Error fork")
    elif pid == 0:  # the created child process
        sleep(2)
        a_global += 10
        b_local += 10
    else:  # pid greater than 0 represents the parent process
        print("Parent Process ID:", getpid())
        print("Child's process ID:", pid)
        a_global += 1
        b_local += 1
        wait()

    print(f"pid; {getpid()}, pid_var:{pid} a:{a_global} b:{b_local}")

if __name__ == "__main__":
    main()
