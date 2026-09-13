"""Etapa 3 — Load: validar y dejar el resultado disponible.

Guarda tres cosas, y las tres importan:
    - el CSV limpio            -> el dato
    - datapackage.json         -> la ficha que explica el dato
    - una línea en el log      -> qué pasó en esta corrida
"""
import csv
import json
from datetime import datetime

from config import COLUMNAS_SALIDA, VERSION

# Descripción de cada columna de salida. Es lo que va a la ficha, y es la
# única fuente de verdad sobre qué significa cada campo.
CAMPOS = [
    {"name": "documento", "type": "string",
     "description": "DNI del beneficiario. Identifica la fila."},
    {"name": "nombre", "type": "string",
     "description": "Apellido y nombre, con espacios normalizados."},
    {"name": "localidad", "type": "string",
     "description": "Localidad de residencia."},
    {"name": "provincia", "type": "string",
     "description": "Provincia de residencia."},
    {"name": "pais", "type": "string",
     "description": "Código telefónico de país. Siempre 54."},
    {"name": "area", "type": "string",
     "description": "Característica telefónica, sin el 0 inicial."},
    {"name": "linea", "type": "string",
     "description": "Número de línea, sin el 15 de celular."},
    {"name": "edad", "type": "integer",
     "description": "Edad declarada. Vacía si no se pudo determinar.",
     "constraints": {"minimum": 0, "maximum": 120}},
    {"name": "fecha_nacimiento", "type": "date",
     "description": "Fecha de nacimiento en formato ISO. Vacía si el original "
                    "traía un año de dos dígitos."},
]


def validar(filas):
    """Corta el proceso si el resultado no está en condiciones de entregarse.

    Es mejor no entregar nada que entregar un padrón con teléfonos rotos:
    un archivo malo en disco es un archivo que alguien va a levantar.
    """
    if not filas:
        raise ValueError("No hay filas para guardar")

    sin_area = [fila for fila in filas if fila["area"] is None]
    if sin_area:
        raise ValueError(
            f"{len(sin_area)} teléfonos con característica desconocida "
            f"(por ejemplo el documento {sin_area[0]['documento']}). "
            f"Si la característica es válida, agregala a AREAS en config.py"
        )

    documentos = [fila["documento"] for fila in filas]
    if len(documentos) != len(set(documentos)):
        raise ValueError("Quedaron documentos repetidos después de transformar")


def guardar_csv(filas, ruta):
    """Escribe el padrón limpio.

    Escribe primero en un archivo temporal y recién al final lo renombra.
    Si el proceso se corta a mitad de camino, no queda un archivo incompleto
    con el nombre del archivo bueno.
    """
    ruta.parent.mkdir(parents=True, exist_ok=True)
    temporal = ruta.with_suffix(".tmp")

    with open(temporal, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS_SALIDA)
        escritor.writeheader()
        escritor.writerows(filas)

    temporal.replace(ruta)


def guardar_metadata(filas, ruta_csv, ruta_json, ruta_origen):
    """Escribe la ficha que describe al CSV.

    Un CSV no dice de dónde salió, cuándo se generó ni qué significa cada
    columna. En una base de datos eso lo responde el catálogo del sistema;
    con archivos sueltos hay que escribirlo al lado.

    El formato es Data Package, un estándar abierto (datapackage.org).
    """
    ficha = {
        "name": "padron-beneficiarios",
        "title": "Padrón de beneficiarios del programa",
        "version": VERSION,
        "created": datetime.now().isoformat(timespec="seconds"),
        "sources": [
            {"title": "Área de Programas Sociales", "path": str(ruta_origen.name)}
        ],
        "resources": [
            {
                "name": "padron",
                "path": ruta_csv.name,
                "format": "csv",
                "encoding": "utf-8",
                "filas": len(filas),
                "schema": {
                    "fields": CAMPOS,
                    "missingValues": [""],
                    "primaryKey": ["documento"],
                },
            }
        ],
    }

    ruta_json.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(ficha, archivo, ensure_ascii=False, indent=2)


def registrar(resumen, ruta_log):
    """Agrega una línea al log.

    Se abre en modo "a": cada corrida suma una línea y ninguna pisa el
    historial anterior.
    """
    ruta_log.parent.mkdir(parents=True, exist_ok=True)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(ruta_log, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{ahora} | v{VERSION} | "
            f"{resumen['filas_leidas']} leídas -> "
            f"{resumen['filas_guardadas']} guardadas | "
            f"{resumen['documentos_duplicados']} duplicados | "
            f"{resumen['sin_edad']} sin edad | "
            f"{resumen['sin_fecha']} sin fecha\n"
        )
