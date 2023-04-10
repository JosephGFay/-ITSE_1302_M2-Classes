from utils import Answer, Question, exercise

@exercise
def classes():
  
  # Question 1 
  class Rectangle:
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    # Question 2 
    def __init__(self, x1, y1, x2, y2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2

  # Question 3 
    def width(self):
      return self.x2 - self.x1

    def height(self):
      return self.y2 - self.y1

  # Question 4 
    def area(self):
      return self.width() * self.height()

  # Question 5 
    def circumference(self):
      return 2 * self.width() + 2 * self.height()

  # Question 6 
    def __str__(self):
      return f"({self.x1},{self.y1}) ({self.x2},{self.y2})"

  my_rect = Rectangle(0, 4, 6, 8)
  my_rect2 = Rectangle(0, 2, 5, 4)

  # Question 1
  Question(1, """
    Implement a class named 'Rectangle' to store the coordinates
    of a rectangle given by (x1, y1) and (x2,y2).
  """)
  Answer("Refer to code implementation")
  
  # Question 2
  Question(2, """
    Implement a class constructor with parameters (x1, y1, x2, y2) 
    and store them in the class instances using the self keyword.
  """)
  Answer("Refer to code implementation")
  
  # Question 3
  Question(3, """
    Implement the 'width()' and 'height()' methods which return 
    respectively the width and height of a rectangle. 
    Create two objects, instances of 'rectangle' to test the calculations.
  """)
  
  Answer(f"Rectangle Instance 1 width: {my_rect.width()}")
  Answer(f"Rectangle Instance 1 height: {my_rect.height()}")
  Answer(f"Rectangle Instance 2 width: {my_rect2.width()}")
  Answer(f"Rectangle Instance 2 height: {my_rect2.height()}")
  
  # Question 4
  Question(4, """
    Implement a method 'area' to return the area of the rectangle 
    (width*height)
  """)
  Answer(f'Rectangle area: {my_rect.area()}')
  
  # Question 5
  Question(5, """
    Implement the method 'circumference' to return the perimeter of the 
    rectangle 2*width + 2*height).
  """)
  Answer(f'Rectangle circumference: {my_rect.circumference()}')

  # Question 6
  Question(6, """
    Do a print of one of the objects created to test the class. 
    Implement the '__str__" method such that when youj print one 
    of the objects it prints the coordinates as (x1, y1)(x2,y2)
  """)
  Answer(f'Rectangle __str__:{my_rect}')
