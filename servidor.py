import socket
import struct


def handle_client(client_socket):
    # Recebe os dados do cliente
    data = client_socket.recv(1024)

    # Decodifica os dados para um array de floats
    float_array = struct.unpack('!{}f'.format(len(data) // 4), data)

    # Calcula o valor máximo
    max_value = max(float_array)

    # Converte o valor máximo de volta para bytes
    response = struct.pack('!f', max_value)

    # Envia a resposta de volta para o cliente
    client_socket.send(response)

    # Fecha a conexão
    client_socket.close()


def start_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket a uma interface e porta específicas
    server_socket.bind(('localhost', 8080))

    # Habilita o socket para aceitar conexões
    server_socket.listen(1)
    print('Aguardando conexões...')

    while True:
        # Aguarda por uma conexão
        client_socket, client_address = server_socket.accept()
        print('Conexão recebida de:', client_address)

        # Lida com a conexão em uma nova thread
        handle_client(client_socket)


if __name__ == "__main__":
    start_server()
