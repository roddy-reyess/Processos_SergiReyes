
import random

def llistes_rand():
    novaLlista = []
    for x in range(10):
        novaLlista.append(random.randint(1,100))
    return novaLlista

prova1 = llistes_rand()
print(prova1)
