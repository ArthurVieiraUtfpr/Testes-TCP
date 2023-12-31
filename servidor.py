import socket
import struct


def handle_client(client_socket):
    # Recebe os dados do cliente
    data = client_socket.recv(1024)

    # Decodifica os dados para um array de floats
    float_array = struct.unpack('!{}f'.format(len(data) // 4), data)
    #print('array received: ',float_array)
    #print(f'array received: {float_array}')

    # # Round the received values to a specific precision
    # precision = 5
    # rounded_array = [round(value, precision) for value in float_array]

    # Calcula os valores máximo e mínimo
    max_value = max(float_array)
    min_value = min(float_array)

    # # Converte o valor máximo de volta para bytes
    # response = struct.pack('!f', max_value)
    # # Converte o valor mínimo de volta para bytes
    # response = struct.pack('!f', min_value)

    # Python has an imprecision with floating-point numbers
    # Округлить полученные значения до указанной точности
    precision = 5
    rounded_array = [round(value, precision) for value in float_array]
    print('\narray received: ',rounded_array)

    #Cria um array com os dois valores
    array = [min_value, max_value]
    response = struct.pack('!{}f'.format(len(array)), *array)
    # Envia a resposta de volta para o cliente
    client_socket.send(response)
    max_value = round(max_value, 5)
    min_value = round(min_value, 5)
    print(f'\nmax value received: {max_value}')
    print(f'min value received: {min_value}')

    # Fecha a conexão
    client_socket.close()


def start_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket a uma interface e porta específicas MUDAR IP
    server_socket.bind(('10.4.3.102', 51515))

    # Habilita o socket para aceitar conexões
    server_socket.listen(1)
    print('Waiting conections...')

    while True:
        # Aguarda por uma conexão
        client_socket, client_address = server_socket.accept()
        print('Conection received from:', client_address)

        # Lida com a conexão em uma nova thread
        handle_client(client_socket)


if __name__ == "__main__":
    start_server()
