from __future__ import print_function
import os
import pandas as pd
project_folder = "/media/minhkv/Data/HocTap/DaiHoc/MasterI/datasets_mica/Annotation_dataset"
spread_sheet_folder = os.path.join(project_folder, "spreadsheet")
name = "20171123_Hung_lan1_23-11-2017__11-05-57"
path = os.path.join(spread_sheet_folder, name + ".xlsx")
xl = pd.ExcelFile(path)
print(xl.sheet_names)
df = pd.read_excel(path)
print(df.head)