#!/bin/python
import sys
import os
from pathlib import Path

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

import subprocess
class Ui(QtWidgets.QDialog):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('MainUI.ui', self)

        self.sFileName=""

        self.printButton.clicked.connect(self.HelloWorld)
        self.clearButton.clicked.connect(self.plainTextEdit.clear)
        self.cmdButton.clicked.connect(self.cmdLaunch)
        self.fileSelectButton.clicked.connect(self.openFileNameDialog)
        self.subButton.clicked.connect(self.dwnSub)
        self.show()

    def HelloWorld(self):
        self.plainTextEdit.setPlainText("Hello World")
        print("Hello World")

    def cmdLaunch(self):
        cmd = "who"
        # temp = subprocess.Popen([cmd], stdout = subprocess.PIPE) 
        # # get the output as a string
        # output = str(temp.communicate()) 
        # print(output)
        sp = subprocess.run([cmd], capture_output=True)
        strOutput = str(sp.stdout.decode('ascii'))
        self.plainTextEdit.setPlainText(strOutput)
        print(strOutput)
    
    def dwnSub(self):
        if self.sFileName != "":
            sp = subprocess.run(["subliminal", "download", "-l", "en", self.sFileName], capture_output=True)
            strOutput = str(sp.stdout.decode('ascii'))
            self.plainTextEdit.setPlainText(strOutput)
            print(strOutput)

    def openFileNameDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            print(fname[0])
            self.sFileName=fname[0]
            self.fileName.setText(self.sFileName)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())