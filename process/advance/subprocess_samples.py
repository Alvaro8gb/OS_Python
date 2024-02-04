import subprocess
import time

"""
Advance use of process, subprocess library
"""
def run_and_capture_output():
    # Run a command and capture its output
    result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
    print("Command Output:")
    print(result.stdout)

def run_and_capture_exit_code():
    # Run a command and capture its exit code
    result = subprocess.run(["ls", "nonexistent_directory"], stderr=subprocess.PIPE, text=True)
    print("Exit Code:", result.returncode)
    print("Error Message:")
    print(result.stderr)

def run_with_shell():
    # Run a command using the shell
    result = subprocess.run("echo Hello, subprocess!", shell=True, stdout=subprocess.PIPE, text=True)
    print("Command Output:")
    print(result.stdout)

def pipe_input_to_command():
    # Pipe input to a command
    input_data = "This is some input data."
    result = subprocess.run(["grep", "input"], input=input_data, stdout=subprocess.PIPE, text=True)
    print("Command Output:")
    print(result.stdout)

def run_asynchronously():
    # Run a command asynchronously
    process = subprocess.Popen(["sleep", "3"])

    # Do other work while the command is running
    print("Doing other work...")
    time.sleep(2)

    # Wait for the command to finish
    process.wait()
    print("Command finished.")

if __name__ == "__main__":
    run_and_capture_output()
    print("\n" + "="*40 + "\n")
    
    run_and_capture_exit_code()
    print("\n" + "="*40 + "\n")

    run_with_shell()
    print("\n" + "="*40 + "\n")

    pipe_input_to_command()
    print("\n" + "="*40 + "\n")

    run_asynchronously()
