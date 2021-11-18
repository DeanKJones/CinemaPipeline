import os.path
import maya.cmds as cmds


class MayaEngine:

    # Needed Buttons
    buttons = {
        "Save_PB": "Save",
        "Open_PB": "Open",
        "Link_PB": "Reference"
        }

    def open(self):
        cmds.file(self, open=True, f=True)

    def save(self, file):

        # TODO: Have the tool window update when a file is saved
        # Increments and Saves files

        filepath = os.path.dirname(cmds.file(q=True, expandName=True))

        filename = file.split('.')[0]
        filenameonly = filename.split('_')[0]

        filenumber = filename.split('_')[1]
        filenumber = int(filenumber) + 1
        filenumber = '{:03}'.format(filenumber)

        newfilename = (filenameonly + "_" + str(filenumber))
        newfilepath = filepath + "/" + newfilename

        cmds.file(rename=newfilepath)
        cmds.file(save=True, type="mayaBinary")

    def link(self):
        cmds.file(self, reference=True)
        print("File has been referenced")

if __name__ == '__main__':
    pass