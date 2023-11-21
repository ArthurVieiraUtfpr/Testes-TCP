import socket
import struct


def send_array_to_server(float_array):

    # Converte o array de floats para bytes
    data = struct.pack('!{}f'.format(len(float_array)), *float_array)

    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor MUDAR IP
    client_socket.connect(('10.4.3.102', 51515))

    # Envia os dados para o servidor
    client_socket.send(data)

    # Recebe a resposta do servidor
    response = client_socket.recv(1024)

    # Decodifica a resposta para obter os valores mínimo e máximo
    data = struct.unpack('!{}f'.format(len(response) // 4), response)
    max_value = data[1]
    min_value = data[0]

    # Fecha a conexão
    client_socket.close()
    return max_value, min_value


if __name__ == "__main__":
    # Exemplo de uso do cliente
    array_to_send = [3.14, 2.71, 1.618, 0.577]
    precision = 5
    print('array sent: ', array_to_send)
    max_value_from_server, min_value_from_server = send_array_to_server(array_to_send)
    #I will round the values to surpass Python's inherent imprecision of floating-point numbers
    min_value_from_server = round(min_value_from_server, 5)
    max_value_from_server = round(max_value_from_server, 5)
    print(f"\nThe minium value from given array is: {min_value_from_server}")
    print(f"The maximum value from give array is: {max_value_from_server}")

    # array_to_send = [3.14, 2.71, 11.618, 220.577]
    # max_value_from_server = send_array_to_server(array_to_send)
    #
    # print(f"O valor máximo do array é: {max_value_from_server}")
