#TrdeBotQtPartSecond
"""
source bin/activate
pip install pyqt5-tools
pip install pyqt5
python3 -m venv .

"""
import sys
from PyQt5 import QtWidgets,QtCore, uic
from PyQt5.QtWidgets import QFileDialog,QWidget, QGridLayout, QMainWindow,QPushButton,QTextEdit

import math
import os
from PyQt5.QtCore import Qt

from tkinter import *

class Ui_BYBit_TradeBot(object):
    def setupUi(self, BYBit_TradeBot):
        BYBit_TradeBot.setObjectName("BYBit_TradeBot")
        BYBit_TradeBot.setEnabled(True)
        BYBit_TradeBot.resize(400, 300)
        BYBit_TradeBot.setStyleSheet("background-color: rgb(36, 31, 49);")
        self.centralwidget = QtWidgets.QWidget(BYBit_TradeBot)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 9, 120, 241))
        self.groupBox.setStyleSheet("background-color: rgb(193, 17, 221);\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 170, 101, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 200, 101, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 10, 131, 241))
        self.graphicsView.setObjectName("graphicsView")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(130, 10, 111, 241))
        self.openGLWidget.setObjectName("openGLWidget")
        BYBit_TradeBot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BYBit_TradeBot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        BYBit_TradeBot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BYBit_TradeBot)
        self.statusbar.setObjectName("statusbar")
        BYBit_TradeBot.setStatusBar(self.statusbar)

        self.retranslateUi(BYBit_TradeBot)
        QtCore.QMetaObject.connectSlotsByName(BYBit_TradeBot)

    def retranslateUi(self, BYBit_TradeBot):
        _translate = QtCore.QCoreApplication.translate
        BYBit_TradeBot.setWindowTitle(_translate("BYBit_TradeBot", "MainWindow"))
        self.pushButton.setText(_translate("BYBit_TradeBot", "PushButton"))
        self.pushButton_2.setText(_translate("BYBit_TradeBot", "PushButton"))
        self.pushButton_3.setText(_translate("BYBit_TradeBot", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BYBit_TradeBot = QtWidgets.QMainWindow()
    ui = Ui_BYBit_TradeBot()
    ui.setupUi(BYBit_TradeBot)
    BYBit_TradeBot.show()
    sys.exit(app.exec_())
