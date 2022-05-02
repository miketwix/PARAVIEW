import openpyxl
from openpyxl.styles import Font, Alignment
from openpyxl.drawing.image import Image
import time
import os
import PRUEBA as PRUEBA
from Auxiliar_Functions import info as info
from datetime import *

today= datetime.today()
setup_info = info.get_info("amd.json")
#------------------------------JSON----------------------------
#--------------------------------------------------------------
#    b=Exel libro1     SIM_Data=Excel Sheet with simulations    SET_Data=Excel Sheet with sets of simulations      Tener Excel llamdo Libro1 en AMD
b = openpyxl.load_workbook("C:\\Users\\danie\\Documents\\Downloads\\Libro1.xlsx")
SET_Data = b.worksheets[1]
SIM_Data = b.worksheets[0]
BASELINE = b.worksheets[2]

#---------------------SET UP--------------------------------------------------
menu_num_assembly = 15
while (menu_num_assembly>=7):
  menu_assembly = "ASSEMBLY:\n    [0] COMPLETE CAR    [1] FW    [2] RW    [3] Difusser    [4] Side Channel    [5] Sidepod    [6] Engine Cover   ------>   "
  menu_num_assembly = input(menu_assembly)
  menu_num_assembly = int(menu_num_assembly)
  if(menu_num_assembly==0):
        assembly = "Complete CAR"
        part = "Complete CAR"
  if (menu_num_assembly==1):
        print("\nPART:")
        menu_FW = "[0] MainWing    [1] SecondaryFlap    [2] TertiaryFlap    [3] OuterEndplate    [4] InnerEndplate    [5] DuplexFlap ------>   "
        menu_num_FW = input(menu_FW)
        menu_num_FW = int(menu_num_FW)
        num_assembly = "310"
        assembly = "FW"
        if(menu_num_FW==0):
            part = "Main Wing"
            num_part = "01"
        if(menu_num_FW==1):
            part = "Secondary Flap"
            num_part = "02"
        if (menu_num_FW == 2):
            part = "Tertiary Flap"
            num_part = "03"
        if (menu_num_FW == 3):
            part = "Outer Endplate"
            num_part = "06"
        if (menu_num_FW == 4):
            num_part = "Inner Endplate"
            num_part = "07"
        if (menu_num_FW == 5):
            num_part = "Duplex Flap"
  if (menu_num_assembly==2):
      print("\nPART:")
      menu_RW = "[0] MainWing    [1] SecondaryFlap    [2] TertiaryFlap    [3] OuterEndplate    [4] InnerEndplate    [5] DuplexFlap ------>   "
      menu_num_RW = input(menu_RW)
      menu_num_RW = int(menu_num_RW)
      num_assembly = "311"
      assembly = "RW"
      if (menu_num_RW == 0):
          part = "Main Wing"
          num_part = "01"
      if (menu_num_RW == 1):
          part = "Secondary Flap"
          num_part = "02"
      if (menu_num_RW == 2):
          part = "Tertiary Flap"
          num_part = "03"
      if (menu_num_RW == 3):
          part = "Endplate"
          num_part = "07"
      if (menu_num_RW == 4):
          part = "Support Endplate"
          num_part = "09"
      if (menu_num_RW == 5):
          part = "Duplex Flap"
          num_part = "04"
  if (menu_num_assembly==3):
      assembly = "Difusser"
      part = "Difusser"
      num_assembly = "312"
      num_part = "01"
  if (menu_num_assembly==4):
      assembly = "Side Channel"
      part = "Side Channel"
      num_part = "01"
      num_assembly = "313"
  if (menu_num_assembly==5):
      assembly = "Sidepod"
      part = "Sidepod"
      num_part = "01"
      num_assembly = "315"
  if (menu_num_assembly==6):
      assembly = "Engine Cover"
      part = "Engine Cover"
      num_assembly = "318"
      num_part = "01"
  if(menu_num_assembly>6):
      print("Vueleve a introducir un numero")
#-------------------------BASELINE----------------------------------------------------------------
baseline_confirm="y"
while(baseline_confirm!="Y" and baseline_confirm!="N" and baseline_confirm!="baseline"):
      week = int(today.strftime("%U"))
      baseline_confirm = input("\nUsaste baseline semanal [Y] O [N]: ")
      if (baseline_confirm == "Y"):
         baseline = week
      if (baseline_confirm == "N"):
        baseline = 100000
        while(0>baseline or baseline>1000):
         baseline = input("\nIntroduzca baseline utilizada: ")
         baseline = int(baseline)


