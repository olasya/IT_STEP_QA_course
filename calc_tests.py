import unittest
import hometask_3_calc


class CalcTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(hometask_3_calc.addition(6, 2), 8)
        self.assertEqual(hometask_3_calc.addition("3", 2.5), 5)
        self.assertEqual(hometask_3_calc.addition(3, "g"), "Wrong value")

    def test_substraction(self):
        self.assertEqual(hometask_3_calc.substraction(5, 9), -4)
        self.assertEqual(hometask_3_calc.substraction("3", 2.5), 5)
        

    def test_multiplication(self):
        self.assertEqual(hometask_3_calc.multiplication(0, 9), 0)
        self.assertEqual(hometask_3_calc.multiplication("3", 2), 6)
        self.assertEqual(hometask_3_calc.multiplication(3, "g"), "Wrong value")

    def test_division(self):
        self.assertEqual(hometask_3_calc.division(5, 8), 0.625)
        self.assertEqual(hometask_3_calc.division("3", 2.5), 5)
      
    def test_addition_all(self):
        self.assertEqual(hometask_3_calc.addition_all(5, 8, 3, 11), 33)
        self.assertEqual(hometask_3_calc.addition_all(8, "a", 11), "Wrong value")
    
    # def test_substraction_all(self):
    #     self.assertEqual(hometask_3_calc.substraction_all(50, 1, 5, 4), 40)
    #     self.assertEqual(hometask_3_calc.substraction_all(81, "a", 11), "Wrong value")



if __name__ == '__main__':
    unittest.main()