#https://matplotlib.org/stable/gallery/index.html

import pandas as pd
import matplotlib.pyplot as plt

#datos = pd.read_csv('GSAF5.csv', encoding='latin-1') 
i = 0
names = []
values = []
datos = pd.read_csv('shark_filtrado.csv', encoding='latin-1')

agrupado_conteo = datos.groupby('Area')['Fatal (Y/N)'].count()

for label, content in agrupado_conteo.items():
    names.append(label)
    values.append(content)    


fig, axs = plt.subplots(1, 3, layout='constrained', sharex=True, sharey=True)

axs[0].bar(names, values, color=['tab:red', 'tab:blue', 'tab:orange'])
axs[1].scatter(names, values)
axs[2].plot(names, values)
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

