import pandas as pd

pip install openpyxl

"Código para la obtención, transformación y análisis de datos"

"Año 2021"

"""En primer lugar, abrimos el archivo excel descargado de la página web del Instituto Nacional de Estadística 
https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176780&menu=ultiDatos&idp=1254735573175"""

mortalidad2021 = pd.read_excel("C:\\Users\\beama\\Desktop\\Repositorio_DataScience\\MORTALIDAD_ESPAÑA\\muertes2021.xlsx")

"""En segundo lugar, renombramos el título vacío de la columna donde aparecen recopiladas todas las enfermedades 
por la palabra 2021 para identificar el año objeto de estudio."""

mortalidad2021 = mortalidad2021.rename(columns= {" " : "2021"})

"""En tercer lugar, creamos un filtro en el que la condición del número de fallecidos por enfermedad sea diferente 
a cero para manipular los diferentes datos correctamente."""

mortalidad_condicion = mortalidad2021['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2021['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2021['De 30 a 34 años'] != 0

"""En cuarto lugar, aplicamos el filtro mencionado al dataset que vamos a utilizar para el análisis de los datos."""

mortalidad2021_20 = mortalidad2021[mortalidad_condicion]
mortalidad2021_20 = mortalidad2021[mortalidad_condicion2]
mortalidad2021_20 = mortalidad2021[mortalidad_condicion3]

"""En quinto lugar, añadimos una columna en la que aparezca la suma del total de fallecidos por tipo de enfermedad."""

mortalidad2021_20['Total'] = mortalidad2021_20.sum(axis=1)
mortalidad2021_20

"""En sexto lugar, obtenemos el total de fallecidos por año y divididimos el número de fallecidos por tipo de enfermedad 
entre el total, para conocer la representatividad de cada causa sobre el total de defunciones."""

total2021 = mortalidad2021_20['Total'].sum()

mortalidad2021_20['Porcentaje'] = (mortalidad2021_20['Total']/total2021)*100
mortalidad2021_20

"""En séptimo lugar, ordenamos de mayor a menor las enfermedades por el total de personas fallecidas."""

mortalidad2021_20 = mortalidad2021_20.sort_values(by='Total', ascending = False)

"""En octavo lugar, obtenemos las diez enfermedades que han causado más defunciones en el año en cuestión."""

top10_2021 = mortalidad2021_20.head(10)

"""En noveno lugar, reseteamos el índice para que nos aparezcan las diez enfermedades ordenadas del 1 al 10."""

top10_2021 = top10_2021.reset_index()
top10_2021.index += 1

"""En décimo lugar, nos quedamos con últimas cinco columnas y descartamos la que contiene los índices iniciales por defecto."""

top10_2021 = top10_2021.iloc[:, [1, 5]]

"""En undécimo lugar, eliminamos los 4 primeros carácteres de las celdas de la columna donde aparecen las enfermedades para 
eliminar los dígitos que aparecían por defecto en el dataset del INE."""

top10_2021['2021'] = top10_2021['2021'].str.slice(start=4)


"Años 2012 al 2020"

mortalidad2020 = pd.read_excel("muertes2020.xlsx")
mortalidad2020 = mortalidad2020.rename(columns= {" " : "2020"})
mortalidad_condicion = mortalidad2020['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2020['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2020['De 30 a 34 años'] != 0
mortalidad2020_20 = mortalidad2020[mortalidad_condicion]
mortalidad2020_20 = mortalidad2020[mortalidad_condicion2]
mortalidad2020_20 = mortalidad2020[mortalidad_condicion3]
mortalidad2020_20['Total'] = mortalidad2020_20.sum(axis=1)
total2020 = mortalidad2020_20['Total'].sum()
mortalidad2020_20['Porcentaje'] = (mortalidad2020_20['Total']/total2020)*100
mortalidad2020_20 = mortalidad2020_20.sort_values(by='Total', ascending = False)
top10_2020 = mortalidad2020_20.head(10)
top10_2020 = top10_2020.reset_index()
top10_2020.index += 1
top10_2020 = top10_2020.iloc[:, [1, 5, 6]]
top10_2020['2020'] = top10_2020['2020'].str.slice(start=4)

mortalidad2019 = pd.read_excel("muertes2019.xlsx")
mortalidad2019 = mortalidad2019.rename(columns= {" " : "2019"})
mortalidad_condicion = mortalidad2019['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2019['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2019['De 30 a 34 años'] != 0
mortalidad2019_20 = mortalidad2019[mortalidad_condicion]
mortalidad2019_20 = mortalidad2019[mortalidad_condicion2]
mortalidad2019_20 = mortalidad2019[mortalidad_condicion3]
mortalidad2019_20['Total'] = mortalidad2019_20.sum(axis=1)
total2019 = mortalidad2019_20['Total'].sum()
mortalidad2019_20['Porcentaje'] = (mortalidad2019_20['Total']/total2019)*100
mortalidad2019_20 = mortalidad2019_20.sort_values(by='Total', ascending = False)
top10_2019 = mortalidad2019_20.head(10)
top10_2019 = top10_2019.reset_index()
top10_2019.index += 1
top10_2019 = top10_2019.iloc[:, [1, 5, 6]]
top10_2019['2019'] = top10_2019['2019'].str.slice(start=4)

mortalidad2018 = pd.read_excel("muertes2018.xlsx")
mortalidad2018 = mortalidad2018.rename(columns= {" " : "2018"})
mortalidad_condicion = mortalidad2018['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2018['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2018['De 30 a 34 años'] != 0
mortalidad2018_20 = mortalidad2018[mortalidad_condicion]
mortalidad2018_20 = mortalidad2018[mortalidad_condicion2]
mortalidad2018_20 = mortalidad2018[mortalidad_condicion3]
mortalidad2018_20['Total'] = mortalidad2018_20.sum(axis=1)
total2018 = mortalidad2018_20['Total'].sum()
mortalidad2018_20['Porcentaje'] = (mortalidad2018_20['Total']/total2018)*100
mortalidad2018_20 = mortalidad2018_20.sort_values(by='Total', ascending = False)
top10_2018 = mortalidad2018_20.head(10)
top10_2018 = top10_2018.reset_index()
top10_2018.index += 1
top10_2018 = top10_2018.iloc[:, [1, 5, 6]]
top10_2018['2018'] = top10_2018['2018'].str.slice(start=4)

mortalidad2017 = pd.read_excel("muertes2017.xlsx")
mortalidad2017 = mortalidad2017.rename(columns= {" " : "2017"})
mortalidad_condicion = mortalidad2017['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2017['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2017['De 30 a 34 años'] != 0
mortalidad2017_20 = mortalidad2017[mortalidad_condicion]
mortalidad2017_20 = mortalidad2017[mortalidad_condicion2]
mortalidad2017_20 = mortalidad2017[mortalidad_condicion3]
mortalidad2017_20['Total'] = mortalidad2017_20.sum(axis=1)
total2017 = mortalidad2017_20['Total'].sum()
mortalidad2017_20['Porcentaje'] = (mortalidad2017_20['Total']/total2017)*100
mortalidad2017_20 = mortalidad2017_20.sort_values(by='Total', ascending = False)
top10_2017 = mortalidad2017_20.head(10)
top10_2017 = top10_2017.reset_index()
top10_2017.index += 1
top10_2017 = top10_2017.iloc[:, [1, 5, 6]]
top10_2017['2017'] = top10_2017['2017'].str.slice(start=4)

mortalidad2016 = pd.read_excel("muertes2016.xlsx")
mortalidad2016 = mortalidad2016.rename(columns= {" " : "2016"})
mortalidad_condicion = mortalidad2016['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2016['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2016['De 30 a 34 años'] != 0
mortalidad2016_20 = mortalidad2016[mortalidad_condicion]
mortalidad2016_20 = mortalidad2016[mortalidad_condicion2]
mortalidad2016_20 = mortalidad2016[mortalidad_condicion3]
mortalidad2016_20['Total'] = mortalidad2016_20.sum(axis=1)
total2016 = mortalidad2016_20['Total'].sum()
mortalidad2016_20['Porcentaje'] = (mortalidad2016_20['Total']/total2016)*100
mortalidad2016_20 = mortalidad2016_20.sort_values(by='Total', ascending = False)
top10_2016 = mortalidad2016_20.head(10)
top10_2016 = top10_2016.reset_index()
top10_2016.index += 1
top10_2016 = top10_2016.iloc[:, [1, 5, 6]]
top10_2016['2016'] = top10_2016['2016'].str.slice(start=4)

mortalidad2015 = pd.read_excel("muertes2015.xlsx")
mortalidad2015 = mortalidad2015.rename(columns= {" " : "2015"})
mortalidad_condicion = mortalidad2015['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2015['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2015['De 30 a 34 años'] != 0
mortalidad2015_20 = mortalidad2015[mortalidad_condicion]
mortalidad2015_20 = mortalidad2015[mortalidad_condicion2]
mortalidad2015_20 = mortalidad2015[mortalidad_condicion3]
mortalidad2015_20['Total'] = mortalidad2015_20.sum(axis=1)
total2015 = mortalidad2015_20['Total'].sum()
mortalidad2015_20['Porcentaje'] = (mortalidad2015_20['Total']/total2015)*100
mortalidad2015_20 = mortalidad2015_20.sort_values(by='Total', ascending = False)
top10_2015 = mortalidad2015_20.head(10)
top10_2015 = top10_2015.reset_index()
top10_2015.index += 1
top10_2015 = top10_2015.iloc[:, [1, 5, 6]]
top10_2015['2015'] = top10_2015['2015'].str.slice(start=4)

mortalidad2014 = pd.read_excel("muertes2014.xlsx")
mortalidad2014 = mortalidad2014.rename(columns= {" " : "2014"})
mortalidad_condicion = mortalidad2014['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2014['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2014['De 30 a 34 años'] != 0
mortalidad2014_20 = mortalidad2014[mortalidad_condicion]
mortalidad2014_20 = mortalidad2014[mortalidad_condicion2]
mortalidad2014_20 = mortalidad2014[mortalidad_condicion3]
mortalidad2014_20['Total'] = mortalidad2014_20.sum(axis=1)
total2014 = mortalidad2014_20['Total'].sum()
mortalidad2014_20['Porcentaje'] = (mortalidad2014_20['Total']/total2014)*100
mortalidad2014_20 = mortalidad2014_20.sort_values(by='Total', ascending = False)
top10_2014 = mortalidad2014_20.head(10)
top10_2014 = top10_2014.reset_index()
top10_2014.index += 1
top10_2014 = top10_2014.iloc[:, [1, 5, 6]]
top10_2014['2014'] = top10_2014['2014'].str.slice(start=4)

mortalidad2013 = pd.read_excel("muertes2013.xlsx")
mortalidad2013 = mortalidad2013.rename(columns= {" " : "2013"})
mortalidad_condicion = mortalidad2013['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2013['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2013['De 30 a 34 años'] != 0
mortalidad2013_20 = mortalidad2013[mortalidad_condicion]
mortalidad2013_20 = mortalidad2013[mortalidad_condicion2]
mortalidad2013_20 = mortalidad2013[mortalidad_condicion3]
mortalidad2013_20['Total'] = mortalidad2013_20.sum(axis=1)
total2013 = mortalidad2013_20['Total'].sum()
mortalidad2013_20['Porcentaje'] = (mortalidad2013_20['Total']/total2013)*100
mortalidad2013_20 = mortalidad2013_20.sort_values(by='Total', ascending = False)
top10_2013 = mortalidad2013_20.head(10)
top10_2013 = top10_2013.reset_index()
top10_2013.index += 1
top10_2013 = top10_2013.iloc[:, [1, 5, 6]]
top10_2013['2013'] = top10_2013['2013'].str.slice(start=4)

mortalidad2012 = pd.read_excel("muertes2012.xlsx")
mortalidad2012 = mortalidad2012.rename(columns= {" " : "2012"})
mortalidad_condicion = mortalidad2012['De 20 a 24 años'] != 0
mortalidad_condicion2 = mortalidad2012['De 25 a 29 años'] != 0
mortalidad_condicion3 = mortalidad2012['De 30 a 34 años'] != 0
mortalidad2012_20 = mortalidad2012[mortalidad_condicion]
mortalidad2012_20 = mortalidad2012[mortalidad_condicion2]
mortalidad2012_20 = mortalidad2012[mortalidad_condicion3]
mortalidad2012_20['Total'] = mortalidad2012_20.sum(axis=1)
total2012 = mortalidad2012_20['Total'].sum()
mortalidad2012_20['Porcentaje'] = (mortalidad2012_20['Total']/total2012)*100
mortalidad2012_20 = mortalidad2012_20.sort_values(by='Total', ascending = False)
top10_2012 = mortalidad2012_20.head(10)
top10_2012 = top10_2012.reset_index()
top10_2012.index += 1
top10_2012 = top10_2012.iloc[:, [1, 5, 6]]
top10_2012['2012'] = top10_2012['2012'].str.slice(start=4)

"Código visualizaciones"

import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots

py.offline.init_notebook_mode(connected=True) 

porcentaje_suicidios2021 = top10_2021.loc[top10_2021['2021'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2021 = float(porcentaje_suicidios2021)
total_suicidios2021 = top10_2021.loc[top10_2021['2021'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2021 = int(total_suicidios2021)

porcentaje_suicidios2020 = top10_2020.loc[top10_2020['2020'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2020 = float(porcentaje_suicidios2020)
total_suicidios2020 = top10_2020.loc[top10_2020['2020'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2020 = int(total_suicidios2020)

porcentaje_suicidios2019 = top10_2019.loc[top10_2019['2019'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2019 = float(porcentaje_suicidios2019)
total_suicidios2019 = top10_2019.loc[top10_2019['2019'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2019 = int(total_suicidios2019)

porcentaje_suicidios2018 = top10_2018.loc[top10_2018['2018'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2018 = float(porcentaje_suicidios2018)
total_suicidios2018 = top10_2018.loc[top10_2018['2018'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2018 = int(total_suicidios2018)

porcentaje_suicidios2017 = top10_2017.loc[top10_2017['2017'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2017 = float(porcentaje_suicidios2017)
total_suicidios2017 = top10_2017.loc[top10_2017['2017'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2017 = int(total_suicidios2017)

porcentaje_suicidios2016 = top10_2016.loc[top10_2016['2016'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2016 = float(porcentaje_suicidios2016)
total_suicidios2016 = top10_2016.loc[top10_2016['2016'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2016 = int(total_suicidios2016)

porcentaje_suicidios2015 = top10_2015.loc[top10_2015['2015'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2015 = float(porcentaje_suicidios2015)
total_suicidios2015 = top10_2015.loc[top10_2015['2015'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2015 = int(total_suicidios2015)

porcentaje_suicidios2014 = top10_2014.loc[top10_2014['2014'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2014 = float(porcentaje_suicidios2014)
total_suicidios2014 = top10_2014.loc[top10_2014['2014'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2014 = int(total_suicidios2014)

porcentaje_suicidios2013 = top10_2013.loc[top10_2013['2013'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2013 = float(porcentaje_suicidios2013)
total_suicidios2013 = top10_2013.loc[top10_2013['2013'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2013 = int(total_suicidios2013)

porcentaje_suicidios2012 = top10_2012.loc[top10_2012['2012'] == 'Suicidio y lesiones autoinfligidas', 'Porcentaje']
porcentaje_suicidios2012 = float(porcentaje_suicidios2012)
total_suicidios2012 = top10_2012.loc[top10_2012['2012'] == 'Suicidio y lesiones autoinfligidas', 'Total']
total_suicidios2012 = int(total_suicidios2012)

Año1 = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Porcentajes1 = [porcentaje_suicidios2012, porcentaje_suicidios2013, porcentaje_suicidios2014, porcentaje_suicidios2015, porcentaje_suicidios2016, porcentaje_suicidios2017, porcentaje_suicidios2018, porcentaje_suicidios2019, porcentaje_suicidios2020, porcentaje_suicidios2021]
porcentaje_suicidios = pd.DataFrame({"Año" : Año1, "Porcentaje" : Porcentajes1})

Año = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Totales = [total_suicidios2012, total_suicidios2013, total_suicidios2014, total_suicidios2015, total_suicidios2016, total_suicidios2017, total_suicidios2018, total_suicidios2019,total_suicidios2020, total_suicidios2021]
totales_suicidios = pd.DataFrame({"Año" : Año, "Defunciones por suicidio" : Totales})

fig_barras = go.Figure(go.Bar(
    x=totales_suicidios['Año'],
    y=totales_suicidios['Defunciones por suicidio'],
    marker=dict(
        color='red'),
    name='Número de fallecidos por sucidio'
))
fig_lineal = go.Figure(go.Scatter(
    x=porcentaje_suicidios['Año'],
    y=porcentaje_suicidios['Porcentaje'],
    name='Porcentaje de fallecidos por suicidio',
    line=dict(color='firebrick', width=4)
))
fig_barras.update_layout(
    yaxis=dict(
        title='Número de fallecidos por sucidio',
        tickformat='$,.0f',
        showgrid=False
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        orientation='h'
    )
)
fig_lineal.update_layout(
    yaxis=dict(
        title='Porcentaje defunciones',
        tickformat='$,.0f',
        showgrid=False
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        orientation='h'
    )
)
fig = make_subplots(rows=1, cols=2)

fig.add_trace(fig_barras.data[0], row=1, col=1)
fig.add_trace(fig_lineal.data[0], row=1, col=2)

fig.update_layout(title_text="Evolución de suicidios de personas jóvenes en España")

fig.show()

porcentaje_accidentes2021 = top10_2021.loc[top10_2021['2021'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2021 = float(porcentaje_accidentes2021)

total_accidentes2021 = top10_2021.loc[top10_2021['2021'] == 'Accidentes de tráfico', 'Total']
total_accidentes2021 = int(total_accidentes2021)

porcentaje_accidentes2020 = top10_2020.loc[top10_2020['2020'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2020 = float(porcentaje_accidentes2020)
total_accidentes2020 = top10_2020.loc[top10_2020['2020'] == 'Accidentes de tráfico', 'Total']
total_accidentes2020 = int(total_accidentes2020)

porcentaje_accidentes2019 = top10_2019.loc[top10_2019['2019'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2019 = float(porcentaje_accidentes2019)
total_accidentes2019 = top10_2019.loc[top10_2019['2019'] == 'Accidentes de tráfico', 'Total']
total_accidentes2019 = int(total_accidentes2019)

porcentaje_accidentes2018 = top10_2018.loc[top10_2018['2018'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2018 = float(porcentaje_accidentes2018)
total_accidentes2018 = top10_2018.loc[top10_2018['2018'] == 'Accidentes de tráfico', 'Total']
total_accidentes2018 = int(total_accidentes2018)

porcentaje_accidentes2017 = top10_2017.loc[top10_2017['2017'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2017 = float(porcentaje_accidentes2017)
total_accidentes2017 = top10_2017.loc[top10_2017['2017'] == 'Accidentes de tráfico', 'Total']
total_accidentes2017 = int(total_accidentes2017)

porcentaje_accidentes2016 = top10_2016.loc[top10_2016['2016'] == 'Accidentes de tráfico', 'Porcentaje']
porcentaje_accidentes2016 = float(porcentaje_accidentes2016)
total_accidentes2016 = top10_2016.loc[top10_2016['2016'] == 'Accidentes de tráfico', 'Total']
total_accidentes2016 = int(total_accidentes2016)

porcentaje_accidentes2015 = top10_2015.loc[top10_2015['2015'] == 'Accidentes de tráfico de vehículos de motor', 'Porcentaje']
porcentaje_accidentes2015 = float(porcentaje_accidentes2015)
total_accidentes2015 = top10_2015.loc[top10_2015['2015'] == 'Accidentes de tráfico de vehículos de motor', 'Total']
total_accidentes2015 = int(total_accidentes2015)

porcentaje_accidentes2014 = top10_2014.loc[top10_2014['2014'] == 'Accidentes de tráfico de vehículos de motor', 'Porcentaje']
porcentaje_accidentes2014 = float(porcentaje_accidentes2014)
total_accidentes2014 = top10_2014.loc[top10_2014['2014'] == 'Accidentes de tráfico de vehículos de motor', 'Total']
total_accidentes2014 = int(total_accidentes2014)

porcentaje_accidentes2013 = top10_2013.loc[top10_2013['2013'] == 'Accidentes de tráfico de vehículos de motor', 'Porcentaje']
porcentaje_accidentes2013 = float(porcentaje_accidentes2013)
total_accidentes2013 = top10_2013.loc[top10_2013['2013'] == 'Accidentes de tráfico de vehículos de motor', 'Total']
total_accidentes2013 = int(total_accidentes2013)

porcentaje_accidentes2012 = top10_2012.loc[top10_2012['2012'] == 'Accidentes de tráfico de vehículos de motor', 'Porcentaje']
porcentaje_accidentes2012 = float(porcentaje_accidentes2012)
total_accidentes2012 = top10_2012.loc[top10_2012['2012'] == 'Accidentes de tráfico de vehículos de motor', 'Total']
total_accidentes2012 = int(total_accidentes2012)

Año2 = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Porcentajes2 = [porcentaje_accidentes2012, porcentaje_accidentes2013, porcentaje_accidentes2014, porcentaje_accidentes2015, porcentaje_accidentes2016, porcentaje_accidentes2017, porcentaje_accidentes2018, porcentaje_accidentes2019, porcentaje_accidentes2020, por
porcentaje_accidentes = pd.DataFrame({"Año" : Año2, "Porcentaje" : Porcentajes2})

Año = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Totales = [total_accidentes2012, total_accidentes2013, total_accidentes2014, total_accidentes2015, total_accidentes2016, total_accidentes2017, total_accidentes2018, total_accidentes2019,total_accidentes2020, total_accidentes2021]
totales_accidentes = pd.DataFrame({"Año" : Año, "Defunciones por accidente de tráfico" : Totales})

fig_barras = go.Figure(go.Bar(
    x=totales_accidentes['Año'],
    y=totales_accidentes['Defunciones por accidente de tráfico'],
    marker=dict(
        color='blue'),
    name='Número de fallecidos por accidente de tráfico'
))
fig_lineal = go.Figure(go.Scatter(
    x=porcentaje_accidentes['Año'],
    y=porcentaje_accidentes['Porcentaje'],
    name='Porcentaje de fallecidos por suicidio',
    line=dict(color='darkblue', width=4)
))
fig_barras.update_layout(
    yaxis=dict(
        title='Número de fallecidos por accidente de tráfico',
        tickformat='$,.0f',
        showgrid=False
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        orientation='h'
    )
)
fig_lineal.update_layout(
    yaxis=dict(
        title='Porcentaje defunciones',
        tickformat='$,.0f',
        showgrid=False
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        orientation='h'
    )
)
fig = make_subplots(rows=1, cols=2)

fig.add_trace(fig_barras.data[0], row=1, col=1)
fig.add_trace(fig_lineal.data[0], row=1, col=2)

fig.update_layout(title_text="Evolución de defunciones por accidente de tráfico de personas jóvenes en España")

fig.show()