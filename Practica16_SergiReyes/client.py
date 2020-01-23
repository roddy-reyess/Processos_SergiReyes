# Echo client program
import socket
import messages
from threading import Thread

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    thread = Thread(target = messages.send_message, args = (raw_input("Envia un missatge pel server: "), s, HOST, PORT, ))
    thread.start()
    thread.join()
    if messages.recv_message(s) == False:
        break

s.close()
