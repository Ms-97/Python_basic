import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt09.ui")[0]


class MainClass(QMainWindow, form_class):
    
    global num
    num =""
    
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        self.pb4.clicked.connect(self.myclick4)
        self.pb5.clicked.connect(self.myclick5)
        self.pb6.clicked.connect(self.myclick6)
        self.pb7.clicked.connect(self.myclick7)
        self.pb8.clicked.connect(self.myclick8)
        self.pb9.clicked.connect(self.myclick9)
        self.pb0.clicked.connect(self.myclick0)
        self.show()
        
    def myclick1(self):
        global num   
        num += "1"
        
        self.le.setText(num)
    
    def myclick2(self):  
        global num 
        num += "2"
        
        self.le.setText(num)           
    
    def myclick3(self): 
        global num  
        num += "3"
        
        self.le.setText(num)
    
    def myclick4(self): 
        global num  
        num += "4"
        
        self.le.setText(num)    
        
    def myclick5(self): 
        global num  
        num += "5"
        
        self.le.setText(num)
    
    def myclick6(self): 
        global num  
        num += "6"
        
        self.le.setText(num)
    
    def myclick7(self):   
        global num
        num += "7"
        
        self.le.setText(num)           
    
    def myclick8(self):
        global num   
        num += "8"
        
        self.le.setText(num)
    
    def myclick9(self):
        global num   
        num += "9"
        
        self.le.setText(num)   
        
    def myclick0(self): 
        global num  
        num += "0"
        
        self.le.setText(num)
    
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()