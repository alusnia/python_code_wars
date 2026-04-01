import socket

def socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 1111))
    server.listen()
    connection, address = server.accept()
    with connection:
        while True:
            msg_raw = connection.recv(1024)
            if not msg_raw:
                break
            text = msg_raw.decode('utf-8')
            if text == "quit":
                break
            respond = text.encode('utf-8')
            connection.sendall(respond)
    server.shutdown()