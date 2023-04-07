"MULTAS DE TRÁFICO"

"OBTENCIÓN, TRANSFORMACIÓN Y ANÁLISIS DE DATOS"

import pandas as pd

"""Se explican únicamente los pasos efectuados en el dataset del año 2021, ya que en el resto de años se ha seguido el mismo procedimiento para la obtención, transformación y análisis de los datos."""

"2021"

"""En primer lugar, abrimos el archivo excel descargado del Portal de datos abiertos del Ayuntamiento de Madrid que contiene 
el detalle de las multas de circulación en el mes de diciembre de 2021
https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=fb9a498a6bdb9410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default"""

dic2021 = pd.read_excel('202112_detalle.xlsx')

"""En segundo lugar, creamos un filtro en el que la condición de la calificación de la multa sea grave para obtener el listado de multas graves impuestas en el 
mes de diciembre de 2021"""

graves2021_f = dic2021['CALIFICACION'] == 'GRAVE     '
graves2021 = dic2021[graves2021_f]

"""En tercer lugar, agrupamos las multas graves por el tipo de infracción cometida y las ordenamos de menor de mayor"""

grouped_multas_graves_2021 = graves2021.groupby('HECHO-BOL')
multas_graves_2021 = grouped_multas_graves_2021['HECHO-BOL'].count()

multas_graves_2021 = multas_graves_2021.to_frame(name = 'Total')
multas_graves_2021 = multas_graves_2021.reset_index()

multas_graves_2021 = multas_graves_2021.sort_values('Total', ascending=False)

"""En cuarto lugar, obtenemos el listado de las cinco principales infracciones del listado de multas graves impuestas"""

multas_graves_2021 = multas_graves_2021.head(5)

"""En quinto lugar, creamos un filtro en el que la condición de la calificación de la multa sea muy grave para obtener el listado de multas muy graves impuestas en el 
mes de diciembre de 2021"""

muygraves2021_f = dic2021['CALIFICACION'] == 'MUY GRAVE '
muygraves2021 = dic2021[muygraves2021_f]

"""En sexto lugar, agrupamos las multas muy graves por el tipo de infracción cometida y las ordenamos de menor de mayor"""

grouped_multas_muy_graves_2021 = muygraves2021.groupby('HECHO-BOL')
multas_muy_graves_2021 = grouped_multas_muy_graves_2021['HECHO-BOL'].count()

multas_muy_graves_2021  = multas_muy_graves_2021.to_frame(name = 'Total')
multas_muy_graves_2021  = multas_muy_graves_2021.reset_index()

multas_muy_graves_2021  = multas_muy_graves_2021.sort_values('Total', ascending=False)

"""En séptimo lugar, obtenemos el listado de las cinco principales infracciones del listado de multas muy graves impuestas"""

multas_muy_graves_2021 = multas_muy_graves_2021.head(5)

"""Por último, obtenemos el número de infracciones graves provocadas por la utilización de un dispositivo móvil mientras se conducía"""

móvil_2021_c = dic2021['HECHO-BOL'] == 'CONDUCIR UTILIZANDO MANUALMENTE TELEFONÍA MÓVIL, NAVEGADOR O SISTEMA DE COMUNICACIÓN ODETECCIÓN DE RADAR.                    '
móvil_2021 = dic2021[móvil_2021_c]

"2020"

dic2020 = pd.read_excel('202012_detalle.xlsx')

graves2020_f = dic2020['CALIFICACION'] == 'GRAVE     '
graves2020 = dic2020[graves2020_f]

grouped_multas_graves_2020 = graves2020.groupby('HECHO-BOL')
multas_graves_2020 = grouped_multas_graves_2020['HECHO-BOL'].count()
multas_graves_2020 = multas_graves_2020.to_frame(name='Total')
multas_graves_2020 = multas_graves_2020.reset_index()
multas_graves_2020 = multas_graves_2020.sort_values('Total', ascending=False)
multas_graves_2020 = multas_graves_2020.head(5)

muygraves2020_f = dic2020['CALIFICACION'] == 'MUY GRAVE '
muygraves2020 = dic2020[muygraves2020_f]

grouped_multas_muy_graves_2020 = muygraves2020.groupby('HECHO-BOL')
multas_muy_graves_2020 = grouped_multas_muy_graves_2020['HECHO-BOL'].count()
multas_muy_graves_2020 = multas_muy_graves_2020.to_frame(name='Total')
multas_muy_graves_2020 = multas_muy_graves_2020.reset_index()
multas_muy_graves_2020 = multas_muy_graves_2020.sort_values('Total', ascending=False)
multas_muy_graves_2020 = multas_muy_graves_2020.head(5)

móvil_2020_c = dic2020['HECHO-BOL'] == 'CONDUCIR UTILIZANDO MANUALMENTE TELEFONÍA MÓVIL, NAVEGADOR O SISTEMA DE COMUNICACIÓN ODETECCIÓN DE RADAR.                    '
móvil_2020 = dic2020[móvil_2020_c]

"2019"

dic2019 = pd.read_excel('201912_detalle.xlsx')

