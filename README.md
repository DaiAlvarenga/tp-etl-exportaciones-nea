# Diplomatura en Data Analytics — UNNE

Template estándar para proyectos de análisis de datos. Cloná este repositorio como punto de partida y reutilizá esta misma estructura en tus futuros proyectos: es simple, ordenada y sigue las buenas prácticas de la industria.

---

## Estructura del proyecto

```
diplo_data-analytics_unne/
├── data/
│   ├── raw/          # Datos originales, tal cual se reciben. NUNCA se editan.
│   └── processed/    # Datos ya limpios y transformados, listos para analizar.
├── notebooks/        # Notebooks de análisis (.ipynb).
│   └── 00_notebook_prueba.ipynb   # Verifica que tu entorno funciona.
├── src/              # Funciones y código reutilizable (.py).
├── outputs/          # Gráficos, tablas y reportes que genera tu análisis.
├── .gitignore        # Qué archivos NO se suben al repositorio.
├── requirements.txt  # Librerías que necesita el proyecto (versiones fijas).
├── LICENSE
└── README.md         # Este archivo.
```

**Por qué esta separación:** mantener los datos crudos intactos (`raw/`) te permite rehacer todo el proceso desde cero si algo sale mal. Separar notebooks, código y salidas hace que el proyecto sea fácil de entender para vos y para cualquiera que lo abra después.

> Nota: por defecto, el contenido de `data/` y `outputs/` no se sube al repositorio (ver `.gitignore`). Se versiona la estructura de carpetas, no los archivos pesados o privados.

---

## Puesta en marcha

Si es tu primera vez configurando el entorno, seguí la **Guía de configuración inicial** del curso. En resumen:

1. **Cloná el repositorio** (en la terminal de VS Code):

   ```bash
   git clone https://github.com/daianadte24/diplo_data-analytics_unne.git
   cd diplo_data-analytics_unne
   ```

2. **Creá y activá el entorno virtual:**

   Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Si todo salió bien, vas a ver `(.venv)` al principio de la línea de la terminal.

3. **Instalá las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

   Todas las versiones están fijas para que trabajes con exactamente lo mismo que el resto del curso.

4. **Probá que funciona:** abrí `notebooks/00_notebook_prueba.ipynb`, seleccioná el intérprete `.venv` como kernel y ejecutá todas las celdas. Si corren sin errores, tu entorno está listo.

---

## Cómo usar este template en tus propios proyectos

1. Usá este repositorio como base: en GitHub, hacé clic en **Use this template** para crear un repo nuevo con esta estructura (o simplemente copiala).
2. Poné tus datos originales en `data/raw/`.
3. Trabajá tus análisis en `notebooks/`, numerándolos por orden (`01_...`, `02_...`).
4. Guardá los datos ya procesados en `data/processed/` y los resultados en `outputs/`.
5. Si repetís una función en varias notebooks, movela a `src/` para reutilizarla.

---

## Ejemplo de ETL: del archivo desprolijo al dato usable

En `src/` hay un pipeline completo y funcionando que sirve de modelo para el trabajo
final. Procesa un padrón de beneficiarios cargado a mano —con nombres en tres
formatos, edades como texto y teléfonos escritos de cuatro maneras distintas— y
devuelve una tabla limpia, documentada y reproducible.

### Cómo correrlo

```bash
python src/main.py                # corre el pipeline completo
python tests/test_transform.py    # corre las pruebas de las funciones
```

Produce tres archivos:

```
data/processed/padron_limpio.csv    el dato limpio
data/processed/datapackage.json     la ficha que lo describe
logs/proceso.log                    una línea por corrida
```

Corrélo dos veces: el CSV queda idéntico y el log suma una línea. Eso es
**idempotencia**.

### El recorrido

| Archivo | Etapa | Qué hace |
|---|---|---|
| `notebooks/01_exploracion.ipynb` | — | Mira el archivo crudo y arma la lista de problemas |
| `src/extract.py` | **Extract** | Lee el crudo. No limpia nada |
| `src/transform.py` | **Transform** | Cuatro funciones de limpieza. No lee ni escribe archivos |
| `src/load.py` | **Load** | Valida, guarda el CSV, escribe la ficha y registra la corrida |
| `src/main.py` | — | Llama a las etapas en orden |
| `src/config.py` | — | Rutas, versión y parámetros: lo que cambia entre corridas |
| `tests/test_transform.py` | — | Prueba cada función con `assert`, sin tocar el disco |
| `docs/metadata.md` | — | Qué es la metadata y qué significa cada columna |

**El orden importa y es el punto del ejemplo: primero se explora, después se
programa.** La exploración es la que descubrió que había teléfonos de Oberá y
Clorinda con características que no estábamos contemplando. Sin ese paso, el ETL
habría roto cuatro teléfonos en silencio.

### Las tres reglas que ilustra

1. **`extract` no limpia.** Separar "qué trajimos" de "qué le hicimos" es lo que
   permite responder de dónde salió cada número.
2. **`transform` no toca archivos.** Recibe filas y devuelve filas, y por eso se
   puede probar sin conexión y sin abrir nada.
3. **`load` valida antes de escribir.** Si no, el archivo malo ya está en disco y
   alguien lo va a levantar.

---

*Diplomatura en Data Analytics — Universidad Nacional del Nordeste (UNNE)*
