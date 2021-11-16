import sys
import clear

clear.do('tools')
clear.do('engine')

# Dependencies
package_path = 'C:\\Users\\etudiant\\PycharmProjects\\FirstProject\\venv\\Lib\\site-packages'
sys.path.append(package_path)

# The Tool
sys.path.insert(0, 'C:\\Users\\etudiant\\PycharmProjects\\FirstProject')

import pathlib2
import importlib
from tools.ui import tool_window as tw

importlib.reload(tw)
t = tw.ToolWindow()
t.show()