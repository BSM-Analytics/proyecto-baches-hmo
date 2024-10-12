# Rutas default para almacenamiento de datos en sus distintas etapas
RAW_DATA_STORAGE_PATH = "./data/raw"
TIDY_DATA_STORAGE_PATH = "./data/tidying"

# Endpoint a AJAX API del Bachometro de Hermosillo (encontrado monitoreando el trafico en el sitio web)
URL_BACHOMETRO_HMO = "https://bachometro.hermosillo.gob.mx/mapa/ajax"
RAW_BACHES_FILENAME = "baches_hmo_2021_2024.csv"

# Endpoint para descarga de archivo SHP y complementos de AGEBS de Hermosillo en sitio web INEGI
URL_AGEBS_HMO = "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/urbana/SHP_2/Sonora/702825317744_s.zip"
AGEBS_ZIP_FILENAME = "agebs_hmo.zip"
HMO_AGEB_FILE_LIST = ['.html', 'a.dbf','a.prj','a.shp', 'a.shp.xml', 'a.dbf', 'a.shx']
HMO_SHP_FILENAME = "260300001a.shp"

# Endpoint para descarga de archivo CSV con datos Socioeconomicos (Rezago Social) de Hermosillo en sitio web INEGI
URL_SOCIOECONOMICO_HMO = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/ageb_manzana/ageb_mza_urbana_26_cpv2020_csv.zip"
SOCIOECONOMICO_ZIP_FILENAME = "socioeconomico_2020.zip"
RAW_SOCIOECONOMICO_FILENAME = "conjunto_de_datos_ageb_urbana_26_cpv2020.csv"

# Informacion para generacion de archivo TXT con informacion de datos
RAW_DATA_DOWNLOAD_LOG_TEMPLATE_PATH = "modules/templates/data_download_log_template.txt"
RAW_DATA_DOWNLOAD_LOG_FILENAME = "raw_data_download_log.txt"

# Nombres para archivos de datos en formato tidy
TIDY_BACHE_AGEB_DATA_FILENAME = "tidy_baches_agebs_hmo.csv"
TIDY_SOCIOECONOMICO_DATA_FILENAME = "tidy_socioeconomico_hermosillo.csv"

# Informacion para generacion de archivo TXT con informacion de datos
TIDY_DATA_DOWNLOAD_LOG_TEMPLATE_PATH = "modules/templates/data_tidying_log_template.txt"
TIDY_DATA_DOWNLOAD_LOG_FILENAME = "data_tidying_log.txt"