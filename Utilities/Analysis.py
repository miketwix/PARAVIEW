from supportFunctions import select_sim, create_output_folder
#from paraview.simple import *
from viewsDict import car_views
import glob


def single(info):
    # -------------------------------------- Folder configuration      ------------------------------#
    simulation = {"Name": [], "inFolder": [], "outFolder": [], "casefoamPath": [], "carPath": [], "partPath": []}
    # Select the desired simulation
    sim_name_path_foam = select_sim(info)
    # ------ Fill the dictionary with the simulation data
    simulation["casefoamPath"] = sim_name_path_foam
    # Extract the simulation folder name
    sim_name = sim_name_path_foam.replace(info["FolderInfo"]["inFolder"]+"\\", "")
    simulation["Name"] = sim_name.replace("\\case.foam", "")
    print("The selected simulation is :" + simulation["Name"])

    # Get the adress of the folder of the simulation that will be simulated
    simulation["inFolder"] = sim_name_path_foam.replace("\\case.foam", "")

    # Create the output folder of the case
    simulation["outFolder"] = create_output_folder(info["FolderInfo"]["outFolder"], simulation["Name"])

    simulation["carPath"] = glob.glob(str(simulation["inFolder"]) + "\\*CAR.stl", recursive=True)
    simulation["partPath"] = glob.glob(str(simulation["inFolder"]) + "\\*PART.stl", recursive=True)
    # ---------------------------------------------- Paraview Analysis       ------------------------------#

    ########################################################################################################
    #                                                   SETUP - RESOURCE IMPORT                            #
    ########################################################################################################
    image_size = info["ImageRes"]
    block_names = ["Block - Fluid", "CAR"]  # "Block - Fluid", "Block - CAR"
    car_views_dictionary, stl_views_dictionary, slice_views_dictionary = car_views()
    font_path = info["FolderInfo"]["fontFolder"]
    ########################################################################################################
    #                                                   INITIALIZATION                                    #
    ########################################################################################################
    print(info["FolderInfo"]["casefoamPath"])
    CAR_stl = STLReader(registrationName='CAR', FileNames=[info["FolderInfo"]["casefoamPath"]])
    # set active source
    SetActiveSource(CAR_stl)
    renderView1 = GetActiveViewOrCreate('RenderView')
    CARDisplay = Show(CAR_stl, renderView1, 'GeometryRepresentation')


def comparison(info):
    print("Hello from a function")

def figOnly(info):
    print("Hello from a function")
