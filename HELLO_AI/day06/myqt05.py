import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from day06.mymnist_holl_load_class import HerKY

form_class = uic.loadUiType("myqt05.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
        
    def myclick(self):   
        com = ""
        result = ""
        mine = ""
        
        mine = self.le_mine.text()
        
        hky = HerKY()
        
        ans = -1
        if mine == "홀":
            ans = hky.guess([[1,0]]) 
        else:
            ans = hky.guess([[1,0]])    
        
        if ans == 0:
            com = "홀"
        else:
            com = "짝"
            
        if com == mine:
            result = "유저 승리"
        else:
            result = "com 승리"    
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()