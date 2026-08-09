# Diplomatura en Data Analytics — UNNE

> ### Estás en la branch `tp-final`
>
> El material del **Trabajo Práctico Final de la Unidad II** está en la carpeta **[`tp-final/`](tp-final/)**.
>
> - Empezá por **[`tp-final/docs/guia-git.md`](tp-final/docs/guia-git.md)**: te explica paso a paso qué descargar y cómo entregar.
> - La consigna completa está en **[`tp-final/docs/consigna.md`](tp-final/docs/consigna.md)**.
> - Lo que tenés que copiar a tu computadora es la carpeta **`tp-final/template/`**.
>
> El resto de este README describe la estructura general del repositorio de la materia.

---

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

*Diplomatura en Data Analytics — Universidad Nacional del Nordeste (UNNE)*
