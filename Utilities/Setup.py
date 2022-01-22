# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT
#   SETUP FILE
#   Version 1                                                                                     #
#   15/08/2021                                                                                                         #
# -------------------------------------------------------------------------------------------------------------------- #
#   Author: Miguel Pérez Cuadrado
#   Description: This script contains the main parameters to run the Paraview code. User shall change parameters as
#   Desired for the different mode of use of the postprocessing run and simulation variables
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- RUN TYPE --------------------------------------
# Select the type of Run that will be performed. Use [1] for single simulation analysis. Use [2] for a comparison
# analysis and [3] for a figure only  run.
runType = 1
# --------------------------------------------- FOLDER CONFIGURATION --------------------------------------
input_path = Path("/home/administrador/Escritorio/Paraview_Batch_Postproc/Case_Files")
output_path = Path("/home/administrador/Escritorio/Paraview_Batch_Postproc/Output")
# ---------------------------------------------------------------------------------------------------------
setup_file = {"inFolder": input_path, "outFolder": output_path, "RunType": runType}

