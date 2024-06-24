import pandas as pd      # manejo de estructuras series y dataframes
import numpy as np       # manejo de vectores y matrices
import matplotlib.pyplot as plt # manejo de gráficos

from collections import Counter
import re #para las expresiones regulares

datos = pd.read_csv('shark_filtrado_agrupado.csv', encoding='latin-1')
"""
California, Oregon, Washington, Hawaii
"""
def calcular_frecuencia(texto):
    # Eliminar signos de puntuación y convertir todo a minúsculas

    texto_procesado = re.sub(r'[^\w\s]', '', texto.lower())

    # Dividir el texto en palabras
    palabras = texto_procesado.split()

    # Calcular la frecuencia de las palabras
    frecuencia = Counter(palabras)

    return frecuencia

texto = ''
for i in range(len(datos)):    
    texto = texto + str(datos.iloc[i]['Injury']) + ' \n'
    
frecuencia_palabras = calcular_frecuencia(texto)
lista_palabras = []
for palabra in frecuencia_palabras:
    if len(palabra) > 3:
        lista_palabras.append(palabra)

# Convertir el diccionario en un DataFrame de pandas
tabla_datos = pd.DataFrame(list(frecuencia_palabras.items()), columns=["Palabra", "Frecuencia"])
#tabla_datos = pd.DataFrame(lista_palabras, columns=["Palabra"])
# Exportar el DataFrame a un archivo csv
#tabla_datos.to_csv("datos4.csv", index=False)

# Mostrar la tabla de frecuencias
#print(tabla_datos)
label_palabra = []
values_palabra = []
for label, content in frecuencia_palabras.items():
    #if content > 2:        
        label_palabra.append(label)
        values_palabra.append(content)  

fig, axs = plt.subplots(1, 3, layout='constrained', sharex=True, sharey=True)

axs[0].bar(label_palabra, values_palabra, color=['tab:red', 'tab:blue', 'tab:orange'])
axs[1].scatter(label_palabra, values_palabra)
axs[2].plot(label_palabra, values_palabra)
for i in range(0,3):
    if i == 0:
        tipo = '(bar)'
    elif i == 1:
        tipo = '(scatter)'
    elif i == 2:
        tipo = '(plot)'
    axs[i].set_title(f'Fatality per Area {tipo}')
    axs[i].set_xlabel('Areas')
    axs[i].set_ylabel('Fatal (Y/N)')

plt.show()