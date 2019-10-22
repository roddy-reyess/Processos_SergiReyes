# coding: utf8
import sys

"""programa que et mostra n números primers."""
class llista_primers:
    """
    La classe llista_primers, a partir d'un número introduït
    pel usuari mostra els números primers corresponent. Exemmples:
    >>> llista_primers(5).llista
    [2,3,5,7,11]
    >>> llista_primers(10).llista
    [2,3,5,7,11,13,17,19,23,29]
    """
    def __init__(self, n):
        """
        Initzialitza la classe llista_primers.
        n es el número de números primers que serán mostrats.
        """
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        Busca els números primers que formaran part de l'array
        de números que mostra el programa al final.
        """
        if (len(self.llista) == 0): #com la llista está buida s'afageix el número 2
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n): #si la llargada de la llista es més petita que el número, entra aquí
            trobat = False
            seguent = self.llista[-1]+1 #llista[-1]+1 ----> ultim número afegit + 1
            while not trobat: # el bucle es repetirá mentre trobat sea False
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent) #afegeix el número a la ultima posició
            self.busca()


if __name__ == '__main__':
    l = llista_primers(int(sys.argv[1]))
    print l.llista
