import supportFunctions
import paraview.simple as pvs
import viewsDict
import glob


def single(info):
    # -------------------------------------- Folder configuration      ------------------------------#
    simulation = {"Name": [], "inFolder": [], "outFolder": [], "casefoamPath": [], "carPath": [], "partPath": []}
    # Select the desired simulation
    sim_name_path_foam = select_sim(info)
    # ------ Fill the dictionary with the simulation data
    simulation["casefoamPath"] = sim_name_path_foam
    # Extract the simulation folder name
    sim_name = sim_name_path_foam.replace(info["FolderInfo"]["inFolder"]+"/", "")
    simulation["Name"] = sim_name.replace("/case.foam", "")
    print("The selected simulation is :" + simulation["Name"])

    # Get the adress of the folder of the simulation that will be simulated
    simulation["inFolder"] = sim_name_path_foam.replace("/case.foam", "")

    # Create the output folder of the case
    simulation["outFolder"] = create_output_folder(info["FolderInfo"]["outFolder"], simulation["Name"])

    simulation["carPath"] = glob.glob(str(simulation["inFolder"]) + "/*CAR.stl", recursive=True)
    simulation["partPath"] = glob.glob(str(simulation["inFolder"]) + "/*PART.stl", recursive=True)
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

    # Create the render view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # Import the part STL and extract variables needed
    print(simulation["partPath"])
    part_stl = STLReader(registrationName='Part.stl', FileNames=[simulation["partPath"]])
    part_stl_display = Show(part_stl, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'STLSolidLabeling'
    sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

    # trace defaults for the display properties.
    part_stl_display.Representation = 'Surface'
    part_stl_display.ColorArrayName = ['CELLS', 'STLSolidLabeling']
    part_stl_display.LookupTable = sTLSolidLabelingLUT
    part_stl_display.SelectTCoordArray = 'None'
    part_stl_display.SelectNormalArray = 'None'
    part_stl_display.SelectTangentArray = 'None'
    part_stl_display.OSPRayScaleFunction = 'PiecewiseFunction'
    part_stl_display.SelectOrientationVectors = 'None'
    part_stl_display.ScaleFactor = 0.2695983052253723
    part_stl_display.SelectScaleArray = 'STLSolidLabeling'
    part_stl_display.GlyphType = 'Arrow'
    part_stl_display.GlyphTableIndexArray = 'STLSolidLabeling'
    part_stl_display.GaussianRadius = 0.013479915261268616
    part_stl_display.SetScaleArray = [None, '']
    part_stl_display.ScaleTransferFunction = 'PiecewiseFunction'
    part_stl_display.OpacityArray = [None, '']
    part_stl_display.OpacityTransferFunction = 'PiecewiseFunction'
    part_stl_display.DataAxesGrid = 'GridAxesRepresentation'
    part_stl_display.PolarAxes = 'PolarAxesRepresentation'

    print("Hello from a function")


def comparison(info):
    print("Hello from a function")

def figOnly(info):
    print("Hello from a function")
