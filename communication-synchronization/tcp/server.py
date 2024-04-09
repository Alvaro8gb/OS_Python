import socket
import threading

def client_thread(connection, client_address):
    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f"Received {data.decode()}")
            if data:
                print(f"Sending data back to the client")
                connection.sendall(data)
            else:
                print(f"No more data from {client_address}")
                break
    finally:
        # Clean up the connection
        connection.close()

def tcp_server(server_port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_address = ('localhost', server_port)
    print(f"Starting up on port {server_port}")
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("Waiting for a connection")
        connection, client_address = sock.accept()

        # Create a new thread for each incoming connection
        thread = threading.Thread(target=client_thread, args=(connection, client_address))
        thread.start()

if __name__ == '__main__':
    PORT = 8002
    tcp_server(PORT)
