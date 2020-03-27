import sys, os, re

import pyinputplus as pyip

from pathlib import Path

user_input = pyip.inputStr("Type in your regex: ")
regex = re.compile(r'%s' % user_input)

matches = []

p = Path(Path.cwd())
textfile_list = list(p.glob("*.txt"))

for textfile in textfile_list:
    my_content = open(textfile, 'r')
    lines = my_content.readlines()
    for line in lines:
        mo = regex.findall(line)
        if not mo:
            continue
        else:
            matches.append(mo)

for index, value in enumerate(matches):
    matches[index] = ' '.join(matches[index])
    print(matches[index])