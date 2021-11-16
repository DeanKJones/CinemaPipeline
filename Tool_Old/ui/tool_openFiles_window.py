from Qt import QtWidgets, QtCompat
from pathlib import Path

ui_path = Path(__file__).parent / 'qt' / 'open_file_window.ui'

class ToolWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)
        self._connectUi()

    def _connectUi(self):
        self.openFiles_pb.clicked.connect(self.OpenFile)
        self.listFiles_container.clicked.connect()

    def OpenFile(self):
        print('Your wonderful File has been opened :)')

if __name__ == '__main__':

    from pathlib import Path
    current = Path(__file__).parent / 'qt' / 'open_file_window.ui'
    print(current)

    print('running')
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()


