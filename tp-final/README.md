# TP Final — Unidad II · Fundamentos de la Programación

## Pipeline ETL de exportaciones del NEA

Todo el material del trabajo práctico final está en esta carpeta.

---

## Para estudiantes: qué tenés que hacer

**Lo que te llevás es la carpeta `template/`.** El resto es documentación.

| Carpeta / archivo | Qué es |
|---|---|
| **`template/`** | El punto de partida de tu TP. Copiala, renombrala y trabajá ahí. |
| `docs/consigna.md` | La consigna completa: qué entregar y cómo se evalúa. |
| `docs/guia-git.md` | Paso a paso para crear tu repositorio y entregarlo. **Empezá por acá.** |
| `docs/rubrica.md` | Con qué criterios se corrige. Usala como checklist. |

### En tres pasos

1. Leé **`docs/consigna.md`**.
2. Seguí **`docs/guia-git.md`** para armar tu repositorio a partir de `template/`.
3. Completá los 13 TODOs y entregá el link de tu repo por el campus.

---

## De qué se trata

Construís un pipeline **ETL** que se conecta a la API de Series de Tiempo de
datos.gob.ar, procesa las exportaciones de **Chaco, Corrientes, Formosa y
Misiones** (INDEC, 1993–2024) y produce un dataset analítico de
**1.408 filas × 13 columnas**.

```
   API datos.gob.ar          data/raw/*.json         data/processed/
   (INDEC, 8 llamadas)  -->  (crudo, sin tocar) -->  exportaciones_nea.csv
                                                     resumen.json
        EXTRACT                  TRANSFORM              CHEQUEAR + LOAD
```

Ese CSV **lo vas a volver a usar en el módulo de estadística descriptiva**:
tiene 6 variables categóricas y 7 numéricas, con nulos y valores atípicos
reales. Por eso importa que quede bien.

### El dataset de salida

| # | Columna | Tipo | # | Columna | Tipo |
|:---:|---|---|:---:|---|---|
| 1 | `anio` | int | 8 | `var_interanual_pct` | float |
| 2 | `provincia` | str | 9 | `decada` | str |
| 3 | `destino` | str | 10 | `ranking_destino` | int |
| 4 | `region_destino` | str | 11 | `es_top3` | bool |
| 5 | `valor_musd` | float | 12 | `rubro_principal` | str |
| 6 | `total_provincia_musd` | float | 13 | `pp_participacion_pct` | float |
| 7 | `participacion_pct` | float | | | |

Dos filas de ejemplo, con valores reales de la API:

```csv
2024,Chaco,China,Asia,110.93,401.74,27.61,46.36,2020s,1,True,Productos primarios,81.3
2024,Chaco,Brasil,Mercosur,18.12,401.74,4.51,30.45,2020s,6,False,Productos primarios,81.3
```

### Qué se ejercita en cada TODO

| TODO | Función | Contenido de la unidad |
|:---:|---|---|
| 1 | `ancho_a_largo()` | Bucles anidados sobre listas y diccionarios |
| 2 | `clasificar_region()` | Diccionario de mapeo + `.get()` con default |
| 3 | `calcular_decada()` | División entera `//` y f-strings |
| 4–5 | `calcular_participacion()`, `calcular_variacion()` | Funciones con `return`, manejo de `None` |
| 6 | `agregar_variacion_interanual()` | Diccionario como índice de búsqueda |
| 7 | `agregar_ranking()` | `sorted()`, `enumerate()`, booleanos |
| 8 | `construir_indice_rubros()`, `unir_con_rubros()` | JOIN por clave compuesta |
| 9–10 | Quality checks | Sets y comprensión de listas |
| 11–12 | Resumen y persistencia | `json.dump`, modos `"w"` vs `"a"` |
| 13 | Tests propios | Testing (bonus) |

---

## Fuente de datos

| | |
|---|---|
| Dataset 357.1 | Exportaciones por provincia y país de destino |
| Dataset 350.1 | Exportaciones por provincia y rubro |
| Origen | INDEC, vía `apis.datos.gob.ar/series/api/` |
| Período | 1993–2024 (32 años) |
| Unidad | Millones de dólares FOB |

No hace falta registrarse ni usar credenciales: es una API abierta.

---

## Nota de mantenimiento

Los IDs de series de `template/config.py` fueron **verificados el 2026-08-02**.
Si INDEC los regenera, se buscan así:

```
https://apis.datos.gob.ar/series/api/search/?q=exportaciones+<provincia>&limit=20
```

Hay que actualizar `SERIES_DESTINO`, `SERIES_TOTAL` y `SERIES_RUBRO`.

---

*Diplomatura en Data Analytics e IA Aplicada — UNNE / Extender*
