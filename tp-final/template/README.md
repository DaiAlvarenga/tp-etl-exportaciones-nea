# Pipeline ETL de exportaciones del NEA

## Qué hace el pipeline

- **Extract:** El pipeline se conecta a una API del Estado (datos.gob.ar, con datos del INDEC) desde el cual descarga datos relacionados a las exportaciones de Chaco, Corrientes, Formosa y Misiones entre 1993 y 2024, detallando el país de destino y el rubro de los productos que se exportan. Guarda los datos en 8 archivos JSON.
- **Transform:** En la API cada país es una columna; el pipeline lo reordena para que haya una fila por año, provincia y país de destino. Después se agregan columnas con la zona del país de destino, el porcentaje sobre el total, la variación respecto al año anterior y si el destino está entre los 3 principales. Por último, suma el rubro principal de cada año y el porcentaje de productos primarios.
- **Load:** Antes de guardar, el pipeline verifica la cantidad de filas esperada, que todas tengan las columnas del contrato, que no haya datos duplicados y que los valores no sean negativos ni exagerados. Si alguno de estos controles falla, se corta la ejecución. Si está todo bien, guarda el dataset en un CSV y genera un resumen en JSON con la fuente, el período, las provincias y los valores mínimo, máximo y promedio. Por último, agrega una línea al log de corridas con la fecha, la cantidad de filas y el período.


## Cómo instalarlo y ejecutarlo

Para instalarlo y ejecutarlo, solo se necesita tener Python instalado (versión 3.8 o superior). Para esta actividad no es necesario instalar librerías externas, ya que el proyecto utiliza únicamente las que vienen predeterminadas en la biblioteca estándar de Python.

1. Clonar el repositorio y entrar a la carpeta del trabajo:

```
git clone https://github.com/DaiAlvarenga/tp-etl-exportaciones-nea.git
cd tp-etl-exportaciones-nea
git checkout tp-final
cd tp-final/template
```

2. Ejecutar el pipeline (la primera vez necesita internet):

```
python src/main.py
```

3. Si ya descargó los datos antes, se puede correr sin conexión:

```
python src/main.py --sin-internet
```

4. Correr los tests:

```
python tests/test_transform.py
```

Los resultados quedan en `data/processed/` (el CSV y el resumen JSON) y en `logs/` (el historial de corridas).

## De dónde salen los datos

Los datos de este trabajo salen de la API pública de series de tiempo de datos abiertos del Estado (`datos.gob.ar`), que recopila información oficial del INDEC. 

Para armar el análisis, el proyecto toma dos datasets clave que cubren 32 años de historia (desde 1993 hasta 2024): por un lado, las exportaciones según la provincia y el país de destino, y por el otro, el detalle por rubros. Todo esto abarca a las cuatro provincias de nuestra región (Chaco, Corrientes, Misiones y Formosa), con los valores medidos en millones de dólares FOB.

## Qué encontré en los datos
Al explorar el dataset final, encontré algunos comportamientos que me llamaron mucho la atención. Por ejemplo, en el caso de Corrientes y su comercio con Brasil, las exportaciones pasaron abruptamente de 25.29 millones de dólares en 2019 a 399.14 millones en 2020, lo que representa un aumento descomunal del 1478# Pipeline ETL de exportaciones del NEA

## Qué hace el pipeline

- **Extract:** El pipeline se conecta a una API del Estado (datos.gob.ar, con datos del INDEC) desde el cual descarga datos relacionados a las exportaciones de Chaco, Corrientes, Formosa y Misiones entre 1993 y 2024, detallando el país de destino y el rubro de los productos que se exportan. Guarda los datos en 8 archivos JSON.
- **Transform:** En la API cada país es una columna; el pipeline lo reordena para que haya una fila por año, provincia y país de destino. Después se agregan columnas con la zona del país de destino, el porcentaje sobre el total, la variación respecto al año anterior y si el destino está entre los 3 principales. Por último, suma el rubro principal de cada año y el porcentaje de productos primarios.
- **Load:** Antes de guardar, el pipeline verifica la cantidad de filas esperada, que todas tengan las columnas del contrato, que no haya datos duplicados y que los valores no sean negativos ni exagerados. Si alguno de estos controles falla, se corta la ejecución. Si está todo bien, guarda el dataset en un CSV y genera un resumen en JSON con la fuente, el período, las provincias y los valores mínimo, máximo y promedio. Por último, agrega una línea al log de corridas con la fecha, la cantidad de filas y el período.


## Cómo instalarlo y ejecutarlo

Para instalarlo y ejecutarlo, solo se necesita tener Python instalado (versión 3.8 o superior). Para esta actividad no es necesario instalar librerías externas, ya que el proyecto utiliza únicamente las que vienen predeterminadas en la biblioteca estándar de Python.

1. Clonar el repositorio y entrar a la carpeta del trabajo:

```
git clone https://github.com/DaiAlvarenga/tp-etl-exportaciones-nea.git
cd tp-etl-exportaciones-nea
git checkout tp-final
cd tp-final/template
```

2. Ejecutar el pipeline (la primera vez necesita internet):

```
python src/main.py
```

3. Si ya descargó los datos antes, se puede correr sin conexión:

```
python src/main.py --sin-internet
```

4. Correr los tests:

```
python tests/test_transform.py
```

Los resultados quedan en `data/processed/` (el CSV y el resumen JSON) y en `logs/` (el historial de corridas).

## De dónde salen los datos

Los datos de este trabajo salen de la API pública de series de tiempo de datos abiertos del Estado (`datos.gob.ar`), que recopila información oficial del INDEC. 

Para armar el análisis, el proyecto toma dos datasets clave que cubren 32 años de historia (desde 1993 hasta 2024): por un lado, las exportaciones según la provincia y el país de destino, y por el otro, el detalle por rubros. Todo esto abarca a las cuatro provincias de nuestra región (Chaco, Corrientes, Misiones y Formosa), con los valores medidos en millones de dólares FOB.

## Qué encontré en los datos
Al explorar el dataset final, encontré algunos comportamientos que me llamaron mucho la atención. Por ejemplo, en el caso de Corrientes y su comercio con Brasil, las exportaciones pasaron abruptamente de 25.29 millones de dólares en 2019 a 399.14 millones en 2020, lo que representa un aumento descomunal del 1475.25% respecto al año anterior..25% respecto al año anterior.