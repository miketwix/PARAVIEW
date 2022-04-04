import openpyxl
import openpyxl.styles
import time
import os
#------------------------------JSON----------------------------
FVel = 15
Yaw=0
Steering=0
Roll=0
Pitch=0
owner="alguien"
#--------------------------------------------------------------
#    b=Exel libro1     SIM_Data=Excel Sheet with simulations    SET_Data=Excel Sheet with sets of simulations      Tener Excel llamdo Libro1 en AMD
b = openpyxl.load_workbook("C:\\Users\\danie\\Documents\\Downloads\\Libro1.xlsx")
SIM_Data = b.active
#---------------------SET UP--------------------------------------------------
SIM_Data.insert_rows(4)
SIM_Data['B4'] = time.strftime('%x')
SIM_Data['D4'] = owner
SIM_Data['M4'] = FVel
SIM_Data['N4'] = Yaw
SIM_Data['O4'] = Roll
SIM_Data['P4'] = Pitch
SIM_Data['Q4'] = Steering
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
        assembly = "FW"
        if(menu_num_FW==0):
            part = "Main Wing"
        if(menu_num_FW==1):
            part = "Secondary Flap"
        if (menu_num_FW == 2):
            part = "Tertiary Flap"
        if (menu_num_FW == 3):
            part = "Outer Endplate"
        if (menu_num_FW == 4):
            part = "Inner Endplate"
        if (menu_num_FW == 5):
            part = "Duplex Flap"
  if (menu_num_assembly==2):
      print("\nPART:")
      menu_RW = "[0] MainWing    [1] SecondaryFlap    [2] TertiaryFlap    [3] OuterEndplate    [4] InnerEndplate    [5] DuplexFlap ------>   "
      menu_num_RW = input(menu_RW)
      menu_num_RW = int(menu_num_RW)
      assembly = "RW"
      if (menu_num_RW == 0):
          part = "Main Wing"
      if (menu_num_RW == 1):
          part = "Secondary Flap"
      if (menu_num_RW == 2):
          part = "Tertiary Flap"
      if (menu_num_RW == 3):
          part = "Outer Endplate"
      if (menu_num_RW == 4):
          part = "Inner Endplate"
      if (menu_num_RW == 5):
          part = "Duplex Flap"
  if (menu_num_assembly==3):
      assembly = "Difusser"
      part = "Difusser"
  if (menu_num_assembly==4):
      assembly = "Side Channel"
      part = "Side Channel"
  if (menu_num_assembly==5):
      assembly = "Sidepod"
      part = "Sidepod"
  if (menu_num_assembly==6):
      assembly = "Engine Cover"
      part = "Engine Cover"
  if(menu_num_assembly>6):
      print("Vueleve a introducir un numero")








#----------SACAR DATOS SIMULACION---------------------------------------------------------

sim_file = os.listdir("C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles")
ruta = "C:\\Users\\danie\\Desktop\\Paraview_Batch_Postproc\\CaseFiles" + "\\" + sim_file[0]

set_name = input("\nSIMULATION NAME: ")

SIM_Data['F4'] = assembly
SIM_Data['G4'] = part
SIM_Data['C4'] = set_name

b.save("C:\\Users\\danie\\Documents\\Downloads\\Libro1.xlsx")







