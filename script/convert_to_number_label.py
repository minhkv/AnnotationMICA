from __future__ import print_function
from utils import *
import os

def convert_to_number_label(kinect_num):
    print("[Kinect] {}".format(kinect_num))
    input_txt = os.path.join(project_folder, "text_label", kinect_num)
    output_txt = os.path.join(project_folder, "number_label", kinect_num)

    if not os.path.exists(output_txt):
        os.makedirs(output_txt)

    list_txt = get_list_file_txt(input_txt)

    for input_file in list_txt:
        if "eadme." in input_file or "mapping" in input_file:
            continue
        print ("[Convert] Converting: {}".format(os.path.basename(input_file)))
        list_action = read_line_in_file(input_file)
        list_action = convert_list_action(list_action, to_text=False)
        save_converted_file(output_txt, os.path.basename(input_file), list_action)
    # print(list_action)
project_folder = "/media/minhkv/Data/HocTap/DaiHoc/MasterI/datasets_mica/Annotation_dataset"
kinect_num = "Kinect3"   
list_kinect = os.listdir(os.path.join(project_folder, "text_label"))
print(list_kinect)
for kinect_num in list_kinect:
    convert_to_number_label(kinect_num)
