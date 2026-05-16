# Import pyrender3d classes
try:
    from ..camera import Camera
    from ..object import Object
except ImportError:
    from pyrender3d import Camera
    from pyrender3d import Object

# Other imports
import turtle