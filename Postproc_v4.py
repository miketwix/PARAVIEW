# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT
#   MAIN FILE
#   Version 4                                                                                                          #
#   03/03/22                                                                                                           #
# -------------------------------------------------------------------------------------------------------------------- #
#   Author: Sergio Batuecas / Miguel Pérez /Rafael Enríquez / Daniel Orozco

#   Description: this script will be used from AWS/Windows/Ubuntu to generate all the cfd post-processing data,
#               figures, graphs, etc. needed. Modified from traces obtained from the Paraview app.
# -------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------ Import of libraries ----------------------------------------------------- #
from Auxiliar_Functions import env_config as envConfig
from Auxiliar_Functions import info as info
from Auxiliar_Functions import paraview as pv
import os
# ------------------------------------------- Configuration of the simulation objects ---------------------------------#


class Simulation:
    def __init__(self, name, foam, car_stl):
        self.name = name
        self.foam = foam
        self.CAR = car_stl

# ------------------------------------------ Environment configuration------------------------------------------------ #


# Set current working directory as the file's location
    try:
        location = os.path.dirname(__file__)
        os.chdir(location)

    except OSError:
        print('Working directory could not be set')
    else:
        print('Directory successfully set in: ' + location)


# Get the simulations' data from JSON files
setup_info = info.get_info()

# Clean the Output folder
valid_ans = 0
cont = input('Output folder  will be emptied, do you wish to proceed? [y/n]: ')

while valid_ans == 0:
    if cont == 'y':
        envConfig.remove_files(setup_info["FolderInfo"]["outFolder"])
        valid_ans = 1
    elif cont == 'n':
        quit()
    else:
        cont = input('Please enter a valid option [y/n]: ')


# Find the simulations
sim_path = envConfig.find_folders(setup_info["FolderInfo"]["inFolder"])
# Detect number of simulations
sim_id = list()
for k in range(len(sim_path)):
    sim_id.append('s'+str(k+1))

num_sym = 0

for selected_sim in sim_path:
    [foam, car] = envConfig.find_files(selected_sim)
    sim_id[num_sym] = Simulation(selected_sim.replace(setup_info["FolderInfo"]["inFolder"] + "\\", ''), foam, car)
    pv.analyze_sim(setup_info, sim_id[num_sym])
    num_sym = num_sym + 1







