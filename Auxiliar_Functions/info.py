import json
import os


def get_info():
    # Opening JSON file
    f = open("C:\\Users\\Usuario\\Desktop\\Paraview_Batch_Postproc\\config.json")

    # returns JSON object as
    # a dictionary
    setup_info = json.load(f)

    # Closing file
    f.close()

    return setup_info


