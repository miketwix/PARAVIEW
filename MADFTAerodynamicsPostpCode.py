# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT
#   MAIN FILE
#   Version 5                                                                                     #
#   22/1/22                                                                                                         #
# -------------------------------------------------------------------------------------------------------------------- #
#   Author: Sergio Batuecas Domínguez/ Miguel Pérez Cuadrado
#   Description: this script will be used from AWS/Windows/Ubuntu to generate all the cfd post-processing data,
#               figures, graphs, etc. needed. Modified from traces obtained from the Paraview app.
# -------------------------------------------------------------------------------------------------------------------- #

########################################################################################################################
# ------------------------------------------------- IMPORT OF LIBRARIES NEEDED ----------------------------------------#
########################################################################################################################
# Library to operate within the operating system of the user
import os
import sys
# Library to navigate within the operating system of the user
from pathlib import Path
# Library to use as finder
import glob
# Library to compute the time taken to run program
import time
# Library to use .json files
import json

current_loc = "/home/administrador/PycharmProjects/Postprocessing"
utilities_loc = (str(current_loc) + "/Utilities")
sys.path.append(utilities_loc)

import Analysis as Analyze

########################################################################################################################
# ------------------------------------------------- CONFIG DATA IMPORT-------- ----------------------------------------#
########################################################################################################################
# Opening JSON file
f = open("/home/administrador/PycharmProjects/Postprocessing/config.json")

# returns JSON object as
# a dictionary
setup_info = json.load(f)

# Closing file
f.close()

start_time = time.time()
########################################################################################################################
# ------------------------------------------------- ERASE PREVIOUS RUNS OF POSTPROC -----------------------------------#
########################################################################################################################
# Clean everything in output folder
files = os.listdir(setup_info["FolderInfo"]["outFolder"])
for f in files:
    os.rmdir(setup_info["FolderInfo"]["outFolder"] + "/" + f)
########################################################################################################################
# ------------------------------------------------- Postproc run type branch selection --------------------------------#
########################################################################################################################

if setup_info["RunType"] == 1:
    Analyze.single(setup_info)
elif setup_info["RunType"] == 2:
    Analyze.comparison(setup_info)
elif setup_info["RunType"] == 3:
    Analyze.figOnly(setup_info)
else:
    print("Please select a valid RunType at the Setup file and restart the run")

print("The process finished successfully.")
print("Execution time: %s seconds" % (time.time() - start_time))
