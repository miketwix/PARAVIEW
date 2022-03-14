import os
import shutil
import glob

def remove_files(folder_path):
    for file_object in os.listdir(folder_path):
        Files = os.path.join(folder_path, file_object)
        if os.path.isfile(Files):
         os.unlink(Files)
        else:
            shutil.rmtree(Files)


def folder_names(ruta):
    contenido = os.listdir(ruta)
    return contenido

def find_folders(ruta):
    sim_list = folder_names(ruta)
    lista = list()                               #lista: lista para los nombres de la carpeta CaseFiles
    casefiles = list()
    casefiles1 = list()                          #casefiles: lista para los nombres de los arcchivos de cada simulacion
    casefoam_list = list()
    casefoam_files = list()  #casefoam_list: lista para las simulaciones que contienen un archivo casefoam
    s = 0
    for i in range(len(sim_list)):
        dir = ruta + '\\' + sim_list[i]
        lista.append(dir)
        casefiles1 = folder_names(ruta + "\\" + sim_list[i])
        casefiles.append(casefiles1)
        if os.path.isfile(lista[i] + "\\case.foam"):
            casefoam_list.append(lista[i])              # return casefoam_list
            casefoam_files.append(sim_list[i])
    return casefoam_list


def find_files(targetPattern):
    targetExtension1 = "*case.foam"
    targetExtension2 = "*.stl"
    files = list()
    files = glob.glob(targetPattern+targetExtension1)
    files += glob.glob(targetPattern+"/**"+targetExtension1)
    files+= glob.glob(targetPattern + targetExtension2)
    files += glob.glob(targetPattern + "/**" + targetExtension2)
    return files
