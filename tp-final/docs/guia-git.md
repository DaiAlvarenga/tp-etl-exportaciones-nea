# Guía Git y GitHub — Cómo entregar el TP Final

**Unidad II · Fundamentos de la Programación**

Esta guía te lleva desde bajar el template hasta entregar el link de tu
repositorio. Si nunca usaste Git, seguila en orden: son 15 minutos.

---

## Primero: los dos lugares donde vas a trabajar

Todo lo de esta guía pasa en **uno de estos dos lugares**. En cada paso te
vamos a decir cuál de los dos usar, así no te perdés.

| Lugar | Qué es | Cómo se ve |
|---|---|---|
| **NAVEGADOR** | La página web de GitHub (`github.com`), abierta en Chrome, Firefox o el que uses. Ahí se hace todo lo visual: crear el repositorio, mirar tus archivos, copiar el link. | Botones y menús |
| **TERMINAL de VS Code** | Una consola de texto dentro de VS Code. Ahí van todos los comandos que empiezan con `git`. | Texto y comandos |

Regla simple: **si el paso tiene un botón, es el navegador. Si tiene un
comando, es la terminal.**

### Cómo abrir la carpeta del proyecto en VS Code

1. Abrí **VS Code**.
2. Menú **File → Open Folder…** (en Mac: **Archivo → Abrir carpeta…**).
3. Elegí la carpeta de tu proyecto (la que descomprimiste del ZIP).
4. Aceptá si te pregunta si confiás en los autores de la carpeta.

En el panel de la izquierda tenés que ver `src/`, `tests/`, `config.py`, etc.

### Cómo abrir la terminal en VS Code

Menú **Terminal → New Terminal** (o **Terminal → Nueva terminal**).

También con el atajo:

| Sistema | Atajo |
|---|---|
| Windows / Linux | `Ctrl` + `ñ` — o `Ctrl` + la tecla de acento grave |
| Mac | `Cmd` + `ñ` — o `Ctrl` + la tecla de acento grave |

Se abre un panel abajo con una línea de texto donde vas a escribir los comandos.

> **Importante:** si abriste la carpeta del proyecto como se explicó arriba, la terminal ya arranca parada ahí. No necesitás hacer `cd` a ningún lado. Para confirmarlo, escribí `dir` (Windows) o `ls` (Mac/Linux) y fijate que aparezcan `src`, `tests` y `config.py`.

---

## Antes de empezar

Necesitás dos cosas.

**1. Git instalado.**

**En la TERMINAL de VS Code**, escribí:

```bash
git --version
```

