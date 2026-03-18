class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def getArea(self):
    return self.width * self.height
  def getPerimeter(self):
    return 2*self.width + 2*self.height

r1 = Rectangle(2, 4)
area1 = r1.getArea()
print(area1)
peri1 = r1.getPerimeter()
print(peri1)