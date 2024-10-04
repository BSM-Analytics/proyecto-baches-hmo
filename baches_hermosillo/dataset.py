import requests  # Importamos la libreria "requests" para las solicitudes HTTP hacia las APIs
import pandas as pd # Importamos la libreria "pandas" para el manejo en DataFrames y exportacion de los datos
import shutil # Importamos la libreria "shutils" para manejo de archivos y directorios
import zipfile # Importamos la libreria "zipfile" para descomprimir carpetas comprimidas
import os # Importamos la libreria "os" para manejo de rutas

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

# ------ PROCESO DE DESCARGA Y ALMACENAMIENTO ------

# Aseguramos que existan los directorios destino, de lo contrario se generan
if not os.path.exists("./data"): os.mkdir("./data")
if not os.path.exists("./data/raw"): os.mkdir("./data/raw")

response_api_bachometro = requests.get(URL_BACHOMETRO_HMO)  # Enviamos una solicitud HTTP tipo GET hacia la API

# El formato en que viene la respuesta nos obliga a pasarlo por dos estructuras de datos distintas
# Extraemos la informacion de la respuesta con el metodo JSON y transformamos en lista de Python
df_bachometro = pd.DataFrame(list(response_api_bachometro.json())) # Depositamos la informacion de la lista en un DataFrame

#Almacenamos el contenido del DataFrame en un archivo CSV en el directorio data/raw
df_bachometro.to_csv(os.path.join(STORAGE_PATH,RAW_BACHES_FILENAME))

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