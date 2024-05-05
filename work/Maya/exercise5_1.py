import os
import sys

def pipe(cmd1, arg1, cm2, arg2):
    r_fd, w_fd = os.pipe()

    pid = os.fork()

    if pid == 0:
        os.close(w_fd)
        os.dup2(r_fd, sys.stdin.fileno())
        os.execlp(cm2, cm2, arg2)
    if pid > 0:
        os.close(r_fd)
        os.dup2(w_fd, sys.stdout.fileno())
        os.execlp(cmd1, cmd1, arg1)

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print("Usage: %s cmd1 arg1 cmd2 arg2" % sys.argv[0])
        sys.exit(1)
    else:
        pipe(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])