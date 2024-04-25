#  Write a program that emulates the behavior of the shell in executing a statement in the form:
    # cmd1 arg1 | cmd2 arg2
# The program will create an unnamed pipeline and create a child:
# The parent process will redirect the standard output to the write end of the pipe and execute command1 argument1.
# The child process will redirect the standard input to the read end of the pipe and execute cmd2 arg2.
# Test the operation with a statement similar to: /pipe_ex.py echo 12345 wc-c
    # will output 6 -> length of string (with newline)

import os
import sys

def main():
    if len(sys.argv) < 5:
        print("Usage: python pipe_ex.py cmd1 arg1 cmd2 arg2")
        sys.exit(1)
    
    cmd1 = sys.argv[1]
    arg1 = sys.argv[2]
    cmd2 = sys.argv[3]
    arg2 = sys.argv[4]
    
    # create a pipe
    read_end, write_end = os.pipe()
    
    pid = os.fork()
    
    if pid > 0:
        # parent process
        # close read end of the pipe
        os.close(read_end)
        
        # redirect stdout to write end of pipe
        os.dup2(write_end, sys.stdout.fileno())
        
        os.execlp(cmd1, cmd1, arg1)
    
    if pid == 0:
        # child process
        # close write end of pipe
        os.close(write_end)
        
        # redirect stdin to read end of pipe
        os.dup2(read_end, sys.stdin.fileno())
        
        os.execlp(cmd2, cmd2, arg2)
    
    else:
        print("Error in fork, exiting")
        sys.exit(0)

if __name__ == "__main__":
    main()
