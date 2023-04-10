from utils import Answer, Question, exercise

class Rectangle:
  x1 = None
  y1 = None
  x2 = None
  y2 = None

  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

  def width(self):
    return self.x2 - self.x1

  def height(self):
    return self.y2 - self.y1

  def area(self):
    return self.width() * self.height()

  def circumference(self):
    return 2 * self.width() + 2 * self.height()

  def __str__(self):
    return f"({self.x1},{self.y1}) ({self.x2},{self.y2})"

@exercise
def inheritance():

  # Question 1
  Question(1, """
    Create a 'Square' class as sublcass of 'Rectangle'
  """)
  Answer("Refer to code implementation")

  class Square(Rectangle):

    def __init__(self, x1, y1, size):
      super().__init__(x1, y1, (x1 + size), (y1 + size))

  # Question 2
  Question(2, """
    Implement the 'Square' constructor. The Constructor should 
    have only the x1, y1 coordinates and the size of the square.
    Notice which arguments you'll have to use where you invoke the 
    'Rectangle' constructor when you use 'super'
  """)
  Answer("Refer to code implementation")

  # Question 3 
  Question(3, """
    Instantiate two objects of 'Square', invoke the area method 
    and print the objects. Make sure that all calculations are returning 
    correct numbers and that the coordinates of the square are consistent 
    with the size of the square used as arguements.
  """)

  # Invoke Area
  my_square = Square(1, 4, 2)
  Answer(f"Square Instance 1 area: {my_square.area()}")
  # Print Object
  Answer(f'Square Instance 1 coordinates: {my_square}')

  # Invoke Area
  my_square2 = Square(1, 6, 5)
  Answer(f"Square Instance 2 area: {my_square2.area()}")
  # Print Object
  Answer(f'Square Instance 2 coordinates: {my_square2}')
