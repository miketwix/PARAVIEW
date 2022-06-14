import json
import os


def get_info(FileName):
    # Opening JSON file
    f = open(FileName)

    # returns JSON object as
    # a dictionary
    setup_info = json.load(f)

    # Closing file
    f.close()

    return setup_info


