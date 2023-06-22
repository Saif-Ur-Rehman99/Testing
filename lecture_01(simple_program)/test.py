import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(11, 14), 25)
        self.assertEqual(calculator.add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(11, 14), -3)
        self.assertEqual(calculator.subtract(0, 5), -5)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(1, 14), 14)
        self.assertEqual(calculator.multiply(0, 5), 0)

    # If someone gives string as input
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculator.add("10", 5)
            calculator.add(4, 'a')
        with self.assertRaises(TypeError):
            calculator.subtract("11", 14)
        with self.assertRaises(TypeError):
            calculator.multiply(0, "5")

    # If someone gives Y = 0
    def test_zero_input(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()