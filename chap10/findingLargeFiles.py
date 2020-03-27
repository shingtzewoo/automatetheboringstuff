#! python
# This program walks through a folder, subfolders, and files to check which files are above 100MB and lists those out
# Usage: python3 findingLargeFiles.py

import os
from pathlib import Path
import pyinputplus as pyip

print("Usage: python3 findingLargeFiles.py")

location = pyip.inputStr("Enter location of the folder you want to check: ")
location = os.path.abspath(location)

if Path(location).exists() == False:
    print("The location does not exist")

tally_size = 0
large_files = []

for foldername, subfolders, filenames in os.walk(location):
    
    for filename in filenames:
        
        file_size = os.path.getsize(os.path.abspath(os.path.join(foldername, filename)))
        
        tally_size += file_size

        if file_size < 100000000:
            print(f"The size of {filename} in {foldername} is: {file_size}. It isn't very big.")
        else:
            print(f"The size of {filename} in {foldername} is: {file_size}. This file is very big.")
            large_files.append(os.path.abspath(os.path.join(foldername, filename)))

if not large_files:
    print("You have no large files!")
else:
    separator = ', '
    print(f"If you want to free up space, consider removing the following files: {separator.join(large_files)}")

print(f"The total size of your folder is: {tally_size}")



    

        