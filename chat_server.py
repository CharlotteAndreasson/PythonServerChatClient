import socket

# Stora bokstäver betyder konstanter, de ändras inte under programmets gång
HOST = "127.0.0.1"
PORT = 9877

def main():
    # Create a socket that uses ip¤ (AF_INET), and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Knyter host och port till server_socket.
    # Lägger i en Tuple dubbelparentes, för att bind kräver Tuple
    server_socket.bind((HOST, PORT))
    # Väntar
    server_socket.listen()

    # Wait for connection, BLOCKING
    client_socket, client_address = server_socket.accept()
    print(f'Client connected from {client_address}')

    while True: # socket och address är skilda i Python
        # Get data from client, BLOCKING
        message = client_socket.recv(1024)
        # Gör om bytes till en sträng
        message = message.decode('utf-8')
        print("Got message", message)
        return_message = "We got: " + message
        client_socket.send(return_message.encode('utf-8'))



if __name__ == '__main__':
    main()
