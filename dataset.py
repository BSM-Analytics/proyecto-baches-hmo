import requests  # Importamos la libreria "requests" para las solicitudes HTTP hacia las APIs
import pandas as pd # Importamos la libreria "pandas" para el manejo en DataFrames y exportacion de los datos
import shutil # Importamos la libreria "shutils" para manejo de archivos y directorios
import zipfile # Importamos la libreria "zipfile" para descomprimir carpetas comprimidas
import os # Importamos la libreria "os" para manejo de rutas
import time, datetime # Importamos las libreria "time" y "datetime" para generar timestamps y medir duraciones

# ------ VARIABLES ESTATICAS DE CONFIGURACION ------

STORAGE_PATH = "./data/raw"

# Endpoint a AJAX API del Bachometro de Hermosillo (encontrado monitoreando el trafico en el sitio web)
URL_BACHOMETRO_HMO = "https://bachometro.hermosillo.gob.mx/mapa/ajax"
RAW_BACHES_FILENAME = "baches_hmo_2021_2024.csv"

# Endpoint para descarga de archivo SHP y complementos de AGEBS de Hermosillo en sitio web INEGI
URL_AGEBS_HMO = "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/urbana/SHP_2/Sonora/702825317744_s.zip"
AGEBS_ZIP_FILENAME = "agebs_hmo.zip"
HMO_AGEB_FILE_LIST = ['.html', 'a.dbf','a.prj','a.shp', 'a.shp.xml', 'a.dbf', 'a.shx']

# Endpoint para descarga de archivo CSV con datos Socioeconomicos (Rezago Social) de Hermosillo en sitio web INEGI
URL_SOCIOECONOMICO_HMO = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/ageb_manzana/ageb_mza_urbana_26_cpv2020_csv.zip"
SOCIOECONOMICO_ZIP_FILENAME = "socioeconomico_2020.zip"
RAW_SOCIOECONOMICO_FILENAME = ""

DATA_DESCRIPTION_FILENAME = "data_description.txt"

# Plantilla para generacion de archivo TXT con informacion de datos descargados
DATA_DESCRIPTION_TEMPLATE = \
"""DESCRIPCION DE LOS DATOS DESCARGADOS:

DATOS DEL BACHOMETRO DE HERMOSILLO ---------------------------------------------------*

DESCRIPCION: Este conjunto de datos contiene informacion sobre baches reportados por ciudadanos
en el municipio de Hermosillo, Sonora, en el periodo comprendido entre el 17 de septiembre del 2021
hasta el ultimo mes transcurrido del actual año.

Cuenta con informacion relevante tal como:
Ubicacion (latitud, longitud) del bache reportado, Fecha y Comentarios.

FUENTE: %s
TIPO: API (no documentada)
FECHA Y HORA DE DESCARGA: %s
TIEMPO TOTAL DE EXTRACCION: %s s

DATOS DE AGEBS DE HERMOSILLO ---------------------------------------------------*

DESCRIPCION: Este conjunto de datos contiene las AGEBS del municipio de Hermosillo, Sonora, provistas
por el INEGI en el año 2010. Este nos permitira clasificar distintas areas del municipio por alguna de
sus caracteristicas socioeconomicas y ubicar mas claramente los baches del conjunto de datos del bachometro.

La informacion de mayor relevancia que contiene son las AGEBS.

FUENTE: %s
TIPO: Descarga de archivo
FECHA Y HORA DE DESCARGA: %s
TIEMPO TOTAL DE EXTRACCION: %s s

DATOS SOCIOECONOMICOS (REZAGO SOCIAL) DE HERMOSILLO ---------------------------------------------------*

DESCRIPCION: Este conjunto de datos contiene informacion sobre el rezago social del municipio de Hermosillo,
Sonora en el año 2020. Esto nos permitira identificar zonas con mayor rezago y relacionarlo con los AGEBS.

Contiene informacion variada sobre indicadores socioeconomicos, de tipo cualitativo, que podremos trasladar
a cuantitativo para clasificacion.

FUENTE: %s
TIPO DE FUENTE: Descarga de archivo
FECHA Y HORA DE DESCARGA: %s
TIEMPO TOTAL DE EXTRACCION: %s s"""

# ------ PROCESO DE DESCARGA Y ALMACENAMIENTO ------

# Aseguramos que existan los directorios destino, de lo contrario se generan
if not os.path.exists("./data"): os.mkdir("./data")
if not os.path.exists("./data/raw"): os.mkdir("./data/raw")

start = time.time() # Iniciamos contador para medir tiempo de extraccion

response_api_bachometro = requests.get(URL_BACHOMETRO_HMO)  # Enviamos una solicitud HTTP tipo GET hacia la API

# El formato en que viene la respuesta nos obliga a pasarlo por dos estructuras de datos distintas
# Extraemos la informacion de la respuesta con el metodo JSON y transformamos en lista de Python
df_bachometro = pd.DataFrame(list(response_api_bachometro.json())) # Depositamos la informacion de la lista en un DataFrame

