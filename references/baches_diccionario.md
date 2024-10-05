# Diccionario de Datos

Este diccionario describe las columnas del conjunto de datos sobre baches en la ciudad de Hermosillo, Sonora.

| Variable                 | Tipo             | Descripción                                                                     |
|--------------------------|------------------|---------------------------------------------------------------------------------|
|  latitude                |  float           | Latitud geográfica donde se reportó el bache.                                   |
|  longitude               |  float           | Longitud geográfica donde se reportó el bache.                                  |
|  CVEGEO                  |  int  /  NaN     | Código geográfico del área donde se encuentra el bache (puede ser nulo).        |
|  date                    |  datetime        | Fecha en que se reportó el bache.                                               |
|  neighborhoods           |  list[int]       | Código(s) del vecindario(s) donde se encuentra el bache.                        |
|  description             |  string          | Descripción proporcionada por el usuario sobre la ubicación o situación del bache.|
|  geometry                |  POINT           | Coordenadas geográficas representadas como un objeto geométrico tipo POINT.    |