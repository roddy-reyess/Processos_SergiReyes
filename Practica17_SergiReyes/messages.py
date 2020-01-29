import socket


def send_message(socket):
    while True:
        message = raw_input("Envia un missatge: ")
        bytesToSend = str.encode(message)
        socket.sendall(bytesToSend)
        if message.lower() == "bye":
            break



def recv_message(conn):
    while True:
        bytesAddressPair = str(conn.recv(1024))
        print("\n>> " + bytesAddressPair)
        if bytesAddressPair.lower() == "bye":
            conn.sendall(bytesAddressPair)
            break
