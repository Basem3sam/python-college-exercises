class Circle:
  def draw(self):
    print("Drawing a Circle")

class Square:
  def draw(self):
    print("Drawing a Square")

def shape_factory(shape_type):
  if shape_type.lower() == "circle":
    return Circle()
  elif shape_type.lower() == "square":
    return Square()
  else:
    raise ValueError("Unknown shape type")

# Test
shape = shape_factory("circle")
shape.draw()