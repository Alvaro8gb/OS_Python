import socket
import sys

def handle_error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def main(address, port):
    print(f"Trying to create TCP service on address: {address} & port: {port}")

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    try:
        sock.bind((address, int(port)))
    except socket.error as msg:
        handle_error(f"Bind failed. Error: {msg}")

    # Listen for incoming connections
    sock.listen(16)
    print(f"Serving with protocol TCP on port: {port}")

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        connection, client_address = sock.accept()

        try:
            print(f"Connection from {client_address}")

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(150)
                if data:
                    print(f"Received {data} from {client_address}")
                    connection.sendall(data)
                else:
                    print("No data from", client_address)
                    break
        finally:
            # Clean up the connection
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <address> <port>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
