import os # Importamos la libreria "os" para manejo de rutas
import time # Importamos las libreria "time" para medir duraciones
import config # Importamos config.py como modulo para hacer uso de las variables ahi definidas
import tools # Importamos tools.py como modulo para hacer uso de las funciones desarrolladas para el proyecto

# ------ PROCESO DE DESCARGA Y ALMACENAMIENTO ------

# Aseguramos que existan los directorios destino, de lo contrario se generan
tools.check_create_raw_dir(config.RAW_DATA_STORAGE_PATH)

start = time.time() # Iniciamos contador para medir tiempo de extraccion

bachometro_download_timestamp = tools.download_baches_data(
    config.URL_BACHOMETRO_HMO,
    os.path.join(config.RAW_DATA_STORAGE_PATH,config.RAW_BACHES_FILENAME)

)

bachometro_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido

start = time.time() # Iniciamos nuevamente contador para medir tiempo de extraccion

ageb_download_timestamp = tools.download_ageb_data(
    config.URL_AGEBS_HMO,
    config.AGEBS_ZIP_FILENAME,
    config.RAW_DATA_STORAGE_PATH,
    config.HMO_AGEB_FILE_LIST
)

ageb_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido



start = time.time() # Iniciamos nuevamente contador para medir tiempo de extraccion

socioeconomico_download_timestamp = tools.download_se_data(
    config.URL_SOCIOECONOMICO_HMO,
    config.SOCIOECONOMICO_ZIP_FILENAME,
    config.RAW_DATA_STORAGE_PATH
)

socioeconomico_extraction_time = time.time() - start # Calculamos el tiempo de extraccion transcurrido


# Creamos el archivo de texto con la informacion sobre los datos descargados

values = (  config.URL_BACHOMETRO_HMO,
            bachometro_download_timestamp,
            bachometro_extraction_time,
            config.URL_AGEBS_HMO,
            ageb_download_timestamp,
            ageb_extraction_time,
            config.URL_SOCIOECONOMICO_HMO,
            socioeconomico_download_timestamp,
            socioeconomico_extraction_time
        )

tools.fill_template(
    config.RAW_DATA_DOWNLOAD_LOG_TEMPLATE_PATH,
    values,
    os.path.join(config.RAW_DATA_STORAGE_PATH, config.RAW_DATA_DOWNLOAD_LOG_FILENAME))