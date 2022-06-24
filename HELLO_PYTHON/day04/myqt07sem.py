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
        com = ""
        mine = ""
        result = ""
        
        mine = self.le_mine.text()
        
        rnd = random.random()
        
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        
        if com == "가위" and mine == "가위":    result = "비김"
        if com == "가위" and mine == "바위":    result = "이김"
        if com == "가위" and mine == "보":     result = "짐"
        
        if com == "바위" and mine == "가위":    result = "짐"
        if com == "바위" and mine == "바위":    result = "비김"
        if com == "바위" and mine == "보":     result = "이김"
        
        if com == "보" and mine == "가위":    result = "이김"
        if com == "보" and mine == "바위":    result = "짐"
        if com == "보" and mine == "보":     result = "비김"

        
        self.le_com.setText(com)
        self.le_result.setText(result)

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()