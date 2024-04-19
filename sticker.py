from strategy import Strategy


class Sticker(Strategy):

  def __init__(self, party):
    super().__init__(party)
    self.name = "S"
