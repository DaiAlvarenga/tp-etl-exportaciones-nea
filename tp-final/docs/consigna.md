# Trabajo Práctico Final — Unidad II

## Pipeline ETL de exportaciones del NEA

**Diplomatura en Data Analytics e IA Aplicada** — UNNE / Extender
Unidad II · Fundamentos de la Programación

---

## 1. De qué se trata

Vas a construir un **pipeline ETL** completo: un programa que se conecta a
una API pública, transforma los datos crudos en un dataset analítico y lo
guarda en disco, con controles de calidad y registro de lo que hizo.

No es un ejercicio de juguete. Los datos son reales —exportaciones de las
cuatro provincias del NEA publicadas por el INDEC— y el dataset que
produzcas **lo vas a volver a usar en el módulo de estadística
descriptiva**. Lo que armes acá es tu materia prima del módulo siguiente.

## 2. Qué se evalúa

Este TP integra todo lo de la Unidad II:

- Variables, tipos de datos y conversiones
- Estructuras de control: condicionales y bucles
- Funciones, parámetros y valores de retorno
- Colecciones: listas, tuplas, diccionarios y sets
- Comprensión de listas
- Entrada/salida: archivos CSV, JSON y logs
- Manejo de errores
- Buenas prácticas: PEP 8, docstrings y control de versiones con Git

## 3. Los datos

**Fuente:** API de Series de Tiempo del portal de datos abiertos del
Estado argentino (datos.gob.ar), con datos del INDEC.

| | |
|---|---|
| Dataset 357.1 | Exportaciones por provincia y **país de destino** |
| Dataset 350.1 | Exportaciones por provincia y **rubro** |
| Provincias | Chaco, Corrientes, Formosa y Misiones |
| Período | 1993 – 2024 (32 años) |
| Unidad | Millones de dólares FOB |
| Documentación | `https://apis.datos.gob.ar/series/api/` |

No necesitás credenciales ni registrarte: es una API abierta.

## 4. Qué tenés que entregar

### 4.1. Un repositorio propio en GitHub

Partís del **template** que te damos (no arrancás de cero) y creás **tu propio repositorio**. La guía paso a paso está en `docs/guia-git.md`.

### 4.2. El pipeline funcionando

Tres etapas separadas en archivos distintos:

| Archivo | Responsabilidad | Estado en el template |
|---|---|---|
| `src/extract.py` | Descargar de la API y guardar el crudo | **Resuelto** |
| `src/transform.py` | Limpiar, tipar, derivar columnas y unir | **8 TODOs** |
| `src/load.py` | Validar y guardar CSV + JSON + log | **4 TODOs** |
| `src/main.py` | Orquestar las tres etapas | **Resuelto** |
| `tests/test_transform.py` | Probar las transformaciones | **2 TODOs (bonus)** |

### 4.3. El dataset final

`data/processed/exportaciones_nea.csv`, con **13 columnas en este orden**:

| # | Columna | Tipo | Descripción |
|:---:|---|---|---|
| 1 | `anio` | int | Año (1993–2024) |
| 2 | `provincia` | str | Chaco, Corrientes, Formosa o Misiones |
| 3 | `destino` | str | País de destino (o "Resto") |
| 4 | `region_destino` | str | Región geoeconómica |
| 5 | `valor_musd` | float | Exportado a ese destino, millones USD |
| 6 | `total_provincia_musd` | float | Total de la provincia ese año |
| 7 | `participacion_pct` | float | `valor / total × 100` |
| 8 | `var_interanual_pct` | float | Variación vs. año anterior |
| 9 | `decada` | str | 1990s, 2000s, 2010s, 2020s |
| 10 | `ranking_destino` | int | Posición ese año (1 = mayor) |
| 11 | `es_top3` | bool | Si está entre los 3 primeros |
| 12 | `rubro_principal` | str | Rubro más exportado (del join) |
| 13 | `pp_participacion_pct` | float | % de productos primarios (del join) |

**Resultado esperado: 1.408 filas** (4 provincias × 11 destinos × 32 años).
Puede haber alguna menos si el INDEC publicó valores nulos: el pipeline
saltea esas observaciones a propósito.

