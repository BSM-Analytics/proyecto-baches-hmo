import os # Importamos la libreria "os" para manejo de rutas
import logging # Importamos logging para tener registro de errores en caso de presentarse
import config # Importamos config.py como modulo para hacer uso de las variables ahi definidas
import tools # Importamos tools.py como modulo para hacer uso de las funciones desarrolladas para el proyecto

logging.basicConfig(
    filename="modules/dataset_module.log",
    encoding="utf-8",
    format="{asctime} | {levelname} | {message}",
    style="{",
    datefmt="%d-%m-%Y %H:%M:%S")

# ------ PROCESO DE DESCARGA Y ALMACENAMIENTO ------

try:
    # Aseguramos que existan los directorios destino, de lo contrario se generan
    tools.check_create_raw_dir(config.RAW_DATA_STORAGE_PATH)

    bachometro_download_timestamp,bachometro_extraction_time = tools.download_baches_data(
        config.URL_BACHOMETRO_HMO,
        os.path.join(config.RAW_DATA_STORAGE_PATH,config.RAW_BACHES_FILENAME)

    )

    ageb_download_timestamp, ageb_extraction_time = tools.download_ageb_data(
        config.URL_AGEBS_HMO,
        config.AGEBS_ZIP_FILENAME,
        config.RAW_DATA_STORAGE_PATH,
        config.HMO_AGEB_FILE_LIST
    )

    socioeconomico_download_timestamp,socioeconomico_extraction_time = tools.download_se_data(
        config.URL_SOCIOECONOMICO_HMO,
        config.SOCIOECONOMICO_ZIP_FILENAME,
        config.RAW_DATA_STORAGE_PATH
    )

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

except Exception as e:
    logging.critical(str(e))