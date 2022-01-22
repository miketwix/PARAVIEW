# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT                                                               #
#   Version 3 (optimized Version)                                                                                    #
#   15/08/2021                                                                                                         #
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
# Library to do mathematical opertions on python
import numpy as np
