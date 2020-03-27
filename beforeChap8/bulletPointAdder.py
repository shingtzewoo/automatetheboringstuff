#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
#text = pyperclip.paste()
text = '''
Hey there
Yo
'''

lines = text.strip('\n').split('\n')
for index, value in enumerate(lines):    # loop through all indexes in the "lines" list
    lines[index] = '* ' + lines[index] # add star to each string in "lines" list

text = '\n'.join(lines)
print(text)

#pyperclip.copy(text)