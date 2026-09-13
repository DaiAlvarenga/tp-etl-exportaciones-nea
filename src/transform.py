"""Etapa 2 — Transform: dejar el dato usable.

Este módulo no lee ni escribe archivos: recibe filas y devuelve filas.
Por eso se puede probar sin tocar el disco (ver tests/test_transform.py).
"""
from datetime import datetime

from config import AREAS, EDAD_MAXIMA, EDAD_MINIMA


def normalizar_nombre(texto):
    """Saca los espacios de más y deja cada palabra con mayúscula inicial.

    '  juan   pérez ' -> 'Juan Pérez'
    No maneja partículas: 'de la cruz' queda 'De La Cruz'.
    """
    return " ".join(str(texto).split()).title()


def limpiar_edad(valor):
    """Devuelve la edad como número entero, o None si el valor no sirve.

    Acepta '45', '38 años' y ' 52 '.
    Devuelve None para 's/d', para vacío y para edades fuera de rango.
    """
    digitos = "".join(caracter for caracter in str(valor) if caracter.isdigit())
    if not digitos:
        return None

    edad = int(digitos)
    if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        return None
    return edad


def separar_telefono(crudo):
    """Separa un teléfono argentino en (país, característica, línea).

    Acepta los formatos en que suele venir cargado:
        '+54 362 4451278'   '(0376) 442-1509'
        '0362 154 887766'   '3624451278'

    Devuelve (None, None, None) si la característica no está en AREAS.
    """
    digitos = "".join(caracter for caracter in str(crudo) if caracter.isdigit())
    digitos = digitos.removeprefix("54")   # el código de país
    digitos = digitos.lstrip("0")          # el 0 de larga distancia

    for largo in (2, 3, 4):                # las características tienen 2, 3 o 4 dígitos
        area = digitos[:largo]
        if area in AREAS:
            linea = digitos[largo:].removeprefix("15")   # el 15 de los celulares
            return "54", area, linea

    return None, None, None


def a_fecha_iso(texto):
    """Convierte la fecha a formato ISO (aaaa-mm-dd), o None si no puede.

    Acepta 'dd/mm/aaaa' y 'aaaa-mm-dd'.

    NO acepta 'dd-mm-aa': un año de dos dígitos es ambiguo (¿1965 o 2065?) y
    preferimos dejar el dato vacío antes que inventar uno.
    """
    for formato in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(texto).strip(), formato).date().isoformat()
        except ValueError:
            continue
    return None


def transformar(filas):
    """Aplica las cuatro funciones a cada fila y saca los documentos repetidos.

    Devuelve dos cosas:
        - la lista de filas limpias
        - un resumen con los números de la corrida, que después va al log
    """
    limpias = []
    documentos_vistos = set()
    duplicados = 0

    for fila in filas:
        documento = fila["documento"].strip()

        if documento in documentos_vistos:
            duplicados += 1
            continue                       # ya lo teníamos: salteamos esta fila
        documentos_vistos.add(documento)

        pais, area, linea = separar_telefono(fila["telefono"])

        limpias.append({
            "documento": documento,
            "nombre": normalizar_nombre(fila["nombre"]),
            "localidad": fila["localidad"].strip(),
            "provincia": fila["provincia"].strip(),
            "pais": pais,
            "area": area,
            "linea": linea,
            "edad": limpiar_edad(fila["edad"]),
            "fecha_nacimiento": a_fecha_iso(fila["fecha_nac"]),
        })

    resumen = {
        "filas_leidas": len(filas),
        "filas_guardadas": len(limpias),
        "documentos_duplicados": duplicados,
        "sin_edad": sum(1 for fila in limpias if fila["edad"] is None),
        "sin_fecha": sum(1 for fila in limpias if fila["fecha_nacimiento"] is None),
    }
    return limpias, resumen
