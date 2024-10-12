<banner float="left">
  <img src="images/readme_banner.png" width="100%" />
</banner>

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

### Construido con:

[![Python][python-shield]][python-url]
[![HTML5][html5-shield]][html5-url]
[![CSS][css-shield]][css-url]
[![Markdown][md-shield]][md-url]
[![Git][git-shield]][git-url]
[![Github][github-shield]][github-url]

[![Jupyter Notebooks][jupyter-shield]][jupyter-url]
[![Python][ccds-shield]][ccds-url]

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Acerca del Proyecto :dart:
</summary>
<br>

Buscamos determinar si existe una relacion entre la presencia y/o **permanencia de baches** en las calles versus las **caracteristicas socioeconomicas**, para **distintas zonas** del municipio de **Hermosillo, Sonora**.
<br />

Consideramos que los resultados serian de **especial interes** para todo **ciudadano** que reside en el municipio de Hermosillo,
Sonora, sin embargo tambien podrian servir de referencia a las **autoridades locales** e inclusive a habitantes de otras localidades de Mexico.

<img src="images/readme_astronaut.gif" width="300"/>
</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Estructura del Proyecto :file_folder:
</summary>
<br>

```sh
├── modules  <- Codigo fuente del proyecto
│   │
│   ├── __init__.py    <- Convierte el contenido de la carpeta modules en un modulo de Python
│   │
│   ├── dataset.py     <- Script para descarga de datos
│   │
│   ├── tidying.py     <- Script para procesar datos crudos y darles un formato tidy
│   │
│   ├── tools.py       <- Archivo con funciones desarrolladas para el proyecto
│   │
│   ├── config.py      <- Archivo para depositar configuraciones y variables
│   │
│   └── templates      <- El directorio con los datos en formato tidy
│       │
│       ├── data_download_log_template  <- Plantilla para bitacora de descarga de datos
│       │
│       └── data_tidying_log_template   <- Plantilla para bitacora de procesamiento de datos a formato tidy
│
├── data
│   ├── raw            <- El directorio con datos crudos - originales e inmutables
│   │
│   └── processed      <- El directorio con los datos en formato tidy
│
├── README.md          <- El README principal para desarrolladores que usaran el proyecto
│
├── Makefile           <- Makefile con comandos que facilitan el uso del proyecto
│
├── references         <- Diccionarios de datos, manuales, y otro material explicativo
│   │
│   ├── raw     <- El directorio con los diccionarios de datos crudos
│   │   │
│   │   ├── baches_raw_diccionario.md  <- Diccionario Datos Baches crudos
│   │   │
│   │   └── socioeconomico_2020_raw_diccionario.md   <- Diccionario Datos SE crudos
│   │
│   └── processed     <- El directorio con los diccionarios de datos en formato tidy
│       │
│       ├── baches_processed_diccionario.md  <- Diccionario Datos Baches/AGEB Tidy
│       │
│       └── socioeconomico_2020_processed_diccionario.md   <- Diccionario Datos SE Tidy
│
├── reports            <- Reportes de analisis (HTML, PDF, LaTeX, etc.)
│   │
│   ├── baches_report.html          <- Reporte EDA sobre datos de baches HMO
│   │
│   ├── hmo_ec_2020_report.html     <- Reporte EDA sobre datos socioeconomicos de HMO
│   │
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- Archivo que contiene los requerimientos (dependencias) para crear
│                         el entorno virtual. Para este proyecto se genero con
│                         "pip3 freeze > requirements.txt"
│
├── notebooks          <- Jupyter Notebooks utilizados unicamente, de momento, para pruebas
│
├── LICENSE            <- Licencia Open-Source del MIT adaptada para el proyecto
│
├── docs               <- Proyecto default de mkdocs
│
├── models             <- Directorio destinado a modelos - Temporalmente sin uso
│
├── pyproject.toml     <- Archivo de configuracion de proyecto con metadata del
│                         paquete/modulo baches_hermosillo y configuracion para
│                         otras herramientas e.g. black (formato)
│
└── setup.cfg          <- Archivo de configuracion para flake8
```
</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Guia de Uso :notebook:
</summary>

<details>

<summary>

#### Clonando el Repositorio :small_red_triangle_down:
</summary>
<br>

1. Desde una terminal, navegar hasta el directorio donde se desea clonar el repositorio
    ```sh
    cd "<ruta_del_directorio>"
    ```
2. Clonar el repositorio
    ```sh
    git clone https://github.com/MCD-IdC-BSM/proyecto-baches-hmo.git
    ```
</details>



<details>
<summary>

#### Con Python :snake:
</summary>
<br>

<details>
<summary>

#### Creando el Entorno Virtual
</summary>
<br>

1.  Desde una terminal, navegar hasta el directorio donde se clono el repositorio
    ```sh
    cd "<ruta_del_directorio_con_respositorio_clonado>"
    ```
2.  Crear un entorno virtual con las herramientas nativas de Python (venv -> virtual env)
    NOTA: Tambien puedes crearlo con conda u otras herramientas de tu preferencia
    ```sh
    python3 -m venv <nombre_del_entorno>
    ```
