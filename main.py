from os import error
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget,QMessageBox
import sys
import re
from sympy import *
import re
import numpy as np


class Ui(QWidget):# Inherit from QWidget 
    def __init__(self):# constructor of child class Ui
        super(Ui, self).__init__() # pass class and self to constructor of base class 
        uic.loadUi("main.ui", self) # load ui 
        self.graph.setBackground("w") # set background  color of widget to white
        self.graph.showGrid(x=True, y=True, alpha=1)# Show Grid on x,y and transperncey is 100%
        self.plotButton.clicked.connect(self.plot) # on click plot the graph


        
    def validateInputs(self,fx_input,min_value,max_value):
        error=0
        fx_input = fx_input.replace(" ", "")
        if fx_input == "":
           QMessageBox.critical(self, "Error", "please enter a function to plot")
        """
         Regex Explaination To Validate Funciton :
         validate from start to the end  : ^ ... $
         optional to start with negative :^  -? $
         then must be number or varaible  : ^  -? (\d+|\D)  $ => -x | x | 3 | -3 etc ..
         make a group  contain sign and [varialbe or number ]and repeat it : ^  -? (\d+ | \D)(..)* $
         then must be followed by a sign  :(-?  (\d+|\D) ( (\+|\-|\*|\/|\^) )* $ => -x+ | x/ | 3* | 3-  etc ..
         then must be followed by number or variable again : (-?  (\d+|\D) ((\+|\-|\*|\/|\^)(-)?(\d+|\D) )*=> -x+3| x/3-2*x | 3*x^4 etc..
        """
        pattern="^-?(\d+|x)((\+|\-|\*|\/|\^)-?(\d+|x))*$"
        result = re.match(pattern, fx_input)

        if not result and fx_input != "":
            #raise ValueError("Invalid format  example for allowed format :2*x^5+3*x^3*4+5 ")
            QMessageBox.critical(self,"Error", "Invalid format  example for allowed format :2*x^5+3*x^3*4+5 ")
        fx_input = fx_input.replace("^", "**")

        if min_value == "" or max_value == "":
            QMessageBox.critical(self, "Error","Min and max values should be given")

        if min_value.isnumeric() and max_value.isnumeric():
            minval = int(min_value)
            maxval = int(max_value)
            if minval >= maxval  :
              QMessageBox.critical(self, "Error","Max  should be greater than Min")

        elif not min_value == "" and not max_value == "": 
            QMessageBox.critical(self, "Error","Min and max values should be integers")

        return fx_input,minval,maxval

    def plot(self):
        try:
             function=self.expression.text()
             min_value=self.min_value.text()
             max_value=self.max_value.text()

             func_exp,minval,maxval = self.validateInputs(function,min_value,max_value)
             #graph_plot = Graph(func_exp,minval,maxval)

             seriesX = np.linspace(minval, maxval) # to create  sequences from min to max on X
             # convert String to Expression
             x = symbols("x") # create a variable to use in mathmatical expression
             y = sympify(func_exp) # to convert string expression  to SymPy expression to be able to substitue with x and get y for each value 

             # convert Expression to function to be able to get y for each x
             fx = lambdify(x, y, modules=["numpy"])
             seriesY =fx(seriesX)
             self.graph.clear()
             self.graph.plot(seriesX, seriesY, pen="r")
        except:
             return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # to do
    window = Ui()
    window.show() # use an inherited Method to show  
    sys.exit(app.exec_())
