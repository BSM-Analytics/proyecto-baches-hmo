# Diccionario de datos: Censo de Población y Vivienda 2020

Este diccionario se presenta tal como lo proporciona el INEGI.

| Núm. | Indicador | Descripción | Mnemónico | Rangos | Longitud |
|------|-----------|-------------|-----------|--------|----------|
1 | Clave de entidad federativa | Código que identifica a la entidad federativa. El código 00 identifica a los registros con los totales a nivel nacional. | ENTIDAD | 00…32 | 2
2 | Entidad federativa | Nombre oficial de la entidad federativa. | NOM_ENT  | Alfanumérico | 50
3 | Clave de municipio o demarcación territorial | "Código que identifica al municipio o demarcación territorial al interior de una entidad federativa, conforme al Marco Geoestadístico. El código 000 identifica a los registros con los totales a nivel de entidad federativa." | MUN | 000…570 | 3
4 | Municipio o demarcación territorial | Nombre oficial del municipio o demarcación territorial en el caso de la Ciudad de México. | NOM_MUN    | Alfanumérico | 50
5 | Clave de localidad | Código que identifica a la localidad al interior de cada municipio o demarcación territorial conforme al Marco Geoestadístico. El código 0000 identifica a los registros con los totales a nivel de municipio o demarcación territorial. | LOC | 0000…9999 | 4
6 | Localidad | Nombre con el que se reconoce a la localidad dado por la ley o la costumbre. | NOM_LOC  | Alfanumérico | 70
7 | Clave del AGEB | "Clave que identifica al AGEB urbana al interior de una localidad de acuerdo con la desagregación del Marco Geoestadístico." | AGEB  | 001...999; 0...9 o A-P | 4
8 | Clave de manzana | "Clave que identifica a la manzana, al interior de una AGEB, de acuerdo a la desagregación del Marco Geoestadístico." | MZA | 001...999 | 3
