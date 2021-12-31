from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget
import sys
from plot import plot


class Ui(QWidget):# Inherit from QWidget 
    def __init__(self):# constructor of child class Ui
        super(Ui, self).__init__() # pass self to constructor of base class 
        uic.loadUi("main1.ui", self)
        self.graph.setBackground("w") # set background  color of widget to white
        self.graph.showGrid(x=True, y=True, alpha=1)# Show Grid on x,y and transperncey is 100%
        self.plotButton.clicked.connect(lambda: plot(self)) # on click plot the graph


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # to do
    window = Ui()
    window.show() # use an inherited Method to show  
    sys.exit(app.exec_())
