from sympy import *
import re
import numpy as np

"""
A class to handle user input and validate them then plot the graph 
"""
class Graph:
    def __init__(self, fx_input, min_value, max_value):
        self.fx_input = self.validateExpression(fx_input)
        self.min_value = self.validateInteger(min_value)
        self.max_value = self.validateInteger(max_value)
        self.checkMinLessThanMax()
        self.x = np.linspace(self.min_value, self.max_value) # to create  sequences from min to max 
        self.y = self.generateFunction() 

    def validateExpression(self, fx_input):
        fx_input = fx_input.replace(" ", "")
        
        if fx_input == "":
            raise ValueError("please enter a function to plot")


        pattern = "^(-)?((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?)([-\+]((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?))*$"
        #pattern = ""
        result = re.match(pattern, fx_input)
        if not result:
            raise ValueError("Invalid format  example for allowed format :2*x^5+3*x^3*4+5 ")

        return fx_input

    def validateInteger(self, value):
        if value == "":
            raise ValueError("Min and max values should be given")
        try:
            integer = int(value)
            return integer
        except:
            raise ValueError("Min and max values should be integers")

    def checkMinLessThanMax(self):
        if self.max_value <= self.min_value:
            raise ValueError("Max value should be greater than min value")

    def generateFunction(self):
        self.fx_input = self.fx_input.replace("^", "**")

        x, y = self.convertStringToMathExpression()

        function_of_x = self.convertMathExpressionToFunction(x, y)

        return function_of_x(self.x)

    def convertStringToMathExpression(self):
        x = symbols("x") # create a variable to use in mathmatical expression
        y = sympify(self.fx_input) # to convert string expression  to SymPy expression to be able to substitue with x and get y for each value 
        return x, y

    def convertMathExpressionToFunction(self, x, y):
        return lambdify(x, y, modules=["numpy"])
