from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel
from PyQt5.QtWidgets import QSizePolicy, QFontDialog, QTextEdit
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        vbox = QVBoxLayout()

        btn = QPushButton('dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        self.text = QTextEdit()

        vbox.addWidget(self.lbl)
        vbox.addWidget(self.text)

        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
            self.text.setFont(font)
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())