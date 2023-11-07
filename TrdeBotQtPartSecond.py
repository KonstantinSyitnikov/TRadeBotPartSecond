"""
source bin/activate
pip install pyqt5-tools
pip install pyqt5
python3 -m venv .
pyuic5 -x NAMEPROJECT.ui -o NAMEPROJECT.py
"""
import sys
from PyQt5 import QtWidgets,QtCore, uic
from PyQt5.QtWidgets import QFileDialog,QWidget, QGridLayout, QMainWindow,QPushButton,QTextEdit

import math
from PyQt5.QtCore import Qt





class Ui_TradeBot(object):
    def setupUi(self, TradeBot):
        TradeBot.setObjectName("TradeBot")
        TradeBot.resize(741, 589)
        TradeBot.setStyleSheet("background-color: rgb(36, 31, 49);")
        self.centralwidget = QtWidgets.QWidget(TradeBot)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, -20, 481, 601))
        #self.graphicsView.setStyleSheet("background-image: url(:/newPrefix/a-graph-with-a-city-in-the-background_913665-61.jpg);\n"
        self.graphicsView.setStyleSheet("background-image:url(Design/a-graph-with-a-city-in-the-background_913665-61.jpg);")

        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 141, 25))
        self.pushButton.setStyleSheet("background-color: rgb(134, 94, 60);\n"
"font: 75 14pt \"Ubuntu Condensed\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 141, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(134, 94, 60);\n"
"font: 75 14pt \"Ubuntu Condensed\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 0, 241, 541))
        self.label.setText("")
        self.label.setObjectName("label")
        TradeBot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TradeBot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 22))
        self.menubar.setObjectName("menubar")
        TradeBot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TradeBot)
        self.statusbar.setObjectName("statusbar")
        TradeBot.setStatusBar(self.statusbar)

        self.retranslateUi(TradeBot)
        QtCore.QMetaObject.connectSlotsByName(TradeBot)

    def retranslateUi(self, TradeBot):
        _translate = QtCore.QCoreApplication.translate
        TradeBot.setWindowTitle(_translate("TradeBot", "MainWindow"))
        self.pushButton.setText(_translate("TradeBot", "Open Statistic"))
        self.pushButton_2.setText(_translate("TradeBot", "Close Window"))
        self.label.setToolTip(_translate("TradeBot", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
#import ImageForQt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TradeBot = QtWidgets.QMainWindow()
    ui = Ui_TradeBot()
    ui.setupUi(TradeBot)
    TradeBot.show()
    sys.exit(app.exec_())
