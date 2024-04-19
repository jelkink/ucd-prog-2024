import random

from location import Location

from hunter import Hunter
from predator import Predator
from sticker import Sticker
from aggregator import Aggregator


class Party:

  def __init__(self, name):
    self.location = Location()
    self.voters = []
    self.name = name
    self.previous_vote_count = 0

  def add_voter(self, voter):
    self.voters.append(voter)

  def count_votes(self):
    return len(self.voters)

  def reset_voters(self):
    self.previous_vote_count = self.count_votes()
    self.voters = []

  def set_random_strategy(self):
    s = random.randint(1, 4)

    if s == 1:
      self.strategy = Hunter(self)
    elif s == 2:
      self.strategy = Aggregator(self)
    elif s == 3:
      self.strategy = Predator(self)
    else:
      self.strategy = Sticker(self)
