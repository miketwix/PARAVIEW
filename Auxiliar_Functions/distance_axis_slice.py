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


    for part_stl_view in part_stl_views:
        renderView1.CameraPosition = stl_camera[part_stl_view]["Position"]
        renderView1.CameraFocalPoint = stl_camera[part_stl_view]["FocalPoint"]
        renderView1.CameraViewUp = stl_camera[part_stl_view]["ViewUp"]
        renderView1.CameraParallelScale = stl_camera[part_stl_view]["ParallelScale"]
    # save screenshot
        SaveScreenshot(str(sim.outFolder)+'\\'+str(sim.name)+'_'+part_stl_view+'.png', renderView1, ImageResolution=info["ImageRes"])
    Delete(PartSTLDisplay)