# -*- coding: utf8 -*-
import md5, random, sys, time
from multiprocessing import Process, Semaphore, Pipe

def busca(x, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        pass
    else:
        print fr[index+1:index2]
        f.close()
    s.release()

def substitueix(x, y, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    f.close()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        print 'Aquest nombre no existeix'
        s.release()
    else:
        print fr[index+1:index2]
        f = open('fitxer.txt', 'w')
        f.write(fr[:index+1])
        f.write(y + ',' + md5.md5(y).hexdigest()+ "\n")
        f.write(fr[index2+1:])
        f.close()
        s.release()
        busca(y, s)


def inici():
    f = open('fitxer.txt', 'w')
    for i in range(100):
        f.write(str(i)+ ',' + md5.md5(str(i)).hexdigest()+ "\n")
    f.close()
    #print open('fitxer.txt', 'ro').read()

def fill(s, child_conn):
    while True:
        x = child_conn.recv()
        y = child_conn.recv()
        if x.lower() == "q" or y.lower() == "q":
            break
        else:
            substitueix(str(x),str(y), s)

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__' :
    inici()
    parent_conn, child_conn = Pipe()
    s = Semaphore(1)
    running = True
    fill = Process(target=fill, args=(s, child_conn))
    fill.start()
    while running == True:
        txt = raw_input("Quin nombre vols substituir? [nombres del 1 al 100] [q per sortir] ")
        if txt.lower() == "q":
            parent_conn.send(txt)
            parent_conn.send("q")
            time.sleep(1)
            running = False
        elif is_int(txt) == True:
            txt2 = raw_input("Per quin nombre el vols editar? ")
            if txt2.lower() == "q":
                parent_conn.send(txt)
                parent_conn.send(txt2)
                time.sleep(1)
                running = False
            else:
                if is_int(txt2) == True:
                    parent_conn.send(txt)
                    parent_conn.send(txt2)
                    time.sleep(1)
                else:
                    print "No es un nombre vàlid"
        elif is_int(txt) == False:
            print "No es un nombre vàlid"
    fill.join()
