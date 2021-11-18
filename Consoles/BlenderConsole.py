import sys

# Dependencies
paths = [r'C:\\Users\\etudiant\\PycharmProjects\\FirstProject\\venv\\Lib\\site-packages',
         r'C:\\Users\\etudiant\\PycharmProjects\\FirstProject']

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

import clear

clear.do('tools')
clear.do('engine')

import pathlib2
import importlib
from tools.ui import tool_window as tw

importlib.reload(tw)
t = tw.ToolWindow()
t.show()