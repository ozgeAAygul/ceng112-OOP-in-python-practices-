class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  
  def getName(self):
    return self.__name
  
  def getAge(self):
    return self.__age
  
  def __str__(self):
    return f"Person(name={self.__name}, age={self.__age})"

  def __eq__(self, other):
    if not isinstance(other, Person):
      return False
    return self.__name == other.__name and self.__age == other.__age

class Student(Person):
  def __init__(self, name, age, student_id):
    super().__init__(name, age)
    self.__student_id = student_id
    self.courses = []
  
  def searchCourse(self, course):
    for c in self.courses:
      if c.lower() == course.lower():
        return c
    return None
  
  def addCourse(self, course):
    c = self.searchCourse(course)
    if c:
      print(f"{course} already exist.")
      return
    self.courses.append(course)
    print(f"{course} added.")
  
  def dropCourse(self, course):
    c = self.searchCourse(course)
    if c:
      self.courses.remove(course)
      print(f"{course} removed.")
      return
    print(f"{course} is not in courses.")
    return
  
  def getCourses(self):
    return self.courses
  
  def __str__(self):
    return f"Student(name={self.getName()}, age={self.getAge()}, student_id={self.__student_id})"
  
class Instructor(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.__salary = salary
  
  def getSalary(self):
    return self.__salary
  
  def __str__(self):
    return f"Instructor(name={self.getName()}, age={self.getAge()}, salary={self.__salary})"

class Course:
  def __init__(self, course_name):
    self.course_name = course_name
    self.students = []
  
  def searchStudent(self, student):
    for s in self.students:
      if s == student:
        return s
    return None

  def addStudent(self, student):
    s = self.searchStudent(student)
    if s:
      print(f"{student.getName()} already exist.")
      return
    self.students.append(student)
    print(f"{student.getName()} added.")
    return

  def dropStudent(self, student):
    s = self.searchStudent(student)
    if s:
      self.students.remove(s)
      print(f"{s.getName()} removed.")
      return
    print(f"{student.getName()} does not exist in students.")
    return
  
  def getNumberOfStudents(self):
    print(f"Number of students: {len(self.students)}")
  
class University:
  def __init__(self):
    self.people = []
  
  def addPerson(self, person):
    self.people.append(person)
  
  def printAllPeople(self):
    for person in self.people:
      print(person)

class Stack:
  def __init__(self):
    self.__elements = []
  
  def isEmpty(self):
    return len(self.__elements) == 0

  def push(self, value):
    self.__elements.append(value)
  
  def pop(self):
    if self.isEmpty():
      return None
    return self.__elements.pop()
  
  def peek(self):
    if self.isEmpty():
      return None
    return self.__elements[-1]
  
  def getSize(self):
    return len(self.__elements)

def countStudents(people):
  count = 0
  for p in people:
    if isinstance(p, Student):
      count += 1
  return count  

s1 = Student("Ozge", 19, 1)
s2 = Student("Ruya", 21, 2)
i1 = Instructor("Isil", 40, 90000)
c1 = Course("Calculus1")

students = [s1, s2]
people = students + [i1]

for student in students:
  c1.addStudent(student)

uni = University()

for person in people:
  uni.addPerson(person)

uni.printAllPeople()
count = countStudents(people)
print(count)

print(s1 == s2)
print(i1.getSalary())