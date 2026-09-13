# -*- coding: utf-8 -*-
"""Genera el padrón de beneficiarios usado como ejemplo en la Clase 2.

El archivo es deliberadamente imperfecto: cada defecto corresponde a un
concepto de la clase. Semilla fija -> siempre genera el mismo archivo.

    python generar_padron.py
"""
import csv
import random
from datetime import date

random.seed(2026)

NOMBRES = ["Juan", "María", "Ana", "Carlos", "Luis", "Sofía", "Miguel", "Laura",
           "Diego", "Valeria", "Jorge", "Patricia", "Ricardo", "Silvina",
           "Fernando", "Mariana", "Alberto", "Gabriela", "Sergio", "Natalia",
           "Héctor", "Cecilia", "Rubén", "Andrea", "Oscar", "Verónica",
           "Daniel", "Claudia", "Martín", "Lucía", "Pablo", "Rosa", "Raúl",
           "Elena", "Julio", "Marta", "Ramón", "Norma", "Osvaldo", "Mirta",
           "Emilio", "Beatriz", "Ariel", "Susana", "Nicolás", "Alejandra"]

APELLIDOS = ["Pérez", "Gómez", "López", "Ruiz", "Ferreyra", "Benítez",
             "Ramírez", "Sosa", "Acosta", "Romero", "Fernández", "Vera",
             "Ojeda", "Cabrera", "Escobar", "Godoy", "Maidana", "Aguirre",
             "Núñez", "Ibarra", "Insaurralde", "Zalazar", "Duarte", "Bogado",
             "Almirón", "Meza", "Barrios", "Coronel", "Villalba", "Espínola",
             "Gauna", "Leguizamón", "Miño", "Rolón", "Toledo", "Vallejos",
             "Ayala", "Cáceres", "Fariña", "Giménez", "Ledesma", "Medina",
             "Ortiz", "Paredes", "Sanabria", "Velázquez"]

CALLES = ["Av. Sarmiento", "Av. 9 de Julio", "Belgrano", "San Martín",
          "Güemes", "Juan D. Perón", "Av. Alberdi", "Rivadavia", "Mitre",
          "López y Planes", "Av. Italia", "Ameghino", "Santa María de Oro",
          "Pellegrini", "Av. Los Inmigrantes", "Entre Ríos", "Salta"]

# (localidad, provincia, característica) — plan de numeración argentino
LOCALIDADES = [
    ("Resistencia", "Chaco", "362"),
    ("Barranqueras", "Chaco", "362"),
    ("Fontana", "Chaco", "362"),
    ("Corrientes", "Corrientes", "379"),
    ("Formosa", "Formosa", "370"),
    ("Posadas", "Misiones", "376"),
]
# Características que NO están en el AREAS visto en clase: el quality check
# tiene que encontrarlas y el ejercicio es agregarlas.
LOCALIDADES_RARAS = [
    ("Sáenz Peña", "Chaco", "364"),
    ("Goya", "Corrientes", "3777"),
    ("Clorinda", "Formosa", "3718"),
    ("Oberá", "Misiones", "3755"),
]

HOY = date(2026, 9, 7)


def linea_telefonica(area):
    """Número local: entre área y línea suman 10 dígitos."""
    largo = 10 - len(area)
    return "".join(str(random.randint(0, 9)) for _ in range(largo))


def formato_telefono(area, linea, estilo):
    if estilo == "internacional":
        return f"+54 {area} {linea}"
    if estilo == "parentesis":
        corte = len(linea) // 2
        return f"(0{area}) {linea[:corte]}-{linea[corte:]}"
    if estilo == "celular":
        return f"0{area} 15{linea[:1]} {linea[1:]}"
    return f"{area}{linea}"


def formato_fecha(f, estilo):
    if estilo == "iso":
        return f.isoformat()
    if estilo == "guion_corto":
        return f"{f.day:02d}-{f.month:02d}-{f.year % 100:02d}"
    return f"{f.day:02d}/{f.month:02d}/{f.year}"


def ensuciar_nombre(nombre, estilo):
    if estilo == "minuscula":
        return nombre.lower()
    if estilo == "mayuscula":
        return nombre.upper()
    if estilo == "espacios":
        n, a = nombre.split(" ", 1)
        return f"  {n}  {a} "
    return nombre


