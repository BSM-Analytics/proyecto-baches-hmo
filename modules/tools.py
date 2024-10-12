import requests  # Importamos la libreria "requests" para las solicitudes HTTP hacia las APIs
import pandas as pd # Importamos la libreria "pandas" para el manejo en DataFrames y exportacion de los datos
import shutil # Importamos la libreria "shutils" para manejo de archivos y directorios
import zipfile # Importamos la libreria "zipfile" para descomprimir carpetas comprimidas
import os # Importamos la libreria "os" para manejo de rutas
import time, datetime # Importamos las libreria "time" y "datetime" para generar timestamps y medir duraciones
import requests

# Funciones para facilitar las tareas ejecutadas por el resto de los scripts para el ETL

def fill_template(template_file_path:str, values:tuple, destination_file_path:str):

    """
    DOCSTRING PENDING
    """

    if os.path.exists(destination_file_path):
        file = open(destination_file_path, "r+")
        file.seek(0)
        file.truncate()

    with open(destination_file_path, "w") as file:
        with open(template_file_path,"r") as template:
            str_template = template.read()
            file.write(str_template % values)


def download_baches_data(api_url:str, destination_filepath:str):

    """
    DOCSTRING PENDING
    """

    response_api_bachometro = requests.get(api_url)  # Enviamos una solicitud HTTP tipo GET hacia la API

    # El formato en que viene la respuesta nos obliga a pasarlo por dos estructuras de datos distintas
    # Extraemos la informacion de la respuesta con el metodo JSON y transformamos en lista de Python
    df_bachometro = pd.DataFrame(list(response_api_bachometro.json())) # Depositamos la informacion de la lista en un DataFrame

    #Almacenamos el contenido del DataFrame en un archivo CSV en el directorio data/raw
    df_bachometro.to_csv(destination_filepath)

    return datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

def download_ageb_data(file_url:str, zip_filename:str, storage_path:str, ageb_list:str):

    """
    DOCSTRING PENDING
    """

    # Enviamos una solicitud HTTP tipo GET para descargar el archivo comprimido del endpoint del sitio web del INEGI
    response_agebs = requests.get(file_url, allow_redirects=True)

    # Definimos rutas que nos facilitaran el manejo de los archivos a extraer y almacenar
    ageb_zip_directory = os.path.join(storage_path, zip_filename)
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
        for file in ageb_list:
            if not os.path.exists(ageb_content_directory + '260300001' + file):
                zip_ref.extract('260300001' + file, storage_path)

    # Eliminamos los archivos residuales (eran parte del comprimido pero no tendran uso alguno en el proyecto)
    shutil.rmtree(ageb_content_directory)
    os.remove(ageb_zip_directory)

    return datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

def download_se_data(file_url:str, zip_filename:str, storage_path:str):

    """
    DOCSTRING PENDING
    """

    # Definimos rutas que nos facilitaran el manejo de los archivos a extraer y almacenar
    socioeconomico_zip_directory = os.path.join(storage_path, zip_filename)
    socioeconomico_content_directory = os.path.splitext(socioeconomico_zip_directory)[0]

    # Enviamos una solicitud HTTP tipo GET para descargar el archivo comprimido del endpoint del sitio web del INEGI
    response_socioeconomico = requests.get(file_url, allow_redirects=True)

    # Almacenamos la carpeta comprimida ZIP
    if not os.path.exists(socioeconomico_zip_directory):
        open(socioeconomico_zip_directory, 'wb').write(response_socioeconomico.content)

    # Extraemos los archivos de la carpeta comprimida ZIP
    with zipfile.ZipFile(socioeconomico_zip_directory) as zip_ref:
        zip_ref.extractall(storage_path)

    # Subimos el archivo de interes en la jerarquia de directorios
    shutil.move(storage_path + '/ageb_mza_urbana_26_cpv2020/conjunto_de_datos/conjunto_de_datos_ageb_urbana_26_cpv2020.csv'
                , storage_path)

    #shutil.move(RAW_DATA_STORAGE_PATH + '/ageb_mza_urbana_26_cpv2020/diccionario_de_datos/diccionario_datos_ageb_urbana_26_cpv2020.csv'
    #            , RAW_DATA_STORAGE_PATH)

    # Eliminamos los archivos residuales (eran parte del comprimido pero no tendran uso alguno en el proyecto)
    shutil.rmtree(storage_path + '/ageb_mza_urbana_26_cpv2020')
    os.remove(socioeconomico_zip_directory)

    return datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos


def check_create_raw_dir(path:str):

    """
    DOCSTRING PENDING
    """

    if not os.path.exists("./data"): os.mkdir("./data")
    if not os.path.exists("./data/raw"): os.mkdir("./data/raw")


"""
def join_baches_agebs_data():


def tidy_baches_agebs_data():


def tidy_se_data():
"""