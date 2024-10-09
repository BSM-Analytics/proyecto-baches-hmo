# Diccionario de Datos: Baches (Processed)

Este diccionario describe las variables del conjunto de datos procesado sobre reportes de baches en Hermosillo, Sonora.

| Variable        | Tipo             | Descripción                                                                         |
|-----------------|------------------|-------------------------------------------------------------------------------------|
|  latitude       |  float           | Latitud geográfica donde se reportó el bache.                                       |
|  longitude      |  float           | Longitud geográfica donde se reportó el bache.                                      |
|  CVEGEO         |  string / NaN    | Código geográfico del área donde se encuentra el bache (puede ser nulo).            |
|  date           |  datetime        |  Fecha en la que se realizó el reporte del bache en formato YYYY-MM-DD.             |
|  neighborhoods  |  string          | Código(s) del vecindario(s) donde se encuentra el bache.                            |
|  description    |  string          | Descripción proporcionada por el usuario sobre la ubicación o situación del bache.  |
|  geometry       |  geometry        | Coordenadas geográficas representadas como un objeto geométrico tipo POINT.         |