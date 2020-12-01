class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def grow(self):
    self.age += 1

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, laws={Robot.laws})'
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'

class Human:
  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}")
  
  def grow(self):
    self.age += 1

  def eat(self, amount):
    if (self.energy + amount) <= Human.MAX_ENERGY:
      self.energy += amount
    else:
      self.energy = Human.MAX_ENERGY
  
  def move(self, distance):
    if (self.energy - distance) >= 0:
      self.energy -= distance
    else:
      print("Can't move, not enough energy!")
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  
  def __str__(self):
    return f'My name is {self.name}, I am {self.age} years old and have {self.energy} energy.'

if (__name__ == "__main__"):
  human = Human()
  print(human.__repr__())
  human.move(40)
  print(human.__repr__())
  human.eat(20)
  print(human.__repr__())
  human.eat(100)
  print(human.__repr__())

