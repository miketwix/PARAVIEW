import openpyxl
import openpyxl.styles
import time
import os
import csv
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