#Almacenamos el contenido del DataFrame en un archivo CSV en el directorio data/raw
df_bachometro.to_csv(os.path.join(STORAGE_PATH,RAW_BACHES_FILENAME))

bachometro_download_timestamp = datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

bachometro_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido

start = time.time() # Iniciamos nuevamente contador para medir tiempo de extraccion

# Enviamos una solicitud HTTP tipo GET para descargar el archivo comprimido del endpoint del sitio web del INEGI
response_agebs = requests.get(URL_AGEBS_HMO, allow_redirects=True)

# Definimos rutas que nos facilitaran el manejo de los archivos a extraer y almacenar
ageb_zip_directory = os.path.join(STORAGE_PATH, AGEBS_ZIP_FILENAME)
ageb_content_directory = os.path.splitext(ageb_zip_directory)[0]

# Almacenamos la carpeta comprimida ZIP
if not os.path.exists(ageb_zip_directory): open(ageb_zip_directory, 'wb').write(response_agebs.content)

# Extraemos los archivos de la carpeta comprimida ZIP
if not os.path.exists(ageb_content_directory):
    with zipfile.ZipFile(ageb_zip_directory, 'r') as zip_ref:
        zip_ref.extractall(path = ageb_content_directory)

# Extraemos los archivos correspondientes unicamente a Hermosillo (discriminando los de otros municipios)
# Para esto se extraen de una subcarpeta que tambien se encuentra comprimida
with zipfile.ZipFile(ageb_content_directory + '/260300001.zip') as zip_ref:
    for file in HMO_AGEB_FILE_LIST:
        if not os.path.exists(ageb_content_directory + '260300001' + file):
            zip_ref.extract('260300001' + file, STORAGE_PATH)

# Eliminamos los archivos residuales (eran parte del comprimido pero no tendran uso alguno en el proyecto)
shutil.rmtree(ageb_content_directory)
os.remove(ageb_zip_directory)

ageb_download_timestamp = datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

ageb_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido

start = time.time() # Iniciamos nuevamente contador para medir tiempo de extraccion

# Definimos rutas que nos facilitaran el manejo de los archivos a extraer y almacenar
socioeconomico_zip_directory = os.path.join(STORAGE_PATH, SOCIOECONOMICO_ZIP_FILENAME)
socioeconomico_content_directory = os.path.splitext(socioeconomico_zip_directory)[0]

# Enviamos una solicitud HTTP tipo GET para descargar el archivo comprimido del endpoint del sitio web del INEGI
response_socioeconomico = requests.get(URL_SOCIOECONOMICO_HMO, allow_redirects=True)

# Almacenamos la carpeta comprimida ZIP
if not os.path.exists(socioeconomico_zip_directory):
    open(socioeconomico_zip_directory, 'wb').write(response_socioeconomico.content)

# Extraemos los archivos de la carpeta comprimida ZIP
with zipfile.ZipFile(socioeconomico_zip_directory) as zip_ref:
    zip_ref.extractall(STORAGE_PATH)

# Subimos el archivo de interes en la jerarquia de directorios
shutil.move(STORAGE_PATH + '/ageb_mza_urbana_26_cpv2020/conjunto_de_datos/conjunto_de_datos_ageb_urbana_26_cpv2020.csv'
            , STORAGE_PATH)

#shutil.move(STORAGE_PATH + '/ageb_mza_urbana_26_cpv2020/diccionario_de_datos/diccionario_datos_ageb_urbana_26_cpv2020.csv'
#            , STORAGE_PATH)

# Eliminamos los archivos residuales (eran parte del comprimido pero no tendran uso alguno en el proyecto)
shutil.rmtree(STORAGE_PATH + '/ageb_mza_urbana_26_cpv2020')
os.remove(socioeconomico_zip_directory)

socioeconomico_download_timestamp = datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

socioeconomico_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido

# Creamos el archivo de texto con la informacion sobre los datos descargados

if os.path.exists(os.path.join(STORAGE_PATH, DATA_DESCRIPTION_FILENAME)):
    # os.remove(os.path.join(STORAGE_PATH, DATA_DESCRIPTION_FILENAME))
    file = open(DATA_DESCRIPTION_FILENAME, "r+")
    file.seek(0)
    file.truncate()

with open(os.path.join(STORAGE_PATH, DATA_DESCRIPTION_FILENAME), "w") as file:
    file.write(DATA_DESCRIPTION_TEMPLATE % (
        URL_BACHOMETRO_HMO,
        bachometro_download_timestamp,
        bachometro_extraction_time,
        URL_AGEBS_HMO,
        ageb_download_timestamp,
        ageb_extraction_time,
        URL_SOCIOECONOMICO_HMO,
        socioeconomico_download_timestamp,
        socioeconomico_extraction_time
    ))