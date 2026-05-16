from .context import *

screen = turtle.Screen()
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()

v = [[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1], [-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1]]
e = [[0, 1], [0, 2], [2, 3], [1, 3], [0, 4], [1, 5], [2, 6], [3, 7], [4, 5], [4, 6], [6, 7], [5, 7]]
a = Object(location=[0, 0, 0], rotation=[0, 0, 0], vertices=v, edges=e)

mainCamera = Camera(screen=screen, pen=pen, location=[0, 0, 0], rotation=[0, 0, 0], offset=[0, 0, 5], objects=[a],
                    vertex_size=5, edge_size=1)
mainCamera.render(auto_draw=True)

def rotate_loop():
    mainCamera.rotY += 0.5
    mainCamera.render(auto_draw=True)
    screen.ontimer(rotate_loop, round(1000 / 60))  # 1000ms / 60 = frame rate

rotate_loop()

screen.mainloop()
