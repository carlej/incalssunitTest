
import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)

class testCaseMin(unittest.TestCase):
    def test_min(self):
        self.assertEqual(calc.min(10,5),5)

class testCaseMult(unittest.TestCase):
    def test_mult(self):
        self.assertEqual(calc.mult(10,5),50)

class testCaseDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(calc.div(10,5),2)

if __name__ == '__main__':
    unittest.main()
