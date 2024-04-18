import os
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3", sys.argv[0] ,"<number>")
        return 1

    number = int(sys.argv[1])

    if number <= 0:
        return 0

    pid = os.fork()

    if pid == 0:
        # Child process
        os.fork() # Fork again
        arguments = ["python3", sys.argv[0], str(number-1)]
        print(arguments)
        os.execvp("python3", arguments) 
    else:
        # Parent process
        os.waitpid(pid, 0)

    return 0

if __name__ == "__main__":
    sys.exit(main())
