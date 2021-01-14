'Chat Room Connection - Client-To-Client'
import threading
import socket
host = '127.0.0.1'
port = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections



def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} Left.'.encode('utf-8'))
            aliases.remove(alias)
            break
# Main function to receive the clients connection


def receive():
    while True:
        print('Server is listening ...')
        client, address = server.accept()
        print(f'User connected with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The nickname of this user is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has logged in to the framework.'.encode('utf-8'))
        client.send('Connection Established!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
