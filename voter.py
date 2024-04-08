from location import Location

class Voter:

  def __init__(self):
    self.location = Location()

  def vote(self, parties):
    nearest = parties[0]
    nearest_distance = Location.maximum_distance()

    for party in parties:
      if self.location.distance(party.location) < nearest_distance:
        nearest = party
        nearest_distance = self.location.distance(party.location)

    nearest.add_voter(self)