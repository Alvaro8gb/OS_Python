import socket

def tcp_client(server_host, server_port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (server_host, server_port)
    print(f"Connecting to {server_host} port {server_port}")
    sock.connect(server_address)

    try:
        # Send data
        message = input("Write a message: ")
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"Received: {data.decode()}")
    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    HOST, PORT = 'localhost', 8002
    tcp_client(HOST, PORT)