Si te responde algo como `git version 2.43.0`, ya lo tenés. Si dice que el
comando no existe, instalalo desde
[git-scm.com/downloads](https://git-scm.com/downloads) y **cerrá y volvé a
abrir VS Code** después de instalarlo.

**2. Una cuenta en GitHub.**

**En el NAVEGADOR**, creá una cuenta gratis en
[github.com](https://github.com) si todavía no tenés.

### Configuración inicial (una sola vez en tu vida)

**En la TERMINAL de VS Code:**

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

Usá el **mismo email** que registraste en GitHub: así tus commits quedan
asociados a tu perfil.

---

## Paso 1 — Descargar el template

**En el NAVEGADOR:**

1. Entrá al repositorio de la materia: `https://github.com/daianadte24/diplo_data-analytics_unne`
2. Arriba a la izquierda del listado de archivos hay un desplegable que dice `main`. Hacé clic y elegí la branch **`tp-final`**.
3. Botón verde **`Code`** → **`Download ZIP`**.

**En tu computadora (explorador de archivos, todavía no VS Code):**

4. Descomprimí el ZIP. Se crea una carpeta llamada `diplo_data-analytics_unne-tp-final`.
5. Entrá a esa carpeta y después a `tp-final/`.
6. Adentro vas a ver `template/` y `docs/`. Copiá **solo la carpeta `template/`** a donde guardás tus proyectos y renombrala, por ejemplo `tp-final-etl`.
7. El resto del ZIP ya no lo necesitás: la documentación la podés leer online desde GitHub.

**En VS Code:**

8. **File → Open Folder…** y abrí `tp-final-etl`.

---

## Paso 2 — Probar que funciona antes de tocar nada

**En la TERMINAL de VS Code:**

```bash
python src/main.py
```

> Si `python` no funciona, probá con `python3`. En Windows a veces es `py`.

Tiene que descargar los datos y **cortar en el TODO 1** con este mensaje:

```
NotImplementedError: TODO 1: implementá ancho_a_largo()
```

Eso está **bien**: significa que el Extract funcionó, bajó los datos a
`data/raw/`, y ahora te toca a vos. Si en cambio ves un error de conexión,
revisá tu internet.

---

## Paso 3 — Convertirlo en tu repositorio

**En la TERMINAL de VS Code**, parado en la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Punto de partida: template del TP final"
```

Qué hizo cada comando:

| Comando | Qué hace |
|---|---|
| `git init` | Crea el repositorio: a partir de acá Git registra los cambios |
| `git add .` | Marca los archivos que querés incluir en la próxima foto |
| `git commit -m "..."` | Saca la foto y le pone un mensaje |

> El template ya trae un `.gitignore` que deja afuera `data/`, `logs/` y `__pycache__/`. Los datos se regeneran corriendo el pipeline: no van al repositorio.

---

## Paso 4 — Crear el repositorio en GitHub

**En el NAVEGADOR:**

1. En GitHub, botón **`+`** arriba a la derecha → **`New repository`**.
2. En *Repository name*, poné un nombre: por ejemplo `tp-final-etl-nea`.
3. Elegí **Public**.
4. **No marques** ninguna de las casillas de "Initialize this repository" (ni README, ni .gitignore, ni licencia). Tu proyecto ya los tiene.
5. Botón **`Create repository`**.

GitHub te muestra una página con comandos. **No la cierres**: vas a copiar
la dirección de tu repositorio de ahí.

---

## Paso 5 — Subirlo por primera vez

**En la TERMINAL de VS Code:**

```bash
git remote add origin https://github.com/TU-USUARIO/tp-final-etl-nea.git
git branch -M main
git push -u origin main
```

Reemplazá `TU-USUARIO` y el nombre del repositorio por los tuyos (están en
la dirección que te mostró GitHub en el paso anterior).

**En el NAVEGADOR:** recargá la página de tu repositorio. Tus archivos
tienen que estar ahí.

> **Si te pide usuario y contraseña:** GitHub ya no acepta la contraseña de la cuenta desde la terminal. **En el NAVEGADOR**, generá un token en *Settings → Developer settings → Personal access tokens → Tokens (classic)*, con el permiso `repo`. Copialo y, **en la TERMINAL**, pegalo cuando te pida la contraseña. (Al pegarlo no vas a ver nada escrito: es normal, la terminal oculta las contraseñas.)

---

## Paso 6 — Trabajar y commitear a medida que avanzás

Este es el ciclo que vas a repetir. **Un commit por TODO resuelto** es un
buen ritmo, y se evalúa.

**En el EDITOR de VS Code:** resolvés el TODO 1 en `src/transform.py` y
guardás con `Ctrl` + `S` (Mac: `Cmd` + `S`).

**En la TERMINAL de VS Code:**

```bash
python tests/test_transform.py
```

Si los tests de ese TODO pasan, guardás el avance:

```bash
git status
git add src/transform.py
git commit -m "Implementa ancho_a_largo: pasa los datos a formato largo"
git push
```

Y volvés al editor para el TODO siguiente.

### Mensajes de commit

Un buen mensaje dice **qué cambió**, en presente y en pocas palabras.

| Mal | Bien |
|---|---|
| `cambios` | `Implementa el join con rubros por provincia y año` |
| `update` | `Corrige el ranking: ahora se calcula por año` |
| `asdf` | `Agrega quality check de unicidad` |
| `subo todo` | `Completa construir_resumen con estadísticas básicas` |

---

## Paso 7 — Antes de entregar

**En la TERMINAL de VS Code:**

```bash
git status
git log --oneline
git push
```

- `git status` no debe mostrar nada pendiente.
- `git log --oneline` te muestra tu historial: fijate que se entienda el avance.

Deberías ver algo así:

```
a1b2c3d Escribe los tests del TODO 13
e4f5g6h Completa el resumen JSON y el log
i7j8k9l Agrega quality checks de unicidad y rangos
m0n1o2p Implementa el join con rubros
q3r4s5t Implementa el ranking por provincia y año
u6v7w8x Implementa variación interanual
y9z0a1b Implementa las derivadas simples
c2d3e4f Implementa ancho_a_largo
g5h6i7j Punto de partida: template del TP final
```

**En el NAVEGADOR:** abrí el link de tu repositorio en una **ventana de
incógnito**. Si se ve sin pedirte iniciar sesión, está público y listo.

---

## Entrega

**En el NAVEGADOR:** copiá el link de tu repositorio desde la barra de
direcciones y entregalo por el campus.

```
https://github.com/TU-USUARIO/tp-final-etl-nea
```

---

## Problemas frecuentes

Todos estos se resuelven **en la TERMINAL de VS Code**.

**"Subí sin querer la carpeta `data/`"**

```bash
git rm -r --cached data/
git commit -m "Saca los datos del repositorio"
git push
```

**"Me equivoqué en el mensaje del último commit"**

```bash
git commit --amend -m "El mensaje corregido"
```

(Solo si todavía no hiciste `push`.)

**"`git push` me rechaza el cambio"**

Alguien —o vos desde otra máquina— subió algo antes. Traé lo de allá primero:

```bash
git pull --rebase
git push
```

**"Quiero ver qué cambié antes de commitear"**

```bash
git diff
```

**"Me perdí y quiero volver al último commit"**

```bash
git checkout -- archivo.py
```

Descarta los cambios de ESE archivo. Cuidado: borra lo que no commiteaste.

**"La terminal dice que no encuentra `src/main.py`"**

Estás parado en otra carpeta. Fijate dónde estás con `dir` (Windows) o
`ls` (Mac/Linux): tenés que ver `src`, `tests` y `config.py`. Si no los
ves, cerrá VS Code y volvé a abrir la carpeta del proyecto con
**File → Open Folder…**.

---

## Los cinco comandos que vas a usar el 95% del tiempo

Todos van **en la TERMINAL de VS Code**.

| Comando | Para qué |
|---|---|
| `git status` | ¿Qué cambié? |
| `git add <archivo>` | Preparar un cambio |
| `git commit -m "..."` | Guardar la foto |
| `git push` | Subir a GitHub |
| `git log --oneline` | Ver el historial |

---

## Resumen: qué se hace en cada lugar

| Paso | Dónde |
|---|---|
| 1. Descargar el ZIP del template | NAVEGADOR |
| 1. Descomprimir y abrir la carpeta | Explorador + VS Code |
| 2. Probar el pipeline | TERMINAL |
| 3. `git init`, `add`, `commit` | TERMINAL |
| 4. Crear el repositorio | NAVEGADOR |
| 5. `remote add`, `push` | TERMINAL |
| 6. Programar y guardar | EDITOR |
| 6. Tests y commits | TERMINAL |
| 7. Verificar que se ve público | NAVEGADOR |
| Entrega: copiar el link | NAVEGADOR |

---

*Más sobre Git, en español y gratis: [git-scm.com/book/es](https://git-scm.com/book/es)*
