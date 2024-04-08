from location import Location

class Party:

  def __init__(self, name):
    self.location = Location()
    self.voters = []
    self.name = name

  def add_voter(self, voter):
    self.voters.append(voter)

  def count_votes(self):
    return len(self.voters)

  def reset_voters(self):
    self.voters = []