#----------SACAR DATOS SIMULACION---------------------------------------------------------
num_sim = 0
sim_file = os.listdir("C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles")
if(baseline_confirm=="Y" or baseline_confirm=="N"):
 for x in range(len(sim_file)):
  ruta = ("C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles" + "\\" + sim_file[x])
  SIM_Data.insert_rows(4)
  SIM_Data['B4'] = datetime.today().strftime('%d-%m-%Y')
  SIM_Data['D4'] = setup_info["owner"]
  SIM_Data['N4'] = setup_info["FVel"]
  SIM_Data['O4'] = setup_info["Yaw"]
  SIM_Data['P4'] = setup_info["Roll"]
  SIM_Data['Q4'] = setup_info["Pitch"]
  SIM_Data['R4'] = setup_info["Steering"]
  SIM_Data['E4'] = setup_info["parameter"] + " - " + "x"

  num_sim = x+1
  num_sim_str = str(num_sim)
  SIM_Data['F4'] = assembly
  SIM_Data['G4'] = part
  SIM_Data['C4'] = sim_file[x]
  week = today.strftime("%U")
  week = int(today.strftime("%U"))

  if(int(today.strftime("%U"))<=9):
      ID = setup_info["project"]+ "-" + str(num_assembly) + str(num_part) + setup_info["num_geometry"] + setup_info["parameter"] + "W0" + str(week) + "-" + str(baseline) + "-" + str(num_sim_str)
      ID_set = setup_info["project"]+ "-" + str(num_assembly) + str(num_part) + setup_info["num_geometry"] + setup_info["parameter"] + "W0" + str(week)
  if(int(today.strftime("%U"))>=10):
      ID = setup_info["project"] + "-" + str(num_assembly) + str(num_part) + setup_info["num_geometry"] + setup_info["parameter"] + "W" + str(week) + "-" + str(baseline) + "-" + str(num_sim_str)
      ID_set = setup_info["project"]+ "-" + str(num_assembly) + str(num_part) + setup_info["num_geometry"] + setup_info["parameter"] + "W" + str(week)

  SIM_Data['H4'] = "C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles\\" + sim_file[x-1+1]
  SIM_Data['A4'] = ID

  #----------CSV----------------------------------------------------------------------------------
  SIM_Data['M4'] = baseline
  if(os.path.exists(ruta + "\\Car.csv")==True):
      result_drag_car = PRUEBA.csv_reader(ruta + "\\Car.csv", 7)
      result_downforce_car = PRUEBA.csv_reader(ruta + '\\Car.csv', 9)
      SIM_Data['I4'] = -result_downforce_car
      SIM_Data['J4'] = result_drag_car
      SIM_Data['K4'] = (-result_downforce_car/result_drag_car)
      if(num_sim_str == "1"):
          result_downforce_car_total = -result_downforce_car
          result_drag_car_total = result_drag_car
          efficency = (-result_downforce_car / result_drag_car)
          num_sim_str_max = num_sim_str
      if(result_downforce_car_total < -result_downforce_car):
          result_downforce_car_total = -result_downforce_car
      if (result_drag_car >= result_drag_car_total):
          result_drag_car_total = result_drag_car
      if (efficency<=(-result_downforce_car / result_drag_car)):
          efficency = (-result_downforce_car / result_drag_car)
      if (setup_info["base_downforce"] < (-result_downforce_car)):
          SIM_Data['I4'].font = Font(color='008000')
      else:
          SIM_Data['I4'].font = Font(color='FF0000')

      if (setup_info["base_drag"] < (result_drag_car)):
          SIM_Data['J4'].font = Font(color='008000')
      else:
          SIM_Data['J4'].font = Font(color='FF0000')

      if((setup_info["base_downforce"]/setup_info["base_drag"])<(-result_downforce_car/result_drag_car)):
          SIM_Data['K4'].font = Font(color = '008000')
      else:
          SIM_Data['K4'].font = Font(color='FF0000')


  if(os.path.exists(ruta + "\\FW.csv")==True):
      result_drag_FW = PRUEBA.csv_reader(ruta + '\\FW.csv', 7)
      result_downforce_FW = PRUEBA.csv_reader(ruta + '\\FW.csv', 9)
      SIM_Data['S4'] = -result_downforce_FW
      SIM_Data['T4'] = result_drag_FW
      SIM_Data['U4'] = (-result_downforce_FW / result_drag_FW)
  if(os.path.exists(ruta + "\\RW.csv")==True):
      result_drag_RW = PRUEBA.csv_reader(ruta + '\\RW.csv', 7)
      result_downforce_RW = PRUEBA.csv_reader(ruta + '\\RW.csv', 9)
      SIM_Data['V4'] = -result_downforce_RW
      SIM_Data['W4'] = result_drag_RW
      SIM_Data['X4'] = (-result_downforce_RW / result_drag_RW)
  if(os.path.exists(ruta + "\\Undertray.csv")==True):
      result_drag_dif = PRUEBA.csv_reader(ruta + '\\Undertray.csv', 7)
      result_downforce_dif = PRUEBA.csv_reader(ruta + '\\Undertray.csv', 9)
      SIM_Data['Y4'] = -result_downforce_dif
      SIM_Data['Z4'] = result_drag_dif
      SIM_Data['AA4'] = (-result_downforce_dif / result_drag_dif)
  if(os.path.exists(ruta + "\\LateralVenturi.csv")==True):
      result_drag_latvent = PRUEBA.csv_reader(ruta + '\\LateralVenturi.csv', 7)
      result_downforce_latvent = PRUEBA.csv_reader(ruta + '\\LateralVenturi.csv', 9)
      SIM_Data['AB4'] = -result_downforce_latvent
      SIM_Data['AC4'] = result_drag_latvent
      SIM_Data['AD4'] = (-result_downforce_latvent / result_drag_latvent)
  if(os.path.exists(ruta + "\\Bodywork.csv")==True):
      result_drag_body = PRUEBA.csv_reader(ruta + '\\Bodywork.csv', 7)
      result_downforce_body = PRUEBA.csv_reader(ruta + '\\Bodywork.csv', 9)
      SIM_Data['AE4'] = -result_downforce_body
      SIM_Data['AF4'] = result_drag_body
      SIM_Data['AG4'] = (-result_downforce_body / result_drag_body)
  if(os.path.exists(ruta + "\\frontTyres.csv")==True):
      result_drag_ftyres = PRUEBA.csv_reader(ruta + '\\frontTyres.csv', 7)
      result_downforce_ftyres = PRUEBA.csv_reader(ruta + '\\frontTyres.csv', 9)
      SIM_Data['AK4'] = -result_downforce_ftyres
      SIM_Data['AL4'] = result_drag_ftyres
      SIM_Data['AM4'] = (-result_downforce_ftyres / result_drag_ftyres)
  if(os.path.exists(ruta + "\\rearTyres.csv")==True):
      result_drag_rtyres = PRUEBA.csv_reader(ruta + '\\rearTyres.csv', 7)
      result_downforce_rtyres = PRUEBA.csv_reader(ruta + '\\rearTyres.csv', 9)
      SIM_Data['AN4'] = -result_downforce_rtyres
      SIM_Data['AO4'] = result_drag_rtyres
      SIM_Data['AP4'] = (-result_downforce_rtyres / result_drag_rtyres)
  if(os.path.exists(ruta + "\\Sidepod.csv")==True):
      result_drag_sidepod = PRUEBA.csv_reader(ruta + '\\Sidepod.csv', 7)
      result_downforce_sidepod = PRUEBA.csv_reader(ruta + '\\Sidepod.csv', 9)
      SIM_Data['AH4'] = -result_downforce_sidepod
      SIM_Data['AI4'] = result_drag_sidepod
      SIM_Data['AJ4'] = (-result_downforce_sidepod / result_drag_sidepod)
