# Echo server program
import socket
from threading import Thread
import time
import messages

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()


while True:
    if messages.recv_message(conn) == False:
        time.sleep(1)
        break
    thread = Thread(target = messages.send_message, args = (raw_input("Envia un missatge pel client: "), conn, HOST, PORT, ))
    thread.start()
    thread.join()


s.close()
