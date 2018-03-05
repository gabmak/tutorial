import unittest

from Main import Calculator


class CalculatorTest(unittest.TestCase):
    def test_tax_with_same(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(30, 30)), "Same!")

    def test_tax_with_combine(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(300000, 108000)), "Use joint")

    def test_tax_with_individual(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(300000000, 300000000)), "Use individual")

    def test_tax_with_error(self):
        cal = Calculator
        self.assertEquals((cal.mainProgram(300000000, 300000000)), "Same!")


if __name__ == '__main__':
    unittest.main()
