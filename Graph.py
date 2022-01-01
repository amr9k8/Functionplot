#from sympy import *
#import re
#import numpy as np



"""
A class to handle user input and validate them then plot the graph 
"""
#class Graph:
#    def __init__(self, fx_input, min_value, max_value):
#        self.fx_input  = fx_input
#        self.min_value = min_value
#        self.max_value = max_value

#        self.x = np.linspace(self.min_value, self.max_value) # to create  sequences from min to max on X
#        # convert String to Expression
#        x = symbols("x") # create a variable to use in mathmatical expression
#        y = sympify(self.fx_input) # to convert string expression  to SymPy expression to be able to substitue with x and get y for each value 

#        # convert Expression to function
#        fx = lambdify(x, y, modules=["numpy"])
#        self.y =fx(self.x)
      




















     

    #def generateFunction(self):
    #    x, y = self.convertStringToMathExpression()
    #     convert String to Expression
    #    x = symbols("x") # create a variable to use in mathmatical expression
    #    y = sympify(self.fx_input) # to convert string expression  to SymPy expression to be able to substitue with x and get y for each value 
    #     convert Expression to function
    #    function_of_x = lambdify(x, y, modules=["numpy"])
    #    return function_of_x(self.x)
    #def convertMathExpressionToFunction(self, x, y):
    #    return lambdify(x, y, modules=["numpy"])

    #def convertStringToMathExpression(self):
    #    x = symbols("x") # create a variable to use in mathmatical expression
    #    y = sympify(self.fx_input) # to convert string expression  to SymPy expression to be able to substitue with x and get y for each value 
    #    return x, y