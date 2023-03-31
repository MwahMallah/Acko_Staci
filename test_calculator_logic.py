# Test for IVS projekt 2, calculator.py
import pytest
from calculator_logic import Calc
import math

@pytest.fixture
def calculator():
   calculator = Calc()
   return calculator
   
def test_sum(calculator):
   calculator.take_expression("59 + 8")
   assert calculator.exec() ==  67
   calculator.take_expression("-7 + 7")
   assert calculator.exec() == 0
#    self.assertEqual(calc.sum(-45, -45), -90)
#    self.assertEqual(calc.sum(0, 0), 0)

# def test_substaction(init_calc):
#    self.assertEqual(calc.substaction(59, 9), 50)
#    self.assertEqual(calc.substaction(-7, 7), -14)
#    self.assertEqual(calc.substaction(-45, -45), 0)
#    self.assertEqual(calc.substaction(0, 0), 0)

# def test_multiplication(init_calc):
#    self.assertEqual(calc.multiplication(59, 9), 531)
#    self.assertEqual(calc.multiplication(-7, 7), -49)
#    self.assertEqual(calc.multiplication(-45, 0), 0)
#    self.assertEqual(calc.multiplication(543, 1), 543)

# def test_division(self):
#    self.assertEqual(calc.division(59, 9), 6.555555555555555)
#    self.assertEqual(calc.division(-7, 7), -1)
#    self.assertEqual(calc.division(14, 7), 2)
#    self.assertEqual(calc.division(-45, 0), "Error")
#    self.assertEqual(calc.division(0, 78), 0)

# def test_sqrt(self):
#    self.assertEqual(calc.sqrt(84), 9.16515138991168)
#    self.assertEqual(calc.sqrt(0), 0)
#    self.assertEqual(calc.sqrt(1), 1)
#    self.assertEqual(calc.sqrt(49), 7) 
#    self.assertEqual(calc.sqrt(-7), "Error")

# def test_square(self):
#    self.assertEqual(calc.square(7, 2), 49)
#    self.assertEqual(calc.square(0, 0), 0)
#    self.assertEqual(calc.square(1, 1), 1)
#    self.assertEqual(calc.square(2, 8), 256)
#    self.assertEqual(calc.square(-7, 5), -16807)
#    self.assertEqual(calc.square(15, -2), 0.00390625)

# def test_factorial(self):
#    self.assertEqual(calc.factorial(33), 8683317618811886495518194401280000000)
#    self.assertEqual(calc.factorial(0), 1)
#    self.assertEqual(calc.factorial(1), 1)
#    self.assertEqual(calc.factorial(4), 24)
#    self.assertEqual(calc.factorial(-7), "Error")