import socket

def send_message(message, socket, HOST, PORT):
    bytesToSend = str.encode(message)
    socket.sendall(bytesToSend)

def recv_message(conn):
    bytesAddressPair = str(conn.recv(1024))
    print(">> " + bytesAddressPair)
    if bytesAddressPair.lower() == "bye":
        return False
    else:
        return True
