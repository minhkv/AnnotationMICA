from __future__ import print_function
import glob
import os
import numpy as np
import re


def get_list_file_txt(folder):
    list_file = glob.glob(os.path.join(folder, "*.txt"))
    return list_file
def read_line_in_file(path):
    try:
        action_list = []
        with open(path, 'r') as fp:
            for line in fp:
                action = line.strip().split(';')
                action = [s.replace('\xef\xbb\xbf', '') for s in action]
                action_list.append(action)
        return action_list
    except IOError as er:
        print("[Error] IOError: {}".format(er))
def convert_label(label, to_text=False):
    mapping = map_class_label
    if to_text:
        mapping = map_label_class
    for key, value in mapping.items():
        if key in label:
            return value
    raise ValueError('[Warning] Not have class: {}'.format(label))
def convert_list_action(list_action, to_text=False):
    converted_list_action = []
    for action in list_action:
        action[0] = convert_label(str(action[0]), to_text=to_text)
        action = [str(a) for a in action]
        action = ';'.join(action)
        converted_list_action.append(action)
    return converted_list_action
def save_converted_file(output_folder, filename, content):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(os.path.join(output_folder, filename), "w") as fp:
        for line in content:
            fp.write("{}\n".format(line))


map_class_label = {
    'walk': 1,
    'run_slowly': 2,
    'static_jump': 3,
    'move_hand_and_leg': 4,
    'left_hand_pick_up': 5,
    'right_hand_pick_up': 6,
    'stagger': 7,
    'front_fall': 8,
    'back_fall': 9,
    'left_fall': 10,
    'right_fall': 11,
    'crawl': 12,
    'sit_on_chair_then_stand_up': 13,
    'move_chair': 14,
    'sit_on_chair_then_fall_left': 15,
    'sit_on_chair_then_fall_right': 16,
    'sit_on_bed_and_stand_up': 17,
    'lie_on_bed_and_sit_up': 18,
    'lie_on_bed_and_fall_left': 19,
    'lie_on_bed_and_fall_right': 20
}  
map_label_class = {str(v): k for k, v in map_class_label.items()}