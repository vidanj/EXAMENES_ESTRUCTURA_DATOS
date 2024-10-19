# Autor: Campuzano Rangel Jesús Efrén
# Grupo: TIDS4-2
# Fecha: 19/10/2024
'''
Un programa al que se le introduzca un párrafo completo (mínimo 20 palabras), y meta las palabras en una lista sin símbolos ortográficos. 
Después hay que imprimir la lista con cada una de las palabras que ingresó en orden alfabético, y cuántas veces está repetida. 

'''
from MisFunciones_2024 import *
import re #Módulo que permite trabajar con expresiones regulares (regex). 

CLS()

while True:
    while True:
        
        textoIngresado = input("Ingrese un texto breve: \n")
        textoDepurado = re.sub(r'[^\w\s]', ' ', textoIngresado) # Eliminar signos especiales usando el regex
        textoDepurado = re.sub(r'[\d_]', ' ', textoDepurado) # Elimina los números y el guion bajo
        
        listaPalabras = textoDepurado.split()
        if listaPalabras.__len__() <20:
            beep_error()
            pausa("Error! Texto demasiado corto. Intente de nuevo.\n\n")
        else:
            break
        
    # print(listaPalabras)

    listaPalabras.sort(key=str.lower)

    print(f"\nPalabras" + (" ")*13 + "→ #")
    print("=" * 24)
    
    dicc = {}
    for e in listaPalabras:
        
        if not e in dicc:
            dicc[e] = listaPalabras.count(e)  # Metemos al elemento en el diccionario
            
    for key in dicc:    # Accediendo a los elementos de un diccionario
        print(f"{key:<20} → {dicc[key]}  ")
        
                
    
    if(str(input("\n¿Desea repetir el programa? ('Si' para confirmar): ").upper()[0]) != "S"): break
    
