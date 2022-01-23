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

# ---------------------------------------------  RUN TYPE --------------------------------------
# Select the type of Run that will be performed. Use [1] for single simulation analysis. Use [2] for a comparison
# analysis and [3] for a figure only  run.
runType = 1
# --------------------------------------------- FOLDER CONFIGURATION --------------------------------------
input_path = "/home/administrador/Escritorio/Paraview_Batch_Postproc/Case_Files"
output_path = "/home/administrador/Escritorio/Paraview_Batch_Postproc/Output"
font_path = "/home/administrador/Escritorio/Paraview_Batch_Postproc"

# --------------------------------------------  IMAGE RESOLUTION--------------------------------------------
image_size = [2048, 1080]  # 2K size

# --------------------------------------------  SIMULATION PARAMETERS --------------------------------------
# Density of the air
rho_air = 1.1965
# Velocity of the free stream
fs_velocity = 15
# -------------------------------------------- DESIRED OUTPUT ----------------------------------------------
part_photos = False  # Set this to false if you don't want to get photos of the part stl
car_photos = False  # Set this to false if you don't want to get photos of the CAR stl

setup_info = {"FolderInfo": {"inFolder": input_path, "outFolder": output_path, "fontFolder": font_path},
              "RunType": runType, "ImageRes": image_size,
              "SimParam": {"Speed": fs_velocity, "Density": rho_air}
              "Output": {"CAR": car_photos, "PART": part_photos}}
