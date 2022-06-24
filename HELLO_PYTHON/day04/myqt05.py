import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt05.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
     
            
        
        
    def myclick(self):   
        me = self.le_mine.text()
        com = ""
        result = ""
        rnd = random()
        
        if rnd > 0.5:
            com = "홀"
        else:
            com = "짝"
            
        if com == me:
            result = "유저 승리"
        else:
            result = "com 승리"    
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()