class Object:
    def __init__(self, location=[0, 0, 0], rotation=[0, 0, 0], vertices=[], edges=[], faces=[]):
        self.location = [location[0], location[1], location[2]]
        self.rotation = [rotation[0], rotation[1], rotation[2]]

        self.vertices = vertices
        self.edges = edges
        self.faces = faces
