class Person:
  def __init__(self, name):
    self.name = name

  def introduce(self):
    print(f"Hi, I'm {self.name}") 

  def __str__(self):
    return f"Person(name={self.name})"

class Student(Person):
  def __init__(self, name, grade):
    super().__init__(name)
    self.grade = grade

  def introduce(self): #override örneği
    print(f"Hi, I'm {self.name} and my grade is {self.grade}")
  
  def __str__(self):
    return f"Student(name={self.name}, grade={self.grade})"

  def __eq__(self, other):
    if not isinstance(other, Student):
      return False
    return self.name == other.name and self.grade == other.grade

#bunun gibi person olan spesifik classlar türetebilirsiniz
class Teacher(Person):
  def __init__(self, name, salary):
    super().__init__(name)
    self.salary = salary
  
  def introduce(self):
    print(f"Hi, my name is {self.name}, I'm teacher and my salary is {self.salary}")
  
  def __str__(self):
    return f"Teacher(name={self.name}, salary={self.salary})"

#bu da polymorphism
def printInfo(person):
  person.introduce()

p1 = Person("Ruya")
s1 = Student("Ozge", 45)
s2 = Student("Ozge", 45)
printInfo(p1)
printInfo(s1)

print(s1 == s2)
print(p1 == s1)