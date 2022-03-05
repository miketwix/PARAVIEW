import os
import shutil


def remove_files(folder_path):
    for file_object in os.listdir(folder_path):
        Files = os.path.join(folder_path, file_object)
        if os.path.isfile(Files):
         os.unlink(Files)
        else:
            shutil.rmtree(Files)


remove_files(input("Write the path of your : ")) # example of path c:/Users/fitir/Desktop/prueba paython1
#hola*