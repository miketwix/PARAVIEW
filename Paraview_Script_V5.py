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
# Paraview library to operate program from python console
import paraview.simple as pvs
# Library to operate within the operating system of the user
import os
# Library to use global variables
import glob
# Library to compute the time taken to run program
import time
# Library to do mathematical operations on python
import numpy as np
# Import data from the setup file
from Utilities.Setup import setup_info

if setup_info["RunType"] == 1:
    execfile('Single.py')
elif setup_info["RunType"] == 2:
    execfile('Comp.py')
elif setup_info["RunType"] == 3:
    execfile('FigOnly.py')
else:
    print("Please select a valid RunType at the Setup file")
