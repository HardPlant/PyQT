'''
QObjects can emit signals
'''
import sys


from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(' ')
        self.show()
    
    def mousePressEvent(self,event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())