# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speack")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said   : ".format(text))
    except:
        print("sorry")
        
---------------------------------------------------
pip install pyqt5

pip install pyqt5-tools



import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="simple window"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
        
     def initUI(self):
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top,  self.width, self.height )
         self.show()
         
if __name__ == '__main__':
     app=QApplication(sys.argv)   
     ex=App()
     sys.exit(app.exec_())

-------------------------------------------------------
import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="simple window"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
        
     def initUI(self):
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top,  self.width, self.height )
         self.statusBar().showMessage('message')
         self.show()
         
if __name__ == '__main__':
     app=QApplication(sys.argv)   
     ex=App()
     sys.exit(app.exec_())

-------------------------------------------------------
import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="simple window"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
        
     def initUI(self):
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top,  self.width, self.height )
         
         button=QPushButton("button", self)
         button.setToolTip('this is an example')
         button.move(100,70)
         button.clicked.connect(self.on_click)
         self.show()

     @pyqtSlot()   
     def on_click(self):
         print('pyqt click')
         
if __name__ == '__main__':
     app=QApplication(sys.argv)   
     ex=App()
     sys.exit(app.exec_())

-------------------------------------------------------

import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="simple window"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
        
     def initUI(self):
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top,  self.width, self.height )
         buttonReply=QMessageBox.question(self, 'message', 'do you like pyqt', QMessageBox.No, QMessageBox.Yes)
         if buttonReply== QMessageBox.Yes:
             print('yes clicked')
         else:
              print('no clicked')
        
         self.show()

     @pyqtSlot()   
     def on_click(self):
         print('pyqt click')
         
if __name__ == '__main__':
     app=QApplication(sys.argv)   
     ex=App()
     sys.exit(app.exec_())

-------------------------------------------------------
import PyQt5

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="simple window"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
        
     def initUI(self):
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top,  self.width, self.height )
         
         mainMenu=self.menuBar()
         filemenu=mainMenu.addMenu('file')
         editmenu=mainMenu.addMenu('Edit')
         viewmenu=mainMenu.addMenu('Veiw')
         searchmenu=mainMenu.addMenu('Search')
         toolmenu=mainMenu.addMenu('Tools')
         helpmenu=mainMenu.addMenu('file')

         exitButton=QAction(QIcon('exit24.png'), 'Exit', self)
         exitButton.setShortcut('Ctrl+Q')
         exitButton.setStatusTip('Exit app')
         exitButton.triggered.connect(self.close)
         fileMenu.addAction(exitButton)
         
        
         self.show()

         
if __name__ == '__main__':
     app=QApplication(sys.argv)   
     ex=App()
     sys.exit(app.exec_())

-------------------------------------------------------
         
        
        
        
        
        
        
     
