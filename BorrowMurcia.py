import os
import shutil
def remove_files(Folder_path):
    for file_object in os.listdir(Folder_path):
        Files = os.path.join(Folder_path, file_object)
        if os.path.isfile(Files):
         os.unlink(Files)
        else:
            shutil.rmtree(Files)


remove_files(input("Write the path of your : ")) # example of path c:/Users/fitir/Desktop/prueba paython1



