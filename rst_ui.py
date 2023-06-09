# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rst.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_80 = QtWidgets.QLabel(self.centralwidget)
        self.label_80.setGeometry(QtCore.QRect(20, 105, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.form_ihi_qst_num = QtWidgets.QLineEdit(self.centralwidget)
        self.form_ihi_qst_num.setGeometry(QtCore.QRect(130, 100, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.form_ihi_qst_num.setFont(font)
        self.form_ihi_qst_num.setObjectName("form_ihi_qst_num")
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(10, 320, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.tip_fix_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_fix_file_path.setEnabled(False)
        self.tip_fix_file_path.setGeometry(QtCore.QRect(180, 320, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_fix_file_path.setFont(font)
        self.tip_fix_file_path.setObjectName("tip_fix_file_path")
        self.tip_fix_file_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.tip_fix_file_path_browse.setGeometry(QtCore.QRect(560, 320, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.tip_fix_file_path_browse.setFont(font)
        self.tip_fix_file_path_browse.setObjectName("tip_fix_file_path_browse")
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setGeometry(QtCore.QRect(10, 554, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.reset_selections = QtWidgets.QPushButton(self.centralwidget)
        self.reset_selections.setGeometry(QtCore.QRect(170, 550, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.reset_selections.setFont(font)
        self.reset_selections.setObjectName("reset_selections")
        self.exit_app = QtWidgets.QPushButton(self.centralwidget)
        self.exit_app.setGeometry(QtCore.QRect(580, 550, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.exit_app.setFont(font)
        self.exit_app.setObjectName("exit_app")
        self.process_input_rst_files = QtWidgets.QPushButton(self.centralwidget)
        self.process_input_rst_files.setGeometry(QtCore.QRect(340, 550, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.process_input_rst_files.setFont(font)
        self.process_input_rst_files.setObjectName("process_input_rst_files")
        self.label_64 = QtWidgets.QLabel(self.centralwidget)
        self.label_64.setGeometry(QtCore.QRect(10, 370, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.tip_free_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_free_file_path.setEnabled(False)
        self.tip_free_file_path.setGeometry(QtCore.QRect(180, 370, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_free_file_path.setFont(font)
        self.tip_free_file_path.setObjectName("tip_free_file_path")
        self.tip_free_file_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.tip_free_file_path_browse.setGeometry(QtCore.QRect(560, 370, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.tip_free_file_path_browse.setFont(font)
        self.tip_free_file_path_browse.setObjectName("tip_free_file_path_browse")
        self.form_engine = QtWidgets.QLineEdit(self.centralwidget)
        self.form_engine.setGeometry(QtCore.QRect(130, 140, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.form_engine.setFont(font)
        self.form_engine.setObjectName("form_engine")
        self.label_81 = QtWidgets.QLabel(self.centralwidget)
        self.label_81.setGeometry(QtCore.QRect(20, 145, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.form_stage = QtWidgets.QLineEdit(self.centralwidget)
        self.form_stage.setGeometry(QtCore.QRect(400, 140, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.form_stage.setFont(font)
        self.form_stage.setObjectName("form_stage")
        self.label_82 = QtWidgets.QLabel(self.centralwidget)
        self.label_82.setGeometry(QtCore.QRect(320, 145, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.form_user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.form_user_name.setGeometry(QtCore.QRect(560, 100, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.form_user_name.setFont(font)
        self.form_user_name.setObjectName("form_user_name")
        self.label_83 = QtWidgets.QLabel(self.centralwidget)
        self.label_83.setGeometry(QtCore.QRect(450, 105, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.form_condition = QtWidgets.QLineEdit(self.centralwidget)
        self.form_condition.setGeometry(QtCore.QRect(560, 140, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.form_condition.setFont(font)
        self.form_condition.setObjectName("form_condition")
        self.label_84 = QtWidgets.QLabel(self.centralwidget)
        self.label_84.setGeometry(QtCore.QRect(450, 145, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 290, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 410, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_85 = QtWidgets.QLabel(self.centralwidget)
        self.label_85.setGeometry(QtCore.QRect(290, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_65 = QtWidgets.QLabel(self.centralwidget)
        self.label_65.setGeometry(QtCore.QRect(10, 440, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.template_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.template_path_browse.setGeometry(QtCore.QRect(560, 440, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.template_path_browse.setFont(font)
        self.template_path_browse.setObjectName("template_path_browse")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 530, 731, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.template_path = QtWidgets.QLineEdit(self.centralwidget)
        self.template_path.setEnabled(False)
        self.template_path.setGeometry(QtCore.QRect(180, 440, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.template_path.setFont(font)
        self.template_path.setObjectName("template_path")
        self.save_in_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.save_in_path_browse.setGeometry(QtCore.QRect(560, 490, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.save_in_path_browse.setFont(font)
        self.save_in_path_browse.setObjectName("save_in_path_browse")
        self.label_66 = QtWidgets.QLabel(self.centralwidget)
        self.label_66.setGeometry(QtCore.QRect(10, 490, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.save_in_path = QtWidgets.QLineEdit(self.centralwidget)
        self.save_in_path.setEnabled(False)
        self.save_in_path.setGeometry(QtCore.QRect(180, 490, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_in_path.setFont(font)
        self.save_in_path.setObjectName("save_in_path")
        self.tip_fix_extract_modes = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_fix_extract_modes.setGeometry(QtCore.QRect(220, 180, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_fix_extract_modes.setFont(font)
        self.tip_fix_extract_modes.setObjectName("tip_fix_extract_modes")
        self.label_86 = QtWidgets.QLabel(self.centralwidget)
        self.label_86.setGeometry(QtCore.QRect(20, 185, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.tip_free_extract_modes = QtWidgets.QLineEdit(self.centralwidget)
        self.tip_free_extract_modes.setGeometry(QtCore.QRect(650, 190, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tip_free_extract_modes.setFont(font)
        self.tip_free_extract_modes.setObjectName("tip_free_extract_modes")
        self.label_87 = QtWidgets.QLabel(self.centralwidget)
        self.label_87.setGeometry(QtCore.QRect(450, 195, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 230, 731, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_67 = QtWidgets.QLabel(self.centralwidget)
        self.label_67.setGeometry(QtCore.QRect(10, 250, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.ansys_path_browse = QtWidgets.QPushButton(self.centralwidget)
        self.ansys_path_browse.setGeometry(QtCore.QRect(560, 250, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.ansys_path_browse.setFont(font)
        self.ansys_path_browse.setObjectName("ansys_path_browse")
        self.ansys_path = QtWidgets.QLineEdit(self.centralwidget)
        self.ansys_path.setEnabled(False)
        self.ansys_path.setGeometry(QtCore.QRect(180, 250, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ansys_path.setFont(font)
        self.ansys_path.setObjectName("ansys_path")
        self.label_88 = QtWidgets.QLabel(self.centralwidget)
        self.label_88.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("image: url(:/ihi/ihi_logo.jpg)")
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.centralwidget)
        self.label_89.setGeometry(QtCore.QRect(570, 10, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("image: url(:/quest/quest_logo.jpg)")
        self.label_89.setObjectName("label_89")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Model Analysis"))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p>ECM # </p></body></html>"))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p>TIP FIX RST FILE</p></body></html>"))
        self.tip_fix_file_path.setText(_translate("MainWindow", "path...."))
        self.tip_fix_file_path_browse.setText(_translate("MainWindow", "BROWSE RST FILE"))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">* All fields are mandatory</span></p></body></html>"))
        self.reset_selections.setText(_translate("MainWindow", "RESET"))
        self.exit_app.setText(_translate("MainWindow", "EXIT"))
        self.process_input_rst_files.setText(_translate("MainWindow", "PROCESS RST FILES"))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p>TIP FREE RST FILE</p></body></html>"))
        self.tip_free_file_path.setText(_translate("MainWindow", "path...."))
        self.tip_free_file_path_browse.setText(_translate("MainWindow", "BROWSE RST FILE"))
        self.label_81.setText(_translate("MainWindow", "<html><head/><body><p>ENGINE #</p></body></html>"))
        self.label_82.setText(_translate("MainWindow", "<html><head/><body><p>STAGE #</p></body></html>"))
        self.label_83.setText(_translate("MainWindow", "<html><head/><body><p>USERNAME</p></body></html>"))
        self.label_84.setText(_translate("MainWindow", "<html><head/><body><p>CONDITION</p></body></html>"))
        self.label_85.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">MODEL ANALYSIS</span></p></body></html>"))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p>TEMPLATE PATH</p></body></html>"))
        self.template_path_browse.setText(_translate("MainWindow", "BROWSE PPT FILE"))
        self.template_path.setText(_translate("MainWindow", "path...."))
        self.save_in_path_browse.setText(_translate("MainWindow", "BROWSE FOLDER"))
        self.label_66.setText(_translate("MainWindow", "<html><head/><body><p>SAVE IN PATH</p></body></html>"))
        self.save_in_path.setText(_translate("MainWindow", "path...."))
        self.label_86.setText(_translate("MainWindow", "<html><head/><body><p>TIP FIX EXTRACT MODES #</p></body></html>"))
        self.label_87.setText(_translate("MainWindow", "<html><head/><body><p>TIP FREE EXTRACT MODES #</p></body></html>"))
        self.label_67.setText(_translate("MainWindow", "<html><head/><body><p>ANSYS PATH</p></body></html>"))
        self.ansys_path_browse.setText(_translate("MainWindow", "BROWSE ANSYS PATH"))
        self.ansys_path.setText(_translate("MainWindow", "path...."))
        self.label_88.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_89.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
