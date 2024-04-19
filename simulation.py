from party import Party
from voter import Voter
from log import Log


class Simulation:

  def __init__(self):
    self.parties = []
    self.voters = []
    self.time = 0
    self.log = Log("simulation_log.txt")

  def run(self, iterations):
    end = self.time + iterations
    while self.time < end:
      self.election()
      self.report_vote_count()
      self.update_parties()
      self.time += 1

  def election(self):
    for party in self.parties:
      party.reset_voters()
      
    for voter in self.voters:
      voter.vote(self.parties)

  def update_parties(self):
    for party in self.parties:
      party.strategy.determine_update(self)

    for party in self.parties:
      party.strategy.execute_update()

  def report_vote_count(self):
    for party in self.parties:
      print("Count of votes for %10s (%1s) at time %03d: %d" % (party.name, party.strategy.name, self.time, party.count_votes()))

  def create_parties(self, n):
    i = 0
    while i < n:
      self.parties.append(Party("Party %d" % (i)))
      i += 1

    self.log.write("Created %d parties" % n)

  def create_voters(self, n):
    i = 0
    while i < n:
      self.voters.append(Voter())
      i += 1

    self.log.write("Created %d voters" % n)
