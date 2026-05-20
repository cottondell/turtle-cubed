# Camera class
- `Camera(screen=None, pen=None, location=[0, 0, 0], rotation=[0, 0, 0], offset=[0, 0, 0], resolution=[600, 480], sensor_size=None, focal_length=0.1, skew=0, objects=[myObject], vertex_size=3, edge_size=3)`
- `add_objects(obj)`
  - `obj` is an instance of `Object` or a list of `Object` instances
- `remove_objects(obj)`
  - `obj` is an instance of `Object` or a list of `Object` instances
- `clear_objects()`
- `render(auto_draw=True/False)`

# Object class
- `Object(self, location=[0, 0, 0], rotation=[0, 0, 0], vertices=[], edges=[], faces=[])`
