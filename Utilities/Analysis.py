from Utilities.supportFunctions import select_sim, create_output_folder


# Paraview library to operate program from python console
#import paraview.simple as pvs
def single(info):
  simulation = {"Name": [], "inFolder":[], "outFolder":[] }
  # Select the desired simulation
  sim_name_path_foam = select_sim(info)

  # Extract the simulation folder name
  sim_name = sim_name_path_foam.replace(info["FolderInfo"]["inFolder"]+"/", "")
  simulation["Name"] = sim_name.replace("/case.foam", "")
  print("The selected simulation is :" + simulation["Name"])

  # Get the adress of the folder of the simulation that will be simulated
  simulation["inFolder"] = sim_name_path_foam.replace("/case.foam", "")

  # Create the output folder of the case
  simulation["outFolder"] = create_output_folder(info["FolderInfo"]["outFolder"], simulation["Name"])

def comparison(info):
  print("Hello from a function")

def figOnly(info):
  print("Hello from a function")
