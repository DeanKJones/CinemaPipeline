import hou
import os.path

class houdiniEngine:

    # Needed Buttons
    buttons = {
        "Save_PB": "Save",
        "Open_PB": "Open",
        "Link_PB": "Merge"
        }

    def open(self):
        hou.hipFile.load(self, suppress_save_prompt=True)

    def save(self, file):
        filepath = os.path.dirname(hou.hipFile.path())
        print(filepath)

        filename = file.split('.')[0]
        filenameonly = filename.split('_')[0]

        filenumber = filename.split('_')[1]
        filenumber = int(filenumber) + 1
        filenumber = '{:03}'.format(filenumber)

        newfilename = (filenameonly + "_" + str(filenumber))
        newfilepath = filepath + "/" + newfilename + ".hipnc"
        print(newfilename)
        print(newfilepath)

        hou.hipFile.save(file_name=newfilepath)

    def link(self):
        hou.hipFile.merge(self, node_pattern="*")
        print("File has been merged")

if __name__ == '__main__':
    pass