# Autor: Campuzano Rangel Jesús Efrén
# Grupo: TIDS4-2
# Fecha: 25/10/2024
'''
Elaborar un programa que pida 9 números enteros y los vaya introduciendo en una matriz de 3x3. 

'''
from MisFunciones_2024 import *
import numpy as np




# ------------- Codigo Principal -------------
while True:
    CLS()
    
    matriz = np.empty((3,3), dtype=int)
    
    for i in range(3):
        for j in range(3):
            matriz[i,j] = leer_int(f"Ingrese el numero ({i},{j}): ")
            
    #matriz[:, 0] selecciona toda la primera columna
    #matriz[0, :] selecciona toda la primera fila
    print(f"{matriz[0,0]:>3} {matriz[0,1]:>3} {matriz[0,2]:>3} | {np.sum(matriz[0,:]):>3}")
    print(f"{matriz[1,0]:>3} {matriz[1,1]:>3} {matriz[1,2]:>3} | {np.sum(matriz[1,:]):>3}")
    print(f"{matriz[2,0]:>3} {matriz[2,1]:>3} {matriz[2,2]:>3} | {np.sum(matriz[2,:]):>3}")
    print("-"*12)
    print(f"{np.sum(matriz[:,0]):>3} {np.sum(matriz[:,1]):>3} {np.sum(matriz[:,2]):>3}")
    
    if(str(input("\n¿Desea repetir el programa? ('Si' para confirmar): ").upper()[0]) != "S"): break