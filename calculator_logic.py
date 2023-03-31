import math

class Calc():
    
    def __init__(self, expression):
        self.expression = expression
        self.first_arg = None
        self.second_arg = None

    def exec(self):
        list_of_args = self.expression.split()
        try:
            self.first_arg = int(list_of_args[0])
        except IndexError:
            pass

        try:
            self.second_arg = int(list_of_args[2])
        except IndexError:
            pass

        operation = list_of_args[1]

        match operation:
            case "+":
                return self.first_arg + self.second_arg
            case "-":
                return self.first_arg - self.second_arg
            case "/":
                return self.first_arg / self.second_arg
            case "*":
                return self.first_arg * self.second_arg
            case "!":
                return math.factorial(self.first_arg)

    def sqrt(self, a):
        # Function for sqrt, where a is number and result is sqrt of a
        return math.sqrt(a)

    def pow(self, a, b):
        # a is number and b is power, where result is a^b
        return math.pow(a, b)

    def logarithm(self, number, base):
        return math.log(number, base)