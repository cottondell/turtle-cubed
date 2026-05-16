from .context import *

# Configure turtle screen
screen = turtle.Screen()
screen.tracer(0)

# Configure turtle pen
pen = turtle.Turtle()
pen.hideturtle()

# Initialise 3d camera
camera = Camera(screen=screen, pen=pen, location=[0, 0, 0], rotation=[0, 0, 0], offset=[0, 0, 5], vertex_size=5, edge_size=1)

# Functions
def render_loop():
    camera.render(auto_draw=True)
    screen.ontimer(render_loop, round(1000 / 60))  # 1000ms / 60 = frame rate

def rotate_left():
    camera.rotY -= 1

def rotate_right():
    camera.rotY += 1

# Define cube object
v = [[-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1], [-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1]]
e = [[0, 1], [0, 2], [2, 3], [1, 3], [0, 4], [1, 5], [2, 6], [3, 7], [4, 5], [4, 6], [6, 7], [5, 7]]
cube = Object(location=[0, 0, 0], rotation=[0, 0, 0], vertices=v, edges=e)
camera.add_objects(cube)

# Start camera render loop
render_loop()

# Configure input listeners
turtle.listen()
turtle.onkeypress(rotate_left, "Left")
turtle.onkeypress(rotate_right, "Right")

# Enter turtle screen mainloop
screen.mainloop()
