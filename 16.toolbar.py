'''
toolbar
quick access to command

'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self) # Abstraction for actions, exit label
        exitAct.setShortcut('Ctrl+Q') # shortcut
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())