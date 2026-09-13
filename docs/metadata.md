# La metadata del padrón

## Por qué existe este archivo

Cuando trabajás con una **base de datos**, el catálogo del sistema ya está: le
preguntás y te dice qué tablas hay, qué columnas, de qué tipo y con qué
restricciones. En SQL estándar eso es `information_schema`; en SQLite, `PRAGMA`.

Cuando trabajás con **archivos sueltos, ese catálogo no existe**. Un CSV no dice de
dónde salió, cuándo se generó, qué significa cada columna ni qué valor representa un
dato faltante. Toda esa información vive en la cabeza de quien lo generó, y se pierde.

> **Si el catálogo no viene con el archivo, hay que escribirlo al lado.**

Eso es `data/processed/datapackage.json`: la ficha del CSV. La escribe `src/load.py`
en la misma corrida que genera el dato, así no se desactualiza.

## Qué formato usa

[**Data Package**](https://datapackage.org/), un estándar abierto. No lo inventamos
nosotros: define exactamente qué campos poner y hay validadores y librerías que lo
leen.

El descriptor se escribe en JSON, pero **el dato sigue siendo un CSV**. El JSON es la
etiqueta, no el contenido. El mismo estándar sirve para describir un CSV, un Excel,
un Parquet o una tabla SQL.

```
data/processed/
├── padron_limpio.csv     <- el dato
└── datapackage.json      <- la ficha que lo describe
```

## Qué dice

| Campo de la ficha | Para qué sirve |
|---|---|
| `name`, `title` | Cómo se llama este conjunto de datos |
| `version` | Qué versión es. Permite decir "el análisis usó la 1.0.0" |
| `created` | Cuándo se generó esta salida |
| `sources` | De dónde salió el dato original |
| `resources[].schema.fields` | Cada columna: nombre, tipo, descripción y restricciones |
| `resources[].schema.missingValues` | Qué valor representa "no hay dato" |
| `resources[].schema.primaryKey` | Qué columna identifica a cada fila |

`missingValues` es el que más se agradece después: declara que el vacío significa "no
hay dato", así ninguna herramienta lo cuenta como si fuera un valor.

## Las columnas de salida

| Columna | Tipo | Qué es |
|---|---|---|
| `documento` | texto | DNI del beneficiario. Es la clave: identifica la fila. |
| `nombre` | texto | Apellido y nombre, con espacios normalizados y mayúscula inicial. |
| `localidad` | texto | Localidad de residencia. |
| `provincia` | texto | Provincia de residencia. |
| `pais` | texto | Código telefónico de país. Siempre `54`. |
| `area` | texto | Característica telefónica, sin el `0` inicial. |
| `linea` | texto | Número de línea, sin el `15` de celular. |
| `edad` | entero | Edad declarada, entre 0 y 120. **Vacía** si no se pudo determinar. |
| `fecha_nacimiento` | fecha | Formato ISO `aaaa-mm-dd`. **Vacía** si el original traía un año de dos dígitos. |

### Por qué hay campos vacíos a propósito

**`edad` vacía** — el original decía `"s/d"`, estaba en blanco, o el valor estaba
fuera de rango (hay una edad de 150). Se deja vacío en lugar de poner cero: un cero
inventado se promedia y ensucia todo el análisis posterior.

**`fecha_nacimiento` vacía** — el original traía la fecha como `dd-mm-aa`, con año de
dos dígitos. `25-03-65` puede ser 1965 o 2065, y Python lo interpreta como 2065 sin
avisar. Sin una regla que nos diga el siglo, la decisión honesta es dejarlo vacío.

Son 27 filas. Si se consigue el criterio correcto (por ejemplo, "ninguna persona del
padrón nació después de 2010"), se puede recuperar: sería una mejora de
`a_fecha_iso()` en `src/transform.py`.

## Cómo versionamos el dato

Los datos **no van a Git** (ver `.gitignore`): se regeneran corriendo el pipeline,
pesan, y en un padrón con nombres y teléfonos son datos personales.

Pero igual necesitan versión, porque si alguien dice "este número no me da" hay que
poder saber con qué versión del padrón se calculó. La versión vive en `VERSION`
dentro de `config.py`, viaja a la ficha, y **la ficha sí está en Git**.

Así el repositorio guarda la historia de qué datos hubo, sin guardar los datos.
