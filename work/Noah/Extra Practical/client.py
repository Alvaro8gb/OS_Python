
import os
import sys
import socket


def main():

    # Error Handling
    if len(sys.argv) < 3:
        print("Usage: python", sys.argv[0], "<Server IP Address> <Server Port>")
        return 1

    # Get the Server IP Address and Port Number from the command line arguments
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Create a UDP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Display command options to the user
        print("Enter 't' for the time, 'd' for the date, 'q' to terminate the server,"
              "'TEST <char>' for the server response prompted by a Netcat command, or 'EXIT' to exit the client:")
        command = input().strip()

        # Exit Command
        if command.lower() == 'exit':
            print("Exiting client.")
            break
        # Netcat Command
        if "test" in command.lower():
            char = command.split(" ")[1]
            print("Command:", command)
            print("Character:", char)
            os.system(f"echo -n '{char}' | nc -u {server_ip} {server_port}")
        # Time, Date, or Terminate Command
        else:
            # Send the command to the server
            client_sock.sendto(command.encode(), (server_ip, server_port))

            # Receive response from the server
            data, _ = client_sock.recvfrom(1024)  # buffer size is 1024 bytes
            print("Received from server:", data.decode())


if __name__ == '__main__':
    main()
