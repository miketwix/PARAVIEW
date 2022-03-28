def car_views():
    # MODIFY VIEWS HERE #######################################################################################

    # VIEWS DICTIONARIES. There are currently three dictionaries
    # which contain data por stl positioning for the differentdw
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
    return stl_views_dictionary, slice_views_dictionary, car_views_dictionary

