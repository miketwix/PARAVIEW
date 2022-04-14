from paraview.simple import *
from Auxiliar_Functions.viewsDict import car_views

def slice_image(info,sim):
    paraview.simple._DisableFirstRenderCameraReset()

    [stl_camera, slice_camera, car_camera] = car_views()
    slice_views = dict.keys(slice_camera)

    # create a new 'OpenFOAMReader'

    CarSlice = SliceReader(registrationName= sim.name + 'car', FileNames=[sim.foam])
    casefoam.MeshRegions = ['internalMesh']
    casefoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p', 'wallShearStress', 'yPlus']

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # Properties modified on casefoam
    casefoam.MeshRegions = ['group/symmetry', 'group/wall', 'internalMesh', 'patch/B12_TE6_B12_TE1', 'patch/B12_TE6_B12_TE147', 'patch/B12_TE6_B12_TE149', 'patch/B12_TE6_B12_TE150', 'patch/B12_TE6_B12_TE151', 'patch/B12_TE6_B12_TE152', 'patch/B12_TE6_B12_TE153', 'patch/B12_TE6_B12_TE154', 'patch/B12_TE6_B12_TE155', 'patch/B14_TE6_B14_TE37', 'patch/B15_TE6_B15_TE1004', 'patch/B15_TE6_B15_TE1005', 'patch/B15_TE6_B15_TE1050', 'patch/B15_TE6_B15_TE1052', 'patch/B15_TE6_B15_TE1056', 'patch/B15_TE6_B15_TE1057', 'patch/B15_TE6_B15_TE982', 'patch/B15_TE6_B15_TE983', 'patch/B15_TE6_B15_TE986', 'patch/B15_TE6_B15_TE987', 'patch/B15_TE6_B15_TE988', 'patch/B15_TE6_B15_TE989', 'patch/B15_TE6_B15_TE990', 'patch/B16_TE6_B16_TE1', 'patch/B16_TE6_B16_TE85', 'patch/B16_TE6_B16_TE87', 'patch/B16_TE6_B16_TE88', 'patch/B16_TE6_B16_TE89', 'patch/B16_TE6_B16_TE90', 'patch/B17_TE6_B17_TE109', 'patch/B17_TE6_B17_TE110', 'patch/B17_TE6_B17_TE112', 'patch/B18_TE6_B18_TE293', 'patch/B18_TE6_B18_TE294', 'patch/B18_TE6_B18_TE295', 'patch/B18_TE6_B18_TE296', 'patch/B18_TE6_B18_TE304', 'patch/B1_TE5_B1_TE138', 'patch/B1_TE5_B1_TE141', 'patch/B1_TE5_B1_TE142', 'patch/B1_TE5_B1_TE143', 'patch/B1_TE5_B1_TE145', 'patch/B1_TE5_B1_TE146', 'patch/B1_TE5_B1_TE2', 'patch/B20_TE6_B20_TE73', 'patch/B20_TE6_B20_TE74', 'patch/B20_TE6_B20_TE77', 'patch/B20_TE6_B20_TE79', 'patch/B21_TE6_B21_TE1', 'patch/B2_TE6_B2_TE1', 'patch/B2_TE6_B2_TE25', 'patch/B3_TE6_B3_TE1', 'patch/B3_TE6_B3_TE337', 'patch/B3_TE6_B3_TE340', 'patch/B4_TE5_B4_TE2', 'patch/B4_TE5_B4_TE242', 'patch/B4_TE5_B4_TE245', 'patch/B4_TE5_B4_TE246', 'patch/B4_TE5_B4_TE247', 'patch/B4_TE5_B4_TE248', 'patch/B4_TE5_B4_TE249', 'patch/B4_TE5_B4_TE250', 'patch/B4_TE5_B4_TE252', 'patch/B5_TE5_B5_TE86', 'patch/B5_TE5_B5_TE91', 'patch/B6_TE5_B6_TE158', 'patch/B6_TE5_B6_TE159', 'patch/B6_TE5_B6_TE161', 'patch/B6_TE5_B6_TE162', 'patch/B6_TE5_B6_TE163', 'patch/B6_TE5_B6_TE164', 'patch/B6_TE5_B6_TE165', 'patch/B6_TE5_B6_TE2', 'patch/B8_TE6_B8_TE73', 'patch/B8_TE6_B8_TE74', 'patch/B8_TE6_B8_TE77', 'patch/B9_TE6_B9_TE1', 'patch/boundingBox1', 'patch/boundingBox2', 'patch/boundingBox3', 'patch/boundingBox4', 'patch/boundingBox5', 'patch/boundingBox6']

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    casefoamDisplay = Show(casefoam, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'p'
    pLUT = GetColorTransferFunction('p')
    pLUT.RescaleOnVisibilityChange = 1
    pLUT.RGBPoints = [-42126.4296875, 0.02, 0.3813, 0.9981, -41104.121824718655, 0.02000006, 0.424267768, 0.96906969, -40081.81396193731, 0.02, 0.467233763, 0.940033043, -39059.50609915597, 0.02, 0.5102, 0.911, -38037.19823637463, 0.02000006, 0.546401494, 0.872669438, -37014.89037359328, 0.02, 0.582600362, 0.83433295, -35992.582510811946, 0.02, 0.6188, 0.796, -34970.2746480306, 0.02000006, 0.652535156, 0.749802434, -33947.96678524926, 0.02, 0.686267004, 0.703599538, -32925.65892246791, 0.02, 0.72, 0.6574, -31903.35105968657, 0.02000006, 0.757035456, 0.603735359, -30881.043196905226, 0.02, 0.794067037, 0.55006613, -29858.735334123885, 0.02, 0.8311, 0.4964, -28836.42747134254, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -27814.1196085612, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, -26791.811745779854, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -25769.503882998513, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, -24747.196020217165, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -23724.888157435827, 0.6439, 0.9773, 0.0469, -22702.580294654483, 0.762401813, 0.984669591, 0.034600153, -21680.27243187314, 0.880901185, 0.992033407, 0.022299877, -20657.964569091797, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, -19635.656706310452, 0.999402998, 0.955036376, 0.079066628, -18613.348843529107, 0.9994, 0.910666223, 0.148134024, -17591.04098074777, 0.9994, 0.8663, 0.2172, -16568.733117966425, 0.999269665, 0.818035981, 0.217200652, -15546.42525518508, 0.999133332, 0.769766184, 0.2172, -14524.117392403736, 0.999, 0.7215, 0.2172, -13501.809529622398, 0.99913633, 0.673435546, 0.217200652, -12479.501666841057, 0.999266668, 0.625366186, 0.2172, -11457.193804059709, 0.9994, 0.5773, 0.2172, -10434.885941278364, 0.999402998, 0.521068455, 0.217200652, -9412.578078497027, 0.9994, 0.464832771, 0.2172, -8390.270215715682, 0.9994, 0.4086, 0.2172, -7367.96235293433, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, -6345.654490152992, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, -5323.346627371655, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, -4301.03876459031, 0.949903037, 0.116867171, 0.252900603, -3278.7309018089654, 0.903199533, 0.078432949, 0.291800389, -2256.4230390276134, 0.8565, 0.04, 0.3307, -1234.1151762462832, 0.798902627, 0.04333345, 0.358434298, -211.8073134649385, 0.741299424, 0.0466667, 0.386166944, 810.5005493164062, 0.6837, 0.05, 0.4139]
    pLUT.ColorSpace = 'RGB'
    pLUT.NanColor = [1.0, 0.0, 0.0]
    pLUT.NumberOfTableValues = 32
    pLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    casefoamDisplay.Representation = 'Surface'
    casefoamDisplay.ColorArrayName = ['POINTS', 'p']
    casefoamDisplay.LookupTable = pLUT
    casefoamDisplay.SelectTCoordArray = 'None'
    casefoamDisplay.SelectNormalArray = 'None'
    casefoamDisplay.SelectTangentArray = 'None'
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
    casefoamDisplay.SelectInputVectors = ['POINTS', 'U']
    casefoamDisplay.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    casefoamDisplay.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    casefoamDisplay.ScaleTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    casefoamDisplay.OpacityTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # show color bar/color legend
    casefoamDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'p'
    pPWF = GetOpacityTransferFunction('p')
    pPWF.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]
    pPWF.ScalarRangeInitialized = 1

    # create a new 'Extract Block'
    extractBlock1 = ExtractBlock(registrationName='ExtractBlock1', Input=casefoam)

    # Properties modified on extractBlock1
    extractBlock1.Selectors = ['/Root/internalMesh']

    # show data in view
    extractBlock1Display = Show(extractBlock1, renderView1, 'UnstructuredGridRepresentation')    #eliminado

    # trace defaults for the display properties.
    extractBlock1Display.Representation = 'Surface'
    extractBlock1Display.ColorArrayName = ['POINTS', 'p']
    extractBlock1Display.LookupTable = pLUT
    extractBlock1Display.SelectTCoordArray = 'None'
    extractBlock1Display.SelectNormalArray = 'None'
    extractBlock1Display.SelectTangentArray = 'None'
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
    extractBlock1Display.OpacityArrayName = ['POINTS', 'p']
    extractBlock1Display.SelectInputVectors = ['POINTS', 'U']
    extractBlock1Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    extractBlock1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0] #?

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    extractBlock1Display.ScaleTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0] #?

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    extractBlock1Display.OpacityTransferFunction.Points = [-42126.4296875, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0] #?

    # hide data in view
    Hide(casefoam, renderView1)

    # show color bar/color legend
    extractBlock1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update() #?

    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=extractBlock1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [5.5, 3.5, 3.6059999256394804]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [5.5, 3.5, 3.6059999256394804]

    # set active source
    SetActiveSource(slice1)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice1.SliceType)

    # hide data in view
    Hide(extractBlock1, renderView1) #eliminado

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType) #eliminado

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=slice1.SliceType) #eliminado

    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0 #eliminado

    # reset view to fit data
    renderView1.ResetCamera(False) #?

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType) # ?


    # reset view to fit data
    renderView1.ResetCamera(False)

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [5.5, 0.002919374333856495, 3.6059999256394804]
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'p']
    slice1Display.LookupTable = pLUT
    slice1Display.SelectTCoordArray = 'None'
    slice1Display.SelectNormalArray = 'None'
    slice1Display.SelectTangentArray = 'None'
    slice1Display.OSPRayScaleArray = 'p'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'U'
    slice1Display.ScaleFactor = 2.8000000000000003
    slice1Display.SelectScaleArray = 'p'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'p'
    slice1Display.GaussianRadius = 0.14
    slice1Display.SetScaleArray = ['POINTS', 'p']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'p']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.SelectInputVectors = ['POINTS', 'U']
    slice1Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    slice1Display.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [-325.0738525390625, 0.0, 0.5, 0.0, 136.2366485595703, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [-325.0738525390625, 0.0, 0.5, 0.0, 136.2366485595703, 1.0, 0.5, 0.0]
2
    Hide(extractBlock1, renderView1) #eliminado

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True) #eliminado

    # update the view to ensure updated data information
    renderView1.Update() #?

    # set scalar coloring
    ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1) #? igual no permite ver la barra de colores

    # rescale color and/or opacity maps used to include current data range
    slice1Display.RescaleTransferFunctionToDataRange(True, False) #puede ser util para variar el rango del mapa de color

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'U'
    uLUT = GetColorTransferFunction('U')
    uLUT.RescaleOnVisibilityChange = 1
    uLUT.RGBPoints = [0.0, 0.02, 0.3813, 0.9981, 2.790735296602469, 0.02000006, 0.424267768, 0.96906969, 5.581470593204938, 0.02, 0.467233763, 0.940033043, 8.372205889807407, 0.02, 0.5102, 0.911, 11.162941186409876, 0.02000006, 0.546401494, 0.872669438, 13.953676483012345, 0.02, 0.582600362, 0.83433295, 16.744411779614815, 0.02, 0.6188, 0.796, 19.53514707621728, 0.02000006, 0.652535156, 0.749802434, 22.325882372819752, 0.02, 0.686267004, 0.703599538, 25.116617669422222, 0.02, 0.72, 0.6574, 27.90735296602469, 0.02000006, 0.757035456, 0.603735359, 30.698088262627163, 0.02, 0.794067037, 0.55006613, 33.48882355922963, 0.02, 0.8311, 0.4964, 36.2795588558321, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 39.07029415243457, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 41.86102944903704, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 44.651764745639504, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 47.44250004224199, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 50.233235338844445, 0.6439, 0.9773, 0.0469, 53.023970635446915, 0.762401813, 0.984669591, 0.034600153, 55.81470593204938, 0.880901185, 0.992033407, 0.022299877, 58.605441228651856, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 61.396176525254326, 0.999402998, 0.955036376, 0.079066628, 64.1869118218568, 0.9994, 0.910666223, 0.148134024, 66.97764711845926, 0.9994, 0.8663, 0.2172, 69.76838241506174, 0.999269665, 0.818035981, 0.217200652, 72.5591177116642, 0.999133332, 0.769766184, 0.2172, 75.34985300826668, 0.999, 0.7215, 0.2172, 78.14058830486914, 0.99913633, 0.673435546, 0.217200652, 80.93132360147159, 0.999266668, 0.625366186, 0.2172, 83.72205889807408, 0.9994, 0.5773, 0.2172, 86.51279419467656, 0.999402998, 0.521068455, 0.217200652, 89.30352949127901, 0.9994, 0.464832771, 0.2172, 92.09426478788149, 0.9994, 0.4086, 0.2172, 94.88500008448398, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 97.67573538108643, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 100.46647067768889, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 103.25720597429137, 0.949903037, 0.116867171, 0.252900603, 106.04794127089383, 0.903199533, 0.078432949, 0.291800389, 108.83867656749632, 0.8565, 0.04, 0.3307, 111.62941186409876, 0.798902627, 0.04333345, 0.358434298, 114.42014716070123, 0.741299424, 0.0466667, 0.386166944, 117.21088245730371, 0.6837, 0.05, 0.4139]
    uLUT.ColorSpace = 'RGB'
    uLUT.NanColor = [1.0, 0.0, 0.0]
    uLUT.NumberOfTableValues = 32
    uLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'U'
    uPWF = GetOpacityTransferFunction('U')
    uPWF.Points = [0.0, 0.0, 0.5, 0.0, 117.21088245730371, 1.0, 0.5, 0.0]
    uPWF.ScalarRangeInitialized = 1

    # Rescale transfer function
    uLUT.RescaleTransferFunction(0.0, 30.0)

    # Rescale transfer function
    uPWF.RescaleTransferFunction(0.0, 30.0)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # reset view to fit data
    renderView1.ResetCamera(False) #eliminado

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2132, 1044)

    for slice_view in slice_views:
        renderView1.CameraPosition = slice_camera[slcie_view]["Position"]
        renderView1.CameraFocalPoint = slice_camera[slice_view]["FocalPoint"]
        renderView1.CameraViewUp = slice_camera[slice_view]["ViewUp"]
        renderView1.CameraParallelScale = slice_camera[slice_view]["ParallelScale"]
        # save screenshot
        SaveScreenshot(str(sim.outFolder) + '\\' + str(sim.name) + '_' + slice_view + '.png', renderView1,ImageResolution=info["ImageRes"])

Delete(casefoam)
