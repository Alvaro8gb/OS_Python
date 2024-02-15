import socket
import sys

def main(server_address, server_port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address_full = (server_address, int(server_port))
    print(f"Connecting to {server_address} port {server_port}")
    sock.connect(server_address_full)

    try:
        while True:
            # Read data from stdin
            message = input("Enter message (Q to quit): ")
            if message == "Q":
                print("Exiting.")
                break

            # Send data
            sock.sendall(message.encode())

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(150)
                amount_received += len(data)
                print(f"Received: {data.decode()}")

    finally:
        print("Closing socket")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <address> <port>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
