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

# Import the needed libraries to work in the environment

# Library to operate within the operating system of the user
import os
from pathlib import Path
# Library to use as finder
import glob
# Library to compute the time taken to run program
import time
# Import data from the setup file
from Utilities.Setup import setup_info
import Utilities.supportFunctions as Support
import Utilities.Analysis as Analyze

start_time = time.time()
# Clean everything in output folder
files = os.listdir(setup_info["FolderInfo"]["outFolder"])
for f in files:
    os. rmdir(setup_info["FolderInfo"]["outFolder"]+"/" + f)

# TODO Buscar forma de ejecutar códigos desde otras carpetas
if setup_info["RunType"] == 1:
    Analyze.single(setup_info)
elif setup_info["RunType"] == 2:
    Analyze.comparison(setup_info)
elif setup_info["RunType"] == 3:
    Analyze.figOnly(setup_info)
else:
    print("Please select a valid RunType at the Setup file")

print("The process finished successfully.")
print("Execution time: %s seconds" % (time.time() - start_time))
