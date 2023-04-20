# Test for IVS projekt 2, calculator.py
import pytest
from calculator_logic import Calc
import math

@pytest.fixture
def calculator():
   calculator = Calc()
   return calculator

# tests for sum function, which will be sum of two numbers
def test_sum(calculator):
   calculator.take_expression("59 + 8")
   assert calculator.parse() ==  67
   calculator.take_expression("-7 + 7")
   assert calculator.parse() == 0
   calculator.take_expression("-45 + -45")
   assert calculator.parse() == -90
   calculator.take_expression("0 + 0")
   assert calculator.parse() == 0

# tests for substract function, which will be substract of two numbers
def test_substaction(calculator):
   calculator.take_expression("59 - 9")
   assert calculator.parse() == 50
   calculator.take_expression("-7 - 7")
   assert calculator.parse() == -14
   calculator.take_expression("-45 - -45")
   assert calculator.parse() == 0
   calculator.take_expression("0 - 0")
   assert calculator.parse() == 0

# tests for multiplication function, which will be multiplication of two numbers
def test_multiplication(calculator):
   calculator.take_expression("59 * 9")
   assert calculator.parse() == 531
   calculator.take_expression("-7 * 7")
   assert calculator.parse() == -49
   calculator.take_expression("-45 * 0")
   assert calculator.parse() == 0
   calculator.take_expression("543 * 1")
   assert calculator.parse() == 543

# tests for division function, which will be division of two numbers
def test_division(calculator):
   calculator.take_expression("59 / 9")
   assert calculator.parse() == 6.555555555555555
   calculator.take_expression("-7 / 7")
   assert calculator.parse() == -1
   calculator.take_expression("14 / 7")
   assert calculator.parse() == 2
   calculator.take_expression("-45 / 0")
   assert calculator.parse() == "Error"
   calculator.take_expression("0 / 78")
   assert calculator.parse() == 0

def test_sqrt(calculator):
   calculator.take_expression("sqrt(84)")
   assert calculator.parse() == 9.16515138991168
   calculator.take_expression("sqrt(0)")
   assert calculator.parse() == 0
   calculator.take_expression("sqrt(1)")
   assert calculator.parse() == 1
   calculator.take_expression("sqrt(49)")
   assert calculator.parse() == 7
   calculator.take_expression("sqrt(-7)")
   assert calculator.parse() == "Error"

def test_square(calculator):
   calculator.take_expression("7^2")
   assert calculator.parse() == 49
   calculator.take_expression("0^0")
   assert calculator.parse() == 1
   calculator.take_expression("1^1")
   assert calculator.parse() == 1
   calculator.take_expression("2^8")
   assert calculator.parse() == 256
   calculator.take_expression("-7^5")
   assert calculator.parse() == -16807
   calculator.take_expression("15^-2")
   assert calculator.parse() == 0.0044444444444444444

def test_factorial(calculator):
   calculator.take_expression("7!")
   assert calculator.parse() == 5040
   calculator.take_expression("0!")
   assert calculator.parse() == 1
   calculator.take_expression("1!")
   assert calculator.parse() == 1
   calculator.take_expression("4!")
   assert calculator.parse() == 24
   calculator.take_expression("-7!")
   assert calculator.parse() == TypeError

def test_expression(calculator):
   calculator.take_expression("1 + 2*3")
   assert calculator.parse() == 7
   calculator.take_expression("12 + sqrt(16)")
   assert calculator.parse() == 16
   calculator.take_expression("2*4 + 48")
   assert calculator.parse() == 56
   calculator.take_expression("2*4 + (53 + 2)")
   assert calculator.parse() == 63
