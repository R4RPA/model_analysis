#pyinstaller --onefile --windowed --paths Lib\site-packages -i "icon.ico" app.py

import sys
import json
from PyQt5 import QtWidgets
from utilities.master_wrapper import process_rst_files
from rst_ui import Ui_MainWindow
import datetime


class UiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiWindow, self).__init__()
        """Initiate GUI Window"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_tab_order()
        
        """On Click and On Change Actions"""
        self.ui.tip_fix_file_path_browse.clicked.connect(self.tip_fix_file_path_browse)
        self.ui.tip_free_file_path_browse.clicked.connect(self.tip_free_file_path_browse)
        
        self.ui.template_path_browse.clicked.connect(self.template_path_browse)
        self.ui.save_in_path_browse.clicked.connect(self.save_in_path_browse)
        self.ui.ansys_path_browse.clicked.connect(self.ansys_path_browse)
        
        self.ui.process_input_rst_files.clicked.connect(self.process_input_rst_files)
        self.ui.reset_selections.clicked.connect(self.reset_selections)
        self.ui.exit_app.clicked.connect(self.close)
        

    def browse_folder(self):
        """Browse for Folder """
        return QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', '')
    
    def browse_file(self):
        """Browse for File"""
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*)')[0]

    def tip_fix_file_path_browse(self):
        """Browse for input file"""
        file_path = self.browse_file()
        self.ui.tip_fix_file_path.setText(file_path)
        self.ui.tip_fix_file_path.setToolTip(file_path)

    def tip_free_file_path_browse(self):
        """Browse for input file"""
        file_path = self.browse_file()
        self.ui.tip_free_file_path.setText(file_path)
        self.ui.tip_free_file_path.setToolTip(file_path)

    def template_path_browse(self):
        """Browse for template file"""
        file_path = self.browse_file()
        self.ui.template_path.setText(file_path)
        self.ui.template_path.setToolTip(file_path)
        
    def save_in_path_browse(self):
        """Browse for folder to save output file"""
        file_path = self.browse_folder()
        self.ui.save_in_path.setText(file_path)
        self.ui.save_in_path.setToolTip(file_path)
        
    def ansys_path_browse(self):
        """Browse for ansys application"""
        file_path = self.browse_file()
        self.ui.ansys_path.setText(file_path)
        self.ui.ansys_path.setToolTip(file_path)
        
    def reset_selections(self):
        """Reset all extract xlife form fields to default status"""
        self.ui.form_ihi_qst_num.setText("")
        self.ui.form_engine.setText("")
        self.ui.form_stage.setText("")
        self.ui.form_condition.setText("")
        self.ui.form_user_name.setText("")
        self.ui.tip_fix_extract_modes.setText("")
        self.ui.tip_free_extract_modes.setText("")
        self.ui.tip_fix_file_path.setText("path....")
        self.ui.tip_free_file_path.setText("path....")
        self.ui.template_path.setText("path....")
        self.ui.save_in_path.setText("path....")
        self.ui.ansys_path.setText("path....")
        self.ui.statusbar.showMessage('')
        
    def process_input_rst_files(self):
        """Initiate master wrapper script to process rst file"""
        self.ui.statusbar.showMessage('')
        input_params = self.get_input_params()
        if input_params:
            process_rst_files(data_points=input_params)
            self.ui.statusbar.showMessage('Check SAVE_IN_PATH folder for reports')
        
    def get_input_params(self):
        """read data from form fields"""
        form_ihi_qst_num = self.ui.form_ihi_qst_num.text()
        form_engine = self.ui.form_engine.text()
        form_stage = self.ui.form_stage.text()
        form_condition = self.ui.form_condition.text()
        form_user_name = self.ui.form_user_name.text()
        tip_fix_extract_modes = self.ui.tip_fix_extract_modes.text()
        tip_free_extract_modes = self.ui.tip_free_extract_modes.text()
        tip_fix_file_path = self.ui.tip_fix_file_path.text()
        tip_free_file_path = self.ui.tip_free_file_path.text()
        template_path = self.ui.template_path.text()
        save_in_path = self.ui.save_in_path.text()
        ansys_path = self.ui.save_in_path.text()
        tip_fix_file_path = tip_fix_file_path if tip_fix_file_path != "path...." else ""
        tip_free_file_path = tip_free_file_path if tip_free_file_path != "path...." else ""
        template_path = template_path if template_path != "path...." else ""
        save_in_path = save_in_path if save_in_path != "path...." else ""
        ansys_path = ansys_path if ansys_path != "path...." else ""
        
        data_points = {
            'tip_fix_rst_filename': tip_fix_file_path,
            'tip_free_rst_filename': tip_free_file_path,
            'ansys_path': ansys_path,
            'template_path': template_path,
            'output_path': save_in_path,
            'tip_fix_extract_modes':tip_fix_extract_modes,
            'tip_free_extract_modes':tip_free_extract_modes
            }
        
        data_points1 = {
            '{ECM_Num}': form_ihi_qst_num,
            '{EngineProg}': form_engine,
            '{StageNum}': form_stage,
            '{Condition}': form_condition,
            '{Date}': datetime.date.today().strftime("%d-%m-%Y"),
            '{UserName}': form_user_name
            }
            
        missing_fields = self.validate_datapoints(data_points1)
        missing_fields += self.validate_datapoints(data_points)
        
        if missing_fields != '':
            self.ui.statusbar.showMessage('Missing Values: ' + missing_fields)
        else:
            data_points.update({'data': data_points1})
            
        return data_points if missing_fields == '' else {}
        
    def validate_datapoints(self, data_dict):
        """Validate input params to check if any blank fields"""
        missing_fields = ''
        for key in data_dict:
            val = data_dict[key]
            if len(val) == 0:
                missing_fields += key + ', '
        return missing_fields

    def set_tab_order(self):
        """Set tab index order to navigate between fields with tab"""
        self.ui.form_ihi_qst_num.setFocus()
        QtWidgets.QWidget.setTabOrder(self.ui.form_ihi_qst_num, self.ui.form_user_name)
        QtWidgets.QWidget.setTabOrder(self.ui.form_user_name, self.ui.form_engine)
        QtWidgets.QWidget.setTabOrder(self.ui.form_engine, self.ui.form_stage)
        QtWidgets.QWidget.setTabOrder(self.ui.form_stage, self.ui.form_condition)
        QtWidgets.QWidget.setTabOrder(self.ui.form_condition, self.ui.tip_fix_extract_modes)
        QtWidgets.QWidget.setTabOrder(self.ui.tip_fix_extract_modes, self.ui.tip_free_extract_modes)
        QtWidgets.QWidget.setTabOrder(self.ui.tip_free_extract_modes, self.ui.ansys_path_browse)
        QtWidgets.QWidget.setTabOrder(self.ui.ansys_path_browse, self.ui.tip_fix_file_path_browse)
        QtWidgets.QWidget.setTabOrder(self.ui.tip_fix_file_path_browse, self.ui.tip_free_file_path_browse)
        QtWidgets.QWidget.setTabOrder(self.ui.tip_free_file_path_browse, self.ui.template_path_browse)
        QtWidgets.QWidget.setTabOrder(self.ui.template_path_browse, self.ui.save_in_path_browse)
        QtWidgets.QWidget.setTabOrder(self.ui.save_in_path_browse, self.ui.process_input_rst_files)
        QtWidgets.QWidget.setTabOrder(self.ui.process_input_rst_files, self.ui.reset_selections)
        QtWidgets.QWidget.setTabOrder(self.ui.reset_selections, self.ui.exit_app)
        QtWidgets.QWidget.setTabOrder(self.ui.exit_app, self.ui.form_ihi_qst_num)
        
        
def create_app():
    """Initiate PyQT Application"""
    app = QtWidgets.QApplication(sys.argv)
    win = UiWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    create_app()
