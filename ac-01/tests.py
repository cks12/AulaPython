import unittest
from atividade_recursao import * 

class TestSomatorio(unittest.TestCase):
    def test_somatorio(self):
        self.assertEqual(somatorio(0), 0)
        self.assertEqual(somatorio(2), 3)
        self.assertEqual(somatorio(5), 15)
        self.assertEqual(somatorio(10), 55)
        self.assertEqual(somatorio(100), 5050)
    
    def test_potencia_de_2(self):
        self.assertEqual(potencia_de_2(1), True)
        self.assertEqual(potencia_de_2(2), True)
        self.assertEqual(potencia_de_2(4), True)
        self.assertEqual(potencia_de_2(8), True)
        self.assertEqual(potencia_de_2(16), True)
        self.assertEqual(potencia_de_2(3), False)
        self.assertEqual(potencia_de_2(10), False)
        self.assertEqual(potencia_de_2(1023), False)
    
    def test_qtd_digitos(self):
        self.assertEqual(qtd_digitos(4), 1)
        self.assertEqual(qtd_digitos(9),1)
        self.assertEqual(qtd_digitos(10), 2)
        self.assertEqual(qtd_digitos(99), 2)
        self.assertEqual(qtd_digitos(1071), 4)
    
    def test_soma_digitos(self):
        self.assertEqual(soma_digitos(4), 4)
        self.assertEqual(soma_digitos(45), 9)
        self.assertEqual(soma_digitos(451), 10)
        self.assertEqual(soma_digitos(2345), 14)
    
    def test_soma_lista(self):
        self.assertEqual(soma_lista([1,2,3,4],0), 10)
        self.assertEqual(soma_lista([1,2,3,4],2), 7)
        self.assertEqual(soma_lista([22,33,44,55],1), 132)


if __name__ == '__main__':
    unittest.main()