import os
import sys


def get_engine():
    basename = os.path.basename(sys.executable)
    current_engine = basename.split('.')[0]

    print("basename: " + basename)
    print("current engine: " + current_engine)

    if current_engine == 'maya':
        import engine.maya_engine as engi
        return engi.MayaEngine

    elif 'houdini' in sys.executable:
        import engine.houdini_engine as engi
        return engi.HoudiniEngine

    elif 'Nuke' in sys.executable:
        import engine.nuke_engine as engi
        return engi.NukeEngine

    elif 'blender' in sys.executable:
        import engine.blender_engine as engi
        return engi.BlenderEngine
