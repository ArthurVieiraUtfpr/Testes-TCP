import socket
import struct
import random

def generate_random_array(size=4):
    # Generate a random array of floats between 0 and 1
    random_array = [random.uniform(0, 1000) for _ in range(size)]
    precision = 2
    random_array = [round(value, precision) for value in random_array]
    return random_array

def send_array_to_server(number_array, operation):
    # Convert the array of numbers to bytes
    data = struct.pack('!I{}f'.format(len(number_array)), operation, *number_array)

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 51515))

    # Send the data to the server
    client_socket.send(data)

    # Receive the server's response
    response = client_socket.recv(4)  # Adjust the size to match the packed data size

    # Decode the response to get the result
    result = struct.unpack('!f', response)[0]

    # Close the connection
    client_socket.close()
    return result

if __name__ == "__main__":
    # Example of using the client
    number_array = generate_random_array()
    precision = 5
    operation = int(input("Choose operation \n(0 for minimum, 1 for maximum):\n "))

    print('Array sent:', number_array)
    result_from_server = send_array_to_server(number_array, operation)

    # Round the result to surpass Python's inherent imprecision of floating-point numbers
    result_from_server = round(result_from_server, 5)

    if operation == 1:
        print(f"\nThe maximum value from the given array is: {result_from_server}")
    else:
        print(f"The minimum value from the given array is: {result_from_server}")
