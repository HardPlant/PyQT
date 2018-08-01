'''absolute
The size and the position of a widget do not change if we resize a window
Applications might look different on various platforms
Changing fonts in our application might spoil the layout
If we decide to change our layout, we must completely redo our layout, which is tedious and time consuming
'''

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        okButton = QPushButton("OK")        
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())