from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
mFT02_311C1402CARstl = STLReader(registrationName='MFT02_311-C1-402-CAR.stl', FileNames=['C:\\Users\\fitir\\Desktop\\Paraview_Batch_Postproc\\Case_Files\\Prueba de paraview\\MFT02_311-C1-402-CAR.stl'])

# set active source
SetActiveSource(mFT02_311C1402CARstl)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
mFT02_311C1402CARstlDisplay = Show(mFT02_311C1402CARstl, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')
sTLSolidLabelingLUT.RescaleOnVisibilityChange = 1
sTLSolidLabelingLUT.RGBPoints = [0.0, 0.02, 0.3813, 0.9981, 0.21428571428571427, 0.02000006, 0.424267768, 0.96906969, 0.42857142857142855, 0.02, 0.467233763, 0.940033043, 0.6428571428571428, 0.02, 0.5102, 0.911, 0.8571428571428571, 0.02000006, 0.546401494, 0.872669438, 1.0714285714285712, 0.02, 0.582600362, 0.83433295, 1.2857142857142856, 0.02, 0.6188, 0.796, 1.4999999999999996, 0.02000006, 0.652535156, 0.749802434, 1.7142857142857142, 0.02, 0.686267004, 0.703599538, 1.9285714285714284, 0.02, 0.72, 0.6574, 2.1428571428571423, 0.02000006, 0.757035456, 0.603735359, 2.357142857142857, 0.02, 0.794067037, 0.55006613, 2.571428571428571, 0.02, 0.8311, 0.4964, 2.7857142857142856, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 3.0, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 3.2142857142857144, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 3.4285714285714284, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 3.6428571428571432, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 3.8571428571428568, 0.6439, 0.9773, 0.0469, 4.071428571428571, 0.762401813, 0.984669591, 0.034600153, 4.285714285714285, 0.880901185, 0.992033407, 0.022299877, 4.5, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 4.714285714285714, 0.999402998, 0.955036376, 0.079066628, 4.928571428571429, 0.9994, 0.910666223, 0.148134024, 5.142857142857142, 0.9994, 0.8663, 0.2172, 5.357142857142857, 0.999269665, 0.818035981, 0.217200652, 5.571428571428571, 0.999133332, 0.769766184, 0.2172, 5.7857142857142865, 0.999, 0.7215, 0.2172, 6.0, 0.99913633, 0.673435546, 0.217200652, 6.2142857142857135, 0.999266668, 0.625366186, 0.2172, 6.428571428571429, 0.9994, 0.5773, 0.2172, 6.642857142857143, 0.999402998, 0.521068455, 0.217200652, 6.857142857142857, 0.9994, 0.464832771, 0.2172, 7.071428571428571, 0.9994, 0.4086, 0.2172, 7.2857142857142865, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 7.5, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 7.7142857142857135, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 7.928571428571429, 0.949903037, 0.116867171, 0.252900603, 8.142857142857142, 0.903199533, 0.078432949, 0.291800389, 8.357142857142858, 0.8565, 0.04, 0.3307, 8.57142857142857, 0.798902627, 0.04333345, 0.358434298, 8.785714285714285, 0.741299424, 0.0466667, 0.386166944, 9.0, 0.6837, 0.05, 0.4139]
sTLSolidLabelingLUT.ColorSpace = 'RGB'
sTLSolidLabelingLUT.NanColor = [1.0, 0.0, 0.0]
sTLSolidLabelingLUT.NumberOfTableValues = 32
sTLSolidLabelingLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
mFT02_311C1402CARstlDisplay.Representation = 'Surface'
mFT02_311C1402CARstlDisplay.ColorArrayName = ['CELLS', 'STLSolidLabeling']
mFT02_311C1402CARstlDisplay.LookupTable = sTLSolidLabelingLUT
mFT02_311C1402CARstlDisplay.SelectTCoordArray = 'None'
mFT02_311C1402CARstlDisplay.SelectNormalArray = 'None'
mFT02_311C1402CARstlDisplay.SelectTangentArray = 'None'
mFT02_311C1402CARstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mFT02_311C1402CARstlDisplay.SelectOrientationVectors = 'None'
mFT02_311C1402CARstlDisplay.ScaleFactor = 0.2915771007537842
mFT02_311C1402CARstlDisplay.SelectScaleArray = 'STLSolidLabeling'
mFT02_311C1402CARstlDisplay.GlyphType = 'Arrow'
mFT02_311C1402CARstlDisplay.GlyphTableIndexArray = 'STLSolidLabeling'
mFT02_311C1402CARstlDisplay.GaussianRadius = 0.01457885503768921
mFT02_311C1402CARstlDisplay.SetScaleArray = [None, '']
mFT02_311C1402CARstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mFT02_311C1402CARstlDisplay.OpacityArray = [None, '']
mFT02_311C1402CARstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mFT02_311C1402CARstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
mFT02_311C1402CARstlDisplay.PolarAxes = 'PolarAxesRepresentation'
mFT02_311C1402CARstlDisplay.SelectInputVectors = ['CELLS', 'STLSolidLabeling']
mFT02_311C1402CARstlDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mFT02_311C1402CARstlDisplay.OSPRayScaleFunction.Points = [0.08105005493164062, 0.0, 0.5, 0.0, 810.5005493164062, 1.0, 0.5, 0.0]

# show color bar/color legend
mFT02_311C1402CARstlDisplay.SetScalarBarVisibility(renderView1, True)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# get opacity transfer function/opacity map for 'STLSolidLabeling'
sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')
sTLSolidLabelingPWF.Points = [0.0, 0.0, 0.5, 0.0, 9.0, 1.0, 0.5, 0.0]
sTLSolidLabelingPWF.ScalarRangeInitialized = 1

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(2132, 1046)

# current camera placement for renderView1
renderView1.CameraPosition = [-4.536598631089438, 4.056588839416917, 1.5828243202411878]
renderView1.CameraFocalPoint = [0.5183476589260684, -0.02966465871146555, 0.5758308368413083]
renderView1.CameraViewUp = [0.22769322072305787, 0.04193178077994626, 0.9728296474704003]
renderView1.CameraParallelScale = 1.7023916985995404

# save screenshot
SaveScreenshot('C:/Users/fitir/Desktop/Paraview_Batch_Postproc/Case_Files/Prueba de paraview/STL_Photo.png', renderView1, ImageResolution=[2132, 1046])


#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2132, 1046)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-4.536598631089438, 4.056588839416917, 1.5828243202411878]
renderView1.CameraFocalPoint = [0.5183476589260684, -0.02966465871146555, 0.5758308368413083]
renderView1.CameraViewUp = [0.22769322072305787, 0.04193178077994626, 0.9728296474704003]
renderView1.CameraParallelScale = 1.7023916985995404

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).