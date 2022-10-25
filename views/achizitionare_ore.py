# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'achizitionare_ore.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_background = QtWidgets.QLabel(self.centralwidget)
        self.image_background.setGeometry(QtCore.QRect(-80, -10, 1121, 741))
        self.image_background.setAutoFillBackground(False)
        self.image_background.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.image_background.setText("")
        self.image_background.setPixmap(QtGui.QPixmap("../../../cojoc/Downloads/Image1.png"))
        self.image_background.setObjectName("image_background")
        self.login_titlu_label = QtWidgets.QLabel(self.centralwidget)
        self.login_titlu_label.setGeometry(QtCore.QRect(230, 0, 601, 121))
        self.login_titlu_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 25pt \"Arial Black\";")
        self.login_titlu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_titlu_label.setObjectName("login_titlu_label")
        self.achizitioneaza_button = QtWidgets.QPushButton(self.centralwidget)
        self.achizitioneaza_button.setGeometry(QtCore.QRect(700, 610, 211, 61))
        self.achizitioneaza_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.achizitioneaza_button.setObjectName("achizitioneaza_button")
        self.table_achizitionanre = QtWidgets.QTableWidget(self.centralwidget)
        self.table_achizitionanre.setGeometry(QtCore.QRect(20, 130, 631, 541))
        self.table_achizitionanre.setLineWidth(1)
        self.table_achizitionanre.setMidLineWidth(0)
        self.table_achizitionanre.setShowGrid(True)
        self.table_achizitionanre.setWordWrap(True)
        self.table_achizitionanre.setCornerButtonEnabled(True)
        self.table_achizitionanre.setRowCount(14)
        self.table_achizitionanre.setObjectName("table_achizitionanre")
        self.table_achizitionanre.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.table_achizitionanre.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_achizitionanre.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_achizitionanre.setHorizontalHeaderItem(2, item)
        self.table_achizitionanre.horizontalHeader().setCascadingSectionResizes(False)
        self.table_achizitionanre.horizontalHeader().setDefaultSectionSize(199)
        self.table_achizitionanre.horizontalHeader().setMinimumSectionSize(50)
        self.table_achizitionanre.verticalHeader().setDefaultSectionSize(36)
        self.table_achizitionanre.verticalHeader().setHighlightSections(True)
        self.cauta_dupa_instructor_label = QtWidgets.QLabel(self.centralwidget)
        self.cauta_dupa_instructor_label.setGeometry(QtCore.QRect(700, 170, 281, 31))
        self.cauta_dupa_instructor_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"")
        self.cauta_dupa_instructor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cauta_dupa_instructor_label.setObjectName("cauta_dupa_instructor_label")
        self.caunta_innstructor_input = QtWidgets.QLineEdit(self.centralwidget)
        self.caunta_innstructor_input.setGeometry(QtCore.QRect(700, 210, 281, 41))
        self.caunta_innstructor_input.setObjectName("caunta_innstructor_input")
        self.cauta_vehicul_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cauta_vehicul_input.setGeometry(QtCore.QRect(700, 380, 281, 41))
        self.cauta_vehicul_input.setObjectName("cauta_vehicul_input")
        self.cauta_dupa_vehicul_label = QtWidgets.QLabel(self.centralwidget)
        self.cauta_dupa_vehicul_label.setGeometry(QtCore.QRect(700, 340, 281, 31))
        self.cauta_dupa_vehicul_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"")
        self.cauta_dupa_vehicul_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cauta_dupa_vehicul_label.setObjectName("cauta_dupa_vehicul_label")
        self.cauta_instructor = QtWidgets.QPushButton(self.centralwidget)
        self.cauta_instructor.setGeometry(QtCore.QRect(770, 260, 141, 41))
        self.cauta_instructor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.cauta_instructor.setObjectName("cauta_instructor")
        self.cauta_vehicul = QtWidgets.QPushButton(self.centralwidget)
        self.cauta_vehicul.setGeometry(QtCore.QRect(770, 430, 141, 41))
        self.cauta_vehicul.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.cauta_vehicul.setObjectName("cauta_vehicul")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_titlu_label.setText(_translate("MainWindow", "Achizitonare ore"))
        self.achizitioneaza_button.setText(_translate("MainWindow", "Achizitioneaza"))
        self.table_achizitionanre.setSortingEnabled(True)
        item = self.table_achizitionanre.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instructor"))
        item = self.table_achizitionanre.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicul"))
        item = self.table_achizitionanre.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ore"))
        self.cauta_dupa_instructor_label.setText(_translate("MainWindow", "Cauta dupa Instructor"))
        self.cauta_dupa_vehicul_label.setText(_translate("MainWindow", "Cauta dupa Vehicul"))
        self.cauta_instructor.setText(_translate("MainWindow", "Cauta"))
        self.cauta_vehicul.setText(_translate("MainWindow", "Cauta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
