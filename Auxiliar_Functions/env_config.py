import os
import shutil
import glob
from pathlib import Path
import csv

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
    lista = list()  # lista: lista para los nombres de la carpeta CaseFiles
    casefiles = list()
    casefiles1 = list()  # casefiles: lista para los nombres de los arcchivos de cada simulacion
    casefoam_list = list()
    casefoam_files = list()  # casefoam_list: lista para las simulaciones que contienen un archivo casefoam
    list_directorio = list()  # list_directorio: lista para todos los archivos dentro de la simulacion (excel,stl,foam)
    for i in range(len(sim_list)):
        dir = ruta + '\\' + sim_list[i]
        lista.append(dir)
        casefiles1 = folder_names(ruta + "\\" + sim_list[i])
        casefiles.append(casefiles1)
        s = 1
        if os.path.isfile(lista[i] + "\\case.foam"):
            directorio = os.listdir(lista[i])
            list_directorio.append(directorio)
            for r in range(len(directorio)):
                if directorio[r].endswith(
                        "stl"):  # a veces guarda el stl como .STL y otras como .stl, por ello hay 2 if
                    s = s + 1
                    if s == 2:
                        casefoam_list.append(lista[i])
                        casefoam_files.append(sim_list[i])
                if directorio[r].endswith("STL"):
                    s = s + 1
                    if s == 2:
                        casefoam_list.append(lista[i])
                        casefoam_files.append(sim_list[i])
    return casefoam_list

def find_files(targetPattern):
    targetExtension1 = "*case.foam"
    targetExtension2 = "*CAR.stl"
    targetExtension3 = "*PART.stl"
    files = list()
    files = glob.glob(targetPattern+targetExtension1)
    files += glob.glob(targetPattern+"/**"+targetExtension1)
    files += glob.glob(targetPattern + targetExtension2)
    files += glob.glob(targetPattern + "/**" + targetExtension2)
    files += glob.glob(targetPattern + targetExtension3)
    files += glob.glob(targetPattern + "/**" + targetExtension3)
    return files

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def simname_creator(output_path,sim_name):
  path = Path(output_path+'\\'+sim_name)
  path.mkdir(parents=True)

  subfolders = ['CAR_STL', 'PART_STL', 'Cp', 'y+', 'WSS', 'Cpx', 'Cpz', 'P', 'U', 'Pt', 'Pre_CAR', 'CLA', 'CDA', 'Mesh', 'GIF_Preassure_Contour', 'GIF_Velocity_Contour']
  for subfolder in subfolders:
      subfolder_path = path / subfolder
      subfolder_path.mkdir(parents=True)

  return str(path)

def csv_reader(ruta,l):
  with open(ruta) as File:
        reader = csv.reader(File)
        result = 0
        lista = list()
        for row in reader:
             lista.append(row)
        for x in range(75, 101):
             result = result + float(lista[x][l])
  result = result / 25
  return result

