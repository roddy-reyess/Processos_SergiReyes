# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    messageClient = raw_input("Introdueix un missatge per el servidor: ")
    bytesToSend = str.encode(messageClient)
    s.sendto(bytesToSend, (HOST, PORT))
    if "bye" in messageClient.lower():
        break
s.close()
