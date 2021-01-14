import threading
import socket
alias = input('Username:  ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('4.tcp.eu.ngrok.io', 10307))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "alias?":
                client.send(alias.encode('ascii'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
