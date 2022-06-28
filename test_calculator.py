from Calc import add,subtract,multiply
# from Calc import *
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_calc_addition(self):
        # “””Verify the output of `calc_addition` function”””
        self.assertEqual(add(2,4),6)
        # output = add(2,4)
        # assert output == 6
    
    def test_calc_substraction(self):
        # “””Verify the output of `calc_substraction` function”””
        self.assertEqual(subtract(7,4),3)
        # output = subtract(2, 4)
        # assert output == -2
        
    def test_calc_multiply(self):
        # “””Verify the output of `calc_multiply` function”””
        self.assertEqual(multiply(2,4),8)
        # output = multiply(2,4)
        # assert output == 8
        
if __name__ == '__main__':
    unittest.main()