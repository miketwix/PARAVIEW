
def AllImagesViews():
    for i in [1, 2, 3]:
        for j in car_views()[i].keys():
            #info = ""
            #sim = definido por ParaView
            ViewName = car_views()[0][i-1] + "_" + j
            Position = car_views()[i][j]["Position"]
            FocalPoint = car_views()[i][j]["FocalPoint"]
            ViewUp = car_views()[i][j]["ViewUp"]
            ParallelScale = car_views()[i][j]["ParallelScale"]

            analyze_sim (info,sim,ViewName,Position,FocalPoint,ViewUp,ParallelScale)