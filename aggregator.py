from strategy import Strategy

class Aggregator(Strategy):

  def __init__(self, party):
    super().__init__(party)
    self.name = "A"

  def determine_update(self, simulation):
    pass