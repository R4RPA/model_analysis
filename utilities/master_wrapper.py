import json
from utilities.extract_from_rst import extract_result_data
from utilities.create_result_ppt import create_result_ppt
import utilities.support_functions as sup_functions
import os


def process_rst_files(data_points):
    
    print(json.dumps(data_points,indent=2))
    
    """Initiate variables"""
    tip_fix_rst_filename = data_points['tip_fix_rst_filename']
    tip_fix_extract_modes = int(data_points['tip_fix_extract_modes'])
    tip_free_rst_filename = data_points['tip_free_rst_filename']
    tip_free_extract_modes = int(data_points['tip_free_extract_modes'])
    result_images_folder = data_points['output_path']
    template_path = data_points['template_path']
    output_path = data_points['output_path']

    """get modes, frequencies, result images from ansys results rst file"""
    tip_fix_results_list = []
    tip_free_results_list = []
    if len(tip_fix_rst_filename) > 0:
        tip_fix_results_list = extract_result_data(tip_fix_rst_filename, 'tip_fix', tip_fix_extract_modes, result_images_folder)
    if len(tip_free_rst_filename) > 0:
        tip_free_results_list = extract_result_data(tip_free_rst_filename, 'tip_free', tip_free_extract_modes, result_images_folder)

    """Check number of modes / results found in each restult file"""
    print('tip_fix_results_list', len(tip_fix_results_list))
    print('tip_free_results_list', len(tip_free_results_list))

    """Create results report using the template given"""
    result_dict = {'data': data_points['data'],
                   'tip_fix_list': tip_fix_results_list,
                   'tip_free_list': tip_free_results_list
                   }

    print('result_dict', json.dumps(result_dict, indent=2))
    create_result_ppt(template_path, output_path, result_dict)
    delete_result_images(tip_fix_results_list)
    delete_result_images(tip_free_results_list)

def delete_result_images(image_list):
    for result in image_list:
        file_path = result['image']
        sup_functions.delete_file(file_path)

def main():
    """set folder to store results images and results"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    template_path = os.path.join(root_dir, 'data/template/modal_analysis_final_report_template.pptx')
    output_path = os.path.join(root_dir, 'data/output_reports')

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    tip_fix_rst_filename = os.path.join(root_dir, 'data/rst_file/result_file.rst')
    tip_free_rst_filename = os.path.join(root_dir, 'data/rst_file/result_file.rst')

    data_points = {'tip_fix_rst_filename': tip_fix_rst_filename, 
                   'tip_free_rst_filename': tip_free_rst_filename, 
                   'ansys_path': '', 
                   'template_path': template_path, 
                   'output_path': output_path, 
                   'tip_fix_extract_modes': '8', 
                   'tip_free_extract_modes': '8',
                   'data': {
                       'ECM_Num': 'IHIQST-23-1234', 
                       'EngineProg': 'ENG01', 
                       'StageNum': '5B', 
                       'Condition': 'COLD', 
                       'UserName': 'RAGHU'
                       }
                   }
    process_rst_files(data_points)
    print('Check : ', output_path, 'for reports')


if __name__ == '__main__':
    main()
