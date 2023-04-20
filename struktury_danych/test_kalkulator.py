import unittest
import kalkulator

class TestKalkulator(unittest.TestCase):

    # metoda testowa musi sie zaczynac od slowa 'test_'
    def test_add(self):
        self.assertEqual(kalkulator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(kalkulator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(kalkulator.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(kalkulator.divide(10, 5), 2)

        # self.assertRaises(ValueError, kalkulator.divide, 10, 0)

        with self.assertRaises(ValueError):
            kalkulator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()