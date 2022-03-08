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
from Auxiliar_Functions import jasonImport as getInf
# ------------------------------------------ Environment configuration------------------------------------------------ #
# Get the simulations data from JSON files
setup_info = getInf.get_info()
# Clean the Output folder
envConfig.remove_files(setup_info["FolderInfo"]["outFolder"])
# Find the simulations
sim_list = envConfig.folder_names(setup_info["FolderInfo"]["inFolder"])
print(sim_list)