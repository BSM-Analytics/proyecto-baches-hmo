<style>
.hr1 {
    border: 0;
    height: 1px;
    background-image: linear-gradient(to right, #afa9a3, #616165, #fc7e4f);
}
</style>

<banner float="left">
  <img src="images/readme_banner.png" width="650" />
  <img src="images/readme_astronaut.gif" width="300" />
</banner>

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

Sebastian Browarski Ruiz [a219203551]   |   Jesus Manuel Solis Duran [a212211288]   |  Luis Fernando Martinez Mendoza [a224230121]

<hr class="hr1" />

<details>
<summary>Acerca del Proyecto</summary>
<br>
Buscamos determinar si existe una relacion entre la presencia y/o permanencia de baches en las calles versus las caracteristicas socioeconomicas, para distintas zonas del municipio de Hermosillo, Sonora.

Consideramos que los resultados serian de especial interes para todo aquel que reside en el municipio de Hermosillo,
Sonora, sin embargo tambien podrian servir de referencia para habitantes de otras localidades de Mexico.
</details>

<hr class="hr1" />

<details>
<summary>Estructura del Proyecto</summary>
<br>
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         baches_hermosillo and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── baches_hermosillo   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes baches_hermosillo a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
</details>

<hr class="hr1" />

<details>
<summary>Guia de Uso</summary>
<br>
<details>
<summary>Clonando el Repositorio</summary>
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
<br>
<details>
<summary>Creando el Entorno Virtual</summary>
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
<summary>Descargando los Datos</summary>
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
<summary>Procesando los Datos a Formato Tidy</summary>
<br>

1.  Desde una terminal, estando ubicado en el directorio raiz del proyecto, navegar hacia el directorio ***modules***
    ```sh
    cd modules
    ```
2.  Abrir la herramienta de Jupyter Notebook. Esto abrira una IDE en el navegador predeterminado.
    ```sh
    jupyter notebook
    ```
3.  Abrir el notebook ***tidy.ipynb*** desde el menu Archivo/File en la IDE

4.  Ejecutar todas las celdas del notebook ***tidy.ipynb***. Esto procesara todos los datos ubicados en ***data/raw*** y
    generara los conjuntos de datos tidy en la carpeta ***data/processed***

5.  Opcional: Verificar que se hayan descargado los datos a la carpeta ***data/processed***
    ```sh
    ls -d ./data/processed
    ```
</details>
</details>

<hr class="hr1" />

<details>
<summary>Mini-EDA</summary>
<br>
    Puedes ver el EDA de baches haciendo click en el url: https://mcd-idc-bsm.github.io/proyecto-baches-hmo/reports/baches_report.html.
</details>

<hr class="hr1" />

<details>
<summary>Fuentes</summary>
<br>

1. [API del Sitio Web del Bachometro del Ayuntamiento de Hermosillo](https://bachometro.hermosillo.gob.mx/)
2. [AGEBS INEGI Hermosillo (2021)](https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/urbana/SHP_2/Sonora/702825317744_s.zip)
3. [Indicadores Socioeconomicos INEGI Hermosillo (2020)](https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/ageb_manzana/ageb_mza_urbana_26_cpv2020_csv.zip)


</details>

<hr class="hr1" />

<details>
<summary>Tecnologia & Herramientas</summary>
<br>

[![Python][python-shield]][python-url]
[![Jupyter Notebooks][jupyter-shield]][jupyter-url]
[![Python][ccds-shield]][ccds-url]
</details>

<hr class="hr1" />

<details>
<summary>Licenciamiento</summary>
<br>
Distribuido bajo la licencia del MIT. Para mas informacion consulte el documento LICENSE.
</details>

<hr class="hr1" />

<details>
<summary>Contacto</summary>
<br>
Desarrolladores:

* Jesus Solis | Email: jesolis_14@hotmail.com | [LinkedIn JMSD](https://www.linkedin.com/in/jesolis14/)
* Sebastian Browarski | Email: sebas.browar@gmail.com
* Fernando Martinez | Email: lfmartinezmendoza@gmail.com | [LinkedIn LFMM](www.linkedin.com/in/lf-mm)
</details>

[contributors-shield]: https://img.shields.io/github/contributors/MCD-IdC-BSM/proyecto-baches-hmo.svg?style=for-the-badge
[contributors-url]: https://github.com/MCD-IdC-BSM/proyecto-baches-hmo/graphs/contributors

[license-shield]: https://img.shields.io/github/license/MCD-IdC-BSM/proyecto-baches-hmo.svg?style=for-the-badge
[license-url]: https://github.com/MCD-IdC-BSM/proyecto-baches-hmo/blob/master/LICENSE.txt

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/

[jupyter-shield]: https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter
[jupyter-url]: https://jupyter.org/

[ccds-shield]: https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter
[ccds-url]: https://cookiecutter-data-science.drivendata.org/