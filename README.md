![banner](images/readme_banner.png)

Integrantes:

Sebastian Browarski Ruiz [a219203551]
Jesus Manuel Solis Duran [aXXXXXXXXX]
Luis Fernando Martinez Mendoza [a224230121]

------------------------------------------------------------------------------------------------

La pregunta que buscaremos responder es: ¿Existe una relacion entre la cantidad de baches no atendidos en una zona y el nivel socio-economico predominante de la poblacion en dicha zona?

![astronaut](images/readme_astronaut.gif)

El producto de datos final esta destinado a: Toda la poblacion de Hermosillo.

Nuestras fuentes primarias de informacion son:

API del Sitio Web del Bachometro del Ayuntamiento de Hermosillo: https://bachometro.hermosillo.gob.mx/

Datos de ENOE del INEGI: https://www.inegi.org.mx/programas/enoe/15ymas/#datos_abiertos

Los datos cumplen con los criterios de:

Series de Tiempo: OK? (Si contamos con datos para varios años, falta concretar ideas)

Georeferenciada: OK

Cualitativa & Cuantitativa: OK

Datos en Texto: OK

------------------------------------------------------------------------------------------------

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
