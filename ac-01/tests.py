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

if __name__ == '__main__':
    unittest.main()