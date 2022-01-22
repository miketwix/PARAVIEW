# -------------------------------------------------------------------------------------------------------------------- #
#   MAD FORMULA TEAM PARAVIEW CFD POST-PROCESSING SCRIPT                                                               #
#   Version 3 (optimized Version)                                                                                    #
#   15/08/2021                                                                                                         #
# -------------------------------------------------------------------------------------------------------------------- #
#   Author: Sergio Batuecas Domínguez/ Miguel Pérez Cuadrado
#   Description: this script will be used from AWS/Windows/Ubuntu to generate all the cfd post-processing data,
#               figures, graphs, etc. needed. Modified from traces obtained from the Paraview app.
# -------------------------------------------------------------------------------------------------------------------- #

# Import statements(functions)
import paraview.simple as pvs
import os
import glob
import time
import numpy as np


# disable automatic stl reset on 'Show'
pvs._DisableFirstRenderCameraReset()

# File locations
input_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\Paraview_Batch_Postproc\\Case_Files')
output_path_base = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\Paraview_Batch_Postproc\\Output')

def car_views():
    # MODIFY VIEWS HERE #######################################################################################

    # VIEWS DICTIONARIES. There are currently three dictionaries
    # which contain data por stl positioning for the different
    # views in each part of the code. Each of these dictionaries
    # contain a number of dictionaries (one for each view). If
    # you want to add a custom view to any of these, just copy
    # and paste any existing view and copy the position, focal
    # point and view up from paraview (leave the parallelscale as is).
    # Remember to add this new view to its corresponding
    # dictionary.

    # Definition of dictionaries containing view parameters for each view.
    # Dictionaries for stl file views
    stl_top_view_dictionary = {
        "Position": [0.55, 0, 4.0],
        "FocalPoint": [0.55, 0, 0.4],
        "ViewUp": [0.0, 1.0, 0.0],
        "ParallelScale": 1.76
    }
    stl_lside_view_dictionary = {
        "Position": [0.7, -4.0, 0.4],
        "FocalPoint": [0.7, 0, 0.4],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    stl_rside_view_dictionary = {
        "Position": [0.7, 4.0, 0.4],
        "FocalPoint": [0.7, 0, 0.4],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    stl_bottom_view_dictionary = {
        "Position": [0.7, 0, -4.0],
        "FocalPoint": [0.7, 0, 0.4],
        "ViewUp": [0.0, -1.0, 0.0],
        "ParallelScale": 1.76
    }
    stl_front_view_dictionary = {
        "Position": [-2.5, 0, 0.28],
        "FocalPoint": [0.55, 0, 0.28],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    stl_back_view_dictionary = {
        "Position": [3.6, 0, 0.3],
        "FocalPoint": [0.55, 0, 0.3],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    stl_isometric_view_dictionary = {
        "Position": [-1.9, 3.5, 2.1],
        "FocalPoint": [0.62, -0.14, 0.34],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    # This last dictionary contains all of the above dictionaries for easy reference.
    stl_views_dictionary = {
        "Top": stl_top_view_dictionary,
        "LSide": stl_lside_view_dictionary,
        "RSide": stl_rside_view_dictionary,
        "Bottom": stl_bottom_view_dictionary,
        "Front": stl_front_view_dictionary,
        "Back": stl_back_view_dictionary,
        "Isometric": stl_isometric_view_dictionary
    }

    # Dictionaries for slice views
    slice_top_view_dictionary = {
        "Position": [1.2, 0.93, 7.5],
        "FocalPoint": [1.2, 0.92, 3.5],
        "ViewUp": [0.0, 1.0, 0.0],
        "ParallelScale": 1.76
    }
    slice_side_view_dictionary = {
        "Position": [1.2, -6.18, 1.26],
        "FocalPoint": [1.2, 3.5, 1.26],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    slice_front_view_dictionary = {
        "Position": [-2.88, 0.13, 0.58],
        "FocalPoint": [0.0, 0.13, 0.58],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    # This last dictionary contains all of the above dictionaries for easy reference.
    slice_views_dictionary = {
        "Top": slice_top_view_dictionary,
        "Side": slice_side_view_dictionary,
        "Front": slice_front_view_dictionary
    }

    # Dictionaries for car surface views
    car_top_view_dictionary = {
        "Position": [0.55, 0.35, 3.83],
        "FocalPoint": [0.55, 0.35, 0.41],
        "ViewUp": [0.0, 1.0, 0.0],
        "ParallelScale": 1.76
    }
    car_rside_view_dictionary = {
        "Position": [0.55, 3.78, 0.41],
        "FocalPoint": [0.55, 0.35, 0.41],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    car_bottom_view_dictionary = {
        "Position": [0.65, 0.35, -3.0],
        "FocalPoint": [0.65, 0.35, 0.41],
        "ViewUp": [0.0, 1.0, 0.0],
        "ParallelScale": 1.76
    }
    car_front_view_dictionary = {
        "Position": [-2.28, 0.35, 0.41],
        "FocalPoint": [0.55, 0.35, 0.41],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    car_back_view_dictionary = {
        "Position": [3.98, 0.35, 0.41],
        "FocalPoint": [0.55, 0.35, 0.41],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    car_isometric_view_dictionary = {
        "Position": [-2.45, 2.63, 2.15],
        "FocalPoint": [0.36, 0.14, 0.4],
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    # This last dictionary contains all of the above dictionaries for easy reference.
    car_views_dictionary = {
        "Top": car_top_view_dictionary,
        "RSide": car_rside_view_dictionary,
        "Bottom": car_bottom_view_dictionary,
        "Front": car_front_view_dictionary,
        "Back": car_back_view_dictionary,
        "Isometric": car_isometric_view_dictionary
    }
    return car_views_dictionary, stl_views_dictionary, slice_views_dictionary
def create_extract_block(name, source, indices):
    """ This function performs a ExtractBlock operation on a given source using a list of indices and then returns it
    with the given name.

    --- inputs
    + name: str, name to give to the block
    + source: source from which to extract the block
    + indices: int, list of indices of the properties to extract
    """
    # Extract block
    extract_block = pvs.ExtractBlock(Input=source)
    # Indices
    extract_block.BlockIndices = indices
    # Rename
    pvs.RenameSource(name, extract_block)

    return extract_block
def create_output_folders(out_path, case_files, element):
    """ This function creates all the folders needed to store the output files for the different simulations.

    """
    paths = []
    basenames = []
    for case in case_files:
        base_name = os.path.basename(os.path.dirname(case))
        basenames.append(base_name)
        if element == "":
                path = out_path + "\\" + base_name

        else:
                path = out_path + "\\" + element
        try:
            os.makedirs(path)
            paths.append(path)

        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s" % path)

    return paths, basenames
def get_block_indices(composite_data_information, index=0):
    """
    Source: https://discourse.paraview.org/t/get-block-name-and-id-from-multiblock-dataset/4014/2
    :param composite_data_information:
    :param index:
    :return:
    """
    localDict = {}

    if composite_data_information.GetDataIsMultiPiece():
        index += composite_data_information.GetNumberOfChildren()
    else:
        if composite_data_information.GetDataIsComposite():
            for i in range(composite_data_information.GetNumberOfChildren()):
                index += 1
                _blockName = composite_data_information.GetName(i)
                localDict[_blockName] = index
                leafDict, index = get_block_indices(composite_data_information.GetDataInformation(i).GetCompositeDataInformation(), index)
                localDict.update(leafDict)

    return localDict, index
def get_files(input_path, output_path_base):

    """ This function looks for case.foam files and

    """

    print("Searching for case.foam files...")
    list_cases = glob.glob(str(input_path) + "/**/case.foam", recursive=True)
    list_stl = glob.glob(str(input_path) + "/**/*CAR.stl", recursive=True)
    list_part = glob.glob(str(input_path) + "/**/*PART.stl", recursive=True)
    if list_cases:
        print(str(len(list_cases)) + " cases found.")

        out_paths, base_names = create_output_folders(out_path=output_path_base, case_files=list_cases, element="")

        print(list_cases)

    else:
        raise Exception("NO CASE.FOAM FILES FOUND.")

    return list_cases, out_paths, list_stl, list_part, base_names
def part_views(bounds, x_dim, y_dim, z_dim):
    # MODIFY VIEWS HERE #######################################################################################
    # HACIENDO PRUEBA 1: USAR COMO PUNTO FOCAL EL CENTRO DE LA PART, ROTAR USANDO EL PUNTO FOCAL Y EL VIEWUP
    # LA POSICION SE CALCULA USANDO EL PUNTOO FOCAL SUMADO A UN "ESPACIO" EN LA  DIRECCION EN LA QUE SE HACE LA
    # VISTA
    focal_point = [sum(bounds[0:2]) / 2, sum(bounds[2:4]) / 2, sum(bounds[4:]) / 2]
    space = 2.5
    part_top_view_dictionary = {
        "Position": list(np.array(focal_point) + np.array([0, 0, space])),
        "FocalPoint": focal_point,
        "ViewUp": [int(x_dim <= y_dim), int(x_dim > y_dim), 0.0],
        "ParallelScale": 1.76
    }
    part_lside_view_dictionary = {
        "Position": list(np.array(focal_point) + np.array([0, space, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [int(x_dim <= z_dim), 0.0, int(x_dim > z_dim)],
        "ParallelScale": 1.76
    }
    part_rside_view_dictionary = {
        "Position": list(np.array(focal_point) - np.array([0, space, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [int(x_dim <= z_dim), 0.0, int(x_dim > z_dim)],
        "ParallelScale": 1.76
    }
    part_bottom_view_dictionary = {
        "Position": list(np.array(focal_point) - np.array([0, 0, space])),
        "FocalPoint": focal_point,
        "ViewUp": [(int(x_dim <= y_dim)), (int(x_dim > y_dim)), 0.0],
        "ParallelScale": 1.76
    }
    part_front_view_dictionary = {
        "Position": list(np.array(focal_point) - np.array([space, 0, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [0.0, int(z_dim >= y_dim), int(y_dim > z_dim)],
        "ParallelScale": 1.76
    }
    part_back_view_dictionary = {
        "Position": list(np.array(focal_point) + np.array([space, 0, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [0.0, (int(z_dim >= y_dim)), (int(y_dim > z_dim))],
        "ParallelScale": 1.76
    }
    part_isometric_view_dictionary = {
        "Position": list(np.array(focal_point) + 0.5*(np.array([-space, -space, space]))),
        "FocalPoint": focal_point,
        "ViewUp": [0.0, 0.0, 1.0],
        "ParallelScale": 1.76
    }
    # This last dictionary contains all of the above dictionaries for easy reference.
    part_views_dictionary = {
        "Top": part_top_view_dictionary,
        "LSide": part_lside_view_dictionary,
        "RSide": part_rside_view_dictionary,
        "Bottom": part_bottom_view_dictionary,
        "Front": part_front_view_dictionary,
        "Back": part_back_view_dictionary,
        "Isometric": part_isometric_view_dictionary
    }

    # VIEWS FOR FOCUS SLIDES
    # Dictionaries for slice views
    slice_top_view_dictionary = {
        "Position": list(np.array(focal_point) + np.array([0, 0, space])),
        "FocalPoint": focal_point,
        "ViewUp": [int(x_dim <= y_dim), int(x_dim > y_dim), 0.0],
        "ParallelScale": 1.76
    }
    slice_side_view_dictionary = {
        "Position": list(np.array(focal_point) - np.array([0, space, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [int(x_dim <= z_dim), 0.0, int(x_dim > z_dim)],
        "ParallelScale": 1.76
    }
    slice_front_view_dictionary = {
        "Position": list(np.array(focal_point) - np.array([space, 0, 0])),
        "FocalPoint": focal_point,
        "ViewUp": [0.0, int(z_dim >= y_dim), int(y_dim > z_dim)],
        "ParallelScale": 1.76
    }
    # This last dictionary contains all of the above dictionaries for easy reference.
    slice_views_dictionary = {
        "Top": slice_top_view_dictionary,
        "Side": slice_side_view_dictionary,
        "Front": slice_front_view_dictionary
    }

    return part_views_dictionary, slice_views_dictionary
def set_mesh_regions(case):
    """ This function takes a case and writes lists containing the patches corresponding to the different mesh regions
    of interest.

    --- inputs
    + case : openFoamReader object, the case.foam to analyse.

    --- outputs
    + patches_lists : list of the lists of patches generated by the function. In this version it contains:
        - index 0: patches, list of all the patches in the case.foam.
        - index 1: internal_mesh, list which only contains the internalMesh patch.
        - index 2: car_surfaces, list which only contains the patches corresponding to the car surface.

    """
    # Get all patches. case.GetProperty provides a list with numbers identifying each patch. I am not interested in
    # those numbers so the list is iterated over to discard them.
    patches_aux = case.GetProperty("PatchArrayInfo")
    print("This is the patches_aux list: " + str(patches_aux))
    patches = []

    for patch in patches_aux:
        if not patch.isdigit():
            patches.append(patch)

    # print(patches)

    # Initialize lists
    internal_mesh = ["internalMesh"]
    car_surfaces = []

    # Search for all patches which belong to car surface and add them to the list
    for patch in patches:
        if not patch.startswith("boundingBox") and not patch.startswith("internalMesh") and not patch.isdigit():
            car_surfaces.append(patch)

    # Build the list of lists
    patches_lists = [patches, internal_mesh, car_surfaces]

    return patches_lists
def paraview_trace(filename, output_path, stl_file, part_file, base_name):
    """ This function contains the trace obtained from paraview, modified to allow for multiple cases to be analysed
        using the same code. Chunks of code which were not originally on the trace are marked by a # ATT. comment line.
        Inputs
        * i : int, case number.
        * filename: str, directory where the case.foam file to analyse is stored.
        """

    # --------------------IN THIS SECTION,PLEASE SELECT THE DESIRED OUTPUTS-------------------------------------------#
    # Set to false if you don't want to obtain any specific output
    part_photos = False  # Set this to false if you don't want to get photos of the part stl
    car_photos = False  # Set this to false if you don't want to get photos of the CAR stl
    slices = True  # Set this to false if you don't want to get fluid domain slices
    streamlines = False  # Set this to false if you don't want to get streamlines
    surface_plots = False  # Set this to false if you don't want to get surface plots
    cp_plots = False  # Set this to false if you don't want to get cp plots
    #line_plots = False  # Set this to false if you don't want to get line plots
    pt_slices = False  # Set this to false if you don't want to get Pt slices
    isosurfaces = True  # Set this to false if you don't want to get isosurfaces
    # WARNING --> TO BE ABLE TO RUN MESH-FOCUS MESH NEEDS TO BE SET ON TRUE
    mesh = False  # Set this to false if you don't want to get mesh photos
    mesh_focus = False  # Set this to false if you don't want to get mesh centered on the part photos
    # ----------------------------------------------------------------------------------------------------------------#

    # -------------------------SCREENSHOTS PARAMETERS (Resolution,font,colors,views)----------------------------------#
    # Define the resolution of the photos
    image_size = [7680, 4320]  # 8K size
    # font file location
    font_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\Paraview_Batch_Postproc')
    # color file location
    # color_preset_path = Path("/home/administrador/Escritorio/Paraview_Batch_Postproc") NOT DEFINED YET
    # Import the views for the CAR,PART and slices
    car_views_dictionary, stl_views_dictionary, slice_views_dictionary = car_views()
    # ----------------------------------------------------------------------------------------------------------------#

    # GENERAL VARIABLES NEEDED FOR THE CODE
    block_names = ["Block - Fluid", "CAR"]  # "Block - Fluid", "Block - CAR"

    # FLOW VARIABLES
    # Density of the air
    rho_air = 1.1965
    # Velocity of the free stream
    fs_velocity = 15

    # ----------------------------------------- 1: PART STL ----------------------------------------------------------#
    """ The code below is outside of the part_photo conditional in order to be able to get out the dimensions of the 
    part, which might be used in other sections in onder to be able to focus on certain zones of the car """

    # create a new 'STL Reader'
    part_model = pvs.STLReader(FileNames=[part_file])
    # get active view
    renderView1 = pvs.GetActiveViewOrCreate('RenderView')
    # show data in view
    part_model_display = pvs.Show(part_model, renderView1, 'GeometryRepresentation')

    # Obtain model dimensions
    part_bounds = part_model.GetDataInformation().GetBounds()
    part_x_dim = part_bounds[1] - part_bounds[0]
    part_y_dim = part_bounds[3] - part_bounds[2]
    part_z_dim = part_bounds[5] - part_bounds[4]
    # Obtain part views from boundaries of the stl (See PRUEBAS PART STL/LOG STL)
    part_views_dictionary, part_slice_dictionary = part_views(part_bounds, part_x_dim, part_y_dim, part_z_dim)
    if part_photos:

        # Set render view to image size
        renderView1.ViewSize = image_size

        # create layout (SUS --> layout1 no se usa para nada)
        layout1 = pvs.GetLayout()

        # reset view to fit data
        renderView1.ResetCamera()

        # Set view names
        views = ["RSide", "LSide", "Front", "Back", "Isometric", "Top", "Bottom"]

        # Create STL-PART folder
        [stl_part_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                        element='STL-PART')

        for view in views:
            # current stl placement for renderView1
            renderView1.CameraPosition = part_views_dictionary[view]["Position"]
            renderView1.CameraFocalPoint = part_views_dictionary[view]["FocalPoint"]
            renderView1.CameraViewUp = part_views_dictionary[view]["ViewUp"]
            renderView1.CameraParallelScale = part_views_dictionary[view]["ParallelScale"]

            # save screenshot
            file_name = stl_part_folder[0] + '/' + view + ".png"
            pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

        # hide data in view
    pvs.Hide(part_model, renderView1)
    pvs.Delete(part_model)
    # ----------------------------------------- 2: CAR STL ----------------------------------------------------------
    """ The code below is outside of the car_photo conditional in order to be able to get out the dimensions of the 
    CAR, which might be used in other sections in onder to be able to focus on certain zones of the car, for surface
    plots or cp plots"""

    # create a new 'STL Reader'
    stl_model = pvs.STLReader(FileNames=[stl_file])
    # get active view
    renderView1 = pvs.GetActiveViewOrCreate('RenderView')
    # show data in view
    stl_model_display = pvs.Show(stl_model, renderView1, 'GeometryRepresentation')

    # ATT. get model dimensions
    stl_bounds = stl_model.GetDataInformation().GetBounds()
    stl_x_dim = stl_bounds[1] - stl_bounds[0]
    stl_y_dim = stl_bounds[3] - stl_bounds[2]
    stl_z_dim = stl_bounds[5] - stl_bounds[4]

    if car_photos:
        # reset view to fit data
        renderView1.ResetCamera()

        # set image size for the view
        renderView1.ViewSize = image_size
        # TODO no funciona el pvs load palette

        #    pvs.LoadPalette(paletteName='BlackBackground')

        # Set view names
        views = ["LSide", "Front", "Back", "Isometric", "Top", "Bottom"]
        # TODO poner esto más bonico

        # Create STL-CAR folder
        [stl_car_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name], element='STL-CAR')

        for view in views:
            # current stl placement for renderView1
            renderView1.CameraPosition = stl_views_dictionary[view]["Position"]
            renderView1.CameraFocalPoint = stl_views_dictionary[view]["FocalPoint"]
            renderView1.CameraViewUp = stl_views_dictionary[view]["ViewUp"]
            renderView1.CameraParallelScale = stl_views_dictionary[view]["ParallelScale"]

            # save screenshot
            file_name = stl_car_folder[0] + '/' + view + ".png"
            print(file_name)
            pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

        # hide data in view
    pvs.Hide(stl_model, renderView1)

    # ------------------------------ Import process of the case.foam, required for the following sections -------------#

    # create a new 'OpenFOAMReader'
    casefoam = pvs.OpenFOAMReader(FileName=filename)
    casefoam.SkipZeroTime = 1
    casefoam.CaseType = 'Reconstructed Case'
    casefoam.LabelSize = '32-bit'
    casefoam.ScalarSize = '64-bit (DP)'
    casefoam.Createcelltopointfiltereddata = 1
    casefoam.Adddimensionalunitstoarraynames = 0
    casefoam.MeshRegions = ['internalMesh']
    casefoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress', 'y', 'yPlus']
    casefoam.PointArrays = []
    casefoam.LagrangianArrays = []
    casefoam.Cachemesh = 1
    casefoam.Decomposepolyhedra = 1
    casefoam.ListtimestepsaccordingtocontrolDict = 0
    casefoam.Lagrangianpositionswithoutextradata = 1
    casefoam.Readzones = 0
    casefoam.Copydatatocellzones = 0

    # ATT. Rename openFoamReader
    pvs.RenameSource("Case", casefoam)

    # ATT. Get all regions of interest
    list_of_patches = set_mesh_regions(casefoam)
    print("This is the list of all patches found: " + str(list_of_patches[0]))
    print("This is the list of internalMesh patches: " + str(list_of_patches[1]))
    print("This is the list of car patches: " + str(list_of_patches[2]))

    # Properties modified on casefoam
    casefoam.MeshRegions = list_of_patches[0]

    # get active view
    renderView1 = pvs.GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    renderView1.ViewSize = image_size

    # get layout
    layout1 = pvs.GetLayout()

    # show data in view
    casefoamDisplay = pvs.Show(casefoam, renderView1, 'GeometryRepresentation')

    # find source
    casefoam = pvs.FindSource('Case')
    # hide data in view
    pvs.Hide(casefoam, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # ATT. Get dictionary containing the indices for each block in the dataset
    index_dict, ind = get_block_indices(casefoam.GetDataInformation().DataInformation.GetCompositeDataInformation())
    print("This is the ind variable: " + str(ind))
    print("This is the index_dict variable: " + str(index_dict))

    # ATT. Build a list of lists of indices for the whole dataset and the different blocks defined.
    lists_of_indices = []

    iter_list_of_patches = iter(list_of_patches)
    next(iter_list_of_patches)  # Skip the first one since it contains the whole dataset
    for list_patches in iter_list_of_patches:

        list_of_indices = []
        for patch in list_patches:
            index = index_dict[patch]
            list_of_indices.append(index)

        lists_of_indices.append(list_of_indices)

    # ATT. Extract the blocks using the lists of indices
    n = 0
    list_blocks = []
    for list_indices in lists_of_indices:
        ext_blk = create_extract_block(name=block_names[n], source=casefoam, indices=list_indices)
        list_blocks.append(ext_blk)
        n += 1

    # ---------------------------------------- Block - Fluid -----------------------------------------------------------
    # In this section all the needed filters are applied on the Fluid block. This includes streamlines, pressure
    # and velocity contours and mesh visualization.

    # find source
    block_fluid = pvs.FindSource(block_names[0])
    # set active source
    pvs.SetActiveSource(block_fluid)

    # ----------------------------------------- 3: SLICES ----------------------------------------------------------#
    """ This section is dedicated to creating slices from the fluid block and capturing screenshots of them. The slices
    are created from different planes and in a number of different positions defined below. The fields represented on 
    the slices can also be modified."""

    if slices:
        ################################################################################################################
        #                                       MODIFY SLICE PARAMETERS HERE                                           #
        # -------------------------------------------------------------------------------------------------------------#
        slice_views = ["Front", "Side", "Top"]  # ["Front", "Side", "Top"]
        pos_offset = 0.1
        positions_front = np.arange(stl_bounds[0] - pos_offset, stl_bounds[1] + pos_offset, 0.1).tolist()
        positions_side = np.arange(0.001, stl_bounds[3] + pos_offset, 0.1).tolist()
        positions_top = np.arange(0.001, stl_bounds[5] + pos_offset, 0.1).tolist()
        slice_fields = ["p", "U"]  # ["p", "U"]
        slice_fields_units = {
            'p': '[Pa]',
            'U': '[m/s]'
        }
        p_transfer_function_range = [-500, 500]
        u_transfer_function_range = [0, 35]
        ################################################################################################################

        # Set the background color to black.
        pvs.LoadPalette(paletteName='BlackBackground')

        # Hide the fluid block data.
        pvs.Hide(block_fluid, renderView1)

        # Create default slice to initiate
        pvs.SetActiveSource(block_fluid)
        slice1 = pvs.Slice(Input=block_fluid)

        slice1.SliceType = 'Plane'
        slice1.HyperTreeGridSlicer = 'Plane'
        slice1.UseDual = 0
        slice1.Crinkleslice = 0
        slice1.Triangulatetheslice = 1
        slice1.Mergeduplicatedpointsintheslice = 1
        slice1.SliceOffsetValues = [0.0]
        # init the 'Plane' selected for 'SliceType'
        slice1.SliceType.Origin = [1, 3.499022969044745, 3.6059999256394804]
        Hide3DWidgets(proxy=slice1.SliceType)
        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = image_size

        # get layout
        layout1 = pvs.GetLayout()
        for field in slice_fields:

            # Create output folder
            [out_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name], element=field)
            for view in slice_views:
                if view == "Front":
                    positions = positions_front
                elif view == "Side":
                    positions = positions_side
                elif view == "Top":
                    positions = positions_top

                for position in positions:
                    # Set slice and stl position
                    x_cam = slice_views_dictionary[view]['Position'][0]
                    y_cam = slice_views_dictionary[view]['Position'][1]
                    z_cam = slice_views_dictionary[view]['Position'][2]

                    if view == "Front":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [position, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [position, 0.0, 0.0]
                        slice1.SliceType.Normal = [1.0, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam + position, y_cam, z_cam]

                    elif view == "Side":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, position, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, position, 0.0]
                        slice1.SliceType.Normal = [0.0, 1.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 1.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam + position, z_cam]

                    elif view == "Top":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, 0.0, position]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, position]
                        slice1.SliceType.Normal = [0.0, 0.0, 1.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 0.0, 1.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam, z_cam + position]

                    renderView1.CameraFocalPoint = slice_views_dictionary[view]['FocalPoint']
                    renderView1.CameraParallelScale = slice_views_dictionary[view]['ParallelScale']
                    renderView1.CameraViewUp = slice_views_dictionary[view]['ViewUp']

                    # show data in view
                    slice1Display = pvs.Show(slice1, renderView1, 'GeometryRepresentation')

                    # get color transfer function/color map for 'p'
                    pLUT = pvs.GetColorTransferFunction(field)

                    # trace defaults for the display properties.
                    slice1Display.Representation = 'Surface'
                    slice1Display.ColorArrayName = ['CELLS', field]
                    slice1Display.LookupTable = pLUT
                    slice1Display.OSPRayScaleArray = field
                    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    slice1Display.SelectOrientationVectors = 'U'
                    slice1Display.ScaleFactor = 2.8000000000000003
                    slice1Display.SelectScaleArray = field
                    slice1Display.GlyphType = 'Arrow'
                    slice1Display.GlyphTableIndexArray = field
                    slice1Display.GaussianRadius = 0.14
                    slice1Display.SetScaleArray = ['CELLS', field]
                    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
                    slice1Display.OpacityArray = ['CELLS', field]
                    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
                    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
                    slice1Display.PolarAxes = 'PolarAxesRepresentation'

                    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
                    slice1Display.ScaleTransferFunction.Points = [-652.62841796875, 0.0, 0.5, 0.0, 174.41958618164062,
                                                                  1.0,
                                                                  0.5, 0.0]

                    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
                    slice1Display.OpacityTransferFunction.Points = [-652.62841796875, 0.0, 0.5, 0.0, 174.41958618164062,
                                                                    1.0, 0.5, 0.0]

                    # show color bar/color legend
                    slice1Display.SetScalarBarVisibility(renderView1, True)

                    # update the view to ensure updated data information
                    renderView1.Update()

                    # get opacity transfer function/opacity map for 'p'
                    pPWF = pvs.GetOpacityTransferFunction(field)

                    # get color legend/bar for pLUT in view renderView1
                    pLUTColorBar = pvs.GetScalarBar(pLUT, renderView1)

                    # Properties modified on pLUTColorBar
                    pLUTColorBar.AutoOrient = 0
                    pLUTColorBar.Orientation = 'Horizontal'
                    pLUTColorBar.WindowLocation = 'UpperCenter'
                    pLUTColorBar.Title = field
                    pLUTColorBar.ComponentTitle = slice_fields_units[field]
                    pLUTColorBar.HorizontalTitle = 1
                    pLUTColorBar.ScalarBarThickness = 100
                    pLUTColorBar.ScalarBarLength = 0.7
                    pLUTColorBar.TitleFontFamily = 'Arial'
                    pLUTColorBar.TitleBold = 1
                    pLUTColorBar.TitleFontSize = 15
                    pLUTColorBar.LabelFontFamily = 'Arial'
                    pLUTColorBar.LabelItalic = 0
                    pLUTColorBar.LabelFontSize = 12
                    # Properties modified on pLUTColorBar
                    pLUTColorBar.TitleFontFamily = 'File'
                    pLUTColorBar.TitleFontFile = font_path + '\\'+ 'MADFT-Da Mad Rave.ttf'
                    pLUTColorBar.LabelFontFamily = 'File'
                    pLUTColorBar.LabelFontFile = font_path + '\\'+ 'contm.ttf'
                    # Properties modified on pLUTColorBar
                    pLUTColorBar.DrawTickLabels = 0

                    # get color transfer function/color map for 'p'
                    pLUT = pvs.GetColorTransferFunction(field)
                    # get opacity transfer function/opacity map for 'p'
                    pPWF = pvs.GetOpacityTransferFunction(field)

                    if field == "p":
                        transfer_function_range = p_transfer_function_range
                        # Apply a preset using its name.
                        pLUT.ApplyPreset('Cool to Warm (Extended)', True)
                    elif field == "U":
                        transfer_function_range = u_transfer_function_range
                        # Apply a preset using its name.
                        pLUT.ApplyPreset('Viridis (matplotlib)', True)
                    # Rescale transfer function
                    pPWF.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])
                    # Rescale transfer function
                    pLUT.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])

                    # save screenshot

                    file_name = out_folder[0] + "/" + view + "_" + str(position) + ".png"
                    pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

                    if field == "U":
                        # Save surface LIC representation
                        # change representation type
                        slice1Display.SetRepresentationType('Surface LIC')

                        # Properties modified on cARDisplay
                        # slice1Display.SelectInputVectors = ['POINTS', 'U']

                        # save screenshot
                        file_name = out_folder[0] + "/" + "LIC_" + view + "_" + str(position) + ".png"
                        pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

                        # ATT. Add image to list for animation creation.
                        # anim_images.append(Image.open(file_name))

                        # change representation type
                        slice1Display.SetRepresentationType('Surface')

                    # turn off scalar coloring
                    pvs.ColorBy(slice1Display, None)
        pvs.Delete(slice1)
        del slice1
    # ----------------------------------------- 4: STREAMLINES -------------------------------------------------------#
    """ """
    if streamlines:
        ################################################################################################################
        #                                       MODIFY STREAMLINES PARAMETERS HERE                                     #
        # -------------------------------------------------------------------------------------------------------------#
        streamlines_views = ["LSide", "RSide", "Front", "Back", "Isometric", "Top", "Bottom"]
        ################################################################################################################
        # find source
        block_fluid = pvs.FindSource(block_names[0])
        # set active source
        pvs.SetActiveSource(block_fluid)
        # create a new 'Stream Tracer'
        streamTracer1 = pvs.StreamTracer(Input=block_fluid, SeedType='Point Source')
        streamTracer1.SeedType.Radius = 1.2
        streamTracer1.Vectors = ['POINTS', 'U']
        streamTracer1.MaximumStreamlineLength = 28.0
        # create new output folder
        [streamlines_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                           element='Streamline')

        # init the 'High Resolution Line Source' selected for 'SeedType'
        # streamTracer1.SeedType.Point1 = [-8.5, -8.615501894199456e-38, 0.006000000052154064]
        # streamTracer1.SeedType.Point2 = [19.5, 7.0, 7.205999851226807]

        # toggle 3D widget visibility (only when running from the GUI)
        pvs.Show3DWidgets(proxy=streamTracer1.SeedType)

        # Properties modified on streamTracer1
        # streamTracer1.SeedType = 'Point Source'

        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')

        # get layout
        layout1 = pvs.GetLayout()

        # show data in view
        streamTracer1Display = pvs.Show(streamTracer1, renderView1, 'GeometryRepresentation')

        # get color transfer function/color map for 'p'
        pLUT = pvs.GetColorTransferFunction('p')

        # trace defaults for the display properties.
        streamTracer1Display.Representation = 'Surface'
        streamTracer1Display.ColorArrayName = ['POINTS', 'p']
        streamTracer1Display.LookupTable = pLUT
        streamTracer1Display.OSPRayScaleArray = 'p'
        streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
        streamTracer1Display.SelectOrientationVectors = 'Normals'
        streamTracer1Display.ScaleFactor = 2.798934078216553
        streamTracer1Display.SelectScaleArray = 'p'
        streamTracer1Display.GlyphType = 'Arrow'
        streamTracer1Display.GlyphTableIndexArray = 'p'
        streamTracer1Display.GaussianRadius = 0.13994670391082764
        streamTracer1Display.SetScaleArray = ['POINTS', 'p']
        streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
        streamTracer1Display.OpacityArray = ['POINTS', 'p']
        streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
        streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
        streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
        #    streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
        #    streamTracer1Display.WriteLog = ''

        # streamTracer1Display.NumberOfPoints = 200

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        streamTracer1Display.ScaleTransferFunction.Points = [-4663.77783203125, 0.0, 0.5, 0.0, 381.0517272949219, 1.0,
                                                             0.5,
                                                             0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        streamTracer1Display.OpacityTransferFunction.Points = [-4663.77783203125, 0.0, 0.5, 0.0, 381.0517272949219, 1.0,
                                                               0.5, 0.0]

        # hide data in view
        pvs.Hide(block_fluid, renderView1)

        # show color bar/color legend
        streamTracer1Display.SetScalarBarVisibility(renderView1, True)

        # update the view to ensure updated data information
        renderView1.Update()

        # get opacity transfer function/opacity map for 'p'
        pPWF = pvs.GetOpacityTransferFunction('p')

        # show data in view
        stlDisplay = pvs.Show(stl_model, renderView1, 'GeometryRepresentation')

        # get color transfer function/color map for 'STLSolidLabeling'
        sTLSolidLabelingLUT = pvs.GetColorTransferFunction('STLSolidLabeling')

        # trace defaults for the display properties.
        stlDisplay.Representation = 'Surface'
        stlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
        stlDisplay.LookupTable = sTLSolidLabelingLUT
        stlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
        stlDisplay.SelectOrientationVectors = 'None'
        stlDisplay.ScaleFactor = 0.29495136737823485
        stlDisplay.SelectScaleArray = 'STLSolidLabeling'
        stlDisplay.GlyphType = 'Arrow'
        stlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
        stlDisplay.GaussianRadius = 0.014747568368911744
        stlDisplay.SetScaleArray = [None, '']
        stlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
        stlDisplay.OpacityArray = [None, '']
        stlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
        stlDisplay.DataAxesGrid = 'GridAxesRepresentation'
        stlDisplay.PolarAxes = 'PolarAxesRepresentation'
        #   stlDisplay.SelectInputVectors = [None, '']
        #   stlDisplay.WriteLog = ''

        # show color bar/color legend
        stlDisplay.SetScalarBarVisibility(renderView1, True)

        # update the view to ensure updated data information
        renderView1.Update()

        # get opacity transfer function/opacity map for 'STLSolidLabeling'
        sTLSolidLabelingPWF = pvs.GetOpacityTransferFunction('STLSolidLabeling')

        # turn off scalar coloring
        pvs.ColorBy(stlDisplay, None)

        # Hide the scalar bar for this color map if no visible data is colored by it.
        pvs.HideScalarBarIfNotNeeded(sTLSolidLabelingLUT, renderView1)

        # set active source
        pvs.SetActiveSource(streamTracer1)

        # toggle 3D widget visibility (only when running from the GUI)
        pvs.Show3DWidgets(proxy=streamTracer1.SeedType)

        # set scalar coloring
        pvs.ColorBy(streamTracer1Display, ('POINTS', 'U', 'Magnitude'))

        # Hide the scalar bar for this color map if no visible data is colored by it.
        pvs.HideScalarBarIfNotNeeded(pLUT, renderView1)

        # rescale color and/or opacity maps used to include current data range
        streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

        # show color bar/color legend
        streamTracer1Display.SetScalarBarVisibility(renderView1, True)

        # get color transfer function/color map for 'U'
        uLUT = pvs.GetColorTransferFunction('U')

        # get opacity transfer function/opacity map for 'U'
        uPWF = pvs.GetOpacityTransferFunction('U')

        # rescale color and/or opacity maps used to exactly fit the current data range
        streamTracer1Display.RescaleTransferFunctionToDataRange(False, True)

        # Properties modified on streamTracer1Display
        streamTracer1Display.RenderLinesAsTubes = 1

        # Properties modified on streamTracer1Display
        streamTracer1Display.LineWidth = 3.0

        # toggle 3D widget visibility (only when running from the GUI)
        pvs.Hide3DWidgets(proxy=streamTracer1.SeedType)

        # update the view to ensure updated data information
        renderView1.Update()

        # update the view to ensure updated data information
        renderView1.Update()

        # Rescale transfer function
        uLUT.RescaleTransferFunction(0.0, 30.0)

        # Rescale transfer function
        uPWF.RescaleTransferFunction(0.0, 30.0)

        pvs.LoadPalette(paletteName='BlackBackground')

        for view in streamlines_views:
            # current stl placement for renderView1
            renderView1.CameraPosition = stl_views_dictionary[view]["Position"]
            renderView1.CameraFocalPoint = stl_views_dictionary[view]["FocalPoint"]
            renderView1.CameraViewUp = stl_views_dictionary[view]["ViewUp"]
            renderView1.CameraParallelScale = stl_views_dictionary[view]["ParallelScale"]

            # save screenshot
            file_name = streamlines_folder[0] + '/' + view + ".png"
            pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

        # Hide stl
        pvs.Hide(stl_model, renderView1)
        # Hide streamlines
        pvs.Hide(streamTracer1, renderView1)
    # --------------------------- 5:SURFACE PLOTS: PRESSURE, WALL SHEAR STRESS AND Y+ ---------------------------------#
    """ This section is dedicated to extracting surface data and creating surface plots for pressure, wall shear stress
    and y+."""
    # __________________________________________________________________________________________________________________
    # ---------------------------------------- Block - CAR -------------------------------------------------------------
    # In this section all the needed filters are applied on the CAR block. This includes lift and drag representations
    # and integration, pressure field on the car surfaces and y+ plot.

    # find source
    block_car = pvs.FindSource('CAR')

    # set active source
    pvs.SetActiveSource(block_car)

    if surface_plots:
        ####################################################################################################################
        #                                    MODIFY SURFACE PLOTS PARAMETERS HERE                                          #
        # -----------------------------------------------------------------------------------------------------------------#
        surface_fields = ["p", "wallShearStress", "yPlus"]
        surface_fields_units = {
            'p': '[Pa]',
            'wallShearStress': '[Pa]',
            'yPlus': ' '
        }
        surface_views = ["RSide", "Front", "Back", "Isometric", "Top", "Bottom"]
        yplus_transfer_function_range = [0, 1000]
        p_transfer_function_range = [-350, 350]
        wallshearstress_transfer_function_range = [0, 3.5]
        ####################################################################################################################

        # create a new 'Extract Surface'
        extractSurface1 = pvs.ExtractSurface(Input=block_car)

        for field in surface_fields:
            # create output folder
            [surf_field_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                              element=field+ '  Surface')
            # get active view
            renderView1 = pvs.GetActiveViewOrCreate('RenderView')
            # uncomment following to set a specific view size
            renderView1.ViewSize = image_size

            # get layout
            layout1 = pvs.GetLayout()

            # show data in view
            extractSurface1Display = pvs.Show(extractSurface1, renderView1, 'GeometryRepresentation')

            # get color transfer function/color map for 'p'
            pLUT = pvs.GetColorTransferFunction(field)

            # trace defaults for the display properties.
            extractSurface1Display.Representation = 'Surface'
            extractSurface1Display.ColorArrayName = ['CELLS', field]
            extractSurface1Display.LookupTable = pLUT
            extractSurface1Display.OSPRayScaleArray = field
            extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
            extractSurface1Display.SelectOrientationVectors = 'U'
            extractSurface1Display.ScaleFactor = 0.29279640913009647
            extractSurface1Display.SelectScaleArray = field
            extractSurface1Display.GlyphType = 'Arrow'
            extractSurface1Display.GlyphTableIndexArray = field
            extractSurface1Display.GaussianRadius = 0.014639820456504821
            extractSurface1Display.SetScaleArray = ['CELLS', field]
            extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
            extractSurface1Display.OpacityArray = ['CELLS', field]
            extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
            extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
            extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'
            #        extractSurface1Display.SelectInputVectors = ['POINTS', 'U']
            #        extractSurface1Display.WriteLog = ''

            # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
            extractSurface1Display.ScaleTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656, 1.0,
                                                                   0.5, 0.0]

            # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
            extractSurface1Display.OpacityTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656,
                                                                     1.0,
                                                                     0.5, 0.0]

            # reset view to fit data
            renderView1.ResetCamera()

            # get the material library
            materialLibrary1 = pvs.GetMaterialLibrary()

            # show color bar/color legend
            extractSurface1Display.SetScalarBarVisibility(renderView1, True)

            # update the view to ensure updated data information
            renderView1.Update()

            # get opacity transfer function/opacity map for 'p'
            pPWF = pvs.GetOpacityTransferFunction(field)

            # get color legend/bar for pLUT in view renderView1
            pLUTColorBar = pvs.GetScalarBar(pLUT, renderView1)

            if field == "p":
                transfer_function_range = p_transfer_function_range

                pLUTColorBar.UseCustomLabels = 0
                # Apply a preset using its name.
                pLUT.ApplyPreset('Cool to Warm (Extended)', True)
            elif field == "yPlus":
                # Import color preset
                transfer_function_range = yplus_transfer_function_range
                # Apply a preset using its name.
                pLUT.ApplyPreset('Rainbow Desaturated', True)

                # Properties modified on yPlusLUTColorBar
                pLUTColorBar.UseCustomLabels = 1
                # Properties modified on yPlusLUTColorBar
                pLUTColorBar.CustomLabels = [0.0, 1.0, 3.0, 30.0, 100.0, 300.0, 1000.0]
                pLUT.RGBPoints = [0.0, 0.0, 0.0, 0.5625, 1.0, 0.0, 0.0, 1.0, 5.0, 0.0, 1.0, 1.0, 30.0, 0.5, 1.0, 0.5,
                                  100.0, 1.0, 1.0, 0.0, 300.0, 1.0, 0.0, 0.0, 1000.0, 0.5, 0.0, 0.0]
            elif field == "wallShearStress":
                transfer_function_range = wallshearstress_transfer_function_range

                pLUTColorBar.UseCustomLabels = 0
                # Apply a preset using its name.
                pLUT.ApplyPreset('Viridis (matplotlib)', True)

            for view in surface_views:

                # current stl placement for renderView1
                renderView1.CameraPosition = car_views_dictionary[view]["Position"]
                renderView1.CameraFocalPoint = car_views_dictionary[view]["FocalPoint"]
                renderView1.CameraViewUp = car_views_dictionary[view]["ViewUp"]
                renderView1.CameraParallelScale = car_views_dictionary[view]["ParallelScale"]

                # Properties modified on pLUTColorBar
                pLUTColorBar.AutoOrient = 0
                pLUTColorBar.Orientation = 'Horizontal'
                pLUTColorBar.WindowLocation = 'UpperCenter'
                pLUTColorBar.Title = field
                pLUTColorBar.ComponentTitle = surface_fields_units[field]
                pLUTColorBar.HorizontalTitle = 1
                pLUTColorBar.ScalarBarThickness = 100
                pLUTColorBar.ScalarBarLength = 0.7
                pLUTColorBar.TitleFontFamily = 'Arial'
                pLUTColorBar.TitleBold = 1
                pLUTColorBar.TitleFontSize = 15
                pLUTColorBar.LabelFontFamily = 'Arial'
                pLUTColorBar.LabelItalic = 0
                pLUTColorBar.LabelFontSize = 12
                # Properties modified on pLUTColorBar
                pLUTColorBar.TitleFontFamily = 'File'
                pLUTColorBar.TitleFontFile = font_path + '\\'+ 'MADFT-Da Mad Rave.ttf'
                pLUTColorBar.LabelFontFamily = 'File'
                pLUTColorBar.LabelFontFile = font_path + '\\' '/contm.ttf'
                # Properties modified on pLUTColorBar
                pLUTColorBar.DrawTickLabels = 0

                # Rescale transfer function
                pPWF.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])
                # Rescale transfer function
                pLUT.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])
                print(surf_field_folder)
                # save screenshot
                file_name = surf_field_folder[0] + '/' + "Surface" + "_" + view + ".png"
                pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

                if field == "p":
                    # Save surface LIC representation
                    # change representation type
                    extractSurface1Display.SetRepresentationType('Surface LIC')

                    # Properties modified on cARDisplay
                    #                extractSurface1Display.SelectInputVectors = ['CELLS', 'wallShearStress']

                    # save screenshot
                    file_name = surf_field_folder[0] + '/' + "Surface" + "_LIC_" + view + ".png"
                    pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

                    # change representation type
                    extractSurface1Display.SetRepresentationType('Surface')

            # turn off scalar coloring
            pvs.ColorBy(extractSurface1Display, None)

            # show color bar/color legend
            extractSurface1Display.SetScalarBarVisibility(renderView1, False)

            # Delete view
            pvs.Delete(renderView1)
            del renderView1

    # ------------------------------------------ 6:CP PLOTS ----------------------------------------------------------#
    """ This section is dedicated to calculating and plotting Cp values. 
    """
    if cp_plots:
        ####################################################################################################################
        #                                    MODIFY CP PLOTS PARAMETERS HERE                                               #
        # -----------------------------------------------------------------------------------------------------------------#
        cp_fields = ["Cp", "Cpz", "Cpx"]
        cp_views = ["RSide", "Front", "Back", "Isometric", "Top", "Bottom"]  # Views to take screenshots from
        cp_range = [-3, 1]  # Color bar range
        pref = 0  # Freestream pressure
        ####################################################################################################################
        extractSurface1 = pvs.ExtractSurface(Input=block_car)
        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = image_size

        # get layout
        layout1 = pvs.GetLayout()
        # show data in view
        extractSurface1Display = pvs.Show(extractSurface1, renderView1, 'GeometryRepresentation')

        pLUT = pvs.GetColorTransferFunction('p')
        # trace defaults for the display properties.
        extractSurface1Display.Representation = 'Surface'
        extractSurface1Display.ColorArrayName = ['CELLS', 'p']
        extractSurface1Display.LookupTable = pLUT
        extractSurface1Display.OSPRayScaleArray = 'p'
        extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
        extractSurface1Display.SelectOrientationVectors = 'U'
        extractSurface1Display.ScaleFactor = 0.29279640913009647
        extractSurface1Display.SelectScaleArray = 'p'
        extractSurface1Display.GlyphType = 'Arrow'
        extractSurface1Display.GlyphTableIndexArray = 'p'
        extractSurface1Display.GaussianRadius = 0.014639820456504821
        extractSurface1Display.SetScaleArray = ['CELLS', 'p']
        extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
        extractSurface1Display.OpacityArray = ['CELLS', 'p']
        extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
        extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
        extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'
        #        extractSurface1Display.SelectInputVectors = ['POINTS', 'U']
        #        extractSurface1Display.WriteLog = ''

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        extractSurface1Display.ScaleTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656, 1.0,
                                                               0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        extractSurface1Display.OpacityTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656,
                                                                 1.0,
                                                                 0.5, 0.0]

        # get active view
        render_view_cp = pvs.GetActiveViewOrCreate('RenderView')
        # create a new 'Generate Surface Normals'
        generateSurfaceNormals1 = pvs.GenerateSurfaceNormals(Input=extractSurface1)

        # hide data in view
        pvs.Hide(extractSurface1, render_view_cp)

        for field in cp_fields:
            # create output folder
            [cp_field_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name], element=field)
            # get active view
            render_view_cp = pvs.GetActiveViewOrCreate('RenderView')
            # create a new 'Calculator'
            calculator1 = pvs.Calculator(Input=generateSurfaceNormals1)
            calculator1.Function = ''
            # Properties modified on calculator1
            calculator1.AttributeType = 'Point Data'
            calculator1.ResultArrayName = field

            if field == "Cp":
                calculator1.Function = '(p-{})/(0.5*{}*{}^2)'.format(pref, rho_air, fs_velocity)
            elif field == "Cpz":
                calculator1.Function = '(Normals_Z*p-{})/(0.5*{}*{}^2)'.format(pref, rho_air, fs_velocity)
            elif field == "Cpx":
                calculator1.Function = '(Normals_X*p-{})/(0.5*{}*{}^2)'.format(pref, rho_air, fs_velocity)

            # show data in view
            calculator1Display = pvs.Show(calculator1, render_view_cp, 'GeometryRepresentation')

            # get color transfer function/color map for field
            cpLUT = pvs.GetColorTransferFunction(field)
            # get opacity transfer function/opacity map for field
            cpPWF = pvs.GetOpacityTransferFunction(field)

            # trace defaults for the display properties.
            calculator1Display.Representation = 'Surface'
            calculator1Display.ColorArrayName = ['POINTS', field]
            calculator1Display.LookupTable = cpLUT
            calculator1Display.OSPRayScaleArray = field
            calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
            calculator1Display.SelectOrientationVectors = 'U'
            calculator1Display.ScaleFactor = 0.29279640913009647
            calculator1Display.SelectScaleArray = field
            calculator1Display.GlyphType = 'Arrow'
            calculator1Display.GlyphTableIndexArray = field
            calculator1Display.GaussianRadius = 0.014639820456504821
            calculator1Display.SetScaleArray = ['POINTS', field]
            calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
            calculator1Display.OpacityArray = ['POINTS', field]
            calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
            calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
            calculator1Display.PolarAxes = 'PolarAxesRepresentation'
            #        calculator1Display.SelectInputVectors = ['POINTS', 'U']
            #        calculator1Display.WriteLog = ''

            # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
            calculator1Display.ScaleTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656, 1.0,
                                                               0.5,
                                                               0.0]

            # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
            calculator1Display.OpacityTransferFunction.Points = [-1059931.125, 0.0, 0.5, 0.0, 195.88905334472656, 1.0,
                                                                 0.5,
                                                                 0.0]

            # hide data in view
            pvs.Hide(generateSurfaceNormals1, render_view_cp)

            # show color bar/color legend
            calculator1Display.SetScalarBarVisibility(render_view_cp, True)

            # update the view to ensure updated data information
            render_view_cp.Update()

            # test
            render_view_cp = pvs.GetActiveViewOrCreate('RenderView')

            # get color legend/bar for cpLUT in view renderView2
            # cpLUT = pvs.GetScalarBar(cpLUT, render_view_cp)

            # get color legend/bar for pLUT in view renderView1
            cpLUTColorBar = pvs.GetScalarBar(cpLUT, render_view_cp)

            for view in cp_views:
                # current stl placement for renderView2
                render_view_cp.CameraPosition = car_views_dictionary[view]["Position"]
                render_view_cp.CameraFocalPoint = car_views_dictionary[view]["FocalPoint"]
                render_view_cp.CameraViewUp = car_views_dictionary[view]["ViewUp"]
                render_view_cp.CameraParallelScale = car_views_dictionary[view]["ParallelScale"]

                # Properties modified on pLUTColorBar
                cpLUTColorBar.AutoOrient = 0
                cpLUTColorBar.Orientation = 'Horizontal'
                cpLUTColorBar.WindowLocation = 'UpperCenter'
                cpLUTColorBar.Title = field
                cpLUTColorBar.ComponentTitle = ''
                cpLUTColorBar.HorizontalTitle = 1
                cpLUTColorBar.ScalarBarThickness = 10
                cpLUTColorBar.ScalarBarLength = 0.7
                cpLUTColorBar.TitleFontFamily = 'File'
                cpLUTColorBar.TitleFontFile = font_path + '\\' + '/MADFT-Da Mad Rave.ttf'
                cpLUTColorBar.TitleBold = 1
                cpLUTColorBar.TitleFontSize = 15
                cpLUTColorBar.LabelFontFamily = 'File'
                cpLUTColorBar.LabelFontFile = font_path + '\\' + '/contm.ttf'
                cpLUTColorBar.LabelItalic = 0
                cpLUTColorBar.LabelFontSize = 12
                cpLUTColorBar.DrawTickLabels = 0

                transfer_function_range = cp_range
                # Apply a preset using its name.
                cpLUT.ApplyPreset('Cool to Warm', True)
                # Properties modified on cpLUTColorBar
                cpLUTColorBar.UseCustomLabels = 0
                # Properties modified on cpLUT
                cpLUT.RGBPoints = [-3.0, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 1.0,
                                   0.705882352941, 0.0156862745098, 0.149019607843]

                # Rescale transfer function
                cpPWF.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])
                # Rescale transfer function
                cpLUT.RescaleTransferFunction(transfer_function_range[0], transfer_function_range[1])

                # save screenshot
                file_name = cp_field_folder[0] + "/" + "Surface" + "_" + view + ".png"
                pvs.SaveScreenshot(file_name, render_view_cp, ImageResolution=image_size)

            # Delete view
            pvs.Delete(render_view_cp)
            del render_view_cp

            # destroy calculator and surface normals
            pvs.Delete(calculator1)
            del calculator1
        del extractSurface1
    # ------------------------------------------ 7:LINE PLOTS ---------------------------------------------------------#

    # ----------------------------------------- 8: PT PLOTS ----------------------------------------------------------#
    # find source
    block_fluid = pvs.FindSource("Block - Fluid")

    # set active source
    pvs.SetActiveSource(block_fluid)
    if pt_slices:
        ################################################################################################################
        #                                       MODIFY SLICE PARAMETERS HERE                                           #
        # -------------------------------------------------------------------------------------------------------------#
        slice_views = ["Front", "Side", "Top"]  # ["Front", "Side", "Top"]
        pos_offset = 0.1
        positions_front = np.arange(stl_bounds[0] - pos_offset, stl_bounds[1] + pos_offset, 0.1).tolist()
        positions_side = np.arange(0.001, stl_bounds[3] + pos_offset, 0.1).tolist()
        positions_top = np.arange(0.001, stl_bounds[5] + pos_offset, 0.1).tolist()
        pt_transfer_function_range = [-500, 500]
        ################################################################################################################

        # Set the background color to black.
        pvs.LoadPalette(paletteName='BlackBackground')

        # Hide the fluid block data.
        pvs.Hide(block_fluid, renderView1)

        # Create output folder
        [out_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name], element='Pt')

        #  Calculator creation
        # create a new 'Calculator'
        calculator1 = pvs.Calculator(Input=block_fluid)

        # Properties on calculator
        calculator1.ResultArrayName = 'Pt'
        calculator1.Function = '0.5*1.196*(mag(U))^2+p'

        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')

        renderView1.ViewSize = image_size

        # get layout
        layout1 = pvs.GetLayout()

        # show data in view
        calculator1Display = pvs.Show(calculator1, renderView1, 'GeometryRepresentation')

        # get color transfer function/color map for 'Pt'
        ptLUT = pvs.GetColorTransferFunction('Pt')
        ptLUT.RGBPoints = [-3188.463134765625, 0.231373, 0.298039, 0.752941, -1065.7987695620723, 0.865003, 0.865003,
                           0.865003, 1056.8655956414805, 0.705882, 0.0156863, 0.14902]
        ptLUT.ScalarRangeInitialized = 1.0

        # trace defaults for the display properties.
        calculator1Display.Representation = 'Surface'
        calculator1Display.ColorArrayName = ['POINTS', 'Pt']
        calculator1Display.LookupTable = ptLUT
        calculator1Display.OSPRayScaleArray = 'Pt'
        calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
        calculator1Display.SelectOrientationVectors = 'U'
        calculator1Display.ScaleFactor = 2.8000000000000003
        calculator1Display.SelectScaleArray = 'Pt'
        calculator1Display.GlyphType = 'Arrow'
        calculator1Display.GlyphTableIndexArray = 'Pt'
        calculator1Display.GaussianRadius = 0.14
        calculator1Display.SetScaleArray = ['POINTS', 'Pt']
        calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
        calculator1Display.OpacityArray = ['POINTS', 'Pt']
        calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
        calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
        calculator1Display.PolarAxes = 'PolarAxesRepresentation'

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        calculator1Display.ScaleTransferFunction.Points = [-3188.463134765625, 0.0, 0.5, 0.0, 1056.8655956414805, 1.0,
                                                           0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        calculator1Display.OpacityTransferFunction.Points = [-3188.463134765625, 0.0, 0.5, 0.0, 1056.8655956414805, 1.0,
                                                             0.5, 0.0]

        # hide data in view
        pvs.Hide(casefoam, renderView1)

        # show color bar/color legend
        calculator1Display.SetScalarBarVisibility(renderView1, True)

        # update the view to ensure updated data information
        renderView1.Update()

        # get opacity transfer function/opacity map for 'Pt'
        ptPWF = pvs.GetOpacityTransferFunction('Pt')
        ptPWF.Points = [-3188.463134765625, 0.0, 0.5, 0.0, 1056.8655956414805, 1.0, 0.5, 0.0]
        ptPWF.ScalarRangeInitialized = 1

        # Rescale transfer function
        ptLUT.RescaleTransferFunction(-500.0, 500.0)

        # Rescale transfer function
        ptPWF.RescaleTransferFunction(-500.0, 500.0)

        for view in slice_views:
            if view == "Front":
                positions = positions_front
            elif view == "Side":
                positions = positions_side
            elif view == "Top":
                positions = positions_top

            for position in positions:
                # set active source
                pvs.SetActiveSource(calculator1)
                slice1 = pvs.Slice(Input=calculator1)

                slice1.SliceType = 'Plane'
                slice1.HyperTreeGridSlicer = 'Plane'
                slice1.UseDual = 0
                slice1.Crinkleslice = 0
                slice1.Triangulatetheslice = 1
                slice1.Mergeduplicatedpointsintheslice = 1
                slice1.SliceOffsetValues = [0.0]

                # toggle 3D widget visibility (only when running from the GUI)
                pvs.Hide3DWidgets(proxy=slice1.SliceType)

                # get active view
                renderView1 = pvs.GetActiveViewOrCreate('RenderView')
                # uncomment following to set a specific view size
                renderView1.ViewSize = image_size

                # get layout
                layout1 = pvs.GetLayout()

                # Set slice and stl position
                x_cam = slice_views_dictionary[view]['Position'][0]
                y_cam = slice_views_dictionary[view]['Position'][1]
                z_cam = slice_views_dictionary[view]['Position'][2]

                if view == "Front":
                    # Properties modified on slice1.SliceType
                    slice1.SliceType.Origin = [position, 0.0, 0.0]
                    slice1.HyperTreeGridSlicer.Origin = [position, 0.0, 0.0]
                    slice1.SliceType.Normal = [1.0, 0.0, 0.0]
                    slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]

                    # current stl placement for renderView1
                    renderView1.CameraPosition = [x_cam + position, y_cam, z_cam]

                elif view == "Side":
                    # Properties modified on slice1.SliceType
                    slice1.SliceType.Origin = [0.0, position, 0.0]
                    slice1.HyperTreeGridSlicer.Origin = [0.0, position, 0.0]
                    slice1.SliceType.Normal = [0.0, 1.0, 0.0]
                    slice1.HyperTreeGridSlicer.Normal = [0.0, 1.0, 0.0]

                    # current stl placement for renderView1
                    renderView1.CameraPosition = [x_cam, y_cam + position, z_cam]

                elif view == "Top":
                    # Properties modified on slice1.SliceType
                    slice1.SliceType.Origin = [0.0, 0.0, position]
                    slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, position]
                    slice1.SliceType.Normal = [0.0, 0.0, 1.0]
                    slice1.HyperTreeGridSlicer.Normal = [0.0, 0.0, 1.0]

                    # current stl placement for renderView1
                    renderView1.CameraPosition = [x_cam, y_cam, z_cam + position]

                renderView1.CameraFocalPoint = slice_views_dictionary[view]['FocalPoint']
                renderView1.CameraParallelScale = slice_views_dictionary[view]['ParallelScale']
                renderView1.CameraViewUp = slice_views_dictionary[view]['ViewUp']

                # show data in view
                slice1Display = pvs.Show(slice1, renderView1, 'GeometryRepresentation')

                # get color transfer function/color map for 'p'
                pLUT = pvs.GetColorTransferFunction('Pt')

                # trace defaults for the display properties.
                slice1Display.Representation = 'Surface'
                slice1Display.ColorArrayName = ['POINTS', 'Pt']
                slice1Display.LookupTable = ptLUT
                slice1Display.OSPRayScaleArray = 'Pt'
                slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                slice1Display.SelectOrientationVectors = 'U'
                slice1Display.ScaleFactor = 2.8000000000000003
                slice1Display.SelectScaleArray = 'Pt'
                slice1Display.GlyphType = 'Arrow'
                slice1Display.GlyphTableIndexArray = 'Pt'
                slice1Display.GaussianRadius = 0.14
                slice1Display.SetScaleArray = ['POINTS', 'Pt']
                slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
                slice1Display.OpacityArray = ['POINTS', 'Pt']
                slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
                slice1Display.DataAxesGrid = 'GridAxesRepresentation'
                slice1Display.PolarAxes = 'PolarAxesRepresentation'

                # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
                slice1Display.ScaleTransferFunction.Points = [-652.62841796875, 0.0, 0.5, 0.0, 174.41958618164062,
                                                              1.0,
                                                              0.5, 0.0]

                # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
                slice1Display.OpacityTransferFunction.Points = [-652.62841796875, 0.0, 0.5, 0.0, 174.41958618164062,
                                                                1.0, 0.5, 0.0]

                # show color bar/color legend
                slice1Display.SetScalarBarVisibility(renderView1, True)

                # update the view to ensure updated data information
                renderView1.Update()

                # get opacity transfer function/opacity map for 'p'
                pPWF = pvs.GetOpacityTransferFunction('Pt')

                # get color legend/bar for pLUT in view renderView1
                pLUTColorBar = pvs.GetScalarBar(pLUT, renderView1)

                # Properties modified on pLUTColorBar
                pLUTColorBar.AutoOrient = 0
                pLUTColorBar.Orientation = 'Horizontal'
                pLUTColorBar.WindowLocation = 'UpperCenter'
                pLUTColorBar.Title = 'Pt'
                pLUTColorBar.ComponentTitle = '[Pa]'
                pLUTColorBar.HorizontalTitle = 1
                pLUTColorBar.ScalarBarThickness = 100
                pLUTColorBar.ScalarBarLength = 0.7
                pLUTColorBar.TitleFontFamily = 'Arial'
                pLUTColorBar.TitleBold = 1
                pLUTColorBar.TitleFontSize = 15
                pLUTColorBar.LabelFontFamily = 'Arial'
                pLUTColorBar.LabelItalic = 0
                pLUTColorBar.LabelFontSize = 12
                # Properties modified on pLUTColorBar
                pLUTColorBar.TitleFontFamily = 'File'
                pLUTColorBar.TitleFontFile = font_path + '\\' + '/MADFT-Da Mad Rave.ttf'
                pLUTColorBar.LabelFontFamily = 'File'
                pLUTColorBar.LabelFontFile = font_path + '\\' + '/contm.ttf'
                # Properties modified on pLUTColorBar
                pLUTColorBar.DrawTickLabels = 0

                # get color transfer function/color map for 'p'
                pLUT = pvs.GetColorTransferFunction('Pt')
                # get opacity transfer function/opacity map for 'p'
                pPWF = pvs.GetOpacityTransferFunction('Pt')

                # Rescale transfer function
                pPWF.RescaleTransferFunction(pt_transfer_function_range[0], pt_transfer_function_range[1])
                # Rescale transfer function
                pLUT.RescaleTransferFunction(pt_transfer_function_range[0], pt_transfer_function_range[1])

                # save screenshot

                file_name = out_folder[0] + "/" + view + "_" + str(position) + ".png"
                pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

                # turn off scalar coloring
                pvs.ColorBy(slice1Display, None)

                # destroy slice1
                pvs.Delete(slice1)
                del slice1

            # Delete view
        pvs.Delete(renderView1)
        del renderView1
    # ---------------------------------------- 9: ISOSURFACES ---------------------------------------------------------#
    if isosurfaces:
        downforce_fraction = 0.2
        vel_isos = np.sqrt(downforce_fraction) * fs_velocity
        isosurf_views = ["LSide", "RSide", "Front", "Back", "Isometric", "Top", "Bottom"]
        # create new output folder
        [isosurf_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                       element='Isosurfaces')
        # find source
        block_fluid = pvs.FindSource(block_names[0])
        # set active source
        pvs.SetActiveSource(block_fluid)
        # create a new 'Calculator'
        calculator1 = pvs.Calculator(Input=casefoam)
        calculator1.ResultArrayName = 'mag(U)'
        calculator1.Function = 'mag(U)'
        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = image_size
        # show data in view
        calculator1Display = pvs.Show(calculator1, renderView1, 'UnstructuredGridRepresentation')
        # get color transfer function/color map for 'magU'
        magULUT = pvs.GetColorTransferFunction('magU')
        magULUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 27.62091694121763, 0.865003, 0.865003, 0.865003,
                             55.24183388243526, 0.705882, 0.0156863, 0.14902]
        magULUT.ScalarRangeInitialized = 1.0

        # get opacity transfer function/opacity map for 'magU'
        magUPWF = pvs.GetOpacityTransferFunction('magU')
        magUPWF.Points = [0.0, 0.0, 0.5, 0.0, 55.24183388243526, 1.0, 0.5, 0.0]
        magUPWF.ScalarRangeInitialized = 1

        # trace defaults for the display properties.
        calculator1Display.Representation = 'Surface'
        calculator1Display.ColorArrayName = ['POINTS', 'mag(U)']
        calculator1Display.LookupTable = magULUT
        calculator1Display.OSPRayScaleArray = 'mag(U)'
        calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
        calculator1Display.SelectOrientationVectors = 'U'
        calculator1Display.ScaleFactor = 2.8000000000000003
        calculator1Display.SelectScaleArray = 'mag(U)'
        calculator1Display.GlyphType = 'Arrow'
        calculator1Display.GlyphTableIndexArray = 'mag(U)'
        calculator1Display.GaussianRadius = 0.14
        calculator1Display.SetScaleArray = ['POINTS', 'mag(U)']
        calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
        calculator1Display.OpacityArray = ['POINTS', 'mag(U)']
        calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
        calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
        calculator1Display.PolarAxes = 'PolarAxesRepresentation'
        calculator1Display.ScalarOpacityFunction = magUPWF
        calculator1Display.ScalarOpacityUnitDistance = 0.09416985440514324
        calculator1Display.ExtractedBlockIndex = 1

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 55.24183388243526, 1.0, 0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 55.24183388243526, 1.0, 0.5, 0.0]

        # hide data in view
        pvs.Hide(casefoam, renderView1)

        # show color bar/color legend
        calculator1Display.SetScalarBarVisibility(renderView1, True)

        # update the view to ensure updated data information
        renderView1.Update()
        # create a new 'Contour'
        contour1 = pvs.Contour(Input=calculator1)
        contour1.ContourBy = ['POINTS', 'mag(U)']
        contour1.Isosurfaces = [27.62091694121763]
        contour1.PointMergeMethod = 'Uniform Binning'

        # Properties modified on contour1
        contour1.Isosurfaces = [vel_isos]

        # show data in view
        contour1Display = pvs.Show(contour1, renderView1, 'GeometryRepresentation')

        # trace defaults for the display properties.
        contour1Display.Representation = 'Surface'
        contour1Display.ColorArrayName = ['POINTS', 'mag(U)']
        contour1Display.LookupTable = magULUT
        contour1Display.OSPRayScaleArray = 'mag(U)'
        contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
        contour1Display.SelectOrientationVectors = 'U'
        contour1Display.ScaleFactor = 0.4401813864707947
        contour1Display.SelectScaleArray = 'mag(U)'
        contour1Display.GlyphType = 'Arrow'
        contour1Display.GlyphTableIndexArray = 'mag(U)'
        contour1Display.GaussianRadius = 0.022009069323539736
        contour1Display.SetScaleArray = ['POINTS', 'mag(U)']
        contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
        contour1Display.OpacityArray = ['POINTS', 'mag(U)']
        contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
        contour1Display.DataAxesGrid = 'GridAxesRepresentation'
        contour1Display.PolarAxes = 'PolarAxesRepresentation'

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        contour1Display.ScaleTransferFunction.Points = [5.0, 0.0, 0.5, 0.0, 5.0009765625, 1.0, 0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        contour1Display.OpacityTransferFunction.Points = [5.0, 0.0, 0.5, 0.0, 5.0009765625, 1.0, 0.5, 0.0]

        # hide data in view
        pvs.Hide(calculator1, renderView1)

        # show color bar/color legend
        contour1Display.SetScalarBarVisibility(renderView1, True)

        # update the view to ensure updated data information
        renderView1.Update()

        # hide data in view
        pvs.Hide(contour1, renderView1)

        # set active source
        pvs.SetActiveSource(contour1)

        # show data in view
        contour1Display = pvs.Show(contour1, renderView1, 'GeometryRepresentation')

        # show color bar/color legend
        contour1Display.SetScalarBarVisibility(renderView1, True)

        # reset view to fit data
        renderView1.ResetCamera()

        axesGrid = renderView1.AxesGrid
        axesGrid.Visibility = 1

        pvs.Show(stl_model, renderView1)

        # update the view to ensure updated data information
        renderView1.Update()

        for view in isosurf_views:
            # current stl placement for renderView1
            renderView1.CameraPosition = stl_views_dictionary[view]["Position"]
            renderView1.CameraFocalPoint = stl_views_dictionary[view]["FocalPoint"]
            renderView1.CameraViewUp = stl_views_dictionary[view]["ViewUp"]
            renderView1.CameraParallelScale = stl_views_dictionary[view]["ParallelScale"]

            # save screenshot
            file_name = isosurf_folder[0] + '/' + view + ".png"
            pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)
        pvs.Delete(contour1)
    # ----------------------------------------- 10: MESH ANALYSIS -----------------------------------------------------#
    if mesh:
        # find source
        block_fluid = pvs.FindSource(block_names[0])
        # set active source
        pvs.SetActiveSource(block_fluid)

        # Set the background color to black.
        pvs.LoadPalette(paletteName='BlackBackground')

        # Hide the fluid block data.
        pvs.Hide(block_fluid, renderView1)

        # Create default slice to initiate
        pvs.SetActiveSource(block_fluid)
        slice1 = pvs.Slice(Input=block_fluid)

        slice1.SliceType = 'Plane'
        slice1.HyperTreeGridSlicer = 'Plane'
        slice1.UseDual = 0
        slice1.Crinkleslice = 0
        slice1.Triangulatetheslice = 1
        slice1.Mergeduplicatedpointsintheslice = 1
        slice1.SliceOffsetValues = [0.0]
        # init the 'Plane' selected for 'SliceType'
        slice1.SliceType.Origin = [1, 3.499022969044745, 3.6059999256394804]
        # get active view
        renderView1 = pvs.GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = image_size

        # get layout
        layout1 = pvs.GetLayout()
        # show data in view
        slice1Display = pvs.Show(slice1, renderView1, 'GeometryRepresentation')
        slice1Display.SetRepresentationType('Surface With Edges')
        # set scalar coloring
        pvs.ColorBy(slice1Display, 'None')
        # turn off scalar coloring
        pvs.ColorBy(slice1Display, None)

        if mesh_focus:
            ########################################################################################################
            #                                       MODIFY SLICE PARAMETERS HERE                                   #
            # -----------------------------------------------------------------------------------------------------#
            slice_views = ["Front", "Side", "Top"]  # ["Front", "Side", "Top"]
            pos_offset = 0.05
            positions_front = np.arange(part_bounds[0] - pos_offset, part_bounds[1] + pos_offset, 0.1).tolist()
            positions_side = np.arange(0.001, part_bounds[3] + pos_offset, 0.1).tolist()
            positions_top = np.arange(0.001, part_bounds[5] + pos_offset, 0.1).tolist()
            ########################################################################################################
            [out_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                       element='Mesh - PART')
            for view in slice_views:
                if view == "Front":
                    positions = positions_front
                elif view == "Side":
                    positions = positions_side
                elif view == "Top":
                    positions = positions_top
                for position in positions:
                    # Set slice and stl position
                    x_cam = part_slice_dictionary[view]['Position'][0]
                    y_cam = part_slice_dictionary[view]['Position'][1]
                    z_cam = part_slice_dictionary[view]['Position'][2]

                    if view == "Front":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [position, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [position, 0.0, 0.0]
                        slice1.SliceType.Normal = [1.0, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam + position, y_cam, z_cam]

                    elif view == "Side":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, position, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, position, 0.0]
                        slice1.SliceType.Normal = [0.0, 1.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 1.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam + position, z_cam]

                    elif view == "Top":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, 0.0, position]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, position]
                        slice1.SliceType.Normal = [0.0, 0.0, 1.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 0.0, 1.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam, z_cam + position]

                    renderView1.CameraFocalPoint = slice_views_dictionary[view]['FocalPoint']
                    renderView1.CameraParallelScale = slice_views_dictionary[view]['ParallelScale']
                    renderView1.CameraViewUp = slice_views_dictionary[view]['ViewUp']

                    # save screenshot
                    file_name = out_folder[0] + "/" + view + "_" + str(position) + ".png"
                    pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

        else:
            ########################################################################################################
            #                                       MODIFY SLICE PARAMETERS HERE                                   #
            # -----------------------------------------------------------------------------------------------------#
            slice_views = ["Front", "Side", "Top"]  # ["Front", "Side", "Top"]
            pos_offset = 0.1
            positions_front = np.arange(stl_bounds[0] - pos_offset, stl_bounds[1] + pos_offset, 0.1).tolist()
            positions_side = np.arange(0.001, stl_bounds[3] + pos_offset, 0.1).tolist()
            positions_top = np.arange(0.001, stl_bounds[5] + pos_offset, 0.1).tolist()
            ########################################################################################################
            [out_folder, caca] = create_output_folders(out_path=output_path, case_files=[base_name],
                                                       element='Mesh - CAR')
            for view in slice_views:
                if view == "Front":
                    positions = positions_front
                elif view == "Side":
                    positions = positions_side
                elif view == "Top":
                    positions = positions_top
                for position in positions:
                    # Set slice and stl position
                    x_cam = slice_views_dictionary[view]['Position'][0]
                    y_cam = slice_views_dictionary[view]['Position'][1]
                    z_cam = slice_views_dictionary[view]['Position'][2]

                    if view == "Front":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [position, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [position, 0.0, 0.0]
                        slice1.SliceType.Normal = [1.0, 0.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam + position, y_cam, z_cam]

                    elif view == "Side":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, position, 0.0]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, position, 0.0]
                        slice1.SliceType.Normal = [0.0, 1.0, 0.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 1.0, 0.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam + position, z_cam]

                    elif view == "Top":
                        # Properties modified on slice1.SliceType
                        slice1.SliceType.Origin = [0.0, 0.0, position]
                        slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, position]
                        slice1.SliceType.Normal = [0.0, 0.0, 1.0]
                        slice1.HyperTreeGridSlicer.Normal = [0.0, 0.0, 1.0]

                        # current stl placement for renderView1
                        renderView1.CameraPosition = [x_cam, y_cam, z_cam + position]

                    renderView1.CameraFocalPoint = slice_views_dictionary[view]['FocalPoint']
                    renderView1.CameraParallelScale = slice_views_dictionary[view]['ParallelScale']
                    renderView1.CameraViewUp = slice_views_dictionary[view]['ViewUp']

                    # save screenshot
                    file_name = out_folder[0] + "/" + view + "_" + str(position) + ".png"
                    pvs.SaveScreenshot(file_name, renderView1, ImageResolution=image_size)

        pvs.Delete(slice1)
        del slice1

# ------------------------------------- MAIN CODE ----------------------------------------------------------------------
# Start timer
start_time = time.time()
# Read files,obtain output direction files, list the cases
list_cases, output_paths, list_stl, list_part, base_names = get_files(input_path, output_path_base)

if list_cases:
    i = 1
    # Perform paraview_trace in each case in the list of cases
    for case in list_cases:
        pvs.ResetSession()
        paraview_trace(filename=case, output_path=output_paths[i-1], stl_file=list_stl[i-1], part_file=list_part[i-1] ,base_name=base_names[i-1])
        i += 1

    print("The process finished successfully.")
    print("Execution time: %s seconds" % (time.time() - start_time))
