'''
displays mouse pointer
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        x=0
        y=0
        self.text = "x:{0}, y:{1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(' ')
        self.show()
    
    def mouseMoveEvent(self, e):
        
        x=e.x()
        y=e.y()
        
        text="x:{0}, y:{1}".format(x,y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())