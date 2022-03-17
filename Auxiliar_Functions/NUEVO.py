sim_list = folder_names(ruta)
lista = list()  # lista: lista para los nombres de la carpeta CaseFiles
casefiles = list()
casefiles1 = list()  # casefiles: lista para los nombres de los arcchivos de cada simulacion
casefoam_list = list()
casefoam_files = list()  # casefoam_list: lista para las simulaciones que contienen un archivo casefoam
list_directorio = list()  #list_directorio: lista para todos los archivos dentro de la simulacion (excel,stl,foam)
for i in range(len(sim_list)):
    dir = ruta + '\\' + sim_list[i]
    lista.append(dir)
    casefiles1 = folder_names(ruta + "\\" + sim_list[i])
    casefiles.append(casefiles1)
    s = 0
    if os.path.isfile(lista[i] + "\\case.foam"):
           directorio = os.listdir(lista[i])
           list_directorio.append(directorio)
           for r in range(len(directorio)):
            if directorio[r].endswith("stl"):    #a veces guarda el stl como .STL y otras como .stl, por ello hay 2 if
               s = s + 1
               if s==2:
                  casefoam_list.append(lista[i])
                  casefoam_files.append(sim_list[i])
            if directorio[r].endswith("STL"):
                s = s + 1
                if s == 2:
                    casefoam_list.append(lista[i])
                    casefoam_files.append(sim_list[i])