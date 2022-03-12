import os
ruta = 'C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles'
def folder_names(ruta):
    contenido = os.listdir(ruta)
    return contenido
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
print(casefoam_files)