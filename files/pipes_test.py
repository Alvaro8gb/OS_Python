import os

# Create a pipe
r, w = os.pipe()

# Fork the process
pid = os.fork()

if pid > 0:  # Parent process
    os.close(1)        # Close the standard output (STDOUT)
    os.dup(w)          # Duplicate the write end of the pipe to STDOUT
    os.close(r)        # Close the read end of the pipe, not needed here
    os.close(w)        # Close the original write end of the pipe

    # Now, any output to STDOUT will go to the pipe.
    # For example:
    print("This will go to the child process.")

else:  # Child process
    os.close(0)        # Close the standard input (STDIN)
    os.dup(r)          # Duplicate the read end of the pipe to STDIN
    os.close(r)        # Close the original read end of the pipe
    os.close(w)        # Close the write end of the pipe, not needed here

    # Now, the child process can read from STDIN and it will come from the pipe.
    # For example, to read what the parent sent:
    input_from_parent = input()
    print(f"Child received: {input_from_parent}")
