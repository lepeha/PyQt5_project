# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 80, 271, 91))
        self.pushButton.setObjectName("pushButton")
        self.checkBox5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox5.setGeometry(QtCore.QRect(980, 30, 41, 21))
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox10.setGeometry(QtCore.QRect(1020, 30, 41, 21))
        self.checkBox10.setObjectName("checkBox10")
        self.checkBox15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox15.setGeometry(QtCore.QRect(1060, 30, 41, 21))
        self.checkBox15.setObjectName("checkBox15")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 20, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(559, 221, 261, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(52, 26, 456, 742))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 80, 271, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(559, 299, 261, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(559, 377, 261, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkBox5, self.checkBox10)
        MainWindow.setTabOrder(self.checkBox10, self.checkBox15)
        MainWindow.setTabOrder(self.checkBox15, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Заполнить таблицу"))
        self.checkBox5.setText(_translate("MainWindow", "5"))
        self.checkBox10.setText(_translate("MainWindow", "10"))
        self.checkBox15.setText(_translate("MainWindow", "15"))
        self.label.setText(_translate("MainWindow", "Выбери количество выводимых слов:"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить выделенное в словарь"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "English words"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Russian words"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Check"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить таблицу"))
        self.pushButton_4.setText(_translate("MainWindow", "Открыть словарь"))
        self.pushButton_5.setText(_translate("MainWindow", "Очистить словарь"))
