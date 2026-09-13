"""Parámetros del proyecto.

Todo lo que puede cambiar de una corrida a otra vive acá, no en el código:
rutas, versión y los valores que usamos para validar.
"""
from pathlib import Path

# La raíz del proyecto es la carpeta que contiene a src/
RAIZ = Path(__file__).resolve().parent.parent

RUTA_CRUDO = RAIZ / "data" / "raw" / "padron_beneficiarios.csv"
RUTA_LIMPIO = RAIZ / "data" / "processed" / "padron_limpio.csv"
RUTA_METADATA = RAIZ / "data" / "processed" / "datapackage.json"
RUTA_LOG = RAIZ / "logs" / "proceso.log"

VERSION = "1.0.0"

# Características telefónicas que sabemos leer.
# Estas siete salieron de la exploración (ver notebooks/01_exploracion.ipynb):
# si aparece una localidad nueva, se agrega acá y queda arreglado en todo el proyecto.
AREAS = {"11", "362", "370", "376", "379", "3718", "3755"}

EDAD_MINIMA = 0
EDAD_MAXIMA = 120

COLUMNAS_SALIDA = ["documento", "nombre", "localidad", "provincia",
                   "pais", "area", "linea", "edad", "fecha_nacimiento"]
