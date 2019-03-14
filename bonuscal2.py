# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SANE\Desktop\bonuscal2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
import connectDB



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 350, 731, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        emp = connectDB.findEmp()
        self.tableWidget.setRowCount(emp.count())
        index = 0
        for data in emp:
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(data['emp_id'])))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(data['firstName']+' '+data['lastName'])))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str('{0:,.2f}'.format(data['emp_salary']))))
            index += 1


        self.profitoutput = QtWidgets.QLabel(self.centralwidget)
        self.profitoutput.setGeometry(QtCore.QRect(310, 190, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.profitoutput.setFont(font)
        self.profitoutput.setText("")
        self.profitoutput.setObjectName("profitoutput")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(170, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.percentoutput = QtWidgets.QLabel(self.centralwidget)
        self.percentoutput.setGeometry(QtCore.QRect(310, 240, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.percentoutput.setFont(font)
        self.percentoutput.setText("")
        self.percentoutput.setObjectName("percentoutput")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.bonusoutput = QtWidgets.QLabel(self.centralwidget)
        self.bonusoutput.setGeometry(QtCore.QRect(310, 290, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bonusoutput.setFont(font)
        self.bonusoutput.setText("")
        self.bonusoutput.setObjectName("bonusoutput")
        self.investInput = QtWidgets.QSpinBox(self.centralwidget)
        self.investInput.setGeometry(QtCore.QRect(330, 30, 241, 41))
        self.investInput.setMaximum(999999999)
        self.investInput.setObjectName("investInput")
        self.incomeInput = QtWidgets.QSpinBox(self.centralwidget)
        self.incomeInput.setGeometry(QtCore.QRect(330, 80, 241, 41))
        self.incomeInput.setMaximum(999999999)
        self.incomeInput.setObjectName("incomeInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# clicked button
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

# clicked reset
        self.resetButton.clicked.connect(self.on_resetButton_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Input Company Income"))
        self.label_2.setText(_translate("MainWindow", "Input Company Investment"))
        self.label_3.setText(_translate("MainWindow", "Company Profit"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.resetButton.setText(_translate("MainWindow","Reset"))
        self.label_5.setText(_translate("MainWindow", "3% of Profit"))
        self.label_7.setText(_translate("MainWindow", "Bonus per Employee"))





    def on_resetButton_clicked(self):


        connectDB.dropCol()
        connectDB.insertCol()

        self.profitoutput.setText('')

        self.percentoutput.setText('')

        self.bonusoutput.setText('')

        emp = connectDB.findEmp()
        index = 0
        for data in emp:
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(data['emp_id'])))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(data['firstName']+' '+data['lastName'])))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str('{0:,.2f}'.format(data['emp_salary']))))
            index+=1

    def on_pushButton_clicked(self):

        emp = connectDB.findEmp()

    #conn = pymongo.MongoClient("localhost", 27017)
    #db = conn.get_database("companyDB")

    #sum = self.IncomeInput.text() - self.InvestInput.text()
        incomeinput = self.incomeInput.value()
        investinput = self.investInput.value()

    #int profit cal
        summ = incomeinput - investinput

    #float percent cal
        percentS = summ*0.3

    #str percentoutput
        percentOut = '{0:,.2f}'.format(percentS)

    #str profitoutput
        profitout = '{0:,.2f}'.format(summ)

        spBonus = summ/emp.count()

        bonusout = '{0:,.2f}'.format(spBonus)
        self.profitoutput.setText(profitout)

        self.percentoutput.setText(percentOut)

        self.bonusoutput.setText(bonusout)

        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("companyDB")
        find = db.employee_salary.find()
        id = 1
        for data in find:
            db.employee_salary.update_one(
                {"_id": id},
                {"$set": {"emp_salary":data['emp_salary']+spBonus}}
            )
            id += 1

        emp = connectDB.findEmp()
        index = 0
        for data in emp:
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(data['emp_id'])))
            self.tableWidget.setItem(index, 1,
                                     QtWidgets.QTableWidgetItem(str(data['firstName'] + ' ' + data['lastName'])))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str('{0:,.2f}'.format(data['emp_salary']))))
            index += 1






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

