import gui
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    newui = gui.MainWindow()
    app.exec(app.exec_())
