from .matrix_calculations import multiply_matrix
from .object import Object

from math import sin, cos, radians, sqrt
from sys import exit
import turtle


class Camera:
    def __init__(self, screen=None, pen=None, location=[0, 0, 0], rotation=[0, 0, 0], offset=[0, 0, 0],
                 resolution=[600, 480], sensor_size=None, focal_length=0.1, skew=0, objects=[], vertex_size=3,
                 edge_size=3):

        if not isinstance(screen, turtle.TurtleScreen):
            print("Required argument `screen` of type `turtle.Screen()` is missing.")
            exit()
        if not isinstance(pen, turtle.Turtle):
            print("Required argument `pen` of type `turtle.Turtle()` is missing.")
            exit()
        if sensor_size is None:
            sensor_size = [resolution[0] / 10000, resolution[1] / 10000]

        self.screen = screen
        self.pen = pen

        self.locX, self.locY, self.locZ = location[0], location[1], location[2]
        self.rotX, self.rotY, self.rotZ = rotation[0], rotation[1], rotation[2]
        self.offsetX, self.offsetY, self.offsetZ = offset[0], offset[1], offset[2]
        self.rX, self.rY = resolution[0], resolution[1]
        self.sX, self.sY = sensor_size[0], sensor_size[1]
        self.focal_length = focal_length
        self.skew = skew

        self.objects = objects
        self.lastRender = []

        self.vertexSize = vertex_size
        self.edgeSize = edge_size

    def add_objects(self, objects):
        if isinstance(objects, list):
            for i in range(len(objects)):
                if isinstance(objects[i], Object):
                    if not self.objects.__contains__(objects[i]):
                        self.objects.append(objects[i])
        elif isinstance(objects, Object):
            if not self.objects.__contains__(objects):
                self.objects.append(objects)

    def remove_objects(self, objects):
        if isinstance(objects, list):
            for i in range(len(objects)):
                if self.objects.__contains__(objects[i]):
                    self.objects.remove(objects[i])
        elif self.objects.__contains__(objects):
            self.objects.remove(objects)

    def clear_objects(self):
        self.objects = []

    def setup_matrices(self):
        ml = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.locX, -self.locY, -self.locZ, 1]
        ]
        mrz = [
            [cos(radians(self.rotZ)), - sin(radians(self.rotZ)), 0, 0],
            [sin(radians(self.rotZ)), cos(radians(self.rotZ)), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        mry = [
            [cos(radians(self.rotY)), 0, sin(radians(self.rotY)), 0],
            [0, 1, 0, 0],
            [- sin(radians(self.rotY)), 0, cos(radians(self.rotY)), 0],
            [0, 0, 0, 1]
        ]
        mrx = [
            [1, 0, 0, 0],
            [0, cos(radians(self.rotX)), - sin(radians(self.rotX)), 0],
            [0, sin(radians(self.rotX)), cos(radians(self.rotX)), 0],
            [0, 0, 0, 1]
        ]
        mc = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.offsetX, -self.offsetY, -self.offsetZ, 1]
        ]
        ms = [
            [(self.focal_length * self.rX) / (2 * self.sX), self.skew, 0, 0],
            [0, (self.focal_length * self.rY) / (2 * self.sY), 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ]
        return ml, mrz, mry, mrx, mc, ms

    def setup_object_matrices(self, obj):
        rot = obj.rotation
        loc = obj.location
        morx = [
            [1, 0, 0, 0],
            [0, cos(radians(rot[0])), -sin(radians(rot[0])), 0],
            [0, sin(radians(rot[0])), cos(radians(rot[0])), 0],
            [0, 0, 0, 1]
        ]
        mory = [
            [cos(radians(rot[1])), 0, sin(radians(rot[1])), 0],
            [0, 1, 0, 0],
            [- sin(radians(rot[1])), 0, cos(radians(rot[1])), 0],
            [0, 0, 0, 1]
        ]
        morz = [
            [cos(radians(rot[2])), -sin(radians(rot[2])), 0, 0],
            [sin(radians(rot[2])), cos(radians(rot[2])), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        moloc = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [loc[0], loc[1], loc[2], 1]
        ]
        return morx, mory, morz, moloc

    def render(self, auto_draw=False):
        ml, mrz, mry, mrx, mc, ms = self.setup_matrices()
        result = []
        for i in range(len(self.objects)):
            result.append([])
            data = self.objects[i].vertices
            morx, mory, morz, moloc = self.setup_object_matrices(self.objects[i])
            for j in range(0, len(data)):
                d = [[data[j][0], data[j][1], data[j][2], 1]]
                result[i].append([])
                result[i][j] = multiply_matrix(d, morz)
                result[i][j] = multiply_matrix(result[i][j], mory)
                result[i][j] = multiply_matrix(result[i][j], morx)
                result[i][j] = multiply_matrix(result[i][j], moloc)
                result[i][j] = multiply_matrix(result[i][j], ml)
                result[i][j] = multiply_matrix(result[i][j], mrz)
                result[i][j] = multiply_matrix(result[i][j], mry)
                result[i][j] = multiply_matrix(result[i][j], mrx)
                result[i][j] = multiply_matrix(result[i][j], mc)
                result[i][j] = multiply_matrix(result[i][j], ms)
                mn = [
                    [1 / result[i][j][0][2], 0, 0, 0],
                    [0, 1 / result[i][j][0][2], 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]
                ]
                result[i][j] = multiply_matrix(result[i][j], mn)
                result[i][j] = [result[i][j][0][0], result[i][j][0][1], result[i][j][0][2]]
        self.lastRender = result
        if auto_draw is True:
            self.draw()

    def draw_vertex(self, x, y):
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.goto(x, y)

    def draw_edge(self, v1, v2):
        self.pen.penup()
        self.pen.goto(v1[0], v1[1])
        self.pen.pendown()
        self.pen.goto(v2[0], v2[1])

    def draw(self):
        self.pen.clear()
        for i in range(len(self.lastRender)):
            for j in range(len(self.lastRender[i])):
                self.pen.pensize(self.vertexSize)
                self.draw_vertex(self.lastRender[i][j][0], self.lastRender[i][j][1])
            edges = self.objects[i].edges
            for j in range(len(edges)):
                self.pen.pensize(self.edgeSize)
                self.draw_edge(self.lastRender[i][edges[j][0]], self.lastRender[i][edges[j][1]])
        self.screen.update()