3.  Activar el entorno virtual
    ```sh
    source activate <nombre_del_entorno>
    ```
4.  Instalar las dependencias del proyecto. Estas se encuentran en el documento ***requirements.txt***
    ```sh
    pip3 install requirements.txt
    ```
5.  Opcional: Puedes verificar que se hayan instalado los paquetes utilizando la funcion ***list*** de ***pip***
    ```sh
    pip3 list
    ```
</details>
<br>

<details>
<summary>

#### Descargando los Datos
</summary>
<br>

1.  Desde una terminal, estando ubicado en el directorio raiz del proyecto, navegar hacia el directorio ***modules***
    ```sh
    cd modules
    ```
2.  Ejecutar el script de Python denominado ***dataset.py***. Este descargara todos los datos a la carpeta ***data/raw***
    ```sh
    python3 dataset.py
    ```
3.  Opcional: Verificar que se hayan descargado los datos a la carpeta ***data/raw***
    ```sh
    ls -d ./data/raw
    ```
</details>
<br>

<details>
<summary>

#### Procesando los Datos a Formato Tidy
</summary>
<br>

1.  Desde una terminal, estando ubicado en el directorio raiz del proyecto, navegar hacia el directorio ***modules***
    ```sh
    cd modules
    ```
2.  Ejecutar el script de Python denominado ***tidy.py***. Esto procesara todos los datos ubicados en
    ***data/raw*** y generara los conjuntos de datos tidy en la carpeta ***data/processed***
    ```sh
    python3 tidy.py
    ```
3.  Opcional: Verificar que se hayan descargado los datos a la carpeta ***data/processed***
    ```sh
    ls -d ./data/processed
    ```
</details>
</details>

<details>
<summary>

#### Con Make :arrow_right:
</summary>
<br>

1. Se puede ejecutar el pipeline completo con el comando:
    ```sh
    make execute_full_pipeline
    ```
2. Para ejecutar el pipeline por cada una de sus etapas, se puede utilizar los siguientes comandos:
    ```sh
    make create_venv
    ```
    ```sh
    make activate_venv
    ```
    ```sh
    make install_venv_requirements
    ```
    ```sh
    make download_data
    ```
    ```sh
    make tidy_data
    ```
</details>

</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### EDAs :bar_chart:
</summary>
<br>

1. [Reporte Datos Baches](https://mcd-idc-bsm.github.io/proyecto-baches-hmo/reports/baches_report.html)
2. [Reporte Datos Socioeconomicos](https://mcd-idc-bsm.github.io/proyecto-baches-hmo/reports/hmo_ec_2020_report.html)
</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Fuentes :information_source:
</summary>
<br>

1. [API del Sitio Web del Bachometro del Ayuntamiento de Hermosillo](https://bachometro.hermosillo.gob.mx/)
2. [AGEBS INEGI Hermosillo (2021)](https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/urbana/SHP_2/Sonora/702825317744_s.zip)
3. [Indicadores Socioeconomicos INEGI Hermosillo (2020)](https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/ageb_manzana/ageb_mza_urbana_26_cpv2020_csv.zip)
</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Licenciamiento :scroll:
</summary>
<br>

Distribuido bajo la licencia del MIT. Para mas informacion consulte el documento [LICENSE](LICENSE).
</details>

<div style="width: 100%;">
  <img src="images/sep_line.svg" style="width: 100%;" alt="sep_line">
</div>

<details>
<summary>

### Contacto :mailbox_with_mail:
</summary>
<br>

#### Desarrolladores: :keyboard:

* **Jesus Solis |** Email: jesolis_14@hotmail.com **|** [LinkedIn JMSD](https://www.linkedin.com/in/jesolis14/)
* **Sebastian Browarski |** Email: sebas.browar@gmail.com
* **Fernando Martinez |** Email: lfmartinezmendoza@gmail.com **|** [LinkedIn LFMM](www.linkedin.com/in/lf-mm)
</details>

[contributors-shield]: https://img.shields.io/github/contributors/MCD-IdC-BSM/proyecto-baches-hmo.svg?style=for-the-badge
[contributors-url]: https://github.com/MCD-IdC-BSM/proyecto-baches-hmo/graphs/contributors

[license-shield]: https://img.shields.io/github/license/MCD-IdC-BSM/proyecto-baches-hmo.svg?style=for-the-badge
[license-url]: https://github.com/MCD-IdC-BSM/proyecto-baches-hmo/blob/master/LICENSE.txt

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/

[html5-shield]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[html5-url]: https://html.spec.whatwg.org/multipage/

[css-shield]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[css-url]: https://www.w3.org/Style/CSS/Overview.en.html

[md-shield]: https://img.shields.io/badge/Markdown-000?style=for-the-badge&logo=markdown
[md-url]: https://www.markdownguide.org/

[git-shield]: https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white
[git-url]: https://git-scm.com/

[github-shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/

[jupyter-shield]: https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter
[jupyter-url]: https://jupyter.org/

[ccds-shield]: https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter
[ccds-url]: https://cookiecutter-data-science.drivendata.org/