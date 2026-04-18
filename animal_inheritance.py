# Task 5: Demonstrate inheritance and polymorphism with Animal, Dog, and Cat classes.
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print("Animal make sound")

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)

  def speak(self):
    print(f"{self.name} says Hav hav") # If we wrote 'pass', it would inherit from Animal and print 'Animal make sound' when running the code.

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name)

  def speak(self):
    print(f"{self.name} says Meow")

'''
a = Animal("animal")
d = Dog("mike")
c = Cat("miyen")

a.speak()
d.speak()
c.speak()
# We could also run them one by one this way.
'''

# This method is called polymorphism
animals = [Dog("chris"), Cat("miyen"), Dog("mike")]

for a in animals:
  a.speak()