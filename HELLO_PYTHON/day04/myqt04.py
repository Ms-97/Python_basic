import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt04.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):   
        
        dan = int(self.le.text())
        
        result =""
        
        for i in range(1,9+1):
            result += ("{}*{}={}\n".format(dan,i,dan*i))
        
        self.te.setText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()