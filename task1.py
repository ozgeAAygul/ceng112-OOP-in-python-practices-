class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printInfo(self):
    print(f"{self.name} is {self.age} years old.")

s1 = Student("Özge", 19)
s1.printInfo()