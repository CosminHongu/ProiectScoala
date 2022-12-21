# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cont_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_background = QtWidgets.QLabel(self.centralwidget)
        self.image_background.setGeometry(QtCore.QRect(-140, 0, 1061, 621))
        self.image_background.setStyleSheet("background-color: rgb(0, 0, 70);")
        self.image_background.setText("")
        self.image_background.setObjectName("image_background")
        self.user_name_account_s = QtWidgets.QLabel(self.centralwidget)
        self.user_name_account_s.setGeometry(QtCore.QRect(110, 10, 671, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.user_name_account_s.setFont(font)
        self.user_name_account_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 24pt \"Arial Black\";")
        self.user_name_account_s.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_account_s.setWordWrap(True)
        self.user_name_account_s.setObjectName("user_name_account_s")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 150, 341, 260))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nume_s = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nume_s.setFont(font)
        self.nume_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nume_s.setObjectName("nume_s")
        self.verticalLayout_2.addWidget(self.nume_s)
        self.prenume_s = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prenume_s.setFont(font)
        self.prenume_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.prenume_s.setObjectName("prenume_s")
        self.verticalLayout_2.addWidget(self.prenume_s)
        self.dataNasterii_s = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dataNasterii_s.setFont(font)
        self.dataNasterii_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.dataNasterii_s.setObjectName("dataNasterii_s")
        self.verticalLayout_2.addWidget(self.dataNasterii_s)
        self.oreDisponibile_s = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oreDisponibile_s.setFont(font)
        self.oreDisponibile_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.oreDisponibile_s.setObjectName("oreDisponibile_s")
        self.verticalLayout_2.addWidget(self.oreDisponibile_s)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.programat_s = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.programat_s.setFont(font)
        self.programat_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.programat_s.setObjectName("programat_s")
        self.verticalLayout_2.addWidget(self.programat_s)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 110, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-93, 102, 1011, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-50, 440, 1071, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.editeaza_cont_button = QtWidgets.QPushButton(self.centralwidget)
        self.editeaza_cont_button.setGeometry(QtCore.QRect(330, 500, 241, 61))
        self.editeaza_cont_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.editeaza_cont_button.setObjectName("editeaza_cont_button")
        self.achizitioneaza_ore_button = QtWidgets.QPushButton(self.centralwidget)
        self.achizitioneaza_ore_button.setGeometry(QtCore.QRect(10, 460, 251, 61))
        self.achizitioneaza_ore_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.achizitioneaza_ore_button.setObjectName("achizitioneaza_ore_button")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(660, 500, 141, 61))
        self.log_out.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.log_out.setObjectName("log_out")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 150, 271, 260))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nume_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nume_label.setFont(font)
        self.nume_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nume_label.setObjectName("nume_label")
        self.verticalLayout.addWidget(self.nume_label)
        self.prenume_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prenume_label.setFont(font)
        self.prenume_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.prenume_label.setObjectName("prenume_label")
        self.verticalLayout.addWidget(self.prenume_label)
        self.data_nasterii_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_nasterii_label.setFont(font)
        self.data_nasterii_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.data_nasterii_label.setObjectName("data_nasterii_label")
        self.verticalLayout.addWidget(self.data_nasterii_label)
        self.ore_disponibile_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ore_disponibile_label.setFont(font)
        self.ore_disponibile_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.ore_disponibile_label.setObjectName("ore_disponibile_label")
        self.verticalLayout.addWidget(self.ore_disponibile_label)
        self.ore_finalizate_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ore_finalizate_label.setFont(font)
        self.ore_finalizate_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.ore_finalizate_label.setObjectName("ore_finalizate_label")
        self.verticalLayout.addWidget(self.ore_finalizate_label)
        self.programat_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.programat_label.setFont(font)
        self.programat_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.programat_label.setObjectName("programat_label")
        self.verticalLayout.addWidget(self.programat_label)
        self.programare_button = QtWidgets.QPushButton(self.centralwidget)
        self.programare_button.setGeometry(QtCore.QRect(10, 530, 251, 61))
        self.programare_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.programare_button.setObjectName("programare_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_name_account_s.setText(_translate("MainWindow", "user_name_account"))
        self.nume_s.setText(_translate("MainWindow", "NULL"))
        self.prenume_s.setText(_translate("MainWindow", "NULL"))
        self.dataNasterii_s.setText(_translate("MainWindow", "NULL"))
        self.oreDisponibile_s.setText(_translate("MainWindow", "NULL"))
        self.label_10.setText(_translate("MainWindow", "NULL"))
        self.programat_s.setText(_translate("MainWindow", "NULL"))
        self.editeaza_cont_button.setText(_translate("MainWindow", "Editieaza cont"))
        self.achizitioneaza_ore_button.setText(_translate("MainWindow", "Achizitioneaza ore"))
        self.log_out.setText(_translate("MainWindow", "Log out"))
        self.nume_label.setText(_translate("MainWindow", "Nume"))
        self.prenume_label.setText(_translate("MainWindow", "Prenume"))
        self.data_nasterii_label.setText(_translate("MainWindow", "Data nașterii"))
        self.ore_disponibile_label.setText(_translate("MainWindow", "Ore disponibile"))
        self.ore_finalizate_label.setText(_translate("MainWindow", "Ore finalizate"))
        self.programat_label.setText(_translate("MainWindow", "Programare: "))
        self.programare_button.setText(_translate("MainWindow", "Programare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())