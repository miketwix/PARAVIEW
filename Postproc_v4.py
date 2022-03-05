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
import os
import sys
import json
# Opening JSON file
f = open("C:\\Users\\Usuario\\Desktop\\Paraview_Batch_Postproc\\config.json")

# returns JSON object as
# a dictionary
setup_info = json.load(f)

# Closing file
f.close()
# ------------------------------------------ Environment configuration------------------------------------------------ #