#------------------set data--------------------------------------------------------------
 SET_Data.insert_rows(2)
 SET_Data["B2"] = datetime.today().strftime('%d-%m-%Y')
 SET_Data["A2"] = ID_set
 SET_Data["D2"] = setup_info["owner"]
 SET_Data["E2"] = setup_info["parameter"]
 SET_Data["F2"] = assembly
 SET_Data["G2"] = part
 SET_Data["H2"] = setup_info["num_geometry"]
 SET_Data["I2"] = baseline
 SET_Data["J2"] = str(num_sim_str) + "   (" + str(num_sim_str_max) + ")"
 SET_Data["K2"] = str(num_sim_str_max)
 SET_Data["K2"] = result_downforce_car_total
 if((setup_info["base_downforce"])<(result_downforce_car_total)):
          SET_Data['K2'].font = Font(color = '008000')
 else:
          SET_Data['K2'].font = Font(color='FF0000')
 SET_Data["L2"] = result_drag_car_total
 if((setup_info["base_drag"])<(result_drag_car_total)):
          SET_Data['L2'].font = Font(color = '008000')
 else:
          SET_Data['L2'].font = Font(color='FF0000')
 SET_Data["M2"] = efficency
 if((setup_info["base_downforce"]/setup_info["base_drag"])<(efficency)):
          SET_Data['M2'].font = Font(color = '008000')
 else:
          SET_Data['M2'].font = Font(color='FF0000')
 set_name = input("\nSET NAME: ")
 SET_Data["C2"] = set_name

