import pandas as pd

"Código obtención de los resultados de la encuesta"

"""En primer lugar, abrimos el archivo csv donde aparecen recopilados los resultados de la encuesta efectuada
https://docs.google.com/spreadsheets/d/1espVWoKwtwFrv8hBeUP1q_k0yeCzYwbzXngXrI0uWNM/edit#gid=998776026"""

resultados_encuesta = pd.read_csv('resultados_encuesta.csv', sep = ',')

"""En segundo lugar, descartamos las dos primeras columnas, ya que aparecía la marca temporal de las respuestas 
y la puntuación obtenida de las mismas, datos que no resultaban relevantes para el análisis."""

resultados_encuesta = resultados_encuesta[resultados_encuesta.columns[2:]]

"""En tercer lugar, descartamos las respuestas de participantes mayores a 34 años, ya que interesa conocer 
únicamente las respuestas de los participantes menores de 34 años."""

filtro_edad = resultados_encuesta['Introduce tu edad'] < '35'
resultados_encuesta = resultados_encuesta[filtro_edad]

"""En cuarto lugar, dividimos los resultados de la encuesta en dos partes: conducción y RRSSS. Para este caso, 
necesitamos únicamente las tres primeras columnas, ya que son las que contienen información relacionada con la conducción."""

accidentes_trafico = resultados_encuesta[resultados_encuesta.columns[1:4]]


"Código para el análisis de los resultados de la encuesta"

"""En primer lugar, vamos a descartar a aquellos participantes que no tienen carnet de conducir, 
ya que las respuestas que nos interesan para el estudio son de personas que conducen."""

filtro_conductores = accidentes_trafico['¿Tienes carnet de conducir?'] == 'Si'
accidentes_trafico = accidentes_trafico[filtro_conductores]

"""En segundo lugar, vamos a conocer el porcentaje de participantes que afirman haber hecho uso de un vehículo 
bajo la influencia de alcohol o estupefacientes."""

conduccion_temeraria = accidentes_trafico['¿Has conducido alguna vez bajo los efectos del alcohol o estupefacientes?'] == 'Sí'
conduccion_temeraria = accidentes_trafico[conduccion_temeraria]

"""En tercer lugar, vamos a conocer el porcentaje de participantes que niegan haber hecho uso de un vehículo bajo 
la influencia de alcohol o estupefacientes."""

conduccion_responsable = accidentes_trafico['¿Has conducido alguna vez bajo los efectos del alcohol o estupefacientes?'] == 'No'
conduccion_responsable = accidentes_trafico[conduccion_responsable]

"""En cuarto lugar, vamos a conocer el porcentaje de las causas que más reparo da a los participantes que han conducido un vehículo 
de manera temeraria."""

multa2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Multa"
multa2 = conduccion_temeraria[multa2]

sanción2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Sanción"
sanción2 = conduccion_temeraria[sanción2]

seguridad2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Poner en peligro la seguridad de otras personas"
seguridad2 = conduccion_temeraria[seguridad2]

"Código para para exportar el data frame a formato excel"

resultados_encuesta.to_excel("resultado.xlsx")
