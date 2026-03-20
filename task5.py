class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print("Animal make sound")

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)

  def speak(self):
    print(f"{self.name} says Hav hav") # eğer pass yazsaydık animaldan alacaktı ve kodu çalıştırdığımızda terminalde animal make sound yazısını görcektik.

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
bu şekilde de tek tek çalıştırabilirdik.
'''

#Bu yöntem polymorphism olarak adlandırılır
animals = [Dog("chris"), Cat("miyen"), Dog("mike")]

for a in animals:
  a.speak()