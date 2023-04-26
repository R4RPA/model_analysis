import os
from ansys.mapdl import reader as pymapdl_reader
import json


def extract_result_data(rst_filename, rst_type, extract_modes, result_images_folder):
    print('rst_filename', rst_filename)
    """Read ansys results rst file"""
    result = pymapdl_reader.read_binary(rst_filename)

    """Loop each result and extract frequency and result image"""
    results_list = []
    for mode in range(min(extract_modes, result.nsets)):
        mode_frequency = result.time_values[mode]
        img_path = os.path.join(result_images_folder, f'{rst_type}_mode_fig_{mode}.png')
        result.plot_nodal_solution(mode, show_edges=True, window_size=[800, 600],
                                   off_screen=True, screenshot=img_path, add_text=True)
        result_dict = {"mode": mode+1,
                       "frequency": round(mode_frequency, 2) if isinstance(mode_frequency, float) else "-",
                       "image": img_path}
        results_list.append(result_dict)
    return results_list


def main():
    """set folder to store results images"""
    result_images_folder = os.path.join(os.getcwd(), '../data/result_images')
    if not os.path.exists(result_images_folder):
        os.makedirs(result_images_folder)

    rst_filename = '../data/rst_file/result_file.rst'
    rst_type = 'tip_fix'
    # rst_type = 'tip_free'
    extract_modes = 4
    results_list = extract_result_data(rst_filename, rst_type, extract_modes, result_images_folder)
    print(json.dumps(results_list, indent=2))


if __name__ == '__main__':
    main()

