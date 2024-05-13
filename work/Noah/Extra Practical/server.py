
import sys
import socket
import datetime


def main():

    # Error Handling
    if len(sys.argv) < 3:
        print("Usage: python", sys.argv[0], "<IP Address> <Port>")
        return 1

    # Get the IP Address and Port Number from the command line arguments
    udp_ip_address = sys.argv[1]
    udp_port_no = int(sys.argv[2])

    # Create the UDP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((udp_ip_address, udp_port_no))
    print("UDP time server is up and listening...")

    # Enter an infinite loop to keep the server running
    while True:

        # Receive data from the client
        data, addr = server_sock.recvfrom(1024)
        command = data.decode().strip()

        # Print the client information
        client_info = socket.getnameinfo(addr, socket.NI_NUMERICHOST | socket.NI_NUMERICSERV)
        print(f"Received from {client_info[0]}:{client_info[1]}")

        # Respond to the client based on the command received
        if command == 't':
            # Send current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            server_sock.sendto(current_time.encode(), addr)
        elif command == 'd':
            # Send current date
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            server_sock.sendto(current_date.encode(), addr)
        elif command == 'q':
            # Terminate the server
            print("Server is shutting down as requested by the client.")
            break
        else:
            error_message = "Invalid command"
            server_sock.sendto(error_message.encode(), addr)


if __name__ == '__main__':
    main()
