"ANTIDEPRESIVOS"

"OBTENCIÓN, TRANSFORMACIÓN Y ANÁLISIS DE DATOS"

import pandas as pd

"""En primer lugar, abrimos el archivo excel descargado de la página web Statista
https://es.statista.com/estadisticas/544028/dosis-diaria-definida-de-antidepresivos-en-espana/?locale=es"""

antidepresivos = pd.read_excel("antidepresivos.xlsx")

"""En segundo lugar, renombramos la columna Unnamed 1 donde aparece la dosis diaria recetada de antidepresivos
por la palabra Dosis diaria para identificar el concepto objeto de estudio."""

antidepresivos = antidepresivos.rename(columns= {"Unnamed: 1" : "Dosis diaria"})

"""En tercer lugar, creamos y aplicamos un filtro en el que la condición del año fuera superior a 2011, ya que los datos de mortalidad
con los que contamos son a partir de 2012."""

antidepresivos = antidepresivos[antidepresivos["Año"] > 2011]

"""En cuarto lugar, añadimos una columna nueva llamada Incremento para reflejar el incremento porcentual respecto al año anterior."""

antidepresivos['Incremento'] = antidepresivos['Dosis diaria'].pct_change()*100

"""Por último, utilizamos el método describe para obtener las variables estadísticas."""

estadísticas_AD = antidepresivos['Dosis diaria'].describe()
estadísticas_AD2 = antidepresivos['Incremento'].describe()

"VISUALIZACIONES"

import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
py.offline.init_notebook_mode(connected=True) 

fig_barras = go.Figure(go.Bar(
    x=antidepresivos['Año'],
    y=antidepresivos['Dosis diaria'],
    marker=dict(
        color='red'),
    name='Dosis diaria recetada de antidepresivos'
))

fig_lineal = go.Figure(go.Scatter(
    x=antidepresivos['Año'],
    y=antidepresivos['Incremento'],
    name='Incremento de la dosis diaria recetada de antidepresivos',
    line=dict(color='firebrick', width=4)
))

fig_barras.update_layout(
    yaxis=dict(
        title='Dosis diaria recetada de antidepresivos',
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
        title='Incremento de la dosis diaria recetada de antidepresivos',
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

fig.update_layout(
    title_text="Evolución de la dosis diaria recetada de antidepresivos")

fig.show()


"AYUDA SOLICITADA"

"OBTENCIÓN, TRANSFORMACIÓN Y ANÁLISIS DE DATOS"

"""En primer lugar, abrimos el archivo excel descargado de la página web EPData
https://www.epdata.es/peticiones-ayuda-telefono-anar-ideacion-suicida-intentos-suicidio-menores-edad/162bc67b-046a-4fd9-9dd4-51af122bf7e5"""

peticion_ayuda = pd.read_excel('peticiones_de_ayuda_al_telefono_de_anar_sobre_ideacion_suicida_e_intentos_de_suicidio_en_menores_de_edad.xlsx')

"""En segundo lugar, creamos y aplicamos un filtro en el que la condición del año fuera superior a 2011, ya que los datos de mortalidad
con los que contamos son a partir de 2012."""

peticion_ayuda = peticion_ayuda[peticion_ayuda["Año"] > 2011]

"""En tercer lugar, añadimos una columna nueva llamada Incremento para reflejar el incremento porcentual respecto al año anterior."""

peticion_ayuda['Incremento'] = peticion_ayuda['Peticiones'].pct_change()*100

"""Por último, utilizamos el método describe para obtener las variables estadísticas."""

estadísticas_PA = peticion_ayuda['Peticiones'].describe()
estadísticas_PA2 = peticion_ayuda['Incremento'].describe()

"VISUALIZACIONES"

fig_barras = go.Figure(go.Bar(
    x=peticion_ayuda['Año'],
    y=peticion_ayuda['Peticiones'],
    marker=dict(
        color='red'),
    name='Peticiones de ayuda de prevención de suicidio'
))

fig_lineal = go.Figure(go.Scatter(
    x=peticion_ayuda['Año'],
    y=peticion_ayuda['Incremento'],
    name='Incremento de las preticiones de ayuda de prevención de suicidio',
    line=dict(color='firebrick', width=4)
))

fig_barras.update_layout(
    yaxis=dict(
        title='Peticiones de ayuda de prevención de suicidio',
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
        title='Incremento de las peticiones de ayuda de prevención de suicidio',
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

fig.update_layout(title_text="Evolución de las peticiones de ayuda de prevención de suicidio")

fig.show()


"PSICÓLOGOS"

"OBTENCIÓN, TRANSFORMACIÓN Y ANÁLISIS DE DATOS"

"""En primer lugar, abrimos el archivo csv descargado de la página web de EPData
https://www.epdata.es/evolucion-numero-psicologos-espana/8a894136-0b07-4194-a1d4-c11eea309d53"""

psicologos = pd.read_csv('psicologos.csv', sep= ";")

"""En segundo lugar, hemos eliminado las columnas y celdas en las que aparecían datos que no resultaban de interés para el análisis."""

psicologos = psicologos.iloc[0:10, [0,2]]

"""En tercer lugar, añadimos una columna nueva llamada Incremento para reflejar el incremento porcentual respecto al año anterior."""

psicologos['Incremento'] = psicologos['Total'].pct_change()*100

"""Por último, utilizamos el método describe para obtener las variables estadísticas."""

estadísticas_PS = psicologos['Total'].describe()
estadísticas_PS2 = psicologos['Incremento'].describe()

"VISUALIZACIONES"

fig_barras = go.Figure(go.Bar(
    x=psicologos['Año'],
    y=psicologos['Total'],
    marker=dict(
        color='red'),
    name='Psicólogos ejercientes en España'
))

fig_lineal = go.Figure(go.Scatter(
    x=psicologos['Año'],
    y=psicologos['Incremento'],
    name='Incremento de los psicólogos ejercientes en España',
    line=dict(color='firebrick', width=4)
))

fig_barras.update_layout(
    yaxis=dict(
        title='Psicólogos ejercientes en España',
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
        title='Incremento de los psicólogos ejercientes en España',
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

fig.update_layout(title_text="Evolución de los psicólogos ejercientes en España")

fig.show()