'''
messagebox
'''


import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()
    
    def closeEvent(self, event): # Handle QCloseEvent
        reply = QMessageBox.question(self, 'Message',
        "Are yur sure to quit?", QMessageBox.Yes # Combination of Buttons
        | QMessageBox.No, QMessageBox.No ) # Default Button

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())