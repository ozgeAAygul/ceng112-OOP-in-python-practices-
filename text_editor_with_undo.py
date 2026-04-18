# Task 8: Implement a TextEditor with undo and redo functionality using a Stack.
class Stack:
  def __init__(self):
    self.elements = []
  
  def isEmpty(self):
    return len(self.elements) == 0
  
  def push(self, element):
    self.elements.append(element)
  
  def pop(self):
    if self.isEmpty():
      return None
    return self.elements.pop()
  
class TextEditor:
  def __init__(self):
    self.text = ""
    self.undo_stack = Stack()
    self.redo_stack = Stack()
  
  def write(self, new_text):
    self.undo_stack.push(self.text)
    self.text += new_text
    self.redo_stack = Stack()

  def undo(self):
    if not self.undo_stack.isEmpty():
      self.redo_stack.push(self.text)
      self.text = self.undo_stack.pop()
    else:
      print("Nothing to undo")
  
  def redo(self):
    if not self.redo_stack.isEmpty():
      self.undo_stack.push(self.text)
      self.text = self.redo_stack.pop()
  
  def show(self):
    print(self.text)

editor = TextEditor()
editor.write("hello")
editor.write(" world")
editor.show()

editor.undo()
editor.show()

editor.redo()
editor.show()