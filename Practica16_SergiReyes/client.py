# Echo client program
import socket
import messages
from threading import Thread
HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
thread = Thread(target = messages.send_message, args = (raw_input("Envia un missatge pel server: "), s, HOST, PORT, ))
thread1 = Thread(target = messages.recv_message, args = (s, ))
thread.start()
thread1.start()
while True:




thread.join()
thread1.join()
s.close()
