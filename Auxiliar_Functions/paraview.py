from paraview.simple import *

def run_paraview (sim_id[id])
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'STL Reader'
    mFT02_wingSupp2stl = STLReader(FileNames=[])

    # destroy mFT02_wingSupp2stl
    Delete(mFT02_wingSupp2stl)
    del mFT02_wingSupp2stl