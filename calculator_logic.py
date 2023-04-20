import math


def expression_to_list(expr):
    list(expr)
    list_split_temp = list()
    list_split = list()
    prev_alpha = ""
    prev_numeric = ""

    for list_char in expr:
        if list_char.isalpha():
            prev_alpha += list_char
        else:
            if prev_alpha != "":
                list_split_temp.append(prev_alpha)
            prev_alpha = ""
            list_split_temp.append(list_char)
    if prev_alpha != "":
        list_split_temp.append(prev_alpha)

    for list_char in list_split_temp:
        if list_char.isnumeric() or list_char == "." or (list_char == "-" and prev_numeric == ""):
            prev_numeric += list_char
        else:
            if prev_numeric != "":
                if prev_numeric == "-":
                    list_split.append(prev_numeric)
                elif "." in prev_numeric:
                    list_split.append(float(prev_numeric))
                else:
                    list_split.append(int(prev_numeric))
            prev_numeric = ""
            list_split.append(list_char)
    if prev_numeric != "":
        if prev_numeric == "-":
            list_split.append(prev_numeric)
        elif "." in prev_numeric:
            list_split.append(float(prev_numeric))
        else:
            list_split.append(int(prev_numeric))
    return list_split


def remove_spaces_from_list(expr):
    list_despaced = [list_item for list_item in expr if list_item != " "]
    return list_despaced


# executes expression
def execute(operation, arg1=None, arg2=None):
    match operation:
        case "+":
            return arg1 + arg2
        case "-":
            return arg1 - arg2
        case "*":
            return arg1 * arg2
        case "/":
            if arg2 == 0:
                return "Error"
            else:
                return arg1 / arg2
        case "^":
            res = pow(arg1, arg2)
            if isinstance(res, complex):
                return "Error"
            else:
                return res
        case "!":
            if (isinstance(arg1, int) or arg1.is_integer()) and arg1 >= 0:
                return math.factorial(arg1)
            else:
                return "Error"


class Calc():
    def __init__(self):
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
        brack_contents = ""
        brack_ctr = 0
        while "(" in self.expression:
            pos_ctr = 0
            for list_item in self.expression[::]:
                if list_item == "(":
                    brack_ctr += 1
                elif list_item == ")":
                    brack_ctr -= 1
                if brack_ctr < 0:
                    pass  # error
                if brack_ctr == 0 and brack_contents is not None:
                    brack_contents = brack_contents[1:]
                    brack_sub = Calc()
                    brack_sub.take_expression(brack_contents)
                elif brack_ctr > 0:
                    brack_contents += str(list_item)
                    self.expression.pop(pos_ctr)
                pos_ctr += 1

        while "!" in self.expression:
            op_index = self.expression.index("!")

            self.expression[op_index] = execute(self.expression[op_index],
                                                self.expression[op_index - 1])
            if self.expression[op_index] == "Error":
                return TypeError
            self.expression.pop(op_index - 1)

        while "sqrt" in self.expression:
            op_index = self.expression.index("sqrt")
            self.expression[op_index], self.expression[op_index + 1] \
                = self.expression[op_index + 1], 1 / 2
            self.expression.insert(op_index + 1, "^")

        while "cbrt" in self.expression:
            op_index = self.expression.index("cbrt")
            self.expression[op_index], self.expression[op_index + 1] \
                = self.expression[op_index + 1], 1 / 3
            self.expression.insert(op_index + 1, "^")

        while "^" in self.expression:
            op_index = self.expression.index("^")

            self.expression[op_index] = execute(self.expression[op_index],
                                                self.expression[op_index - 1],
                                                self.expression[op_index + 1])
            if self.expression[op_index] == "Error":
                return "Error"
            self.expression.pop(op_index - 1)
            self.expression.pop(op_index)

        while "*" in self.expression or "/" in self.expression:
            if "*" in self.expression:
                if "/" in self.expression:
                    if self.expression.index("*") < self.expression.index("/"):
                        op_index = self.expression.index("*")
                    else:
                        op_index = self.expression.index("/")
                else:
                    op_index = self.expression.index("*")
            else:
                op_index = self.expression.index("/")

            self.expression[op_index] = execute(self.expression[op_index],
                                                self.expression[op_index - 1],
                                                self.expression[op_index + 1])
            self.expression.pop(op_index - 1)
            self.expression.pop(op_index)

        while "+" in self.expression or "-" in self.expression:
            if "+" in self.expression:
                if "-" in self.expression:
                    if self.expression.index("+") < self.expression.index("-"):
                        op_index = self.expression.index("+")
                    else:
                        op_index = self.expression.index("-")
                else:
                    op_index = self.expression.index("+")
            else:
                op_index = self.expression.index("-")

            self.expression[op_index] = execute(self.expression[op_index],
                                                self.expression[op_index - 1],
                                                self.expression[op_index + 1])
            if self.expression[op_index] == "Error":
                return "Error"
            self.expression.pop(op_index - 1)
            self.expression.pop(op_index)

        if isinstance(self.expression[0], float) and self.expression[0].is_integer():
            return int(self.expression[0])
        else:
            return self.expression[0]

    def eval(self, text):
        self.take_expression(text)
        result = self.parse()
        return str(result)