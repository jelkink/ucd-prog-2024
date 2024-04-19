from strategy import Strategy

class Predator(Strategy):

  def __init__(self, party):
    super().__init__(party)
    self.name = "P"

  def determine_update(self, simulation):
    pass