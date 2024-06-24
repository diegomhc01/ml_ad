import pandas as pd      # manejo de estructuras series y dataframes
import numpy as np       # manejo de vectores y matrices

#Leer archivo con los datos limpios
datos = pd.read_csv('shark_filtrado.csv', encoding='latin-1')

#Ver los primeros resultados
#print(datos.head(15))

#Ver cuantos registros con valores unicos existen
#datos = datos.nunique()
#print(datos)


#agrupado_conteo = datos.groupby('fatal')['fatal'].count()
#print(agrupado_conteo.describe())
#Ver cuales son los valores duplicados
#datos = datos['Fatal (Y/N)'].drop_duplicates().reset_index(drop=True)
#print(datos)

#Guardo los valores que se encuetren duplicados
#datos10.to_csv('listado_areas.csv',columns=['Area'])

#Ver cuantos registros nulos existe
#datos.isnull().sum()
#print(datos)

#Conocer las columnas
#print(datos.columns)

#Para mostrar promedio, desviación estándar, cuartiles
#datos = datos.describe()
#print(datos)
#Agrupar los datos por Area
#countries = datos.groupby('Area')
#Cantidad por area
#cantidad = countries.count()
#print(cantidad)
#Determinar valores unicos por un campo específico
#unicos = datos['Injury'].unique()
#print(unicos)
#Cantidad de valores unicos por un campo específico
#unicos = datos['Injury'].nunique()
#print(unicos)


#Con estas consultas rápidas puedes conocer qué información contiene el DataFrame y cómo está organizada.
#datos.duplicated().sum()                      #Duplicados del DataFrame
#datos = datos['Fatal (Y/N)'].duplicated().sum()        #Duplicados de la serie
#print(datos)
#duplicates = datos[datos['Fatal (Y/N)'].duplicated(keep=False)]['Fatal (Y/N)'].tolist()
#duplicates = datos[datos['Case Number'].duplicated(keep=False)]['Case Number'].tolist()

#duplicates es una lista no un DataFrame
#print(duplicates)
#for country in duplicates:
#    print(country)


#set_duplicates = set(duplicates)
#for r in set_duplicates:
#    dup = datos[datos['Type'] == r]
#    datos.loc[dup.iloc[1,:].name, 'Type'] = datos.loc[dup.iloc[1,:].name]['Type']

#print(datos)
# Comprobación de que no hay registros duplicados
#print(datos.duplicated().sum())
# Devuelve 0 

#Localizar valores nulos. Eliminar o sustituir
#print(datos.isnull().sum())

#print(datos['Injury'].value_counts())
#print(datos[(datos['Area'].isnull())]['Injury'].value_counts())
#countries = datos.loc[(datos['Country'] == 'ARGENTINA') & (datos['Country'] != 'NaN'), 'Country']