def formato_edad(edad, estilo):
    if estilo == "anios":
        return f"{edad} años"
    if estilo == "sd":
        return "s/d"
    if estilo == "vacio":
        return ""
    if estilo == "espacios":
        return f" {edad} "
    return str(edad)


filas = []
documentos = []
for i in range(1, 341):
    # Las primeras tres filas quedan limpias a propósito: un print(filas[:3])
    # no muestra ninguno de los problemas.
    limpia = i <= 3
    rara = i in (58, 141, 199, 268)

    loc, prov, area = random.choice(LOCALIDADES_RARAS if rara else LOCALIDADES)
    nombre = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}"
    documento = str(random.randint(10_000_000, 45_000_000))
    documentos.append(documento)

    nac = date(random.randint(1945, 2005), random.randint(1, 12),
               random.randint(1, 28))
    edad_real = HOY.year - nac.year - ((HOY.month, HOY.day) < (nac.month, nac.day))

    direccion = f"{random.choice(CALLES)} {random.randint(50, 4800)}"
    if not limpia and random.random() < 0.22:            # coma dentro del campo
        direccion += f", Piso {random.randint(1, 8)}"

    if limpia:
        est_tel, est_nom, est_edad, est_fecha = "internacional", "ok", "ok", "barra"
    else:
        est_tel = random.choices(
            ["internacional", "parentesis", "celular", "pegado"],
            weights=[55, 15, 20, 10])[0]
        est_nom = random.choices(["ok", "minuscula", "mayuscula", "espacios"],
                                 weights=[62, 18, 10, 10])[0]
        est_edad = random.choices(["ok", "anios", "sd", "vacio", "espacios"],
                                 weights=[70, 12, 6, 6, 6])[0]
        est_fecha = random.choices(["barra", "iso", "guion_corto"],
                                   weights=[80, 14, 6])[0]

    filas.append({
        "documento": documento,
        "nombre": ensuciar_nombre(nombre, est_nom),
        "direccion": direccion,
        "localidad": loc,
        "provincia": prov,
        "telefono": formato_telefono(area, linea_telefonica(area), est_tel),
        "edad": formato_edad(edad_real, est_edad),
        "fecha_nac": formato_fecha(nac, est_fecha),
    })

# ---- Casos plantados, en las filas que aparecen en las diapositivas ----
filas[0].update(nombre="juan pérez", localidad="Resistencia", provincia="Chaco",
                telefono="+54 362 4451278", edad="45", fecha_nac="12/03/1981")
filas[1].update(nombre="MARÍA GÓMEZ", localidad="Corrientes",
                provincia="Corrientes", telefono="+54 379 4223344",
                edad="38 años", fecha_nac="04/07/1988")
filas[2].update(nombre="ana lopez", localidad="Formosa", provincia="Formosa",
                telefono="+54 370 4421509", edad="52", fecha_nac="03/11/1973")
filas[213].update(nombre="Carlos  Ruiz", localidad="CABA",
                  provincia="Buenos Aires", telefono="+54 11 4567 8901",
                  edad="s/d", fecha_nac="22/09/1966")
filas[286].update(nombre="luis ferreyra", localidad="Posadas",
                  provincia="Misiones", telefono="(0376) 442-1509", edad="62",
                  fecha_nac="18/05/1964")
filas[301].update(nombre="SOFÍA BENÍTEZ", localidad="Resistencia",
                  provincia="Chaco", telefono="0362 154 887766", edad="29",
                  fecha_nac="07/02/1997")

# Nombre cargado "apellido, nombre": obliga a comillas en el CSV
filas[44]["nombre"] = "Pérez, Juan Manuel"
filas[44]["direccion"] = "Av. 9 de Julio 1240, Piso 2"

# Edades fuera de rango: las tiene que descartar limpiar_edad
filas[97]["edad"] = "0"
filas[172]["edad"] = "150"

# Documento duplicado: rompe la primaryKey declarada en la metadata
filas[255]["documento"] = filas[30]["documento"]

COLUMNAS = ["documento", "nombre", "direccion", "localidad", "provincia",
            "telefono", "edad", "fecha_nac"]

with open("padron_beneficiarios.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=COLUMNAS)
    escritor.writeheader()
    escritor.writerows(filas)

print(f"{len(filas)} filas escritas en padron_beneficiarios.csv")