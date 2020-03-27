import os, shutil, re
from pathlib import Path

fileRegex = re.compile(r"^(.*?)(0+)(\d*)(.*?)$")

for filename in os.listdir('.'):
    match = fileRegex.search(filename)

    if match == None:
        continue
    
    beforePart = match.group(1)
    zeroPart = match.group(2)
    numberPart = match.group(3)
    afterPart = match.group(4)

    print(f'Renaming {match.group(0)} to {beforePart}{numberPart}{afterPart}')
    previous_filename = Path(Path.cwd() / filename)
    new_filename = beforePart + numberPart + afterPart
    new_filename = Path(Path.cwd() / new_filename)

    shutil.move(previous_filename, new_filename)
