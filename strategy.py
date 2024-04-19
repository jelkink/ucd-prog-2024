class Strategy:

  def __init__(self, party):
    print("This class should not be initialized directly!")
    self.name = ""
    self.party = party

    self.target_x = None
    self.target_y = None
    self.target_angle = None 
  
  def get_name(self):
    return self.name

  def determine_update(self, simulation):
    pass

  def execute_update(self):
    if self.target_angle is not None:
      self.party.location.move_in_direction(self.target_angle)
    elif self.target_x is not None:
      self.party.location.move_towards(self.target_x, self.target_y)