graves2019_f = dic2019['CALIFICACION'] == 'GRAVE     '
graves2019 = dic2019[graves2019_f]

grouped_multas_graves_2019 = graves2019.groupby('HECHO-BOL')
multas_graves_2019 = grouped_multas_graves_2019['HECHO-BOL'].count()
multas_graves_2019 = multas_graves_2019.to_frame(name='Total')
multas_graves_2019 = multas_graves_2019.reset_index()
multas_graves_2019 = multas_graves_2019.sort_values('Total', ascending=False)
multas_graves_2019 = multas_graves_2019.head(5)

muygraves2019_f = dic2019['CALIFICACION'] == 'MUY GRAVE '
muygraves2019 = dic2019[muygraves2019_f]

grouped_multas_muy_graves_2019 = muygraves2019.groupby('HECHO-BOL')
multas_muy_graves_2019 = grouped_multas_muy_graves_2019['HECHO-BOL'].count()
multas_muy_graves_2019 = multas_muy_graves_2019.to_frame(name='Total')
multas_muy_graves_2019 = multas_muy_graves_2019.reset_index()
multas_muy_graves_2019 = multas_muy_graves_2019.sort_values(
    'Total', ascending=False)
multas_muy_graves_2019 = multas_muy_graves_2019.head(5)

móvil_2019_c = dic2019['HECHO-BOL'] == 'CONDUCIR UTILIZANDO MANUALMENTE TELEFONÍA MÓVIL, NAVEGADOR O SISTEMA DE COMUNICACIÓN ODETECCIÓN DE RADAR.                    '
móvil_2019 = dic2019[móvil_2019_c]

"2018"

dic2018 = pd.read_excel('201812_detalle.xlsx')

graves2018_f = dic2018['CALIFICACION'] == 'GRAVE     '
graves2018 = dic2018[graves2018_f]

grouped_multas_graves_2018 = graves2018.groupby('HECHO-BOL')
multas_graves_2018 = grouped_multas_graves_2018['HECHO-BOL'].count()
multas_graves_2018 = multas_graves_2018.to_frame(name='Total')
multas_graves_2018 = multas_graves_2018.reset_index()
multas_graves_2018 = multas_graves_2018.sort_values('Total', ascending=False)
multas_graves_2018 = multas_graves_2018.head(5)

muygraves2018_f = dic2018['CALIFICACION'] == 'MUY GRAVE '
muygraves2018 = dic2018[muygraves2018_f]

grouped_multas_muy_graves_2018 = muygraves2018.groupby('HECHO-BOL')
multas_muy_graves_2018 = grouped_multas_muy_graves_2018['HECHO-BOL'].count()
multas_muy_graves_2018 = multas_muy_graves_2018.to_frame(name='Total')
multas_muy_graves_2018 = multas_muy_graves_2018.reset_index()
multas_muy_graves_2018 = multas_muy_graves_2018.sort_values(
    'Total', ascending=False)
multas_muy_graves_2018 = multas_muy_graves_2018.head(5)

móvil_2018_c = dic2018['HECHO-BOL'] == 'CONDUCIR UTILIZANDO MANUALMENTE TELEFONÍA MÓVIL, NAVEGADOR O SISTEMA DE COMUNICACIÓN ODETECCIÓN DE RADAR.                    '
móvil_2018 = dic2018[móvil_2018_c]

"2017"

dic2017 = pd.read_excel('201712_detalle.xlsx')

graves2017_f = dic2017['CALIFICACION'] == 'GRAVE     '
graves2017 = dic2017[graves2017_f]

grouped_multas_graves_2017 = graves2017.groupby('HECHO-BOL')
multas_graves_2017 = grouped_multas_graves_2017['HECHO-BOL'].count()
multas_graves_2017 = multas_graves_2017.to_frame(name='Total')
multas_graves_2017 = multas_graves_2017.reset_index()
multas_graves_2017 = multas_graves_2017.sort_values('Total', ascending=False)
multas_graves_2017 = multas_graves_2017.head(5)

muygraves2017_f = dic2017['CALIFICACION'] == 'MUY GRAVE '
muygraves2017 = dic2017[muygraves2017_f]

grouped_multas_muy_graves_2017 = muygraves2017.groupby('HECHO-BOL')
multas_muy_graves_2017 = grouped_multas_muy_graves_2017['HECHO-BOL'].count()
multas_muy_graves_2017 = multas_muy_graves_2017.to_frame(name='Total')
multas_muy_graves_2017 = multas_muy_graves_2017.reset_index()
multas_muy_graves_2017 = multas_muy_graves_2017.sort_values(
    'Total', ascending=False)
multas_muy_graves_2017 = multas_muy_graves_2017.head(5)

móvil_2017_c = dic2017['HECHO-BOL'] == 'CONDUCIR UTILIZANDO MANUALMENTE TELEFONÍA MÓVIL, NAVEGADOR O SISTEMA DE COMUNICACIÓN ODETECCIÓN DE RADAR.                    '
móvil_2017 = dic2017[móvil_2017_c]