# Task 9: Implement a basic Queue data structure.
class Queue:
  def __init__(self):
    self._data = []
  
  def enqueue(self, value):
    self._data.append(value)
  
  def dequeue(self):
    if self.is_empty():
      return None
    return self._data.pop(0)
  
  def first(self):
    if self.is_Empty():
      return None
    return self._data[0]
