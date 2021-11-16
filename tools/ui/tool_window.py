import os
import six

from Qt import QtCompat, QtWidgets, QtCore

import engine
from tools import datas

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

ui_path = Path(__file__).parent / 'qt' / 'Window.ui'
UserRole = QtCore.Qt.UserRole


class ToolWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.load_ui(str(ui_path), self)
        self.engine = engine.get_engine()
        self.load_ui()

        for f in datas.get_files():
            add_list_widget_item(self.listItems, f, os.path.basename(f))

    def load_ui(self):
        button_list = {}
        self.buttons = engine.get_engine().buttons
        for key, value in self.buttons.items():
            button = QtWidgets.QPushButton(value)
            button.setObjectName(key)
            button.setText(value)

            self.ButtonLayout.addWidget(button)
            button.clicked.connect(self.get_func)
            button_list[key] = button

    def get_func(self):
        clicked_button = self.sender().objectName()
        func_name = None
        for func in dir(ToolWindow):
            current_button = clicked_button.split('_')[0]
            split_func = func.split('_')[0]
            if current_button.lower() == split_func.lower():
                func_name = func

        function = getattr(ToolWindow, func_name)
        function(self)

    def open_file(self):
        item = self.listItems.currentItem()
        path = item.data(UserRole)
        self.engine.open(path)

        print('\nExecuted:\n' + '{} -> {}'.format(item.text(), path))
        print(path)
        print(item.text() + '\n')

    def save_file(self):
        item = self.listItems.currentItem()
        self.engine.save(self, item.text())

        print("Your File Has Been Saved")

    def link_file(self):
        item = self.listItems.currentItem()
        path = item.data(UserRole)
        self.engine.link(path)


def add_list_widget_item(listWidget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    listWidget.addItem(item)
    return item


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()

