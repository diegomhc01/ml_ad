#Hipótesis: 
#“El mayor número de muertes por ataques por parte de tiburones 
#a surfistas que se produjeron en la costa oeste de Estados Unidos.” 
#Esto delimita la información a buscar en el dataset.

import pandas as pd      # manejo de estructuras series y dataframes
import numpy as np       # manejo de vectores y matrices
import matplotlib.pyplot as plt # manejo de gráficos

from collections import Counter
import re #para las expresiones regulares

#Leo los datos desde un archivo .csv
datos = pd.read_csv('GSAF5.csv', encoding='latin-1')
#Imprimo los nombres de columnas para ver cuales selecciono
print(datos.columns)
#Selecciono del archivo anterior, solo los campos que me interesan
datos = datos[["Year", "Country", "Area", "Activity","Injury","Fatal (Y/N)"]]
#print(datos)
#Guardo los datos con las columnas seleccionadas en un archivo nuevo
#para analizar desde este archivo
#datos.to_csv('shark_c.cvs')
datos = pd.read_csv('shark_c.cvs', encoding='latin-1')
#Filtro el campo año con valor igual a 0, si existen, para descartarlos
datos.drop(datos[(datos['Year'] == 0)].index, inplace=False)
#Imprimo los datos para ver si existen registros con año igual a 0
for dato in datos:
    pass


#Filtro los datos con el año mayor a 1900 para achicar el número de registros
#y trabajar con esos datos
#datos1 = datos.drop(datos[(datos['Year'] < 1900)].index, inplace=False)
#Lo guardo en un archivo para seguir trabajando con el mismo
#datos1.to_csv('anios_1900.csv')
#Leo el archivo generado anteriormente
#datos = pd.read_csv('anios_1900.cvs', encoding='latin-1')
#Filtro los registros que contengan el valor Surfing del campo Activity
#datos1 = datos1[datos1['Activity']=='Surfing']
#Filtro los registros que contengan el valor USA del campo Country
#LIKE '%USA%'
#= 'USA'
#datos1 = datos1[datos1['Country']=='USA']
#AREA IN (VALOR, VALOR2,VALOR3, ETC)
#datos1 = datos1[datos1['Area'].str.contains('California')]
# ~se utiliza para negar una condición
#datos1 = datos[~datos['Area'].isin(['California', 'Oregon', 'Washington', 'Hawaii'])]
#Filtro los registros que sean del Area del listado ('California', 'Oregon', 'Washington', 'Hawaii')
#datos1 = datos1[datos1['Area'].isin(('California', 'Oregon', 'Washington', 'Hawaii'))]
#Guardo los datos en un archivo nuevo con los registros que tienen:
#- Año mayor a 1900
#- Que la actividad sea Surfing
#. Que sean del país USA
#- Que sean del área ('California', 'Oregon', 'Washington', 'Hawaii')
#columnas = ["Year", "Country", "Area", "Activity","Injury","Fatal (Y/N)"]
#datos1.to_csv('shark_filtrado.csv' ,columns = columnas,index=False)


