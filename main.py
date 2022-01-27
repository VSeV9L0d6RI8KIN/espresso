import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM инфа").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 350)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setHorizontalHeaderLabels(('ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                    'Описание вкуса', 'Цена (руб.)', 'Объем упаковки (г)'))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
