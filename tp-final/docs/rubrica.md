# Rúbrica de evaluación — TP Final Unidad II

Con estos criterios se corrige el trabajo. Usala como **checklist** antes
de entregar: te dice exactamente dónde están los puntos.

**Puntaje total: 100** (+ hasta 5 de bonus) · **Aprueba con 60**

---

## Resumen de criterios

| # | Criterio | Puntos |
|:---:|---|:---:|
| 1 | El pipeline funciona de punta a punta | 25 |
| 2 | Transform correcto | 20 |
| 3 | Estructura y diseño modular | 15 |
| 4 | Manejo de errores y quality checks | 10 |
| 5 | Calidad de código | 10 |
| 6 | README propio | 10 |
| 7 | Uso de Git | 10 |
| | **Total** | **100** |
| 8 | Bonus | +5 |

---

## 1. El pipeline funciona de punta a punta — 25 pts

| Nivel | Pts | Descripción |
|---|:---:|---|
| Excelente | 22–25 | `python src/main.py` corre sin errores. Genera el CSV con 13 columnas y ~1.408 filas, más `resumen.json` y el log. Es idempotente: correrlo dos veces deja el mismo CSV y suma una línea al log. |
| Bueno | 17–21 | Corre y genera el CSV correcto, pero falta alguna salida (JSON o log) o la idempotencia no se cumple. |
| Suficiente | 12–16 | Corre con intervención manual o genera el CSV incompleto (faltan filas o columnas). |
| Insuficiente | 0–11 | No corre, o no genera el dataset. |

**Cómo lo verificás vos antes de entregar:**

```bash
python src/main.py
wc -l data/processed/exportaciones_nea.csv    # esperado: 1409
head -1 data/processed/exportaciones_nea.csv  # 13 columnas, orden correcto
python src/main.py                            # 2da corrida: CSV igual, log +1
```

## 2. Transform correcto — 20 pts

| Aspecto | Pts |
|---|:---:|
| Ancho → largo bien resuelto (el total NO es un destino; se saltean los nulos) | 5 |
| Derivadas simples correctas (`region_destino`, `decada`, `participacion_pct`) | 4 |
| Variación interanual bien alineada (mismo destino y provincia, año previo) | 4 |
| Ranking calculado por grupo `(provincia, año)`, con `es_top3` coherente | 3 |
| Join con rubros por clave compuesta, tipo LEFT | 4 |

**Errores que restan puntos:** contar `__TOTAL__` como si fuera un destino
(da 1.536 filas en vez de 1.408); calcular el ranking global en vez de por
provincia y año; comparar la variación contra la fila anterior de la lista
en lugar del año anterior de la misma serie; hacer un INNER join que
descarta filas en silencio.

## 3. Estructura y diseño modular — 15 pts

| Nivel | Pts | Descripción |
|---|:---:|---|
| Excelente | 13–15 | Las tres etapas bien separadas. Cada función hace una sola cosa y tiene nombre de verbo. Todo entra por parámetros y sale por `return`. Config separada del código. |
| Bueno | 10–12 | Separación correcta, pero alguna función hace de más o depende de variables globales. |
| Suficiente | 6–9 | Las etapas existen pero están mezcladas, o hay valores hardcodeados en la lógica. |
| Insuficiente | 0–5 | Todo en un solo bloque, sin funciones. |

## 4. Manejo de errores y quality checks — 10 pts

| Aspecto | Pts |
|---|:---:|
| Al menos 3 quality checks implementados y funcionando | 4 |
| Los checks críticos cortan el proceso (no siguen como si nada) | 3 |
| Los casos borde no rompen: división por cero, `None`, clave ausente | 3 |

## 5. Calidad de código — 10 pts

| Aspecto | Pts |
|---|:---:|
| PEP 8: `snake_case`, 4 espacios, líneas de largo razonable | 3 |
| Nombres descriptivos (`valor_musd`, no `x` ni `datos2`) | 3 |
| Docstrings en todas las funciones propias | 2 |
| Comentarios que explican el porqué, no lo obvio | 2 |

## 6. README propio — 10 pts

| Aspecto | Pts |
|---|:---:|
| Explica qué hace el pipeline, con tus palabras | 3 |
| Instrucciones de instalación y ejecución que funcionan | 3 |
| Cita la fuente de datos | 2 |
| Incluye un hallazgo sobre los datos, con sentido | 2 |

Si dejás el README del template sin modificar: **0 puntos**.

## 7. Uso de Git — 10 pts

| Nivel | Pts | Descripción |
|---|:---:|---|
| Excelente | 9–10 | 5 o más commits que muestran avance progresivo. Mensajes claros y específicos ("agrega join con rubros"). Sin archivos de datos ni `__pycache__` versionados. |
| Bueno | 6–8 | Varios commits, pero algunos mensajes son genéricos ("cambios", "update"). |
| Suficiente | 3–5 | 2–4 commits, o se subieron datos/basura al repositorio. |
| Insuficiente | 0–2 | Un solo commit con todo. |

## 8. Bonus — hasta +5 pts

| Extra | Pts |
|---|:---:|
| Tests propios del TODO 13, bien pensados | +2 |
| Columna derivada adicional, justificada en el README | +1 |
| Gráfico de la evolución de una provincia | +1 |
| Provincia parametrizable por CLI o variable de entorno | +1 |
| Notebook de exploración | +1 |

*(El bonus suma hasta 5 puntos como máximo, aunque cumplas más ítems.)*

---

## Sobre integridad académica

El template es un punto de partida común: que el `extract.py` sea igual
entre entregas es esperable. Lo que tiene que ser **propio** es el
Transform, el README y el historial de commits. Dos entregas con el mismo
código en las funciones con TODO, los mismos comentarios y los mismos
nombres de variables auxiliares se revisan en conjunto con ambos
estudiantes.
