import socket

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_socket.bind(('0.0.0.0', 8000))
    
    print("UDP server up and listening")

    # Infinite loop to keep the server running
    while True:
        data, address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Message from Client: {data.decode()}")
        print(f"Client IP Address: {address}")

        # Sending a reply to the client
        server_socket.sendto(data, address)

if __name__ == '__main__':
    main()
