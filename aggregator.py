from strategy import Strategy

class Aggregator(Strategy):

  def __init__(self, party):
    self.party = party
    self.name = "aggregator"

  def determine_update(self, simulation):
    pass