import unittest
import calculator

class Calculatortest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calculator.sum(2, 4), 6)

    def test_minus(self):
        self.assertEqual(calculator.substract(6, 1), 5)

    def test_umnoj(self):
        self.assertEqual(calculator.mult(3, 7), 21)

    def test_del(self):
        self.assertEqual(calculator.mod(9, 3), 0)

if __name__ == '__main__':
    unittest.main()