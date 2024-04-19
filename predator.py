from strategy import Strategy

class Predator(Strategy):

  def __init__(self, party):
    self.party = party
    self.name = "predator"

  def determine_update(self, simulation):
    pass