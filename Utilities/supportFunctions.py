import pathlib
import glob
import os

def create_output_folder(out_path,name):
    path = str(out_path) + "/" + name
    try:
        os.makedirs(path)
        #path.append(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % name)

    return path


def simlist(input_path):
    # function searches all sim files in inp folder
    print("Searching for case.foam files...")
    list_cases = glob.glob(str(input_path) + "/**/case.foam", recursive=True)

    if list_cases:
        print(str(len(list_cases)) + " cases found.")
    else:
        raise Exception("NO CASE.FOAM FILES FOUND.")

    return list_cases


def select_sim(info):
    # TODO Explain this section
    simInFolder = simlist(info["FolderInfo"]["inFolder"])
    counterID = 0
    valid_sel = 0
    for simulation in simInFolder:
        print("Simulation with ID " + str(counterID) + ": " + simulation)
        counterID = counterID + 1
    while valid_sel == 0:
        selected_sim_ID = int(input('Please select the desired simulation by introducing the ID: '))
        if selected_sim_ID not in range (0,counterID):
            print('please select a valid ID')
        else:
            valid_sel = 1

    # TODO Create folder,with name and dictionary with information
    selected_sim = simInFolder[selected_sim_ID]
    return selected_sim
