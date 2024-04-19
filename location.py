import random
import math

class Location:

  def __init__(self):
    self.x = random.random()
    self.y = random.random()
    self.speed = 0.05

  def move_to(self, x, y):
    self.x = min(max(0.0, x), 1.0)
    self.y = min(max(0.0, y), 1.0)

  def move_towards(self, other):
    distance = self.distance(other)
    if distance <= self.speed:
      self.move_to(other.x, other.y)
    else:
      self.move_to(self.x + self.speed / distance * (other.x - self.x),
                   self.y + self.speed / distance * (other.y - self.y))

  def move_in_direction(self, angle):
    self.move_to(self.x + self.speed * math.cos(angle),
                 self.y + self.speed * math.sin(angle))

  def distance(self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

  @staticmethod
  def maximum_distance():
    return math.sqrt(2)