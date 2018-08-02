'''
Widgets
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QTextEdit, QAction, QFileDialog, QCheckBox
from PyQt5.QtGui import QIcon
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):      

        cb = QCheckBox('Show Title', self)
        cb.move(20, 20)
        #cb.toggle() # changetitle will not occur on init
        cb.stateChanged.connect(self.changeTitle)

        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(' ')
        self.show()
        
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())