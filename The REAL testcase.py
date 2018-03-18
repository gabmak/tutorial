import unittest

from Main import Calculator


class CalculatorTest(unittest.TestCase):
    def test_tax_with_same_0(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(0, 0)), "Same!")

    def test_tax_with_same_1(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(49999, 49999)), "Same!")

    def test_tax_with_same_2(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(99999, 99999)), "Same!")

    def test_tax_with_combine_0(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(1000000, 100000)), "Use joint")

    def test_tax_with_combine_1(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(100000,1000000)), "Use joint")

    def test_tax_with_individual(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(300000000, 300000000)), "Use individual")

    def test_tax_with_error(self):
        cal = Calculator
        self.assertEquals((cal.mainProgram(64000, 80000)), "Use individual")


    def test_tax_with_individua_4(self):
        cal = Calculator
        self.assertEqual((cal.mainProgram(300000, 900000)), "Use individual")

if __name__ == '__main__':
    unittest.main()
