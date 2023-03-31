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
   calculator.take_expression("-45 + -45")
   assert calculator.exec() == -90
   calculator.take_expression("0 + 0")
   assert calculator.exec() == 0

def test_substaction(calculator):
   calculator.take_expression("59 - 9")
   assert calculator.exec() == 50
   calculator.take_expression("-7 - 7")
   assert calculator.exec() == -14
   calculator.take_expression("-45 - -45")
   assert calculator.exec() == 0
   calculator.take_expression("0 - 0")
   assert calculator.exec() == 0

def test_multiplication(init_calc):
   calculator.take_expression("59 * 9")
   assert calculator.exec() == 531
   calculator.take_expression("-7 * 7")
   assert calculator.exec() == -49
   calculator.take_expression("-45 * 0")
   assert calculator.exec() == 0
   calculator.take_expression("543 * 1")
   assert calculator.exec() == 543

def test_division(self):
   calculator.take_expression("59 / 9")
   assert calculator.exec() == 6.555555555555555
   calculator.take_expression("-7 / 7")
   assert calculator.exec() == -1
   calculator.take_expression("14 / 7")
   assert calculator.exec() == 2
   calculator.take_expression("-45 / 0")
   assert calculator.exec() == "Error"
   calculator.take_expression("0 / 78")
   assert calculator.exec() == 0

def test_sqrt(self):
   calculator.take_expression("sqrt(84)")
   assert calculator.exec() == 9.16515138991168
   calculator.take_expression("sqrt(0)")
   assert calculator.exec() == 0
   calculator.take_expression("sqrt(1)")
   assert calculator.exec() == 1
   calculator.take_expression("sqrt(49)")
   assert calculator.exec() == 7
   calculator.take_expression("sqrt(-7)")
   assert calculator.exec() == "Error"

def test_square(self):
   calculator.take_expression("7^2")
   assert calculator.exec() == 49
   calculator.take_expression("0^0")
   assert calculator.exec() == 0
   calculator.take_expression("1^1")
   assert calculator.exec() == 1
   calculator.take_expression("2^8")
   assert calculator.exec() == 256
   calculator.take_expression("-7^5")
   assert calculator.exec() == -16807
   calculator.take_expression("15^-2")
   assert calculator.exec() == 0.00390625

def test_factorial(self):
   calculator.take_expression("7!")
   assert calculator.exec() == 5040
   calculator.take_expression("0!")
   assert calculator.exec() == 1
   calculator.take_expression("1!")
   assert calculator.exec() == 1
   calculator.take_expression("4!")
   assert calculator.exec() == 24
   calculator.take_expression("-7!")
   assert calculator.exec() == "Error"