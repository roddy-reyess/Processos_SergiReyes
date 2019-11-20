#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from datetime import datetime
from multiprocessing import Pool
import time

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return num, False
        else:
            pass
    return num, True

if __name__ == '__main__':
    start = datetime.now()
    pool = Pool(processes = 2) #Pool(processes = num_processos)
    """
    Si s'augmenta el numero de processos es faran més ràpids els càlculs si s'han de calcular més processos, fins el máxim posible per l'ordinador.
    En cambi si hi han calculs ràpids, cuant més processos hi ha més es tarda.
    """
    l = range(4000000, 4000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    numbers = pool.map(primers, l)
    for i in numbers:
        print (str(i))
    print datetime.now() - start
