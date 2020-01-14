# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)

    clientAddress = "Client address:{}".format(address)


    if "bye" in clientMsg.lower():
        time.sleep(1)
        break
    else:
        print(clientMsg)
        print(clientAddress)

s.close()
