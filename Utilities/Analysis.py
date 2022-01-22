from Utilities.supportFunctions import select_sim


# Paraview library to operate program from python console
#import paraview.simple as pvs
def single(info):
  sim_name = select_sim(info)
  print(sim_name)

def comparison(info):
  print("Hello from a function")

def figOnly(info):
  print("Hello from a function")
