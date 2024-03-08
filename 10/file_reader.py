import os
from pathlib import Path

path = Path('./text/pi_digits.txt')
if(path.exists()):
    contents = path.read_text()
    print(contents)
    with open(path, 'r') as file:
        file.write('aa\n')
        file.write('aa')

