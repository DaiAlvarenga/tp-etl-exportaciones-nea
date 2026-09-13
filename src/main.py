"""Orquesta el pipeline completo.

Se corre desde la raíz del proyecto:

    python src/main.py

Este archivo no transforma nada: solo llama a las etapas en orden. Cada una
depende de la anterior y, si alguna falla, las siguientes no se ejecutan.
"""
import config
from extract import extraer
from load import guardar_csv, guardar_metadata, registrar, validar
from transform import transformar


def main():
    print("1. Extract   — leyendo el padrón crudo...")
    filas_crudas = extraer(config.RUTA_CRUDO)

    print("2. Transform — limpiando...")
    filas_limpias, resumen = transformar(filas_crudas)

    print("3. Validar   — revisando el resultado...")
    validar(filas_limpias)

    print("4. Load      — guardando...")
    guardar_csv(filas_limpias, config.RUTA_LIMPIO)
    guardar_metadata(filas_limpias, config.RUTA_LIMPIO, config.RUTA_METADATA,
                     config.RUTA_CRUDO)
    registrar(resumen, config.RUTA_LOG)

    print()
    print(f"Listo: {resumen['filas_guardadas']} filas en {config.RUTA_LIMPIO.name}")
    print(f"  {resumen['documentos_duplicados']} documentos duplicados descartados")
    print(f"  {resumen['sin_edad']} filas sin edad")
    print(f"  {resumen['sin_fecha']} filas sin fecha de nacimiento")


if __name__ == "__main__":
    main()
