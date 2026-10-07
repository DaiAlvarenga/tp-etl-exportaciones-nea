# Pipeline ETL de exportaciones del NEA

## Qué hace el pipeline

- **Extract:** El pipeline se conecta a una API del Estado (datos.gob.ar, con datos del INDEC) desde el cual descarga datos relacionados a las exportaciones de Chaco, Corrientes, Formosa y Misiones entre 1993 y 2024, detallando el país de destino y el rubro de los productos que se exportan. Guarda los datos en 8 archivos JSON.
- **Transform:** En la API cada país es una columna; el pipeline lo reordena para que haya una fila por año, provincia y país de destino. Después se agregan columnas con la zona del país de destino, el porcentaje sobre el total, la variación respecto al año anterior y si el destino está entre los 3 principales. Por último, suma el rubro principal de cada año y el porcentaje de productos primarios.
- **Load:** Antes de guardar, el pipeline verifica la cantidad de filas esperada, que todas tengan las columnas del contrato, que no haya datos duplicados y que los valores no sean negativos ni exagerados. Si alguno de estos controles falla, se corta la ejecución. Si está todo bien, guarda el dataset en un CSV y genera un resumen en JSON con la fuente, el período, las provincias y los valores mínimo, máximo y promedio. Por último, agrega una línea al log de corridas con la fecha, la cantidad de filas y el período.

## Cómo instalarlo y ejecutarlo 

## De dónde salen los datos

## Qué encontré en los datos