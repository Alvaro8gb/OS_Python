import os
import sys

def execl_sample():
    print("1. Executing execl:")
    os.execl("/bin/ls", "/bin/ls", "-l")

def execlp_sample():
    print("2. Executing execlp:")
    os.execlp("ls", "ls", "-l")

def execv_sample():
    print("3. Executing execv:")
    os.execv("/bin/ls", ["/bin/ls", "-l"])

def execvp_sample():
    print("4. Executing execvp:")
    os.execvp("ls", ["ls", "-l"])

def execve_sample():
    print("5. Executing execve:")
    os.execve("/bin/ls", ["/bin/ls", "-l"], os.environ)

def execvpe_sample():
    print("6. Executing execvpe:")
    os.execvpe("ls", ["ls", "-l"], os.environ)

def print_usage():
    print(f"Usage: {sys.argv[0]} <example_number>")
    print("Examples:")
    print("  1: execl sample")
    print("  2: execlp sample")
    print("  3: execv sample")
    print("  4: execvp sample")
    print("  5: execve sample")
    print("  6: execvpe sample")

def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(-1)

    example_number = int(sys.argv[1])

    if example_number == 1:
        execl_sample()
    elif example_number == 2:
        execlp_sample()
    elif example_number == 3:
        execv_sample()
    elif example_number == 4:
        execvp_sample()
    elif example_number == 5:
        execve_sample()
    elif example_number == 6:
        execvpe_sample()
    else:
        print("Invalid example number")
        print_usage()
        sys.exit(-1)

if __name__ == "__main__":
    main()
