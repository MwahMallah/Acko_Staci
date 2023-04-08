import math


def expression_to_list(expr):
    list(expr)
    list_split = list()
    prev_numeric = ""
    for list_char in expr:
        if list_char.isnumeric():
            prev_numeric += list_char
        else:
            if prev_numeric != "":
                list_split.append(prev_numeric)
            prev_numeric = ""
            list_split.append(list_char)
    if prev_numeric != "":
        list_split.append(prev_numeric)
    return list_split


def remove_spaces_from_list(expr):
    list_despaced = [list_item for list_item in expr if list_item != " "]
    return list_despaced


class Calc():
    def __init__(self):
        self.first_arg = None
        self.second_arg = None
        self.expression = None

    # takes input from the calculator input line
    # and stores at the self.expression attribute of the object
    def take_expression(self, expression):
        self.expression = expression

    # !!!NEED TO WRITE parse() METHOD TO PARSE THROUGH WHOLE EXPRESSION AND CALLS FOR EXEC() EVERY TIME
    # FOR EXAMPLE: 2 + 3 * 4 = 14, first 3 * 4 executes
    def parse(self):
        self.expression = expression_to_list(self.expression)
        self.expression = remove_spaces_from_list(self.expression)
        brack_contents = list()
        brack_ctr = 0
        # while "(" in self.expression:
        for list_item in self.expression:
            if list_item == "(":
                brack_ctr += 1
            elif list_item == ")":
                brack_ctr -= 1

            if brack_ctr < 0:
                pass  # error
            if brack_ctr == 0 and brack_contents is not None:
                brack_contents.pop(0)
                pass  # přidat počítání v závorce
            elif brack_ctr > 0:
                brack_contents.append(list_item)
        return self.expression

    # executes expression
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
            case "^":
                return math.pow(self.first_arg, self.second_arg)

    def sqrt(self, a):
        # Function for sqrt, where a is number and result is sqrt of a
        return math.sqrt(a)

    def logarithm(self, number, base):
        return math.log(number, base)
