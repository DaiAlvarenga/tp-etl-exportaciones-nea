"""Etapa 1 — Extract: traer el dato tal como está.

Acá no se limpia nada. Si la lectura también transformara, después no habría
forma de saber si un valor vino así del origen o se lo hicimos nosotros.
"""
import csv


def extraer(ruta):
    """Lee el padrón crudo y devuelve una lista de diccionarios.

    Cada fila del CSV se convierte en un diccionario, usando la primera fila
    del archivo como nombres de las claves.
    """
    with open(ruta, encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))
