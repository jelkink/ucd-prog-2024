from simulation import Simulation

def main():
  sim = Simulation()
  sim.create_parties(5)
  sim.create_voters(100)
  sim.run(10)

if __name__ == "__main__":
  main()
