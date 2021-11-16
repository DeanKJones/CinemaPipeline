import os
import sys


def get_engine():
    basename = os.path.basename(sys.executable)
    current_engine = basename.split('.')[0]

    if current_engine == 'maya':
        import engine.maya_engine as engi
        return engi.MayaEngine

    elif current_engine == 'houdini':
        import engine.houdini_engine as engi
        return engi.houdiniEngine
