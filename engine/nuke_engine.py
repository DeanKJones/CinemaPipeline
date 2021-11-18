import os.path
import nuke


class NukeEngine:

    # Needed Buttons
    buttons = {
        "Save_PB": "Save",
        "Open_PB": "Open",
        "Link_PB": "Link"
        }

    def open(self):
        nuke.scriptOpen(self)

    def save(self):
        print("file Saved")

    def link(self):
        pass

if __name__ == '__main__':
    pass