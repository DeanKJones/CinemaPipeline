from Qt import QtWidgets, QtCompat
from pathlib import Path

abs_ui_path = '/Tool_Old/ui/qt/window.ui'
ui_path = Path(__file__).parent / 'qt' / 'window.ui'

class ToolWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToolWindow, self).__init__()
        #QtCompat.loadUi(abs_ui_path, self)
        QtCompat.loadUi(str(ui_path), self)
        self._connectUi()

    def _connectUi(self):
        self.save_pb.clicked.connect(self.fileSaved)

    def fileSaved(self):
        print('you saved it good job! :)')

if __name__ == '__main__':

    # Boomer Way
    import os
    current = os.path.dirname(__file__)
    new = f'{current}/qt/window.ui'
    print(new)

    # Modern Way
    from pathlib import Path
    current = Path(__file__).parent / 'qt' / 'window.ui'
    print(current)

    print('running')
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()


