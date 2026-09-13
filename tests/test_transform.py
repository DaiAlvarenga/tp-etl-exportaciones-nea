"""Pruebas de las funciones de transformación.

Se corren desde la raíz del proyecto:

    python tests/test_transform.py

No hace falta ninguna librería extra: usamos `assert`, que viene con Python.
Un assert que pasa no dice nada; uno que falla dice exactamente qué se rompió.
"""
import sys
from pathlib import Path

# Para poder importar desde src/ estando en tests/
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from transform import a_fecha_iso, limpiar_edad, normalizar_nombre, separar_telefono


def probar_normalizar_nombre():
    assert normalizar_nombre("juan pérez") == "Juan Pérez"
    assert normalizar_nombre("MARÍA GÓMEZ") == "María Gómez"
    assert normalizar_nombre("  Carlos   Ruiz ") == "Carlos Ruiz"
    print("normalizar_nombre   OK")


def probar_limpiar_edad():
    assert limpiar_edad("45") == 45
    assert limpiar_edad("38 años") == 38
    assert limpiar_edad(" 52 ") == 52
    assert limpiar_edad("s/d") is None
    assert limpiar_edad("") is None
    assert limpiar_edad("150") is None      # fuera de rango
    print("limpiar_edad        OK")


def probar_separar_telefono():
    # Los cuatro formatos que aparecen en el padrón
    assert separar_telefono("+54 362 4451278") == ("54", "362", "4451278")
    assert separar_telefono("(0376) 442-1509") == ("54", "376", "4421509")
    assert separar_telefono("0362 154 887766") == ("54", "362", "4887766")
    assert separar_telefono("3794223344") == ("54", "379", "4223344")

    # Buenos Aires: la característica tiene DOS dígitos, no tres
    assert separar_telefono("+54 11 4567 8901") == ("54", "11", "45678901")

    # Una característica que no conocemos no se adivina
    assert separar_telefono("+54 999 1234567") == (None, None, None)
    print("separar_telefono    OK")


def probar_a_fecha_iso():
    assert a_fecha_iso("12/03/1981") == "1981-03-12"
    assert a_fecha_iso("1988-07-04") == "1988-07-04"
    assert a_fecha_iso("") is None

    # Año de dos dígitos: ambiguo. Preferimos vacío antes que inventar.
    assert a_fecha_iso("25-03-65") is None
    print("a_fecha_iso         OK")


if __name__ == "__main__":
    probar_normalizar_nombre()
    probar_limpiar_edad()
    probar_separar_telefono()
    probar_a_fecha_iso()
    print("\nTodas las pruebas pasaron.")
