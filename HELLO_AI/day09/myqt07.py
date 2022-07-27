import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from day09.mymnist_gawi_load_class import HerKY

form_class = uic.loadUiType("myqt07.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.hky = HerKY()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
     
            
        
        
    def myclick(self):   
        mine =""
        com = ""
        winner = ""
        mine = self.le_mine.text()
        
        
        ans = -1
        if mine == "가위":
            ans = self.hky.guess([[1,0,0]]) 
        elif mine == "바위":
            ans = self.hky.guess([[0,1,0]])    
        elif mine == "보":
            ans = self.hky.guess([[0,0,1]])  
        
        if ans == 0:
            com = "가위"
        elif ans == 1:
            com = "바위"
        elif ans == 2:
            com = "보"    
            
            
        
        if mine == com: 
            winner = "무승부"
        
        elif com == "가위" and mine == "보" or com == "바위" and mine == "가위" or com == "보" and mine == "바위":
            winner = "com 승리"
        else:
            winner = "유저 승리"
        
    
        self.le_com.setText(com)
        self.le_result.setText(winner)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()