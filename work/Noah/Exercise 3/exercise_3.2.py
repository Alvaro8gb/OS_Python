
import subprocess


def main():
    # Run a command with niceness -19 (high priority) that sleeps for 30 seconds
    command = ['nice', '-19', 'sleep', '30']
    process = subprocess.Popen(command)
    process.wait()
    # Validate in terminal using the command: ps -eo pid,user,cmd,ni | grep 19


if __name__ == '__main__':
    main()
