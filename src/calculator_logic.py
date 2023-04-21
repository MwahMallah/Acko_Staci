"""!
* Project Name : Projekt IVS Ačkostačí                                               
* File : calculator_logic.py                                                        
* Date : 04.2023                                                                                                                                                                                                                                
* Description : Math library with basic and advanced math operations                                                                                 
"""

"""!
 @file calculator_logic.py                                                          
                                                                           
 @brief Math Library                                                       
"""
import math


def expression_to_list(expr):
    """!
    @brief Converts expression to list of characters
    @param expr Expression to be converted
    @return List of characters
    """
    list(expr)
    list_split_temp = list() # temporary list for splitting 
    list_split = list()  # list for splitting
    prev_alpha = "" # previous character was a letter
    prev_numeric = "" # previous character was a number

    for list_char in expr:
        """!
        @brief Splits expression into list of characters

        @param list_char Character to be checked if it is a number or an operator
        """
        if list_char.isalpha(): 
            prev_alpha += list_char # if character is a letter, add it to the previous letter
        else:
            if prev_alpha != "":
                list_split_temp.append(prev_alpha) # if previous character was a letter, add it to the list
            prev_alpha = "" # reset previous letter
            list_split_temp.append(list_char) # add character to the list
    if prev_alpha != "": 
        list_split_temp.append(prev_alpha) # if previous character was a letter, add it to the list

    for list_char in list_split_temp:
        if list_char.isnumeric() or list_char == "." or (list_char == "-" and prev_numeric == ""):
            prev_numeric += list_char # if character is a number, add it to the previous number
        else:
            if prev_numeric != "":
                if prev_numeric == "-":
                    list_split.append(prev_numeric) # if previous character was a number, add it to the list
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
    """!
    @brief Removes spaces from list of characters
    @param expr List of characters to be checked
    @return List of characters without spaces
    """
    list_despaced = [list_item for list_item in expr if list_item != " "] 
    return list_despaced


# executes expression
def execute(operation, arg1=None, arg2=None):
    """!
    @brief Executes operation with given arguments
    @param operation Operation to be executed
    @param arg1 First argument, if operation is unary, this argument is the only one
    @param arg2 Second argument, if operation is unary, this argument is None
    @return Result of the operation, if operation is invalid, returns "Error"
    """
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
    """!
    @brief Calculator class

    @details Calculator class is used to store expression and parse it

    @param expression Expression to be parsed

    @return None
    """
    def __init__(self): 
        self.expression = None 

    # takes input from the calculator input line
    # and stores at the self.expression attribute of the object
    def take_expression(self, expression):
        """!
        @brief Takes expression from input and stores it in self.expression
        @param expression Expression to be stored
        @return None
        """
        self.expression = expression 

    # !!!NEED TO WRITE parse() METHOD TO PARSE THROUGH WHOLE EXPRESSION AND CALLS FOR EXEC() EVERY TIME
    # FOR EXAMPLE: 2 + 3 * 4 = 14, first 3 * 4 executes
    def parse(self):
        """!
        @brief Parses expression and executes operations

        @details Parses expression and executes operations in order of priority

        @return Result of the expression, if expression is invalid, returns "Error"
        """
        self.expression = expression_to_list(self.expression) # converts expression to list of characters
        self.expression = remove_spaces_from_list(self.expression) 
        brack_contents = "" 
        brack_ctr = 0
        while "(" in self.expression: # checks if there are brackets in the expression and parses them first 
            pos_ctr = 0
            for list_item in self.expression[::]: 
                if list_item == "(": 
                    brack_ctr += 1
                elif list_item == ")":
                    brack_ctr -= 1
                if brack_ctr < 0:
                    pass  # error
                if brack_ctr == 0 and brack_contents != "":
                    brack_contents = brack_contents[1:] 
                    brack_sub = Calc() 
                    brack_sub.take_expression(brack_contents)
                    self.expression[pos_ctr] = brack_sub.parse() 
                    break
                elif brack_ctr > 0:
                    brack_contents += str(list_item)
                    self.expression.pop(pos_ctr)
                    pos_ctr -= 1
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
        """!
        @brief Takes expression from input and parses it
        @details Takes expression from input and parses it
        @param text Expression to be parsed
        @return Result of the expression, if expression is invalid, returns "Error"
        """
        self.take_expression(text) 
        result = self.parse() 
        return str(result)
    
"""! Konec souboru calculator_logic.py """
