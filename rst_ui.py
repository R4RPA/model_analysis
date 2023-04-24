# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rst.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_80 = QtWidgets.QLabel(self.centralwidget)
        self.label_80.setGeometry(QtCore.QRect(20, 25, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.search_open_term = QtWidgets.QLineEdit(self.centralwidget)
        self.search_open_term.setGeometry(QtCore.QRect(130, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_open_term.setFont(font)
        self.search_open_term.setObjectName("search_open_term")
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(10, 140, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.tip_fix_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_fix_file_path.setEnabled(False)
        self.tip_fix_file_path.setGeometry(QtCore.QRect(180, 140, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_fix_file_path.setFont(font)
        self.tip_fix_file_path.setObjectName("tip_fix_file_path")
        self.tip_fix_file_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.tip_fix_file_path_browse.setGeometry(QtCore.QRect(560, 140, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.tip_fix_file_path_browse.setFont(font)
        self.tip_fix_file_path_browse.setObjectName("tip_fix_file_path_browse")
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setGeometry(QtCore.QRect(20, 310, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(20, 260, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(450, 260, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.process_rst_files = QtWidgets.QPushButton(self.centralwidget)
        self.process_rst_files.setGeometry(QtCore.QRect(200, 260, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.process_rst_files.setFont(font)
        self.process_rst_files.setObjectName("process_rst_files")
        self.label_64 = QtWidgets.QLabel(self.centralwidget)
        self.label_64.setGeometry(QtCore.QRect(10, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.tip_free_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_free_file_path.setEnabled(False)
        self.tip_free_file_path.setGeometry(QtCore.QRect(180, 190, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_free_file_path.setFont(font)
        self.tip_free_file_path.setObjectName("tip_free_file_path")
        self.tip_free_file_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.tip_free_file_path_browse.setGeometry(QtCore.QRect(560, 190, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.tip_free_file_path_browse.setFont(font)
        self.tip_free_file_path_browse.setObjectName("tip_free_file_path_browse")
        self.search_open_term_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.search_open_term_2.setGeometry(QtCore.QRect(130, 60, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_open_term_2.setFont(font)
        self.search_open_term_2.setObjectName("search_open_term_2")
        self.label_81 = QtWidgets.QLabel(self.centralwidget)
        self.label_81.setGeometry(QtCore.QRect(20, 65, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.search_open_term_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.search_open_term_3.setGeometry(QtCore.QRect(400, 60, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_open_term_3.setFont(font)
        self.search_open_term_3.setObjectName("search_open_term_3")
        self.label_82 = QtWidgets.QLabel(self.centralwidget)
        self.label_82.setGeometry(QtCore.QRect(320, 65, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.search_open_term_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.search_open_term_4.setGeometry(QtCore.QRect(560, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_open_term_4.setFont(font)
        self.search_open_term_4.setObjectName("search_open_term_4")
        self.label_83 = QtWidgets.QLabel(self.centralwidget)
        self.label_83.setGeometry(QtCore.QRect(450, 25, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.search_open_term_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.search_open_term_5.setGeometry(QtCore.QRect(560, 60, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.search_open_term_5.setFont(font)
        self.search_open_term_5.setObjectName("search_open_term_5")
        self.label_84 = QtWidgets.QLabel(self.centralwidget)
        self.label_84.setGeometry(QtCore.QRect(450, 65, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RST_TO_PPT"))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p>IHI QST #</p></body></html>"))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p>TIP FIX RST FILE <span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.tip_fix_file_path_browse.setText(_translate("MainWindow", "BROWSE RST FILE"))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">* All fields are mandatory</span></p></body></html>"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.process_rst_files.setText(_translate("MainWindow", "PROCESS RST FILES"))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p>TIP FREE RST FILE <span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.tip_free_file_path_browse.setText(_translate("MainWindow", "BROWSE RST FILE"))
        self.label_81.setText(_translate("MainWindow", "<html><head/><body><p>ENGINE #</p></body></html>"))
        self.label_82.setText(_translate("MainWindow", "<html><head/><body><p>STAGE #</p></body></html>"))
        self.label_83.setText(_translate("MainWindow", "<html><head/><body><p>USERNAME</p></body></html>"))
        self.label_84.setText(_translate("MainWindow", "<html><head/><body><p>MODEL #</p></body></html>"))
