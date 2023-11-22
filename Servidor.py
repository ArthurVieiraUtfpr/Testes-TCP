import socket
import struct

def handle_client(client_socket):
    # Receive data from the client
    data = client_socket.recv(1024)

    # Decode the data to an array of floats and the operation variable
    operation, *number_array = struct.unpack('!I{}f'.format((len(data) - 4) // 4), data)

    # Calculate the result based on the operation variable
    result = max(number_array) if operation == 1 else min(number_array)

    # Round the result to a specific precision
    precision = 2
    result = round(result, precision)

    # Send the result back to the client
    response = struct.pack('!f', result)
    client_socket.send(response)

    print(f'Result sent: {result}')

    # Close the connection
    client_socket.close()

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific interface and port
    server_socket.bind(('127.0.0.1', 51515))

    # Enable the socket to accept connections
    server_socket.listen(1)
    print('Waiting for connections...')

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print('Connection received from:', client_address)

        # Handle the connection in a new thread
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
