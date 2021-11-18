import bpy
import os.path


class BlenderEngine:

    # Needed Buttons
    buttons = {
        "Save_PB": "Save",
        "Open_PB": "Open",
        "Link_PB": "Merge"
        }

    def open(self):
        bpy.ops.wm.open_mainfile(filepath=self)

    def save(self):
        pass

    def link(self):
        pass


if __name__ == '__main__':
    pass