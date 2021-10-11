# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT                                                               #
#   Version 4 (optimized Version 3 & 3.1)                                                                                    #
#   15/08/2021                                                                                                         #
# -------------------------------------------------------------------------------------------------------------------- #
#   Author: Sergio Batuecas Domínguez/ Miguel Pérez Cuadrado
#   Description: this script will be used from AWS to generate all the cfd post-processing data,
#               figures, graphs, etc. needed. Modified from traces obtained from the Paraview app.
# -------------------------------------------------------------------------------------------------------------------- #

# Import statements(functions)
import paraview.simple as pvs
import time
from pathlib import Path
from functions.get_files import get_files
from functions.paraview_trace import paraview_trace
from functions.get_block_indices import get_block_indices
from functions.set_mesh_regions import set_mesh_regions

# disable automatic stl reset on 'Show'
pvs._DisableFirstRenderCameraReset()

# File locations
input_path = Path("/home/administrador/Escritorio/Paraview_Batch_Postproc/Case_Files")
output_path_base = Path("/home/administrador/Escritorio/Paraview_Batch_Postproc/Output")
part_file
# ------------------------------------- MAIN CODE ----------------------------------------------------------------------
# Start timer
start_time = time.time()
# Read files,obtain output direction files, list the cases
list_cases, output_paths, list_stl, list_part, base_names, list_stl_files= get_files(input_path, output_path_base)

if list_cases:
    i = 1
    # Perform paraview_trace in each case in the list of cases
    for case in list_cases:
        pvs.ResetSession()
        paraview_trace(filename=case, output_path=output_paths[i-1], stl_file=list_stl[i-1], part_file=list_part[i-1] ,base_name=base_names[i-1], part_folder=list_stl_files[i-1])
        i += 1

    print("The process finished successfully.")
    print("Execution time: %s seconds" % (time.time() - start_time))
