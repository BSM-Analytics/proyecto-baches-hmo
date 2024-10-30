# Importamos los modulos necesarios para la libreta
import pandas as pd #Importamos el modulo pandas
import os #Importamos el modulo os
import logging # Importamos logging para tener registro de errores en caso de presentarse
import config # Importamos config.py como modulo para hacer uso de las variables ahi definidas
import tools # Importamos tools.py como modulo para hacer uso de las funciones desarrolladas para el proyecto

logging.basicConfig(
    filename="modules/tidy_module.log",
    encoding="utf-8",
    format="{asctime} | {levelname} | {message}",
    style="{",
    datefmt="%d-%m-%Y %H:%M:%S")

# Creamos variables guardando los directorios que utilizaremos en parte de elaboración y guardado
agebs_hermosillo_directory = os.path.join(config.RAW_DATA_STORAGE_PATH, config.HMO_SHP_FILENAME)
baches_hermosillo_directory = os.path.join(config.RAW_DATA_STORAGE_PATH, config.RAW_BACHES_FILENAME)
socioeconomico_hermosillo_directory = os.path.join(config.RAW_DATA_STORAGE_PATH, config.RAW_SOCIOECONOMICO_FILENAME)
socioeconomico_ageb_hermosillo_directory = os.path.join(config.RAW_DATA_STORAGE_PATH, config.RAW_SOCIOECONOMICO_AGEB_FILENAME)

# ------ PROCESO DE ELABORACION Y GUARDADO DE ARCHIVOS TIDY ------

try:

    # Aseguramos que existan los directorios destino, de lo contrario se generan
    tools.check_create_tidy_dir(config.TIDY_DATA_STORAGE_PATH)

    # Hacemos JOIN a los dataset de baches y AGEB por medio de sus AGEB/Latitud/Longitud
    baches_agebs_hermosillo, join_baches_ageb_time = tools.join_baches_agebs_data(agebs_hermosillo_directory,baches_hermosillo_directory)

    # Damos el formato tidy al dataset conjunto de AGEBS y baches
    baches_agebs_hermosillo, tidy_baches_agebs_time = tools.tidy_baches_agebs_data(baches_agebs_hermosillo)

    # Hacemos MERGE a los datos de socieconomigo ageb y ageb por medio de sus AGEB/CVEGEO
    socioeconomico_ageb_hermosillo, merge_socioeconomico_ageb_time = tools.merge_se_agebs_data(agebs_hermosillo_directory,socioeconomico_ageb_hermosillo_directory)

    # Damos el formato tidy al dataset de informacion siocieconomica ageb
    socioeconomico_ageb_hermosillo, tidy_socioeconomico_ageb_time = tools.tidy_se_ageb_data(socioeconomico_ageb_hermosillo)

    # Damos el formato tidy al dataset de informacion socioeconomica
    socioeconomico_hermosillo, tidy_socioeconomico_time = tools.tidy_se_data(socioeconomico_hermosillo_directory)

    # Solamente queda guardar los DataFrame en el directorio /data/processed/
    baches_agebs_hermosillo_cvs = os.path.join(config.TIDY_DATA_STORAGE_PATH, config.TIDY_BACHE_AGEB_DATA_FILENAME)
    socioeconomico_hermosillo_csv = os.path.join(config.TIDY_DATA_STORAGE_PATH, config.TIDY_SOCIOECONOMICO_DATA_FILENAME)
    socioeconomico_ageb_hermosillo_csv = os.path.join(config.TIDY_DATA_STORAGE_PATH, config.TIDY_SOCIOECONOMICO_AGEB_DATA_FILENAME)
    baches_agebs_hermosillo.to_csv(baches_agebs_hermosillo_cvs, index=False)
    socioeconomico_hermosillo.to_csv(socioeconomico_hermosillo_csv, index=False)
    socioeconomico_ageb_hermosillo.to_csv(socioeconomico_ageb_hermosillo_csv, index=False)

    values = (
        join_baches_ageb_time,
        tidy_baches_agebs_time,
        tidy_socioeconomico_time,
        tidy_socioeconomico_ageb_time
    )

    tools.fill_template(
    config.TIDY_DATA_DOWNLOAD_LOG_TEMPLATE_PATH,
    values,
    os.path.join(config.TIDY_DATA_STORAGE_PATH, config.TIDY_DATA_DOWNLOAD_LOG_FILENAME))

except Exception as e:
    logging.critical(str(e))