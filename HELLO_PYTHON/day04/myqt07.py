import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("myqt07.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
     
            
        
        
    def myclick(self):   
        user = self.le_mine.text()
        com = ""
        winner = ""
        rnd = random.randint(0, 2)
        
        if rnd == 0:
            com = "가위"
        elif rnd == 1: 
            com = "바위"
        else: 
            com = "보"
            
        
        if user == com: 
            winner = "무승부"
        
        elif com == "가위" and user == "보" or com == "바위" and user == "가위" or com == "보" and user == "바위":
            winner = "com 승리"
        else:
            winner = "유저 승리"
        
    
        self.le_com.setText(com)
        self.le_result.setText(winner)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()