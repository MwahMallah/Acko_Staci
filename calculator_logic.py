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
                list_split.append(int(prev_numeric))
            prev_numeric = ""
            list_split.append(list_char)
    if prev_numeric != "":
        list_split.append(int(prev_numeric))
    return list_split


def remove_spaces_from_list(expr):
    list_despaced = [list_item for list_item in expr if list_item != " "]
    return list_despaced


# executes expression
def execute(arg1=None, arg2=None, operation=None):
    match operation:
        case "+":
            return arg1 + arg2
        case "-":
            return arg1 - arg2


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
        # brack_contents = ""
        # brack_ctr = 0
        # while "(" in self.expression:
        #     for list_item in self.expression:
        #         if list_item == "(":
        #             brack_ctr += 1
        #         elif list_item == ")":
        #             brack_ctr -= 1
        #         if brack_ctr < 0:
        #             pass  # error
        #         if brack_ctr == 0 and brack_contents is not None:
        #             brack_contents = brack_contents[1:]
        #             #print(brack_contents)
        #             pass  # přidat počítání v závorce
        #         elif brack_ctr > 0:
        #             brack_contents += list_item

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

            self.expression[op_index] = execute(self.expression[op_index - 1],
                                                self.expression[op_index + 1],
                                                self.expression[op_index])
            self.expression.pop(op_index - 1)
            self.expression.pop(op_index)

        return self.expression
