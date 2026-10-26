import unittest
from actividad import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "Error")

if __name__ == '__main__':
    unittest.main()