from os import fork, getpid, getppid, wait
from time import sleep

def main():
    for i in range(10):
        pid = fork()
        if pid == 0:
            print(f"I am {getpid()}. My parent is {getppid()}, I am going to sleep for a while...")
            sleep(i + 1)
            print(f"I am {getpid()}. ...I woke up. My parent is {getppid()}.")

            exit(0)
    
    ## Proper use
    #for _ in range(10):
     #   wait()

if __name__ == "__main__":
    main()
