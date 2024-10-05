| Variable      | Tipo          | Descripción                                     | Valores Posibles             |
| ------------- | ------------- | ----------------------------------------------- | ---------------------------- |
|latitude       | float         | Latitud de la ubicación del reporte             | -90.0 a 90.0                 |
|longitude      | float         | Longitud de la ubicación del reporte            | -180.0 a 180.0               |
|date           | string        | Fecha en que se realizó el reporte              | Formato: YYYY-MM-DD          |
|neighborhoods  | string        | Identificador de los vecindarios relacionados   | Lista de IDs de vecindarios  |
|material       | int           | Tipo de material utilizado en la calle (código) | 1=asfalto, 2=concreto        |
|description    | string        | Descripción del problema reportado              | Texto libre                  |
|id             | int           | Identificador único del reporte                 | Número entero                |