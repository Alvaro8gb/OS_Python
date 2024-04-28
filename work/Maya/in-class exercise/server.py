# worked with Maura and Abby

import socket
import datetime

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to any available interface on port 8002
    server_socket.bind(('localhost', 8002))
    
    print("UDP server up and listening")

    # Infinite loop to keep the server running
    while True:
        data, address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        command = data.decode()
        client_hostname = socket.getnameinfo(address, socket.NI_NAMEREQD)[0]
        print(f"Received request from {client_hostname} ({address[0]}:{address[1]})")

        if command == 't':
            response = datetime.datetime.now().strftime('%H:%M:%S')
        elif command == 'd':
            response = datetime.datetime.now().strftime('%Y-%m-%d')
        elif command == 'q':
            print("Server shutting down...")
            break
        else:
            response = "Invalid command"

        server_socket.sendto(response.encode(), address)
    server_socket.close()

if __name__ == '__main__':
    main()