if(baseline_confirm == "baseline"):
    BASELINE.insert_rows(3)
    BASELINE['B3'] = week
    BASELINE['A3'] = "W" + str(week)
    ruta = ("C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles" + "\\" + sim_file[0])
    imag = Image('C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles\\bsxasiocniosc\\STL.png')
    BASELINE['B3'] = "."
    imag.width, imag.height = (224,153)
    BASELINE.add_image(imag, 'B3')

    if (os.path.exists(ruta + "\\car.csv") == True):
        result_drag_car = PRUEBA.csv_reader(ruta + '\\car.csv', 7)
        result_downforce_car = PRUEBA.csv_reader(ruta + '\\car.csv', 9)
        BASELINE['Q3'] = str(-result_downforce_car)
        BASELINE['R3'] = str(result_drag_car)
        BASELINE['S3'] = str((-result_downforce_car / result_drag_car))

    if (os.path.exists(ruta + "\\FW.csv") == True):
        result_drag_FW = PRUEBA.csv_reader(ruta + '\\FW.csv', 7)
        result_downforce_FW = PRUEBA.csv_reader(ruta + '\\FW.csv', 9)
        BASELINE['T3'] = str(-result_downforce_FW)
        BASELINE['U3'] = str(result_drag_FW)
        BASELINE['V3'] = str((-result_downforce_FW / result_drag_FW))

    if (os.path.exists(ruta + "\\RW.csv") == True):
        result_drag_RW = PRUEBA.csv_reader(ruta + '\\RW.csv', 7)
        result_downforce_RW = PRUEBA.csv_reader(ruta + '\\RW.csv', 9)
        BASELINE['W3'] = str(-result_downforce_RW)
        BASELINE['X3'] = str(result_drag_RW)
        BASELINE['Y3'] = str((-result_downforce_RW / result_drag_RW))

    if (os.path.exists(ruta + "\\Undertray.csv") == True):
        result_drag_dif = PRUEBA.csv_reader(ruta + '\\Undertray.csv', 7)
        result_downforce_dif = PRUEBA.csv_reader(ruta + '\\Undertray.csv', 9)
        BASELINE['Z3'] = str(-result_downforce_dif)
        BASELINE['AA3'] = str(result_drag_dif)
        BASELINE['AB3'] = str((-result_downforce_dif / result_drag_dif))

    if (os.path.exists(ruta + "\\LateralVenturi.csv") == True):
        result_drag_latvent = PRUEBA.csv_reader(ruta + '\\LateralVenturi.csv', 7)
        result_downforce_latvent = PRUEBA.csv_reader(ruta + '\\LateralVenturi.csv', 9)
        BASELINE['AC3'] = str(-result_downforce_latvent)
        BASELINE['AD3'] = str(result_drag_latvent)
        BASELINE['AE3'] = str((-result_downforce_latvent / result_drag_latvent))

    if (os.path.exists(ruta + "\\Bodywork.csv") == True):
        result_drag_body = PRUEBA.csv_reader(ruta + '\\Bodywork.csv', 7)
        result_downforce_body = PRUEBA.csv_reader(ruta + '\\Bodywork.csv', 9)
        BASELINE['AI3'] = str(-result_downforce_body)
        BASELINE['AJ3'] = str(result_drag_body)
        BASELINE['AK3'] = str((-result_downforce_body / result_drag_body))

    if (os.path.exists(ruta + "\\frontTyres.csv") == True):
        result_drag_ftyres = PRUEBA.csv_reader(ruta + '\\frontTyres.csv', 7)
        result_downforce_ftyres = PRUEBA.csv_reader(ruta + '\\frontTyres.csv', 9)
        BASELINE['AL3'] = str(-result_downforce_ftyres)
        BASELINE['AM3'] = str(result_drag_ftyres)
        BASELINE['AN3'] = str((-result_downforce_ftyres / result_drag_ftyres))

    if (os.path.exists(ruta + "\\rearTyres.csv") == True):
        result_drag_rtyres = PRUEBA.csv_reader(ruta + '\\rearTyres.csv', 7)
        result_downforce_rtyres = PRUEBA.csv_reader(ruta + '\\rearTyres.csv', 9)
        BASELINE['AO3'] = str(-result_downforce_rtyres)
        BASELINE['AP3'] = str(result_drag_rtyres)
        BASELINE['AQ3'] = str((-result_downforce_rtyres / result_drag_rtyres))

    if (os.path.exists(ruta + "\\Sidepod.csv") == True):
        result_drag_sidepod = PRUEBA.csv_reader(ruta + '\\Sidepod.csv', 7)
        result_downforce_sidepod = PRUEBA.csv_reader(ruta + '\\Sidepod.csv', 9)
        BASELINE['AF3'] = str(-result_downforce_sidepod)
        BASELINE['AG3'] = str(result_drag_sidepod)
        BASELINE['AH3'] = str((-result_downforce_sidepod / result_drag_sidepod))

b.save("C:\\Users\\danie\\Documents\\Downloads\\Libro1.xlsx")


















