class Strategy:

  def __init__(self):
    print("This class should not be initialized directly!")
    self.name = ""

    self.target_x = None
    self.target_y = None
    self.target_radius = None 
  
  def get_name(self):
    return self.name

  def determine_update(self, party, simulation):
    pass

  def execute_update(self, party):
    if self.target_radius is not None:
      party.location.move_in_direction(self.target_radius)
    elif self.target_x is not None:
      party.location.move_towards(self.target_x, self.target_y)