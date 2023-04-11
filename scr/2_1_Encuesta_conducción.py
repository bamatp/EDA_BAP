import pandas as pd


"Código obtención de los resultados de la primera encuesta - Accidentes de Tráfico"

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


"Código análisis de los resultados de la primera encuesta - Accidentes de Tráfico"

"""En primer lugar, descartamos a aquellos participantes que no tienen carnet de conducir, 
ya que las respuestas que nos interesan para el estudio son de personas que conducen."""

filtro_conductores = accidentes_trafico['¿Tienes carnet de conducir?'] == 'Si'
accidentes_trafico = accidentes_trafico[filtro_conductores]

"""En segundo lugar, calculamos el porcentaje de participantes que afirman haber hecho uso de un vehículo 
bajo la influencia de alcohol o estupefacientes."""

conduccion_temeraria = accidentes_trafico['¿Has conducido alguna vez bajo los efectos del alcohol o estupefacientes?'] == 'Sí'
conduccion_temeraria = accidentes_trafico[conduccion_temeraria]

"""En tercer lugar, calculamos el porcentaje de participantes que niegan haber hecho uso de un vehículo bajo 
la influencia de alcohol o estupefacientes."""

conduccion_responsable = accidentes_trafico['¿Has conducido alguna vez bajo los efectos del alcohol o estupefacientes?'] == 'No'
conduccion_responsable = accidentes_trafico[conduccion_responsable]

"""Por último, calculamos el porcentaje de las causas que más reparo da a los participantes que han conducido un vehículo 
de manera temeraria."""

multa2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Multa"
multa2 = conduccion_temeraria[multa2]

sanción2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Sanción"
sanción2 = conduccion_temeraria[sanción2]

seguridad2 = conduccion_temeraria['En caso afirmativo, ¿qué es lo que mas reparo te da cuando lo haces?'] == "Poner en peligro la seguridad de otras personas"
seguridad2 = conduccion_temeraria[seguridad2]



"Código obtención y análisis de los resultados de la segunda encuesta - Accidentes de Tráfico"

"""En primer lugar, abrimos el archivo csv donde aparecen recopilados los resultados de la encuesta efectuada
https://docs.google.com/forms/d/19AcuaWmDUW-RAn7l5gAW7bZRs5pIiwTXGhoW3nZt8BM/edit"""

resultados_encuesta2 = pd.read_csv('Encuestaconducción.csv', sep=',')

"""En segundo lugar, descartamos la primera columna, ya que aparecía la marca temporal de las respuestas, datos que 
no resultaban relevantes para el análisis."""

resultados_encuesta2 = resultados_encuesta2.iloc[:, 1:]

"""En tercer lugar, calculamos el porcentaje de participantes que afirman haberse saltado un semáforo en rojo en
alguna ocasión."""

semáforo = resultados_encuesta2['¿Sueles saltarte semáforos en rojo?'] != 'Nunca'
semáforo = resultados_encuesta2[semáforo]

"""En cuarto lugar, calculamos el porcentaje de participantes que afirman sobrepasar el límite de velocidad en
alguna ocasión."""

velocidad = resultados_encuesta2['¿Sueltes sobrepasar el límite de velocidad?'] != 'Nunca'
velocidad = resultados_encuesta2[velocidad]

"""En quinto lugar, calculamos el porcentaje de participantes que afirman mirar el móvil mientras conducen."""

móvil = resultados_encuesta2['¿Sueles mirar el móvil mientras conduces?'] != 'Nunca'
móvil = resultados_encuesta2[móvil]

"""En sexto lugar, calculamos el porcentaje de participantes que afirman haber tenido alguna vez un accidente de tráfico."""

accidente = resultados_encuesta2['¿Has tenido alguna vez un accidente?'] != 'No'
accidente = resultados_encuesta2[accidente]

"""Por último, calculamos el porcentaje que representa cada causa sobre los accidentes de tráfico."""

alcohol_drogas = resultados_encuesta2['En caso afirmativo, ¿puedes indicar el motivo?'] == 'Alcohol y drogas'
alcohol_drogas = resultados_encuesta2[alcohol_drogas]

distracción = resultados_encuesta2['En caso afirmativo, ¿puedes indicar el motivo?'] == 'Distracciones al volante'
distracción = resultados_encuesta2[distracción]

velocidad2 = resultados_encuesta2['En caso afirmativo, ¿puedes indicar el motivo?'] == 'Velocidad'
velocidad2 = resultados_encuesta2[velocidad2]

señalización = resultados_encuesta2['En caso afirmativo, ¿puedes indicar el motivo?'] == 'Ignorar una señalización de tráfico'
señalización = resultados_encuesta2[señalización]

otros = resultados_encuesta2['En caso afirmativo, ¿puedes indicar el motivo?'] == 'Otros'
otros = resultados_encuesta2[otros]
