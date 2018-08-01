'''
centering
QDesktopWidget : provides information about user's desktop, screen size

'''

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.resize(250, 150)
        self.center() # center the window

        self.setWindowTitle('Centered')
        self.show()

    def center(self):
        qr = self.frameGeometry() # get a rectangle : geometry of the "main" window
        cp = QDesktopWidget().availableGeometry().center() # get screen resolution - get center point
        qr.moveCenter(cp) # move rectangle; doesn't change size
        self.move(qr.topLeft()) # move application window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())