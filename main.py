import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLineEdit, QLCDNumber, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from pathlib import Path
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cursor = self.con.cursor()
        self.res = self.cursor.execute("""SELECT * FROM kofe""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('название сорта'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('степень обжарки'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('молотый/в зернах'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('описание вкуса'))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem('цена'))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem('объем упаковки, гр'))
        for i, row in enumerate(self.res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())