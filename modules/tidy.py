# Importamos los modulos necesarios para la libreta
import pandas as pd #Importamos el modulo pandas
import os #Importamos el modulo os
import geopandas as gpd #Importamos el modulo geopandas
from shapely.geometry import Point #Importamos el metodo Point del modulo shapely 
import numpy as np # Importamos el modulo numpy

# ------ VARIABLES ESTATICAS DE CONFIGURACION ------

PROCESSED_PATH = "./data/processed"
RAW_PATH = "./data/raw"

# Creamos variables guardando los directorios que utilizaremos en parte de elaboración y guardado
agebs_hermosillo_directory = os.path.join(RAW_PATH, "260300001a.shp")

baches_hermosillo_directory = os.path.join(RAW_PATH, "baches_hmo_2021_2024.csv")

socioeconomico_hermosillo_directory = os.path.join(RAW_PATH, "conjunto_de_datos_ageb_urbana_26_cpv2020.csv")


# ------ PROCESO DE ELABORACION Y GUARDADO DE ARCHIVOS TIDY ------

# Aseguramos que existan los directorios destino, de lo contrario se generan
if not os.path.exists("./data/processed"): os.mkdir("./data/processed")

# Creamos un geopandas de las agebs de hermosillo
agebs_hermosillo = gpd.read_file(agebs_hermosillo_directory)

#En el archivo tidy.ipynb, podemos ver que el crs de las agebs está dada por un crs llamado ccl_itrf92
#Cambiemos el crs a uno mas conocido como el EPSG:4326
agebs_hermosillo.to_crs(epsg=4326, inplace=True)

# Creamos un geopandas de los baches de hermosillo
baches_hermosillo = gpd.read_file(baches_hermosillo_directory)

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
baches_agebs_hermosillo = gpd.sjoin(baches_hermosillo, agebs_hermosillo, how='left', predicate='within')

# Ya casi por terminar tomemos las columans que nos interesan
baches_agebs_hermosillo = baches_agebs_hermosillo[['latitude', 'longitude','CVEGEO', 
                                                   'date', 'neighborhoods', 'description', 'geometry']]


# Por último cambiemos el tipo correcto de columna
baches_agebs_hermosillo['date'] = pd.to_datetime(baches_agebs_hermosillo['date'])
baches_agebs_hermosillo['latitude'] = pd.to_numeric(baches_agebs_hermosillo['latitude'])
baches_agebs_hermosillo['longitude'] = pd.to_numeric(baches_agebs_hermosillo['longitude'])

# Creamos un pandas con los datos socieconomicos de Hermosillo
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
        

#Solamente queda guardas los DataFrame en el directorio /data/processed/
baches_agebs_hermosillo_cvs = os.path.join(PROCESSED_PATH, "baches_agebs_hermosillo.csv")
socioeconomico_hermosillo_csv = os.path.join(PROCESSED_PATH, "socioeconomico_hermosillo.csv")

baches_agebs_hermosillo.to_csv(baches_agebs_hermosillo_cvs, index=False)
socioeconomico_hermosillo.to_csv(socioeconomico_hermosillo_csv, index=False)
