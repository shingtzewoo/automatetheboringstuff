#! python
# this program walks through folder tree and searches for files with specific extensions (chosen by user) to copy into a new folder

# Usage: python3 selectiveCopy.py

import os
import shutil
import pyinputplus as pyip
from pathlib import Path

file_extension = pyip.inputStr("Enter a file extension (include the period): ")
location = pyip.inputStr("Enter a folder you'd like to copy these files from: ")
new_folder = pyip.inputStr("Enter a folder you'd like to copy these files to: ")

new_folder = os.path.abspath(new_folder)
location = os.path.abspath(location)

if Path(new_folder).exists() == False or Path(location).exists() == False:
    print('Folder does not exist, please choose valid location(s).')
else:
    for foldername, subfolders, filenames in os.walk(location):
        for filename in filenames:
            if file_extension in os.path.basename(os.path.abspath(filename)):
                print(f'Copying {filename} to {new_folder}.')
                shutil.copy(os.path.abspath(os.path.join(foldername,filename)), new_folder)
            else:
                continue