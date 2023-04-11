from paraview.simple import *
from Auxiliar_Functions.viewsDict import car_views


def analyze_sim(info, sim):
    simvelocity = input('At which velocity (m/s) did you simulate? ')

    # ------------------------------- Import statements and pre-analysis confiuration -------------------------------- #
    [stl_camera, slice_camera, car_camera] = car_views()
    stl_views = dict.keys(stl_camera)
    slice_views = dict.keys(slice_camera)
    # ---------------------------------------------------------------------------------------------------------------- #

    print('Curently analyzing: ' + sim.name + ' STL')

    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    ##########                   ##########
    ########## STL OF OF THE CAR ##########
    ##########                   ##########

    # create a new 'STL Reader'
    CarSTL = STLReader(registrationName=sim.name + 'car', FileNames=[sim.CAR])

    # set active source
    SetActiveSource(CarSTL)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    CarSTLDisplay = Show(CarSTL, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    CarSTLDisplay.Representation = 'Surface'
    CarSTLDisplay.DataAxesGrid = 'GridAxesRepresentation'
    CarSTLDisplay.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    CarSTLDisplay.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062,
                                                1.0, 0.5, 0.0]
    # create a new 'Logo'
    logo1 = Logo()

    # show data in view
    logo1Display = Show(logo1, renderView1, 'LogoSourceRepresentation')

    # a texture
    mADFT_P_Navy = CreateTexture("C:\\Users\\fitir\\Downloads\\MADFT_P_Navy.png")

    # change texture
    logo1.Texture = mADFT_P_Navy

    # Properties modified on logo1Display
    logo1Display.Position = [0.9, 0.9]

    # create a new 'Text'
    text1 = Text()

    # Properties modified on text1
    text1.Text = str(sim.name)

    # show data in view
    text1Display = Show(text1, renderView1, 'TextSourceRepresentation')

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on text1Display
    text1Display.FontFamily = 'File'

    # Properties modified on text1Display
    text1Display.FontFile = 'C:\\Users\\fitir\\Desktop\\Paraview_Batch_Postproc\\Templates\\MADFT-Da Mad Rave.ttf'

    # Properties modified on text1Display
    text1Display.FontSize = 5

    # get layout
    layout1 = GetLayout()

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + '.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    ##########                          ##########
    ########## STL OF A PART OF THE CAR ##########
    ##########                          ##########

    # create a new 'STL Reader'
    PartSTL = STLReader(registrationName=sim.name + 'part', FileNames=[sim.PART])

    # set active source
    SetActiveSource(PartSTL)

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    PartSTLDisplay = Show(PartSTL, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    PartSTLDisplay.Representation = 'Surface'
    PartSTLDisplay.DataAxesGrid = 'GridAxesRepresentation'
    PartSTLDisplay.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    PartSTLDisplay.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062,
                                                 1.0, 0.5, 0.0]
    # create a new 'Logo'
    logo1 = Logo()

    # show data in view
    logo1Display = Show(logo1, renderView1, 'LogoSourceRepresentation')

    # a texture
    mADFT_P_Navy = CreateTexture("C:\\Users\\fitir\\Downloads\\MADFT_P_Navy.png")

    # change texture
    logo1.Texture = mADFT_P_Navy

    # Properties modified on logo1Display
    logo1Display.Position = [0.9, 0.9]

    # create a new 'Text'
    text1 = Text()

    # Properties modified on text1
    text1.Text = str(sim.name)

    # show data in view
    text1Display = Show(text1, renderView1, 'TextSourceRepresentation')

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on text1Display
    text1Display.FontFamily = 'File'

    # Properties modified on text1Display
    text1Display.FontFile = 'C:\\Users\\fitir\\Desktop\\Paraview_Batch_Postproc\\Templates\\MADFT-Da Mad Rave.ttf'

    # Properties modified on text1Display
    text1Display.FontSize = 5

    # get layout
    layout1 = GetLayout()

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'PART.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(PartSTLDisplay)

    ##########                                                                        ##########
    ########## FOAM ANALISYS OF THE SLICES OF PREASSURE, TOTAL PREASSURE AND VELOCITY ##########
    ##########                                                                        ##########

    print('Curently analyzing: ' + sim.name + ' .foam')

    # casefoam = SliceReader(registrationName=sim.name + 'car', FileNames=[sim.foam])
    # create a new 'OpenFOAMReader'
    casefoam = OpenFOAMReader(
        FileName='C:\\Users\\fitir\\Desktop\\Paraview_Batch_Postproc\\Case_Files\\Prueba de paraview\\case.foam')  # nombre casefoam
    casefoam.MeshRegions = ['intern alMesh']
    casefoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress', 'yPlus']

    # Properties modified on casefoam
    casefoam.MeshRegions = ['B12_TE6_B12_TE1', 'B12_TE6_B12_TE147', 'B12_TE6_B12_TE149', 'B12_TE6_B12_TE150',
                            'B12_TE6_B12_TE151', 'B12_TE6_B12_TE152', 'B12_TE6_B12_TE153', 'B12_TE6_B12_TE154',
                            'B12_TE6_B12_TE155', 'B14_TE6_B14_TE37', 'B15_TE6_B15_TE1004', 'B15_TE6_B15_TE1005',
                            'B15_TE6_B15_TE1050', 'B15_TE6_B15_TE1052', 'B15_TE6_B15_TE1056', 'B15_TE6_B15_TE1057',
                            'B15_TE6_B15_TE982', 'B15_TE6_B15_TE983', 'B15_TE6_B15_TE986', 'B15_TE6_B15_TE987',
                            'B15_TE6_B15_TE988', 'B15_TE6_B15_TE989', 'B15_TE6_B15_TE990', 'B16_TE6_B16_TE1',
                            'B16_TE6_B16_TE85', 'B16_TE6_B16_TE87', 'B16_TE6_B16_TE88', 'B16_TE6_B16_TE89',
                            'B16_TE6_B16_TE90', 'B17_TE6_B17_TE109', 'B17_TE6_B17_TE110', 'B17_TE6_B17_TE112',
                            'B18_TE6_B18_TE293', 'B18_TE6_B18_TE294', 'B18_TE6_B18_TE295', 'B18_TE6_B18_TE296',
                            'B18_TE6_B18_TE304', 'B1_TE5_B1_TE138', 'B1_TE5_B1_TE141', 'B1_TE5_B1_TE142',
                            'B1_TE5_B1_TE143', 'B1_TE5_B1_TE145', 'B1_TE5_B1_TE146', 'B1_TE5_B1_TE2',
                            'B20_TE6_B20_TE73', 'B20_TE6_B20_TE74', 'B20_TE6_B20_TE77', 'B20_TE6_B20_TE79',
                            'B21_TE6_B21_TE1', 'B2_TE6_B2_TE1', 'B2_TE6_B2_TE25', 'B3_TE6_B3_TE1', 'B3_TE6_B3_TE337',
                            'B3_TE6_B3_TE340', 'B4_TE5_B4_TE2', 'B4_TE5_B4_TE242', 'B4_TE5_B4_TE245', 'B4_TE5_B4_TE246',
                            'B4_TE5_B4_TE247', 'B4_TE5_B4_TE248', 'B4_TE5_B4_TE249', 'B4_TE5_B4_TE250',
                            'B4_TE5_B4_TE252', 'B5_TE5_B5_TE86', 'B5_TE5_B5_TE91', 'B6_TE5_B6_TE158', 'B6_TE5_B6_TE159',
                            'B6_TE5_B6_TE161', 'B6_TE5_B6_TE162', 'B6_TE5_B6_TE163', 'B6_TE5_B6_TE164',
                            'B6_TE5_B6_TE165', 'B6_TE5_B6_TE2', 'B8_TE6_B8_TE73', 'B8_TE6_B8_TE74', 'B8_TE6_B8_TE77',
                            'B9_TE6_B9_TE1', 'boundingBox1', 'boundingBox2', 'boundingBox3', 'boundingBox4',
                            'boundingBox5', 'boundingBox6', 'internalMesh']

    # get active view
    # get layout
    layout1 = GetLayout()

    # show data in view
    casefoamDisplay = Show(casefoam, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'p'
    pLUT = GetColorTransferFunction('p')
    pLUT.RescaleOnVisibilityChange = 1
    pLUT.RGBPoints = [-42126.4296875, 0.02, 0.3813, 0.9981, -41104.121824718655, 0.02000006, 0.424267768, 0.96906969,
                      -40081.81396193731, 0.02, 0.467233763, 0.940033043, -39059.50609915597, 0.02, 0.5102, 0.911,
                      -38037.19823637463, 0.02000006, 0.546401494, 0.872669438, -37014.89037359328, 0.02, 0.582600362,
                      0.83433295, -35992.582510811946, 0.02, 0.6188, 0.796, -34970.2746480306, 0.02000006, 0.652535156,
                      0.749802434, -33947.96678524926, 0.02, 0.686267004, 0.703599538, -32925.65892246791, 0.02, 0.72,
                      0.6574, -31903.35105968657, 0.02000006, 0.757035456, 0.603735359, -30881.043196905226, 0.02,
                      0.794067037, 0.55006613, -29858.735334123885, 0.02, 0.8311, 0.4964, -28836.42747134254,
                      0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -27814.1196085612,
                      0.023312914349117714, 0.897999359924484, 0.36073871343115577, -26791.811745779854,
                      0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -25769.503882998513,
                      0.27421074700988196, 0.952562960995083, 0.15356836602739213, -24747.196020217165,
                      0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -23724.888157435827, 0.6439, 0.9773,
                      0.0469, -22702.580294654483, 0.762401813, 0.984669591, 0.034600153, -21680.27243187314,
                      0.880901185, 0.992033407, 0.022299877, -20657.964569091797, 0.9995285432627147,
                      0.9995193706781492, 0.0134884641450013, -19635.656706310452, 0.999402998, 0.955036376,
                      0.079066628, -18613.348843529107, 0.9994, 0.910666223, 0.148134024, -17591.04098074777, 0.9994,
                      0.8663, 0.2172, -16568.733117966425, 0.999269665, 0.818035981, 0.217200652, -15546.42525518508,
                      0.999133332, 0.769766184, 0.2172, -14524.117392403736, 0.999, 0.7215, 0.2172, -13501.809529622398,
                      0.99913633, 0.673435546, 0.217200652, -12479.501666841057, 0.999266668, 0.625366186, 0.2172,
                      -11457.193804059709, 0.9994, 0.5773, 0.2172, -10434.885941278364, 0.999402998, 0.521068455,
                      0.217200652, -9412.578078497027, 0.9994, 0.464832771, 0.2172, -8390.270215715682, 0.9994, 0.4086,
                      0.2172, -7367.96235293433, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206,
                      -6345.654490152992, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934,
                      -5323.346627371655, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357,
                      -4301.03876459031, 0.949903037, 0.116867171, 0.252900603, -3278.7309018089654, 0.903199533,
                      0.078432949, 0.291800389, -2256.4230390276134, 0.8565, 0.04, 0.3307, -1234.1151762462832,
                      0.798902627, 0.04333345, 0.358434298, -211.8073134649385, 0.741299424, 0.0466667, 0.386166944,
                      810.5005493164062, 0.6837, 0.05, 0.4139]
    pLUT.ColorSpace = 'RGB'
    pLUT.NanColor = [1.0, 0.0, 0.0]
    pLUT.NumberOfTableValues = 32
    pLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    casefoamDisplay.Representation = 'Surface'
    casefoamDisplay.ColorArrayName = ['POINTS', 'p']
    casefoamDisplay.LookupTable = pLUT
    casefoamDisplay.OSPRayScaleArray = 'p'
    casefoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    casefoamDisplay.SelectOrientationVectors = 'U'
    casefoamDisplay.ScaleFactor = 2.8000000000000003
    casefoamDisplay.SelectScaleArray = 'p'
    casefoamDisplay.GlyphType = 'Arrow'
    casefoamDisplay.GlyphTableIndexArray = 'p'
    casefoamDisplay.GaussianRadius = 0.14
    casefoamDisplay.SetScaleArray = ['POINTS', 'p']
    casefoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    casefoamDisplay.OpacityArray = ['POINTS', 'p']
    casefoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    casefoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
    casefoamDisplay.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    casefoamDisplay.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    casefoamDisplay.ScaleTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    casefoamDisplay.OpacityTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # show color bar/color legend
    casefoamDisplay.SetScalarBarVisibility(renderView1, True)

    # get opacity transfer function/opacity map for 'p'
    pPWF = GetOpacityTransferFunction('p')
    pPWF.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]
    pPWF.ScalarRangeInitialized = 1

    # create a new 'Extract Block'
    extractBlock1 = ExtractBlock(Input=casefoam)

    # Properties modified on extractBlock1
    extractBlock1.BlockIndices = [1]

    # show data in view
    extractBlock1Display = Show(extractBlock1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    extractBlock1Display.Representation = 'Surface'
    extractBlock1Display.ColorArrayName = ['POINTS', 'p']
    extractBlock1Display.LookupTable = pLUT
    extractBlock1Display.OSPRayScaleArray = 'p'
    extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractBlock1Display.SelectOrientationVectors = 'U'
    extractBlock1Display.ScaleFactor = 2.8000000000000003
    extractBlock1Display.SelectScaleArray = 'p'
    extractBlock1Display.GlyphType = 'Arrow'
    extractBlock1Display.GlyphTableIndexArray = 'p'
    extractBlock1Display.GaussianRadius = 0.14
    extractBlock1Display.SetScaleArray = ['POINTS', 'p']
    extractBlock1Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractBlock1Display.OpacityArray = ['POINTS', 'p']
    extractBlock1Display.OpacityTransferFunction = 'PiecewiseFunction'
    extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
    extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'
    extractBlock1Display.ScalarOpacityFunction = pPWF
    extractBlock1Display.ScalarOpacityUnitDistance = 0.13087110402528962
    extractBlock1Display.ExtractedBlockIndex = 1

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    extractBlock1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    extractBlock1Display.ScaleTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                         0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    extractBlock1Display.OpacityTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                           0.0]

    # show color bar/color legend
    extractBlock1Display.SetScalarBarVisibility(renderView1, True)

    # create a new 'Calculator'
    calculator1 = Calculator(Input=extractBlock1)
    calculator1.Function = ''

    # Properties modified on calculator1
    calculator1.ResultArrayName = 'Pt'
    calculator1.Function = 'p+1/2*1.1963*' + str(simvelocity) + '^2'

    # show data in view
    calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

    # get color transfer function/color map for 'Pt'
    ptLUT = GetColorTransferFunction('Pt')
    ptLUT.RescaleOnVisibilityChange = 1
    ptLUT.RGBPoints = [-41991.8459375, 0.02, 0.3813, 0.9981, -40969.53807471866, 0.02000006, 0.424267768, 0.96906969,
                       -39947.23021193732, 0.02, 0.467233763, 0.940033043, -38924.922349155975, 0.02, 0.5102, 0.911,
                       -37902.61448637463, 0.02000006, 0.546401494, 0.872669438, -36880.30662359329, 0.02, 0.582600362,
                       0.83433295, -35857.99876081194, 0.02, 0.6188, 0.796, -34835.6908980306, 0.02000006, 0.652535156,
                       0.749802434, -33813.38303524926, 0.02, 0.686267004, 0.703599538, -32791.075172467914, 0.02, 0.72,
                       0.6574, -31768.767309686573, 0.02000006, 0.757035456, 0.603735359, -30746.459446905228, 0.02,
                       0.794067037, 0.55006613, -29724.151584123887, 0.02, 0.8311, 0.4964, -28701.843721342542,
                       0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -27679.5358585612,
                       0.023312914349117714, 0.897999359924484, 0.36073871343115577, -26657.227995779856,
                       0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -25634.920132998515,
                       0.27421074700988196, 0.952562960995083, 0.15356836602739213, -24612.612270217167,
                       0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -23590.30440743583, 0.6439, 0.9773,
                       0.0469, -22567.996544654485, 0.762401813, 0.984669591, 0.034600153, -21545.688681873144,
                       0.880901185, 0.992033407, 0.022299877, -20523.3808190918, 0.9995285432627147, 0.9995193706781492,
                       0.0134884641450013, -19501.072956310454, 0.999402998, 0.955036376, 0.079066628,
                       -18478.76509352911, 0.9994, 0.910666223, 0.148134024, -17456.457230747772, 0.9994, 0.8663,
                       0.2172, -16434.149367966427, 0.999269665, 0.818035981, 0.217200652, -15411.841505185082,
                       0.999133332, 0.769766184, 0.2172, -14389.533642403738, 0.999, 0.7215, 0.2172, -13367.2257796224,
                       0.99913633, 0.673435546, 0.217200652, -12344.91791684106, 0.999266668, 0.625366186, 0.2172,
                       -11322.61005405971, 0.9994, 0.5773, 0.2172, -10300.302191278366, 0.999402998, 0.521068455,
                       0.217200652, -9277.994328497029, 0.9994, 0.464832771, 0.2172, -8255.686465715684, 0.9994, 0.4086,
                       0.2172, -7233.378602934332, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206,
                       -6211.070740152994, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934,
                       -5188.762877371657, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357,
                       -4166.455014590312, 0.949903037, 0.116867171, 0.252900603, -3144.1471518089675, 0.903199533,
                       0.078432949, 0.291800389, -2121.8392890276155, 0.8565, 0.04, 0.3307, -1099.5314262462853,
                       0.798902627, 0.04333345, 0.358434298, -77.22356346494053, 0.741299424, 0.0466667, 0.386166944,
                       945.0842993164042, 0.6837, 0.05, 0.4139]
    ptLUT.ColorSpace = 'RGB'
    ptLUT.NanColor = [1.0, 0.0, 0.0]
    ptLUT.NumberOfTableValues = 32
    ptLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'Pt'
    ptPWF = GetOpacityTransferFunction('Pt')
    ptPWF.Points = [-41991.8459375, 0.0, 0.5, 0.0, 945.0842993164042, 1.0, 0.5, 0.0]
    ptPWF.ScalarRangeInitialized = 1

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
    calculator1Display.ScalarOpacityFunction = ptPWF
    calculator1Display.ScalarOpacityUnitDistance = 0.13087110402528962
    calculator1Display.ExtractedBlockIndex = 1

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                     0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [-41991.8459375, 0.0, 0.5, 0.0, 945.0842993164042, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [-41991.8459375, 0.0, 0.5, 0.0, 945.0842993164042, 1.0, 0.5,
                                                         0.0]

    # hide data in view
    Hide(extractBlock1, renderView1)

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # Rescale transfer function
    ptLUT.RescaleTransferFunction(-41991.8459375, 945.0842993164063)

    # Rescale transfer function
    ptPWF.RescaleTransferFunction(-41991.8459375, 945.0842993164063)

    # hide data in view
    Hide(calculator1, renderView1)

    # create a new 'Slice'
    slice1 = Slice(Input=calculator1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [5.5, 3.5, 3.6059999256394804]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [5.5, 3.5, 3.6059999256394804]

    normal_to_axis = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    distances_axis = [0.01, 0.02, 0.03]
    for slice_normal_axe in normal_to_axis:
        for slice_distance_axe in distances_axis:
            # Properties modified on slice1.SliceType
            slice1.SliceType.Origin = [ii * slice_distance_axe for ii in slice_normal_axe]
            slice1.SliceType.Normal = slice_normal_axe

            # show data in view
            slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

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

            # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
            slice1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                        0.0]

            # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
            slice1Display.ScaleTransferFunction.Points = [-250.1312334367134, 0.0, 0.5, 0.0, 270.794994522185, 1.0, 0.5,
                                                          0.0]

            # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
            slice1Display.OpacityTransferFunction.Points = [-250.1312334367134, 0.0, 0.5, 0.0, 270.794994522185, 1.0,
                                                            0.5, 0.0]

            # hide data in view
            Hide(calculator1, renderView1)

            # show color bar/color legend
            slice1Display.SetScalarBarVisibility(renderView1, True)

            # update the view to ensure updated data information
            renderView1.Update()

            # Rescale transfer function
            ptLUT.RescaleTransferFunction(50.0, 250.0)

            # Rescale transfer function
            ptPWF.RescaleTransferFunction(50.0, 250.0)

            #### saving camera placements for all active views
            # hide data in view
            Hide(extractBlock1, renderView1)
            # hide data in view
            Hide(casefoam, renderView1)

            ###### PENDIENTE DE PONER EN UNA FUNCION AUXUILIAR #####

            if slice_normal_axe[0] == 1.0:
                axe_name = 'X'
            if slice_normal_axe[1] == 1.0:
                axe_name = 'Y'
            if slice_normal_axe[2] == 1.0:
                axe_name = 'Z'

            for slice_view in slice_views:
                renderView1.CameraPosition = slice_camera[slice_view]["Position"]
                renderView1.CameraFocalPoint = slice_camera[slice_view]["FocalPoint"]
                renderView1.CameraViewUp = slice_camera[slice_view]["ViewUp"]
                renderView1.CameraParallelScale = slice_camera[slice_view]["ParallelScale"]
                # save screenshot
                SaveScreenshot(
                    str(sim.outFolder) + '\\' + str(sim.name) + '_' + slice_view + '_PreTot_' + axe_name + '_' + str(
                        slice_distance_axe) + '.png', renderView1,
                    ImageResolution=info["ImageRes"])

            # set scalar coloring
            ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

            # Hide the scalar bar for this color map if no visible data is colored by it.
            HideScalarBarIfNotNeeded(ptLUT, renderView1)

            # rescale color and/or opacity maps used to include current data range
            slice1Display.RescaleTransferFunctionToDataRange(True, False)

            # show color bar/color legend
            slice1Display.SetScalarBarVisibility(renderView1, True)

            # get color transfer function/color map for 'U'
            uLUT = GetColorTransferFunction('U')
            uLUT.RescaleOnVisibilityChange = 1
            uLUT.RGBPoints = [0.0, 0.02, 0.3813, 0.9981, 2.790735296602469, 0.02000006, 0.424267768, 0.96906969,
                              5.581470593204938, 0.02, 0.467233763, 0.940033043, 8.372205889807407, 0.02, 0.5102, 0.911,
                              11.162941186409876, 0.02000006, 0.546401494, 0.872669438, 13.953676483012345, 0.02,
                              0.582600362, 0.83433295, 16.744411779614815, 0.02, 0.6188, 0.796, 19.53514707621728,
                              0.02000006, 0.652535156, 0.749802434, 22.325882372819752, 0.02, 0.686267004, 0.703599538,
                              25.116617669422222, 0.02, 0.72, 0.6574, 27.90735296602469, 0.02000006, 0.757035456,
                              0.603735359, 30.698088262627163, 0.02, 0.794067037, 0.55006613, 33.48882355922963, 0.02,
                              0.8311, 0.4964, 36.2795588558321, 0.021354336738172372, 0.8645368555261631,
                              0.4285579460761159, 39.07029415243457, 0.023312914349117714, 0.897999359924484,
                              0.36073871343115577, 41.86102944903704, 0.015976108242848862, 0.9310479513349017,
                              0.2925631815088092, 44.651764745639504, 0.27421074700988196, 0.952562960995083,
                              0.15356836602739213, 47.44250004224199, 0.4933546281681699, 0.9619038625309482,
                              0.11119493614749336, 50.233235338844445, 0.6439, 0.9773, 0.0469, 53.023970635446915,
                              0.762401813, 0.984669591, 0.034600153, 55.81470593204938, 0.880901185, 0.992033407,
                              0.022299877, 58.605441228651856, 0.9995285432627147, 0.9995193706781492,
                              0.0134884641450013, 61.396176525254326, 0.999402998, 0.955036376, 0.079066628,
                              64.1869118218568, 0.9994, 0.910666223, 0.148134024, 66.97764711845926, 0.9994, 0.8663,
                              0.2172, 69.76838241506174, 0.999269665, 0.818035981, 0.217200652, 72.5591177116642,
                              0.999133332, 0.769766184, 0.2172, 75.34985300826668, 0.999, 0.7215, 0.2172,
                              78.14058830486914, 0.99913633, 0.673435546, 0.217200652, 80.93132360147159, 0.999266668,
                              0.625366186, 0.2172, 83.72205889807408, 0.9994, 0.5773, 0.2172, 86.51279419467656,
                              0.999402998, 0.521068455, 0.217200652, 89.30352949127901, 0.9994, 0.464832771, 0.2172,
                              92.09426478788149, 0.9994, 0.4086, 0.2172, 94.88500008448398, 0.9947599917687346,
                              0.33177297300202935, 0.2112309638520206, 97.67573538108643, 0.9867129505479589,
                              0.2595183410914934, 0.19012239549291934, 100.46647067768889, 0.9912458875646419,
                              0.14799417507952672, 0.21078892136920357, 103.25720597429138, 0.949903037, 0.116867171,
                              0.252900603, 106.04794127089383, 0.903199533, 0.078432949, 0.291800389,
                              108.83867656749631, 0.8565, 0.04, 0.3307, 111.62941186409876, 0.798902627, 0.04333345,
                              0.358434298, 114.42014716070122, 0.741299424, 0.0466667, 0.386166944, 117.21088245730371,
                              0.6837, 0.05, 0.4139]
            uLUT.ColorSpace = 'RGB'
            uLUT.NanColor = [1.0, 0.0, 0.0]
            uLUT.NumberOfTableValues = 32
            uLUT.ScalarRangeInitialized = 1.0

            # get opacity transfer function/opacity map for 'U'
            uPWF = GetOpacityTransferFunction('U')
            uPWF.Points = [0.0, 0.0, 0.5, 0.0, 117.21088245730371, 1.0, 0.5, 0.0]
            uPWF.ScalarRangeInitialized = 1

            # Rescale transfer function
            uLUT.RescaleTransferFunction(0.0, 35.0)

            # Rescale transfer function
            uPWF.RescaleTransferFunction(0.0, 35.0)
            # hide data in view
            Hide(extractBlock1, renderView1)
            # hide data in view
            Hide(casefoam, renderView1)

            for slice_view in slice_views:
                renderView1.CameraPosition = slice_camera[slice_view]["Position"]
                renderView1.CameraFocalPoint = slice_camera[slice_view]["FocalPoint"]
                renderView1.CameraViewUp = slice_camera[slice_view]["ViewUp"]
                renderView1.CameraParallelScale = slice_camera[slice_view]["ParallelScale"]
                # save screenshot
                SaveScreenshot(
                    str(sim.outFolder) + '\\' + str(sim.name) + '_' + slice_view + '_Vel_' + axe_name + '_' + str(
                        slice_distance_axe) + '.png', renderView1,
                    ImageResolution=info["ImageRes"])

            ##########                        ##########
            ########## PREASSURE OVER THE CAR ##########
            ##########                        ##########

            # set scalar coloring
            ColorBy(slice1Display, ('POINTS', 'p'))

            # Hide the scalar bar for this color map if no visible data is colored by it.
            HideScalarBarIfNotNeeded(uLUT, renderView1)

            # rescale color and/or opacity maps used to include current data range
            slice1Display.RescaleTransferFunctionToDataRange(True, False)

            # show color bar/color legend
            slice1Display.SetScalarBarVisibility(renderView1, True)

            # Rescale transfer function
            pLUT.RescaleTransferFunction(0.0, 50.0)

            # Rescale transfer function
            pPWF.RescaleTransferFunction(0.0, 50.0)

            for slice_view in slice_views:
                renderView1.CameraPosition = slice_camera[slice_view]["Position"]
                renderView1.CameraFocalPoint = slice_camera[slice_view]["FocalPoint"]
                renderView1.CameraViewUp = slice_camera[slice_view]["ViewUp"]
                renderView1.CameraParallelScale = slice_camera[slice_view]["ParallelScale"]
                # save screenshot
                SaveScreenshot(
                    str(sim.outFolder) + '\\' + str(sim.name) + '_' + slice_view + '_Pre_' + axe_name + '_' + str(
                        slice_distance_axe) + '.png', renderView1,
                    ImageResolution=info["ImageRes"])

    # create a new 'Extract Block'
    extractBlock2 = ExtractBlock(Input=casefoam)

    # Properties modified on extractBlock2
    extractBlock2.BlockIndices = [43, 40, 41, 46, 47, 44, 45, 18, 19, 16, 17, 22, 23, 20, 21, 26, 27, 24, 25, 30, 31,
                                  28, 29, 10, 11, 9, 14, 15, 12, 13, 82, 83, 80, 81, 84, 85, 66, 67, 64, 65, 70, 71, 68,
                                  69, 74, 75, 72, 73, 78, 79, 76, 77, 50, 51, 48, 49, 54, 55, 52, 53, 58, 59, 56, 57,
                                  62, 63, 60, 61, 34, 35, 32, 33, 38, 39, 36, 37, 42]

    # show data in view
    extractBlock2Display = Show(extractBlock2, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    extractBlock2Display.Representation = 'Surface'
    extractBlock2Display.ColorArrayName = ['POINTS', 'p']
    extractBlock2Display.LookupTable = pLUT
    extractBlock2Display.OSPRayScaleArray = 'p'
    extractBlock2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractBlock2Display.SelectOrientationVectors = 'U'
    extractBlock2Display.ScaleFactor = 0.2915555477142334
    extractBlock2Display.SelectScaleArray = 'p'
    extractBlock2Display.GlyphType = 'Arrow'
    extractBlock2Display.GlyphTableIndexArray = 'p'
    extractBlock2Display.GaussianRadius = 0.014577777385711671
    extractBlock2Display.SetScaleArray = ['POINTS', 'p']
    extractBlock2Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractBlock2Display.OpacityArray = ['POINTS', 'p']
    extractBlock2Display.OpacityTransferFunction = 'PiecewiseFunction'
    extractBlock2Display.DataAxesGrid = 'GridAxesRepresentation'
    extractBlock2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    extractBlock2Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    extractBlock2Display.ScaleTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0, 456.60955810546875, 1.0, 0.5,
                                                         0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    extractBlock2Display.OpacityTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0, 456.60955810546875, 1.0,
                                                           0.5, 0.0]

    # hide data in view
    Hide(casefoam, renderView1)

    # show color bar/color legend
    extractBlock2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # Rescale transfer function
    pLUT.RescaleTransferFunction(-50.0, 100.0)

    # Rescale transfer function
    pPWF.RescaleTransferFunction(-50.0, 100.0)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'Pre_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    ##########                                ##########
    ########## WALL SHEAR STRESS OVER THE CAR ##########
    ##########                                ##########

    # set scalar coloring
    ColorBy(extractBlock2Display, ('POINTS', 'wallShearStress', 'Magnitude'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    extractBlock2Display.RescaleTransferFunctionToDataRange(True, False)

    # get color transfer function/color map for 'wallShearStress'
    wallShearStressLUT = GetColorTransferFunction('wallShearStress')
    wallShearStressLUT.RescaleOnVisibilityChange = 1
    wallShearStressLUT.RGBPoints = [2.640222169527297e-07, 0.02, 0.3813, 0.9981, 0.5273691473009303, 0.02000006,
                                    0.424267768, 0.96906969, 1.0547380305796437, 0.02, 0.467233763, 0.940033043,
                                    1.5821069138583572, 0.02, 0.5102, 0.911, 2.1094757971370703, 0.02000006,
                                    0.546401494, 0.872669438, 2.6368446804157837, 0.02, 0.582600362, 0.83433295,
                                    3.1642135636944975, 0.02, 0.6188, 0.796, 3.69158244697321, 0.02000006, 0.652535156,
                                    0.749802434, 4.218951330251923, 0.02, 0.686267004, 0.703599538, 4.7463202135306375,
                                    0.02, 0.72, 0.6574, 5.27368909680935, 0.02000006, 0.757035456, 0.603735359,
                                    5.801057980088064, 0.02, 0.794067037, 0.55006613, 6.3284268633667775, 0.02, 0.8311,
                                    0.4964, 6.855795746645492, 0.021354336738172372, 0.8645368555261631,
                                    0.4285579460761159, 7.383164629924204, 0.023312914349117714, 0.897999359924484,
                                    0.36073871343115577, 7.910533513202918, 0.015976108242848862, 0.9310479513349017,
                                    0.2925631815088092, 8.43790239648163, 0.27421074700988196, 0.952562960995083,
                                    0.15356836602739213, 8.965271279760348, 0.4933546281681699, 0.9619038625309482,
                                    0.11119493614749336, 9.49264016303906, 0.6439, 0.9773, 0.0469, 10.020009046317773,
                                    0.762401813, 0.984669591, 0.034600153, 10.547377929596484, 0.880901185, 0.992033407,
                                    0.022299877, 11.0747468128752, 0.9995285432627147, 0.9995193706781492,
                                    0.0134884641450013, 11.602115696153913, 0.999402998, 0.955036376, 0.079066628,
                                    12.129484579432628, 0.9994, 0.910666223, 0.148134024, 12.65685346271134, 0.9994,
                                    0.8663, 0.2172, 13.184222345990053, 0.999269665, 0.818035981, 0.217200652,
                                    13.711591229268768, 0.999133332, 0.769766184, 0.2172, 14.238960112547481, 0.999,
                                    0.7215, 0.2172, 14.766328995826193, 0.99913633, 0.673435546, 0.217200652,
                                    15.293697879104904, 0.999266668, 0.625366186, 0.2172, 15.821066762383621, 0.9994,
                                    0.5773, 0.2172, 16.348435645662335, 0.999402998, 0.521068455, 0.217200652,
                                    16.875804528941043, 0.9994, 0.464832771, 0.2172, 17.403173412219758, 0.9994, 0.4086,
                                    0.2172, 17.930542295498476, 0.9947599917687346, 0.33177297300202935,
                                    0.2112309638520206, 18.457911178777188, 0.9867129505479589, 0.2595183410914934,
                                    0.19012239549291934, 18.9852800620559, 0.9912458875646419, 0.14799417507952672,
                                    0.21078892136920357, 19.51264894533461, 0.949903037, 0.116867171, 0.252900603,
                                    20.040017828613326, 0.903199533, 0.078432949, 0.291800389, 20.56738671189204,
                                    0.8565, 0.04, 0.3307, 21.09475559517075, 0.798902627, 0.04333345, 0.358434298,
                                    21.622124478449464, 0.741299424, 0.0466667, 0.386166944, 22.14949336172818, 0.6837,
                                    0.05, 0.4139]
    wallShearStressLUT.ColorSpace = 'RGB'
    wallShearStressLUT.NanColor = [1.0, 0.0, 0.0]
    wallShearStressLUT.NumberOfTableValues = 32
    wallShearStressLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'wallShearStress'
    wallShearStressPWF = GetOpacityTransferFunction('wallShearStress')
    wallShearStressPWF.Points = [2.640222169527297e-07, 0.0, 0.5, 0.0, 22.14949336172818, 1.0, 0.5, 0.0]
    wallShearStressPWF.ScalarRangeInitialized = 1

    # show data in view
    extractBlock2Display = Show(extractBlock2, renderView1, 'GeometryRepresentation')

    # show color bar/color legend
    extractBlock2Display.SetScalarBarVisibility(renderView1, True)

    # reset view to fit data
    renderView1.ResetCamera()

    # Rescale transfer function
    wallShearStressLUT.RescaleTransferFunction(-1.0, 4.0)

    # Rescale transfer function
    wallShearStressPWF.RescaleTransferFunction(-1.0, 4.0)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'WSStress_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    ##########                            ##########
    ########## DRAG AND LIFT OVER THE CAR ##########
    ##########                            ##########

    # create a new 'Generate Surface Normals'
    generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractBlock2)

    # show data in view
    generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    generateSurfaceNormals1Display.Representation = 'Surface'
    generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'p']
    generateSurfaceNormals1Display.LookupTable = pLUT
    generateSurfaceNormals1Display.OSPRayScaleArray = 'p'
    generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    generateSurfaceNormals1Display.SelectOrientationVectors = 'U'
    generateSurfaceNormals1Display.ScaleFactor = 0.2915555477142334
    generateSurfaceNormals1Display.SelectScaleArray = 'p'
    generateSurfaceNormals1Display.GlyphType = 'Arrow'
    generateSurfaceNormals1Display.GlyphTableIndexArray = 'p'
    generateSurfaceNormals1Display.GaussianRadius = 0.014577777385711671
    generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'p']
    generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
    generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'p']
    generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
    generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
    generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    generateSurfaceNormals1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062,
                                                                 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    generateSurfaceNormals1Display.ScaleTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0, 456.60955810546875,
                                                                   1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    generateSurfaceNormals1Display.OpacityTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0,
                                                                     456.60955810546875, 1.0, 0.5, 0.0]

    # show color bar/color legend
    generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Calculator'
    calculator2 = Calculator(Input=generateSurfaceNormals1)
    calculator2.Function = ''

    # rename source object
    RenameSource('Drag', calculator2)

    # Properties modified on calculator2
    calculator2.ResultArrayName = 'Drag'
    calculator2.Function = 'Normals_X*p'

    # show data in view
    calculator2Display = Show(calculator2, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'Drag'
    dragLUT = GetColorTransferFunction('Drag')
    dragLUT.RescaleOnVisibilityChange = 1
    dragLUT.RGBPoints = [-381.24950400195667, 0.02, 0.3813, 0.9981, -36.15896079372794, 0.02000006, 0.424267768,
                         0.96906969, 308.9315824145008, 0.02, 0.467233763, 0.940033043, 654.0221256227294, 0.02, 0.5102,
                         0.911, 999.1126688309582, 0.02000006, 0.546401494, 0.872669438, 1344.2032120391866, 0.02,
                         0.582600362, 0.83433295, 1689.2937552474154, 0.02, 0.6188, 0.796, 2034.3842984556436,
                         0.02000006, 0.652535156, 0.749802434, 2379.474841663873, 0.02, 0.686267004, 0.703599538,
                         2724.5653848721017, 0.02, 0.72, 0.6574, 3069.65592808033, 0.02000006, 0.757035456, 0.603735359,
                         3414.7464712885594, 0.02, 0.794067037, 0.55006613, 3759.8370144967876, 0.02, 0.8311, 0.4964,
                         4104.927557705017, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159,
                         4450.018100913245, 0.023312914349117714, 0.897999359924484, 0.36073871343115577,
                         4795.108644121474, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092,
                         5140.199187329703, 0.27421074700988196, 0.952562960995083, 0.15356836602739213,
                         5485.289730537932, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336,
                         5830.38027374616, 0.6439, 0.9773, 0.0469, 6175.470816954389, 0.762401813, 0.984669591,
                         0.034600153, 6520.561360162616, 0.880901185, 0.992033407, 0.022299877, 6865.651903370846,
                         0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 7210.7424465790755, 0.999402998,
                         0.955036376, 0.079066628, 7555.8329897873045, 0.9994, 0.910666223, 0.148134024,
                         7900.923532995532, 0.9994, 0.8663, 0.2172, 8246.01407620376, 0.999269665, 0.818035981,
                         0.217200652, 8591.10461941199, 0.999133332, 0.769766184, 0.2172, 8936.195162620219, 0.999,
                         0.7215, 0.2172, 9281.285705828446, 0.99913633, 0.673435546, 0.217200652, 9626.376249036675,
                         0.999266668, 0.625366186, 0.2172, 9971.466792244904, 0.9994, 0.5773, 0.2172,
                         10316.557335453133, 0.999402998, 0.521068455, 0.217200652, 10661.647878661362, 0.9994,
                         0.464832771, 0.2172, 11006.738421869592, 0.9994, 0.4086, 0.2172, 11351.82896507782,
                         0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 11696.91950828605,
                         0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 12042.010051494277,
                         0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 12387.100594702506, 0.949903037,
                         0.116867171, 0.252900603, 12732.191137910735, 0.903199533, 0.078432949, 0.291800389,
                         13077.281681118966, 0.8565, 0.04, 0.3307, 13422.37222432719, 0.798902627, 0.04333345,
                         0.358434298, 13767.46276753542, 0.741299424, 0.0466667, 0.386166944, 14112.55331074365, 0.6837,
                         0.05, 0.4139]
    dragLUT.ColorSpace = 'RGB'
    dragLUT.NanColor = [1.0, 0.0, 0.0]
    dragLUT.NumberOfTableValues = 32
    dragLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    calculator2Display.Representation = 'Surface'
    calculator2Display.ColorArrayName = ['POINTS', 'Drag']
    calculator2Display.LookupTable = dragLUT
    calculator2Display.OSPRayScaleArray = 'Drag'
    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2Display.SelectOrientationVectors = 'U'
    calculator2Display.ScaleFactor = 0.2915555477142334
    calculator2Display.SelectScaleArray = 'Drag'
    calculator2Display.GlyphType = 'Arrow'
    calculator2Display.GlyphTableIndexArray = 'Drag'
    calculator2Display.GaussianRadius = 0.014577777385711671
    calculator2Display.SetScaleArray = ['POINTS', 'Drag']
    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2Display.OpacityArray = ['POINTS', 'Drag']
    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                     0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2Display.ScaleTransferFunction.Points = [-381.24950400195667, 0.0, 0.5, 0.0, 14112.55331074365, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2Display.OpacityTransferFunction.Points = [-381.24950400195667, 0.0, 0.5, 0.0, 14112.55331074365, 1.0,
                                                         0.5, 0.0]

    # hide data in view
    Hide(generateSurfaceNormals1, renderView1)

    # show color bar/color legend
    calculator2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'Drag'
    dragPWF = GetOpacityTransferFunction('Drag')
    dragPWF.Points = [-381.24950400195667, 0.0, 0.5, 0.0, 14112.55331074365, 1.0, 0.5, 0.0]
    dragPWF.ScalarRangeInitialized = 1

    # Rescale transfer function
    dragLUT.RescaleTransferFunction(0.0, 70.0)

    # Rescale transfer function
    dragPWF.RescaleTransferFunction(0.0, 70.0)

    # Rescale transfer function
    dragLUT.RescaleTransferFunction(-381.24950400195667, 14112.55331074365)

    # Rescale transfer function
    dragPWF.RescaleTransferFunction(-381.24950400195667, 14112.55331074365)

    # Rescale transfer function
    dragLUT.RescaleTransferFunction(0.0, 80.0)

    # Rescale transfer function
    dragPWF.RescaleTransferFunction(0.0, 80.0)

    # hide data in view
    Hide(extractBlock2, renderView1)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'Drag_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    # hide data in view
    Hide(calculator2, renderView1)

    # set active source
    SetActiveSource(generateSurfaceNormals1)

    # create a new 'Calculator'
    calculator2_1 = Calculator(Input=generateSurfaceNormals1)
    calculator2_1.Function = ''

    # rename source object
    RenameSource('Lift', calculator2_1)

    # Properties modified on calculator2_1
    calculator2_1.Function = 'Normals_Z*p'

    # show data in view
    calculator2_1Display = Show(calculator2_1, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'Result'
    resultLUT = GetColorTransferFunction('Result')
    resultLUT.RescaleOnVisibilityChange = 1
    resultLUT.RGBPoints = [-10110.821560606593, 0.02, 0.3813, 0.9981, -9570.885157290675, 0.02000006, 0.424267768,
                           0.96906969, -9030.948753974755, 0.02, 0.467233763, 0.940033043, -8491.012350658837, 0.02,
                           0.5102, 0.911, -7951.075947342917, 0.02000006, 0.546401494, 0.872669438, -7411.139544026999,
                           0.02, 0.582600362, 0.83433295, -6871.203140711079, 0.02, 0.6188, 0.796, -6331.266737395161,
                           0.02000006, 0.652535156, 0.749802434, -5791.330334079242, 0.02, 0.686267004, 0.703599538,
                           -5251.393930763323, 0.02, 0.72, 0.6574, -4711.457527447404, 0.02000006, 0.757035456,
                           0.603735359, -4171.521124131484, 0.02, 0.794067037, 0.55006613, -3631.5847208155656, 0.02,
                           0.8311, 0.4964, -3091.6483174996456, 0.021354336738172372, 0.8645368555261631,
                           0.4285579460761159, -2551.7119141837275, 0.023312914349117714, 0.897999359924484,
                           0.36073871343115577, -2011.7755108678084, 0.015976108242848862, 0.9310479513349017,
                           0.2925631815088092, -1471.8391075518903, 0.27421074700988196, 0.952562960995083,
                           0.15356836602739213, -931.9027042359685, 0.4933546281681699, 0.9619038625309482,
                           0.11119493614749336, -391.96630092005216, 0.6439, 0.9773, 0.0469, 147.9701023958678,
                           0.762401813, 0.984669591, 0.034600153, 687.9065057117859, 0.880901185, 0.992033407,
                           0.022299877, 1227.842909027706, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013,
                           1767.7793123436259, 0.999402998, 0.955036376, 0.079066628, 2307.715715659546, 0.9994,
                           0.910666223, 0.148134024, 2847.652118975462, 0.9994, 0.8663, 0.2172, 3387.588522291382,
                           0.999269665, 0.818035981, 0.217200652, 3927.524925607302, 0.999133332, 0.769766184, 0.2172,
                           4467.46132892322, 0.999, 0.7215, 0.2172, 5007.397732239138, 0.99913633, 0.673435546,
                           0.217200652, 5547.334135555055, 0.999266668, 0.625366186, 0.2172, 6087.270538870976, 0.9994,
                           0.5773, 0.2172, 6627.206942186898, 0.999402998, 0.521068455, 0.217200652, 7167.143345502813,
                           0.9994, 0.464832771, 0.2172, 7707.0797488187345, 0.9994, 0.4086, 0.2172, 8247.016152134656,
                           0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 8786.952555450574,
                           0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 9326.888958766489,
                           0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 9866.82536208241, 0.949903037,
                           0.116867171, 0.252900603, 10406.761765398329, 0.903199533, 0.078432949, 0.291800389,
                           10946.69816871425, 0.8565, 0.04, 0.3307, 11486.634572030165, 0.798902627, 0.04333345,
                           0.358434298, 12026.570975346087, 0.741299424, 0.0466667, 0.386166944, 12566.507378662005,
                           0.6837, 0.05, 0.4139]
    resultLUT.ColorSpace = 'RGB'
    resultLUT.NanColor = [1.0, 0.0, 0.0]
    resultLUT.NumberOfTableValues = 32
    resultLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    calculator2_1Display.Representation = 'Surface'
    calculator2_1Display.ColorArrayName = ['POINTS', 'Result']
    calculator2_1Display.LookupTable = resultLUT
    calculator2_1Display.OSPRayScaleArray = 'Result'
    calculator2_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2_1Display.SelectOrientationVectors = 'U'
    calculator2_1Display.ScaleFactor = 0.2915555477142334
    calculator2_1Display.SelectScaleArray = 'Result'
    calculator2_1Display.GlyphType = 'Arrow'
    calculator2_1Display.GlyphTableIndexArray = 'Result'
    calculator2_1Display.GaussianRadius = 0.014577777385711671
    calculator2_1Display.SetScaleArray = ['POINTS', 'Result']
    calculator2_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2_1Display.OpacityArray = ['POINTS', 'Result']
    calculator2_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2_1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2_1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2_1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2_1Display.ScaleTransferFunction.Points = [-10110.821560606593, 0.0, 0.5, 0.0, 12566.507378662005, 1.0,
                                                         0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2_1Display.OpacityTransferFunction.Points = [-10110.821560606593, 0.0, 0.5, 0.0, 12566.507378662005, 1.0,
                                                           0.5, 0.0]

    # hide data in view
    Hide(generateSurfaceNormals1, renderView1)

    # show color bar/color legend
    calculator2_1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # Rescale transfer function
    dragLUT.RescaleTransferFunction(-381.24950400195667, 14112.55331074365)

    # Rescale transfer function
    dragPWF.RescaleTransferFunction(-381.24950400195667, 14112.55331074365)

    # get opacity transfer function/opacity map for 'Result'
    resultPWF = GetOpacityTransferFunction('Result')
    resultPWF.Points = [-10110.821560606593, 0.0, 0.5, 0.0, 12566.507378662005, 1.0, 0.5, 0.0]
    resultPWF.ScalarRangeInitialized = 1

    # Rescale transfer function
    resultLUT.RescaleTransferFunction(0.0, 80.0)

    # Rescale transfer function
    resultPWF.RescaleTransferFunction(0.0, 80.0)

    # hide data in view
    Hide(extractBlock2, renderView1)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'Lift_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    # hide data in view
    Hide(calculator2_1, renderView1)

    ##########                                                                     ##########
    ########## IMAGES OF THE CP IN THE CAR, THE CP IN X AXISA AND THE CP IN Z AXIS ##########
    ##########                                                                     ##########

    # create a new 'Calculator'
    calculator2_2 = Calculator(Input=extractBlock2)
    calculator2_2.Function = ''

    # rename source object
    RenameSource('Cp', calculator2_2)

    # Properties modified on calculator2_2
    calculator2_2.ResultArrayName = 'Cp'
    calculator2_2.Function = 'p/(0.5*1.1963*(' + str(simvelocity) + '^2))'

    # show data in view
    calculator2_2Display = Show(calculator2_2, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'Cp'
    cpLUT = GetColorTransferFunction('Cp')
    cpLUT.RescaleOnVisibilityChange = 1
    cpLUT.RGBPoints = [-105.86375409828455, 0.02, 0.3813, 0.9981, -103.26240866702662, 0.02000006, 0.424267768,
                       0.96906969, -100.6610632357687, 0.02, 0.467233763, 0.940033043, -98.05971780451077, 0.02, 0.5102,
                       0.911, -95.45837237325284, 0.02000006, 0.546401494, 0.872669438, -92.85702694199492, 0.02,
                       0.582600362, 0.83433295, -90.25568151073699, 0.02, 0.6188, 0.796, -87.65433607947907, 0.02000006,
                       0.652535156, 0.749802434, -85.05299064822114, 0.02, 0.686267004, 0.703599538, -82.45164521696321,
                       0.02, 0.72, 0.6574, -79.85029978570529, 0.02000006, 0.757035456, 0.603735359, -77.24895435444736,
                       0.02, 0.794067037, 0.55006613, -74.64760892318944, 0.02, 0.8311, 0.4964, -72.04626349193151,
                       0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -69.44491806067359,
                       0.023312914349117714, 0.897999359924484, 0.36073871343115577, -66.84357262941566,
                       0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -64.24222719815774,
                       0.27421074700988196, 0.952562960995083, 0.15356836602739213, -61.6408817668998,
                       0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -59.039536335641884, 0.6439, 0.9773,
                       0.0469, -56.43819090438396, 0.762401813, 0.984669591, 0.034600153, -53.83684547312604,
                       0.880901185, 0.992033407, 0.022299877, -51.23550004186811, 0.9995285432627147,
                       0.9995193706781492, 0.0134884641450013, -48.63415461061018, 0.999402998, 0.955036376,
                       0.079066628, -46.03280917935225, 0.9994, 0.910666223, 0.148134024, -43.43146374809433, 0.9994,
                       0.8663, 0.2172, -40.830118316836405, 0.999269665, 0.818035981, 0.217200652, -38.22877288557848,
                       0.999133332, 0.769766184, 0.2172, -35.627427454320554, 0.999, 0.7215, 0.2172, -33.02608202306263,
                       0.99913633, 0.673435546, 0.217200652, -30.424736591804717, 0.999266668, 0.625366186, 0.2172,
                       -27.823391160546777, 0.9994, 0.5773, 0.2172, -25.22204572928885, 0.999402998, 0.521068455,
                       0.217200652, -22.620700298030926, 0.9994, 0.464832771, 0.2172, -20.019354866773, 0.9994, 0.4086,
                       0.2172, -17.41800943551506, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206,
                       -14.816664004257149, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934,
                       -12.215318572999223, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357,
                       -9.613973141741297, 0.949903037, 0.116867171, 0.252900603, -7.012627710483372, 0.903199533,
                       0.078432949, 0.291800389, -4.411282279225432, 0.8565, 0.04, 0.3307, -1.8099368479675348,
                       0.798902627, 0.04333345, 0.358434298, 0.791408583290405, 0.741299424, 0.0466667, 0.386166944,
                       3.3927540145483306, 0.6837, 0.05, 0.4139]
    cpLUT.ColorSpace = 'RGB'
    cpLUT.NanColor = [1.0, 0.0, 0.0]
    cpLUT.NumberOfTableValues = 32
    cpLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    calculator2_2Display.Representation = 'Surface'
    calculator2_2Display.ColorArrayName = ['POINTS', 'Cp']
    calculator2_2Display.LookupTable = cpLUT
    calculator2_2Display.OSPRayScaleArray = 'Cp'
    calculator2_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2_2Display.SelectOrientationVectors = 'U'
    calculator2_2Display.ScaleFactor = 0.2915555477142334
    calculator2_2Display.SelectScaleArray = 'Cp'
    calculator2_2Display.GlyphType = 'Arrow'
    calculator2_2Display.GlyphTableIndexArray = 'Cp'
    calculator2_2Display.GaussianRadius = 0.014577777385711671
    calculator2_2Display.SetScaleArray = ['POINTS', 'Cp']
    calculator2_2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2_2Display.OpacityArray = ['POINTS', 'Cp']
    calculator2_2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2_2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2_2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2_2Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2_2Display.ScaleTransferFunction.Points = [-105.86375409828455, 0.0, 0.5, 0.0, 3.3927540145483306, 1.0,
                                                         0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2_2Display.OpacityTransferFunction.Points = [-105.86375409828455, 0.0, 0.5, 0.0, 3.3927540145483306, 1.0,
                                                           0.5, 0.0]

    # hide data in view
    Hide(extractBlock2, renderView1)

    # show color bar/color legend
    calculator2_2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'Cp'
    cpPWF = GetOpacityTransferFunction('Cp')
    cpPWF.Points = [-105.86375409828455, 0.0, 0.5, 0.0, 3.3927540145483306, 1.0, 0.5, 0.0]
    cpPWF.ScalarRangeInitialized = 1

    # get color legend/bar for cpLUT in view renderView1
    cpLUTColorBar = GetScalarBar(cpLUT, renderView1)
    cpLUTColorBar.Title = 'Cp'
    cpLUTColorBar.ComponentTitle = ''

    # Rescale transfer function
    cpLUT.RescaleTransferFunction(-1.0, 1.0)

    # Rescale transfer function
    cpPWF.RescaleTransferFunction(-1.0, 1.0)

    # hide data in view
    Hide(extractBlock2, renderView1)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'Cp_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    # hide data in view
    Hide(calculator2_2, renderView1)

    # create a new 'Generate Surface Normals'
    generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractBlock2)

    # show data in view
    generateSurfaceNormals2Display = Show(generateSurfaceNormals2, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    generateSurfaceNormals2Display.Representation = 'Surface'
    generateSurfaceNormals2Display.ColorArrayName = ['POINTS', 'p']
    generateSurfaceNormals2Display.LookupTable = pLUT
    generateSurfaceNormals2Display.OSPRayScaleArray = 'p'
    generateSurfaceNormals2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    generateSurfaceNormals2Display.SelectOrientationVectors = 'U'
    generateSurfaceNormals2Display.ScaleFactor = 0.2915555477142334
    generateSurfaceNormals2Display.SelectScaleArray = 'p'
    generateSurfaceNormals2Display.GlyphType = 'Arrow'
    generateSurfaceNormals2Display.GlyphTableIndexArray = 'p'
    generateSurfaceNormals2Display.GaussianRadius = 0.014577777385711671
    generateSurfaceNormals2Display.SetScaleArray = ['POINTS', 'p']
    generateSurfaceNormals2Display.ScaleTransferFunction = 'PiecewiseFunction'
    generateSurfaceNormals2Display.OpacityArray = ['POINTS', 'p']
    generateSurfaceNormals2Display.OpacityTransferFunction = 'PiecewiseFunction'
    generateSurfaceNormals2Display.DataAxesGrid = 'GridAxesRepresentation'
    generateSurfaceNormals2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    generateSurfaceNormals2Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062,
                                                                 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    generateSurfaceNormals2Display.ScaleTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0, 456.60955810546875,
                                                                   1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    generateSurfaceNormals2Display.OpacityTransferFunction.Points = [-14247.541015625, 0.0, 0.5, 0.0,
                                                                     456.60955810546875, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(extractBlock2, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Calculator'
    calculator2_3 = Calculator(Input=generateSurfaceNormals2)
    calculator2_3.Function = ''

    # rename source object
    RenameSource('CpX', calculator2_3)

    # Properties modified on calculator2_3
    calculator2_3.ResultArrayName = 'CpX'
    calculator2_3.Function = '(p/(0.5*1.1963*(' + str(simvelocity) + '^2)))*Normals_X'

    # show data in view
    calculator2_3Display = Show(calculator2_3, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'CpX'
    cpXLUT = GetColorTransferFunction('CpX')
    cpXLUT.RescaleOnVisibilityChange = 1
    cpXLUT.RGBPoints = [-2.8328048817331717, 0.02, 0.3813, 0.9981, -0.2686725610909786, 0.02000006, 0.424267768,
                        0.96906969,
                        2.2954597595512145, 0.02, 0.467233763, 0.940033043, 4.859592080193407, 0.02, 0.5102, 0.911,
                        7.423724400835601, 0.02000006, 0.546401494, 0.872669438, 9.987856721477792, 0.02, 0.582600362,
                        0.83433295, 12.551989042119986, 0.02, 0.6188, 0.796, 15.116121362762176, 0.02000006,
                        0.652535156,
                        0.749802434, 17.680253683404374, 0.02, 0.686267004, 0.703599538, 20.244386004046564, 0.02, 0.72,
                        0.6574, 22.808518324688755, 0.02000006, 0.757035456, 0.603735359, 25.372650645330953, 0.02,
                        0.794067037, 0.55006613, 27.936782965973144, 0.02, 0.8311, 0.4964, 30.500915286615342,
                        0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 33.065047607257526,
                        0.023312914349117714, 0.897999359924484, 0.36073871343115577, 35.62917992789972,
                        0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 38.193312248541915,
                        0.27421074700988196, 0.952562960995083, 0.15356836602739213, 40.757444569184116,
                        0.4933546281681699,
                        0.9619038625309482, 0.11119493614749336, 43.3215768898263, 0.6439, 0.9773, 0.0469,
                        45.88570921046849, 0.762401813, 0.984669591, 0.034600153, 48.44984153111068, 0.880901185,
                        0.992033407, 0.022299877, 51.01397385175288, 0.9995285432627147, 0.9995193706781492,
                        0.0134884641450013, 53.578106172395074, 0.999402998, 0.955036376, 0.079066628,
                        56.14223849303727,
                        0.9994, 0.910666223, 0.148134024, 58.706370813679456, 0.9994, 0.8663, 0.2172, 61.27050313432165,
                        0.999269665, 0.818035981, 0.217200652, 63.83463545496385, 0.999133332, 0.769766184, 0.2172,
                        66.39876777560605, 0.999, 0.7215, 0.2172, 68.96290009624823, 0.99913633, 0.673435546,
                        0.217200652,
                        71.52703241689042, 0.999266668, 0.625366186, 0.2172, 74.09116473753262, 0.9994, 0.5773, 0.2172,
                        76.65529705817482, 0.999402998, 0.521068455, 0.217200652, 79.21942937881701, 0.9994,
                        0.464832771,
                        0.2172, 81.7835616994592, 0.9994, 0.4086, 0.2172, 84.34769402010141, 0.9947599917687346,
                        0.33177297300202935, 0.2112309638520206, 86.91182634074359, 0.9867129505479589,
                        0.2595183410914934,
                        0.19012239549291934, 89.47595866138577, 0.9912458875646419, 0.14799417507952672,
                        0.21078892136920357, 92.04009098202798, 0.949903037, 0.116867171, 0.252900603,
                        94.60422330267016,
                        0.903199533, 0.078432949, 0.291800389, 97.16835562331238, 0.8565, 0.04, 0.3307,
                        99.73248794395454,
                        0.798902627, 0.04333345, 0.358434298, 102.29662026459674, 0.741299424, 0.0466667, 0.386166944,
                        104.86075258523894, 0.6837, 0.05, 0.4139]
    cpXLUT.ColorSpace = 'RGB'
    cpXLUT.NanColor = [1.0, 0.0, 0.0]
    cpXLUT.NumberOfTableValues = 32
    cpXLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    calculator2_3Display.Representation = 'Surface'
    calculator2_3Display.ColorArrayName = ['POINTS', 'CpX']
    calculator2_3Display.LookupTable = cpXLUT
    calculator2_3Display.OSPRayScaleArray = 'CpX'
    calculator2_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2_3Display.SelectOrientationVectors = 'U'
    calculator2_3Display.ScaleFactor = 0.2915555477142334
    calculator2_3Display.SelectScaleArray = 'CpX'
    calculator2_3Display.GlyphType = 'Arrow'
    calculator2_3Display.GlyphTableIndexArray = 'CpX'
    calculator2_3Display.GaussianRadius = 0.014577777385711671
    calculator2_3Display.SetScaleArray = ['POINTS', 'CpX']
    calculator2_3Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2_3Display.OpacityArray = ['POINTS', 'CpX']
    calculator2_3Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2_3Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2_3Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2_3Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2_3Display.ScaleTransferFunction.Points = [-2.8328048817331717, 0.0, 0.5, 0.0, 104.86075258523894, 1.0,
                                                         0.5,
                                                         0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2_3Display.OpacityTransferFunction.Points = [-2.8328048817331717, 0.0, 0.5, 0.0, 104.86075258523894, 1.0,
                                                           0.5,
                                                           0.0]

    # hide data in view
    Hide(generateSurfaceNormals2, renderView1)

    # show color bar/color legend
    calculator2_3Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'CpX'
    cpXPWF = GetOpacityTransferFunction('CpX')
    cpXPWF.Points = [-2.8328048817331717, 0.0, 0.5, 0.0, 104.86075258523894, 1.0, 0.5, 0.0]
    cpXPWF.ScalarRangeInitialized = 1

    # Rescale transfer function
    cpXLUT.RescaleTransferFunction(-1.0, 1.0)

    # Rescale transfer function
    cpXPWF.RescaleTransferFunction(-1.0, 1.0)

    # hide data in view
    Hide(extractBlock2, renderView1)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'CpX_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)

    # hide data in view
    Hide(calculator2_3, renderView1)

    # create a new 'Calculator'
    calculator2_4 = Calculator(Input=generateSurfaceNormals2)
    calculator2_4.Function = ''

    # rename source object
    RenameSource('CpZ', calculator2_4)

    # Properties modified on calculator2_4
    calculator2_4.ResultArrayName = 'CpZ'
    calculator2_4.Function = '(p/(0.5*1.1963*(' + str(simvelocity) + '^2)))*Normals_Z'

    # show data in view
    calculator2_4Display = Show(calculator2_4, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'CpZ'
    cpZLUT = GetColorTransferFunction('CpZ')
    cpZLUT.RescaleOnVisibilityChange = 1
    cpZLUT.RGBPoints = [-75.1266149190121, 0.02, 0.3813, 0.9981, -71.11471598384408, 0.02000006, 0.424267768,
                        0.96906969,
                        -67.10281704867606, 0.02, 0.467233763, 0.940033043, -63.09091811350804, 0.02, 0.5102, 0.911,
                        -59.07901917834002, 0.02000006, 0.546401494, 0.872669438, -55.067120243172, 0.02, 0.582600362,
                        0.83433295, -51.05522130800398, 0.02, 0.6188, 0.796, -47.04332237283596, 0.02000006,
                        0.652535156,
                        0.749802434, -43.03142343766793, 0.02, 0.686267004, 0.703599538, -39.01952450249991, 0.02, 0.72,
                        0.6574, -35.0076255673319, 0.02000006, 0.757035456, 0.603735359, -30.995726632163873, 0.02,
                        0.794067037, 0.55006613, -26.983827696995853, 0.02, 0.8311, 0.4964, -22.971928761827833,
                        0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -18.960029826659813,
                        0.023312914349117714, 0.897999359924484, 0.36073871343115577, -14.948130891491786,
                        0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -10.936231956323766,
                        0.27421074700988196, 0.952562960995083, 0.15356836602739213, -6.924333021155732,
                        0.4933546281681699,
                        0.9619038625309482, 0.11119493614749336, -2.9124340859877265, 0.6439, 0.9773, 0.0469,
                        1.0994648491802934, 0.762401813, 0.984669591, 0.034600153, 5.111363784348299, 0.880901185,
                        0.992033407, 0.022299877, 9.123262719516333, 0.9995285432627147, 0.9995193706781492,
                        0.0134884641450013, 13.135161654684353, 0.999402998, 0.955036376, 0.079066628,
                        17.147060589852387,
                        0.9994, 0.910666223, 0.148134024, 21.158959525020393, 0.9994, 0.8663, 0.2172,
                        25.170858460188413,
                        0.999269665, 0.818035981, 0.217200652, 29.182757395356433, 0.999133332, 0.769766184, 0.2172,
                        33.19465633052447, 0.999, 0.7215, 0.2172, 37.20655526569247, 0.99913633, 0.673435546,
                        0.217200652,
                        41.21845420086048, 0.999266668, 0.625366186, 0.2172, 45.230353136028526, 0.9994, 0.5773, 0.2172,
                        49.242252071196546, 0.999402998, 0.521068455, 0.217200652, 53.254151006364566, 0.9994,
                        0.464832771,
                        0.2172, 57.26604994153257, 0.9994, 0.4086, 0.2172, 61.277948876700634, 0.9947599917687346,
                        0.33177297300202935, 0.2112309638520206, 65.28984781186864, 0.9867129505479589,
                        0.2595183410914934,
                        0.19012239549291934, 69.30174674703665, 0.9912458875646419, 0.14799417507952672,
                        0.21078892136920357, 73.31364568220465, 0.949903037, 0.116867171, 0.252900603,
                        77.32554461737269,
                        0.903199533, 0.078432949, 0.291800389, 81.33744355254072, 0.8565, 0.04, 0.3307,
                        85.3493424877087,
                        0.798902627, 0.04333345, 0.358434298, 89.36124142287673, 0.741299424, 0.0466667, 0.386166944,
                        93.37314035804476, 0.6837, 0.05, 0.4139]
    cpZLUT.ColorSpace = 'RGB'
    cpZLUT.NanColor = [1.0, 0.0, 0.0]
    cpZLUT.NumberOfTableValues = 32
    cpZLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    calculator2_4Display.Representation = 'Surface'
    calculator2_4Display.ColorArrayName = ['POINTS', 'CpZ']
    calculator2_4Display.LookupTable = cpZLUT
    calculator2_4Display.OSPRayScaleArray = 'CpZ'
    calculator2_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2_4Display.SelectOrientationVectors = 'U'
    calculator2_4Display.ScaleFactor = 0.2915555477142334
    calculator2_4Display.SelectScaleArray = 'CpZ'
    calculator2_4Display.GlyphType = 'Arrow'
    calculator2_4Display.GlyphTableIndexArray = 'CpZ'
    calculator2_4Display.GaussianRadius = 0.014577777385711671
    calculator2_4Display.SetScaleArray = ['POINTS', 'CpZ']
    calculator2_4Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2_4Display.OpacityArray = ['POINTS', 'CpZ']
    calculator2_4Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2_4Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2_4Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    calculator2_4Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5,
                                                       0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2_4Display.ScaleTransferFunction.Points = [-75.1266149190121, 0.0, 0.5, 0.0, 93.37314035804476, 1.0, 0.5,
                                                         0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2_4Display.OpacityTransferFunction.Points = [-75.1266149190121, 0.0, 0.5, 0.0, 93.37314035804476, 1.0,
                                                           0.5,
                                                           0.0]
    # reset view to fit data
    renderView1.ResetCamera()

    # hide data in view
    Hide(generateSurfaceNormals2, renderView1)

    # show color bar/color legend
    calculator2_4Display.SetScalarBarVisibility(renderView1, True)

    # get opacity transfer function/opacity map for 'CpZ'
    cpZPWF = GetOpacityTransferFunction('CpZ')
    cpZPWF.Points = [-75.1266149190121, 0.0, 0.5, 0.0, 93.37314035804476, 1.0, 0.5, 0.0]
    cpZPWF.ScalarRangeInitialized = 1

    # Rescale transfer function
    cpZLUT.RescaleTransferFunction(-1.0, 1.0)

    # Rescale transfer function
    cpZPWF.RescaleTransferFunction(-1.0, 1.0)

    # hide data in view
    Hide(extractBlock2, renderView1)

    for stl_view in stl_views:
        renderView1.CameraPosition = stl_camera[stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[stl_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + stl_view + 'CpZ_CAR.png', renderView1,
                       ImageResolution=info["ImageRes"])
    Delete(CarSTLDisplay)