Ejemplo de dos filas correctas:

```
2024,Chaco,China,Asia,110.93,401.74,27.61,46.36,2020s,1,True,Productos primarios,81.3
2024,Chaco,Brasil,Mercosur,18.12,401.74,4.51,30.45,2020s,6,False,Productos primarios,81.3
```

### 4.4. Las otras dos salidas

- `data/processed/resumen.json` — ficha técnica del dataset: fuente,
  período, cantidad de filas, estadísticas básicas y resultado de los
  controles de calidad.
- `logs/pipeline.log` — una línea por cada corrida. Si corrés el pipeline
  tres veces, tiene que haber tres líneas.

### 4.5. Un README propio

Reemplazá el README del template por uno tuyo que explique:

- Qué hace tu pipeline
- Cómo instalarlo y ejecutarlo
- De dónde salen los datos
- **Un párrafo con algo que hayas encontrado en los datos**: una
  tendencia, un año raro, un destino que crece o desaparece. No hace
  falta análisis estadístico todavía; alcanza con que mires tu CSV y
  cuentes algo con sentido.

## 5. Requisitos técnicos

**Obligatorios:**

1. Las tres etapas en archivos separados, cada función con una sola
   responsabilidad y nombre de verbo.
2. Configuración separada del código (usá `config.py`, no valores
   escritos a mano en medio de la lógica).
3. Manejo de errores: el pipeline no debe romperse por un dato faltante
   ni por una división por cero.
4. Al menos **3 quality checks** que corten el proceso si algo crítico
   está mal.
5. Docstrings en todas las funciones que escribas.
6. Estilo PEP 8: `snake_case`, 4 espacios de indentación, nombres
   descriptivos.
7. Como mínimo **5 commits** con mensajes que expliquen qué cambió.
   Un único commit "subo todo" no cumple.

**No permitido:**

- Usar `pandas` u otras librerías externas para el pipeline principal.
  El objetivo es que resuelvas la lógica vos. (Sí podés usarlo en la
  sección de bonus si querés graficar.)
- Modificar la lista `COLUMNAS` de `transform.py`: es el contrato de salida.
- Hardcodear los datos: tienen que venir de la API.

## 6. Bonus (hasta 5 puntos extra)

Elegí uno o más:

- Escribir los dos tests del TODO 13 y agregar otros propios.
- Sumar una columna derivada tuya, justificada en el README.
- Un gráfico simple de la evolución de tu provincia (con `matplotlib`).
- Hacer que el pipeline acepte la provincia por línea de comandos o por
  variable de entorno.
- Un `notebooks/exploracion.ipynb` con un primer vistazo a los datos.

## 7. Cómo se entrega

Se entrega **el link a tu repositorio de GitHub** por el campus.

- El repositorio tiene que ser **público** (o privado con acceso para la
  docente; en ese caso avisá).
- El link va al repositorio, no a un archivo suelto ni a un ZIP.
- Verificá antes de entregar: abrí tu link en una ventana de incógnito y
  fijate que se vea.

**Fecha de entrega:** ____ / ____ / ________

## 8. Antes de entregar, revisá

- [ ] `python src/main.py` corre de punta a punta sin errores
- [ ] `python tests/test_transform.py` pasa los 17 tests
- [ ] `exportaciones_nea.csv` tiene 13 columnas y ~1.408 filas
- [ ] Existen `resumen.json` y `pipeline.log`
- [ ] Corrí el pipeline dos veces: el CSV quedó igual, el log tiene 2 líneas
- [ ] El README es mío y explica mi pipeline
- [ ] Tengo al menos 5 commits con mensajes claros
- [ ] Todas mis funciones tienen docstring
- [ ] Mi repositorio es accesible desde el link que voy a entregar

## 9. Consultas

Dudas por el **foro de la materia**. Antes de preguntar, revisá si ya
está respondida. Cuando preguntes, contá qué intentaste y pegá el
mensaje de error completo junto con el fragmento de código.
