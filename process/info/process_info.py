import os
import sys
import resource

def handle_error(msg):
    print(f"{msg}", file=sys.stderr)
    sys.exit(os.EX_FAILURE)

def main():
    pid = os.getpid()
    print(f"PID (Process Identifier): {pid}")
    print(f"PPID (Parent Process Identifier): {os.getppid()}")
    print(f"PGRP (Process Group) or PGID (Process Group Identifier): {os.getpgid(pid)}")
    print(f"SID (Session Identifier): {os.getsid(pid)}")

    buff = os.getcwd()

    print(f"Working directory path: {buff}")

    limits = resource.getrlimit(resource.RLIMIT_NOFILE)


    print(f"Maximum number of files possible: {limits[1]}")
    print(f"Maximum number of files recommended: {limits[0]}")

if __name__ == "__main__":
    main()
