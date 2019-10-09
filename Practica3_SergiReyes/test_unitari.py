import unittest
from equacio1 import equacio1

class test_unitari(unittest.TestCase):

    def test_resultat(self):
        eq1 = equacio1("20x + 30 = 70")
        self.assertEqual(eq1.calcula(), 2.0)

    def test_Operador(self):
        eq1 = equacio1("20x / 30 = 70")
        self.assertEqual(eq1.calcula(), "Error " + eq1.calculante[1])
        self.assertIsInstance(eq1.calculante[1], basestring)

    def test_negatiu(self):
        eq = equacio1("20x - 30 = 70")
        self.assertEqual(eq.calcula(),5)

    def test_float(self):
        eq = equacio1("20x + 30.5 = 7.7")
        self.assertEqual(eq.calcula(),-1.14)

    def test_negatiu(self):
        eq = equacio1("2x - p = 7")
        self.assertEqual(eq.calcula(),"l'equacio conte caracter no calculables: "+eq.s_eq)

    def test_fromat_erroni(self):
        eq = equacio1("3 - 2x = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")

    def test_espai(self):
        eq = equacio1("")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")

if __name__ == '__main__':
    unittest.main()
