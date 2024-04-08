import random
import math

class Location:

  def __init__(self):
    self.x = random.random()
    self.y = random.random()

  def move_to(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

  @staticmethod
  def maximum_distance():
    return math.sqrt(2)