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

    try:
        buff = os.getcwd()
    except OSError:
        handle_error("Error in getcwd()")

    print(f"Working directory path: {buff}")

    try:
        limits = resource.getrlimit(resource.RLIMIT_NOFILE)
    except Exception:
        handle_error("Error in getrlimit()")

    print(f"Numero maximo de ficheros posible: {limits[1]}")
    print(f"Numero maximo de ficheros recomendado: {limits[0]}")

if __name__ == "__main__":
    main()
