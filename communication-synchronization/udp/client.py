import socket
import sys

def main():
  
    hostname = "localhost"
    
    # Convert hostname to IP address
    host_ip = socket.gethostbyname(hostname)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    port = 8000  # Typically echo server port; replace with your port if different
    
    # Loop to send data
    while True:

        data = input("Enter data to send (or 'exit' to quit): ")
        if data == 'exit':
            break
        
        # Send data
        sock.sendto(data.encode('utf-8'), (host_ip, port))
        
        # Receive response
        response, _ = sock.recvfrom(1024)
        print("Received:", response.decode('utf-8'))
    
    # Close the socket
    sock.close()

if __name__ == '__main__':
    main()