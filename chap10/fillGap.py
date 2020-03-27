#! python
# Finds all files with a certain prefix, locates any gaps in the numbering, and remaines the later files to match. 
# Example (the files in a folder):
# Before --> spam001.txt, spam002.txt, spam004.txt
# After --> spam001.txt, spam002.txt, spam003.txt

import os
from pathlib import Path
import pyinputplus as pyip
import shutil
import re

file_extension = pyip.inputStr("Enter a file extension you'd like to check (include the period): ")
file_prefix = pyip.inputStr("Enter the file prefix (e.g. the prefix for spam001.txt would be spam) for the files you want to check: ")
location = pyip.inputStr("Enter a folder you'd like to review: ")

location = os.path.abspath(location)

regex = re.compile(r"((%s)(\d+)(%s))" % (file_prefix, file_extension))

if Path(location).exists() == False:
    print(f"That {location} does not exist!")
else:
    
    # error is happening here because the list of files stay the same, so you have to update list or create a new list
    file_list = list(Path(location).glob(file_prefix + '*' + file_extension))
    file_list.sort()
    
    for i in range(len(file_list)):
        
        curr_filename = os.path.basename(file_list[i])
        
        if i + 1 <= len(file_list) - 1:
            next_filename = os.path.basename(file_list[i+1])
        else:
            break

        curr_match = regex.search(curr_filename)
        next_match = regex.search(next_filename)

        if (int(curr_match.group(3)) + 1 != int(next_match.group(3))) or (len(curr_match.group(3)) != len(next_match.group(3))):
            print(f'Renaming {next_filename} to...')

            # creating the new number and creating any leading zeroes that exist
            new_num = str(int(curr_match.group(3)) + 1).zfill(len(curr_match.group(3)))

            # new filename to replace the next filename
            new_filename = "%s%s%s" % (next_match.group(2), new_num, file_extension)

            # renaming the files
            shutil.move(next_filename, new_filename)

            # appending the new filename
            file_list[i+1] = new_filename


            print(f"{new_filename}")
        else:
            continue
