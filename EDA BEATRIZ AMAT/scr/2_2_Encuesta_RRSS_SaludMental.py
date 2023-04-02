import pandas as pd

"Código obtención de los resultados de la encuesta"

"""En primer lugar, abrimos el archivo csv donde aparecen recopilados los resultados de la encuesta efectuada
https://docs.google.com/spreadsheets/d/1espVWoKwtwFrv8hBeUP1q_k0yeCzYwbzXngXrI0uWNM/edit#gid=998776026""" 

resultados_encuesta = pd.read_csv('resultados_encuesta.csv', sep = ',')

"""En segundo lugar, descartamos las dos primeras columnas, ya que aparecía la marca temporal de las respuestas 
y la puntuación obtenida de las mismas, datos que no resultaban relevantes para el análisis."""

resultados_encuesta = resultados_encuesta[resultados_encuesta.columns[2:-1]]

"""En tercer lugar, descartamos las respuestas de participantes mayores a 34 años, ya que interesa conocer 
únicamente las respuestas de los participantes menores de 34 años."""

filtro_edad = resultados_encuesta['Introduce tu edad'] < '35'
resultados_encuesta = resultados_encuesta[filtro_edad]

"""En cuarto lugar, dividimos los resultados de la encuesta en dos partes: conducción y RRSSS. Para este caso, 
necesitamos los datos que aparecen a partir de la cuarta columna, ya que son las que contienen información relacionada
con la salud mental y el uso delas RRSS."""

saludmental_RRSS = resultados_encuesta[resultados_encuesta.columns[4:-1]]


"Código para el análisis de los resultados de la encuesta"

"En primer lugar, vamos a conocer el porcentaje de participantes que nunca se han comparado con alguien que siguen en RRSS."""

comparaciónRRSS_negativa = saludmental_RRSS['¿Alguna vez te has comparado con personas a las que sigues en RRSS?'] == 'No'
comparaciónRRSS_negativa = saludmental_RRSS[comparaciónRRSS_negativa]

"En segundo lugar, vamos a conocer el porcentaje de participantes que se han comparado con alguien que siguen en RRSS."""

comparaciónRRSS_positiva = saludmental_RRSS['¿Alguna vez te has comparado con personas a las que sigues en RRSS?'] != "No"
comparaciónRRSS_positiva = saludmental_RRSS[comparaciónRRSS_positiva]

"En tercer lugar, vamos a conocer el porcentaje de participantes que afirman haber sentido complejo de inferioridad al compararse en RRSS."

inferioridad = comparaciónRRSS_positiva['¿Te has sentido inferior al hacerlo?'] != "No"
inferioridad = comparaciónRRSS_positiva[inferioridad]

"En cuarto lugar, vamos a conocer el porcentaje de participantes que afirman que las RRSS influencian en la toma de sus decisiones."

influencia = saludmental_RRSS['¿Crees que influye en nuestra toma de decisiones los que vemos en RRSS?'] != 'No'
influencia = saludmental_RRSS[influencia]

"En quinto lugar, vamos a conocer el porcentaje de participantes que son incapaces de estar sin RRSS."

incapazRRSS = saludmental_RRSS['¿Has estado algun periodo de tiempo sin RRSS para desconectar?'] == 'Soy incapaz'
incapazRRSS = saludmental_RRSS[incapazRRSS]

"En sexto lugar, vamos a conocer el porcentaje de participantes que an logrado estar una semana sin RRSS."

semanasinRRSS = saludmental_RRSS['¿Has estado algun periodo de tiempo sin RRSS para desconectar?'] == 'Una semana'
semanasinRRSS = saludmental_RRSS[semanasinRRSS]

"En séptimo lugar, vamos a conocer el porcentaje de participantes que han logrado estar más de un mes sin RRSS."

masdeunmessinRRSS = saludmental_RRSS['¿Has estado algun periodo de tiempo sin RRSS para desconectar?'] == 'Más de un mes'
masdeunmessinRRSS = saludmental_RRSS[masdeunmessinRRSS]

"En octavo lugar, vamos a conocer el porcentaje de participantes que consideran que estar sin RRSS resulta beneficioso para su salud mental."

beneficiosoRRSS = saludmental_RRSS['En caso afirmativo, ¿crees que te benefició?'] != 'No'
beneficiosoRRSS = saludmental_RRSS[beneficiosoRRSS]

"En noveno lugar, vamos a conocer el porcentaje de participantes que consideran que las personas que le rodean no tienen buena salud mental."

saludmentalmala = saludmental_RRSS['¿Consideras que la gente que te rodea goza de una buena salud mental?'] != 'Sí'
saludmentalmala = saludmental_RRSS[saludmentalmala]

"En décimo lugar, vamos a conocer el porcentaje de participantes que no estarían dispuestos a recibir ayuda en caso de tener algún síntoma de depresión."

recibirayuda = saludmental_RRSS['¿Estarías dispuesto de acudir a un especialista si tuvieras algún síntoma de depresión?'] == 'Me esperaría a que se pasara'
recibirayuda = saludmental_RRSS[recibirayuda]

"En onceavo lugar, vamos a conocer el porcentaje de participantes que estarían dispuestos a acudir a un psicólogo en caso de tener algún síntoma de depresión."

recibirayudapsicologo = saludmental_RRSS['¿Estarías dispuesto de acudir a un especialista si tuvieras algún síntoma de depresión?'] == 'Psicólogo'
recibirayudapsicologo = saludmental_RRSS[recibirayudapsicologo]

"En doceavo lugar, vamos a conocer el porcentaje de participantes que estarían dispuestos a acudir a un psiquiatra en caso de tener algún síntoma de depresión."

recibirayudapsiquiatra = saludmental_RRSS['¿Estarías dispuesto de acudir a un especialista si tuvieras algún síntoma de depresión?'] == 'Psiquiatra'
recibirayudapsiquiatra = saludmental_RRSS[recibirayudapsiquiatra]