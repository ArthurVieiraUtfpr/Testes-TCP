import socket
import struct


def send_array_to_server(float_array):
    # Converte o array de floats para bytes
    data = struct.pack('!{}f'.format(len(float_array)), *float_array)

    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect(('localhost', 8080))

    # Envia os dados para o servidor
    client_socket.send(data)

    # Recebe a resposta do servidor
    response = client_socket.recv(1024)

    # Decodifica a resposta para obter o valor máximo
    max_value = struct.unpack('!f', response)[0]

    # Fecha a conexão
    client_socket.close()

    return max_value


if __name__ == "__main__":
    # Exemplo de uso do cliente
    array_to_send = [3.14, 2.71, 1.618, 0.577]
    max_value_from_server = send_array_to_server(array_to_send)

    print(f"O valor máximo do array é: {max_value_from_server}")
