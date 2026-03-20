class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  
  def getName(self):
    print(f"Name: {self.__name}")
  
  def getAge(self):
    print(f"Age: {self.__age}")
  
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
      print(f"{course} removed")
      return
    print(f"{course} is not in courses.")
    return
  
  def getCourses(self):
    for c in self.courses:
      print(f"- {c}")
  
  def __str__(self):
    return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"
  
class Instructor(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.__salary = salary
  
  def getSalary(self):
    print(f"Salary: {self.__salary}")
  
  def __str__(self):
    return f"Instructor(name={self.name}, age={self.age}, salary={self.__salary})"

class Course:
  def __init__(self, course_name):
    self.course_name = course_name
    self.students = []
  
  def searchStudent(self, student):
    for s in self.students:
      if s == student:
        return s

  def addStudent(self, student):
    s = self.searchStudent(student)
    if s:
      print(f"{student} already exist.")
      return
    self.students.append(student)
    print(f"{student} added.")
    return

  def dropStudent(self, student):
    s = self.searchStudent(student)
    if s:
      self.students.remove(s)
      print(f"{s} removed.")
      return
    print(f"{student} does not exist in students.")
    return
  
  def getNumberOfStudents(self):
    print(f"Number of students: {len(self.students)}")
  
class University: