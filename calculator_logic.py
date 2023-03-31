import math


class Calc():    
    def __init__(self):
        self.first_arg = None
        self.second_arg = None

#takes input from the calculator input line
#and stores at the self.expression attribute of the object
    def take_expression(self, expression):
        self.expression = expression


#!!!NEED TO WRITE parse() METHOD TO PARSE THROUGH WHOLE EXPRESSION AND CALLS FOR EXEC() EVERY TIME
#FOR EXAMPLE: 2 + 3 * 4 = 14, first 3 * 4 executes
    def parse(self):
        pass

#executes expression
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