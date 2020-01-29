# Echo server program
import socket
from threading import Thread
import time
import messages


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

thread = Thread(target = messages.send_message, args = (conn, ))
thread1 = Thread(target = messages.recv_message, args = (conn, ))

thread.daemon = True

thread.start()
thread1.start()

thread1.join()

time.sleep(1)
s.close()
