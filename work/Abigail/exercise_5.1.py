import os
import sys

def execute_pipeline(cmd1, arg1, cmd2, arg2):
    # Creating a pipe
    pipe_read, pipe_write = os.pipe()

    # Forking a child process
    pid = os.fork()

    if pid == 0:  # Child process
        # Closes the write end of the pipe 
        os.close(pipe_write)
        # Redirects read end of the pipe to stdin
        os.dup2(pipe_read, sys.stdin.fileno())
        # Closes the original read end of the pipe
        os.close(pipe_read)
        # Executing cmd2 with its arguments
        os.execvp(cmd2, [cmd2, arg2])
    elif pid > 0:  # Parent process
        #Close read part of parent
        os.close(pipe_read)
        # Redirects write end of the pipe to stdout
        os.dup2(pipe_write, sys.stdout.fileno())
        # Closing the original write end of the pipe
        os.close(pipe_write)
        # Executing cmd1 with its arguments
        os.execvp(cmd1, [cmd1, arg1])
    else:
        # Error occurred while forking
        sys.stderr.write("Fork failed\n")
        sys.exit(1)

if __name__ == "__main__":
    # Check if command-line arguments are provided correctly
    if len(sys.argv) != 5:
        print("Usage: {} cmd1 arg1 | cmd2 arg2".format(sys.argv[0]))
        sys.exit(1)

    cmd1, arg1, cmd2, arg2 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    execute_pipeline(cmd1, arg1, cmd2, arg2)