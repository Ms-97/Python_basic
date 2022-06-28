import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton

form_class = uic.loadUiType("omok01.ui")[0]


class MainClass(QMainWindow, form_class):
    
    global num
    num = 0
    
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        for j in range(10):
            for i in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setGeometry(i*40, j*40, 40, 40)
                btn.setIconSize(QtCore.QSize(40,40))
                btn.clicked.connect(self.myclick)

        self.show()
        
    def myclick(self):
        
        global num
        if num % 2 == 0:
            self.sender().setIcon(QtGui.QIcon('1.png'))
            num +=1
        else:
            self.sender().setIcon(QtGui.QIcon('2.png')) 
            num +=1   
        
         
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()