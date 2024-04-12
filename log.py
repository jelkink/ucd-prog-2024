from datetime import datetime

class Log:

  def __init__(self, filename):
    self.filename = filename

  def reset(self):
    with open(self.filename, "w") as f:
      f.write("")
  
  def write(self, message):
    with open(self.filename, "a") as f:
      timestamp = datetime.now().strftime("%d/%m/%Y %H:%M.%S ")
      f.write(timestamp + message + "\n")
