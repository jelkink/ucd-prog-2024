from strategy import Strategy

class Hunter(Strategy):

  def __init__(self, party):
    self.party = party
    self.name = "hunter"

  def determine_update(self, simulation):
    pass