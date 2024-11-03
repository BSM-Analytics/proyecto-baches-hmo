import requests  # Importamos la libreria "requests" para las solicitudes HTTP hacia las APIs
import pandas as pd # Importamos la libreria "pandas" para el manejo en DataFrames y exportacion de los datos
import shutil # Importamos la libreria "shutils" para manejo de archivos y directorios
import zipfile # Importamos la libreria "zipfile" para descomprimir carpetas comprimidas
import os # Importamos la libreria "os" para manejo de rutas
import time, datetime # Importamos las libreria "time" y "datetime" para generar timestamps y medir duraciones
import geopandas as gpd # Importamos el modulo geopandas para manejo de datos georeferenciados
from functools import wraps # Importamos la funcion wraps del paquete functools para medir tiempo con decoradores
from shapely.geometry import Point # Importamos el metodo Point del modulo shapely

# Funciones para facilitar las tareas ejecutadas por el resto de los scripts para el ETL

def exec_time(function):
    @wraps(function)
    def exec_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        wrapped_func_result = function(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        return wrapped_func_result, elapsed_time
    return exec_time_wrapper

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

@exec_time
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

@exec_time
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

@exec_time
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

@exec_time
def download_se_ageb_data(file_url:str, filename:str, storage_path:str):

    """
    DOCSTRING PENDING
    file_url = url
    filename = nombre que deseo pornerle al archivo
    storage_path = direccion de donde se va a guardar el archvio
    """

    # Definimos rutas que nos facilitaran el manejo de los archivos a extraer y almacenar
    socioeconomico_directory = os.path.join(storage_path, filename)

    # Enviamos una solicitud HTTP tipo GET para descargar el archivo comprimido del endpoint del sitio web del INEGI
    response_socioeconomico = requests.get(file_url, allow_redirects=True)

    # Almacenamos la carpeta comprimida ZIP
    if not os.path.exists(socioeconomico_directory):
        open(socioeconomico_directory, 'wb').write(response_socioeconomico.content)


    return datetime.datetime.now() # Obtenemos timestamp de finalizacion de extraccion de datos

def check_create_raw_dir(path:str):

    """
    DOCSTRING PENDING
    """

    if not os.path.exists("./data"): os.mkdir("./data")
    if not os.path.exists("./data/raw"): os.mkdir("./data/raw")

def check_create_tidy_dir(path:str):

    """
    DOCSTRING PENDING
    """

    if not os.path.exists("./data"): os.mkdir("./data")
    if not os.path.exists("./data/processed"): os.mkdir("./data/processed")

@exec_time
def join_baches_agebs_data(agebs_hmo_dir:str, baches_hmo_dir:str):

    # Creamos un geopandas de las agebs de hermosillo
    agebs_hermosillo = gpd.read_file(agebs_hmo_dir)

    #En el archivo tidy.ipynb, podemos ver que el crs de las agebs está dada por un crs llamado ccl_itrf92
    #Cambiemos el crs a uno mas conocido como el EPSG:4326
    agebs_hermosillo.to_crs(epsg=4326, inplace=True)

    # Creamos un geopandas de los baches de hermosillo
    baches_hermosillo = gpd.read_file(baches_hmo_dir)

    """ Aplicaremos el metodo Point para hacer una columna que sea de tipo geometry,
    se la aplicaremos a las columnas longitude y latitude """
    baches_hermosillo['geometry'] = baches_hermosillo  \
            .apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

    # Convertimos a baches hermosillo a un GeoDataFrame
    baches_hermosillo = gpd.GeoDataFrame(baches_hermosillo, geometry='geometry')

    # Fijamos el crs en 4326 para tener el mismo que el GeoDataFrame de agebs_hermosillo
    baches_hermosillo.set_crs(epsg=4326, inplace=True)

    """Usando el metodo sjoin pordemos unir ambos GeoDataFrame de modo izquierdo donde vea si los puntos
    de la columna geometry de baches_hermosillo, este dentro de los polinomios de agebs_hermosillo"""
    return gpd.sjoin(baches_hermosillo, agebs_hermosillo, how='left', predicate='within')

@exec_time
def tidy_baches_agebs_data(baches_agebs_hermosillo):

    # Ya casi por terminar tomemos las columans que nos interesan
    baches_agebs_hermosillo = baches_agebs_hermosillo[['latitude', 'longitude','CVEGEO',
                                                    'date', 'neighborhoods', 'description', 'geometry']]

    # Por último cambiemos el tipo correcto de columna
    baches_agebs_hermosillo['date'] = pd.to_datetime(baches_agebs_hermosillo['date'])
    baches_agebs_hermosillo['latitude'] = pd.to_numeric(baches_agebs_hermosillo['latitude'])
    baches_agebs_hermosillo['longitude'] = pd.to_numeric(baches_agebs_hermosillo['longitude'])
    #baches_agebs_hermosillo['geometry'] = baches_agebs_hermosillo['geometry'].apply(lambda x: x.wkt)

    return baches_agebs_hermosillo

@exec_time
def tidy_se_data(socioeconomico_hermosillo_directory:str):
    # Creamos un DataFrame de pandas con los datos socieconomicos de Hermosillo
    socioeconomico_hermosillo = pd.read_csv(socioeconomico_hermosillo_directory)

    # Lo que haremos en socioeconomico hermosillo sera solamente escribir el tipo de cada columna correctamente
    columnas_categoricas = ['ENTIDAD', 'MUN', 'LOC', 'AGEB', 'MZA']
    columnas_objeto = ['NOM_ENT', 'NOM_MUN', 'NOM_LOC']
    columnas_int = socioeconomico_hermosillo.columns.difference(columnas_categoricas + columnas_objeto)

    socioeconomico_hermosillo[columnas_categoricas] = \
                        socioeconomico_hermosillo[columnas_categoricas].astype('category')

    socioeconomico_hermosillo[columnas_objeto] = \
                        socioeconomico_hermosillo[columnas_objeto].astype('object')

    for col in columnas_int:
        socioeconomico_hermosillo[col] = pd.to_numeric(socioeconomico_hermosillo[col], errors='coerce')

    return socioeconomico_hermosillo[socioeconomico_hermosillo['NOM_LOC']== 'Hermosillo']


@exec_time
def merge_se_agebs_data(agebs_hmo_dir:str, se_agebs_hmo_dir:str):

    # Creamos un geopandas de las agebs de hermosillo
    agebs_hermosillo = gpd.read_file(agebs_hmo_dir)
    agebs_hermosillo.CVEGEO = agebs_hermosillo.CVEGEO.str[-4:]
    
    # Creamos un pandas con los datos de rezago social
    socioeconomico_agebs_hermosillo = pd.read_excel(se_agebs_hmo_dir)
    
    # Regresamos un DataFrame que nos haga un merge entre los datos que nos interesan
    return agebs_hermosillo.merge(socioeconomico_agebs_hermosillo, left_on='CVEGEO', right_on='AGEB')



@exec_time
def tidy_se_ageb_data(se_ageb_hermosillo:str):
    se_ageb_hermosillo['GM_2020'] = se_ageb_hermosillo['GM_2020'].astype('category')
    # Lo que haremos en socioeconomico hermosillo sera solamente escribir el tipo de cada columna correctamente
    socioeconomico_ageb_hermosillo = se_ageb_hermosillo[['CVEGEO','POB_TOT','IM_2020','GM_2020','IMN_2020','geometry']]
    #socioeconomico_ageb_hermosillo['geometry'] = socioeconomico_ageb_hermosillo['geometry'].apply(lambda x: x.wkt)
    return socioeconomico_ageb_hermosillo
