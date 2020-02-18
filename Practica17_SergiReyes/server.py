# Echo server program
import socket
from threading import Thread
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
global usernames
usernames = []
global connections
connections = []

def add_Con():

    while True:
        user = ""
        connections.append(s.accept())
        if len(usernames) == 0:
            connections[-1][0].sendto("Server :Insereix un nom d'usuari", connections[-1][1])
            user = connections[-1][0].recv(1024)
            usernames.append((user, connections[-1][1][1]))
        else:
            for client in connections:
                for uname in usernames:
                    if client[1][1] != uname[1]:
                        client[0].sendto("Server :Insereix un nom d'usuari", client[1])
                        user = client[0].recv(1024)
                        usernames.append((user,  client[1][1]))

        Thread(target = send_to, args = (connections[-1][0], connections[-1][1], user)).start()


def send_to(conn, addr, uname):
    while True:
        message = conn.recv(1024)
        print(message)
        for client in connections:
            if addr[1] != client[1][1]:
                for username in usernames:
                    if addr[1] == username[1]:
                        client[0].sendto(str(username[0]+":"+message), addr)
                        print(message + "    " + str(client[1]))
            else:
                print (str(client[1][1]) + "\n" + str(addr[1]))
        if message[:-1].lower() == "bye":
            for i in range(len(connections)):
                if addr[1] == connections[i][1][1]:
                    connections.pop(i)
                    break
            for i in range(len(usernames)):
                if addr[1] == username[i][1]:
                    usernames.pop(i)
                    break
            break

thread = Thread(target = add_Con, args = ( ))

thread.start()








time.sleep(1)
thread.join()
s.close()
