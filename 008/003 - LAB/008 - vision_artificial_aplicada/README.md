# Unidad 008 — Visión Artificial Aplicada

**Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Laboratorio de Tecnologías de la Imagen Digital · Matías Barreto, 2026

Colección de notebooks sobre detección de puntos clave, control gestual e integración de modelos de visión con interfaces web, usando MediaPipe y Gradio.

---

## Contenido

| Notebook | Tema |
|---|---|
| `01_Detección_Puntos_Clave_Faciales` | Face Mesh: 478 landmarks faciales sobre imagen estática |
| `02_Control_Volumen_con_Manos` | Hand Landmarker: control de volumen en tiempo real por gestos |
| `03_Integración_Gradio_y_MediaPipe` | Gradio (Interface / Blocks) + MediaPipe · concepto de Skills |
| `04_Proyecto_Pose_y_Despliegue` | Proyecto integrador: Pose estimation + deploy en HF Spaces + GitHub |

---

## Cómo descargar esta carpeta

Esta es una subcarpeta dentro de un repositorio más grande. Para descargarla sola, sin clonar todo el repositorio, hay dos herramientas web gratuitas que no requieren registro:

### Opción 1 — Download Directory

Una de las opciones más limpias y directas:

1. Copiá el enlace completo de esta carpeta en GitHub o Hugging Face.
2. Entrá en **[download-directory.github.io](https://download-directory.github.io)**.
3. Pegá la URL en el cuadro de búsqueda y presioná Enter.
4. Se va a descargar automáticamente un archivo `.zip` con únicamente esta carpeta y todos sus archivos.

### Opción 2 — DownGit

Alternativa clásica y muy confiable:

1. Entrá en **[downgit.github.io](https://downgit.github.io)**.
2. Pegá el enlace de la carpeta en el campo que dice *GitHub URL*.
3. Hacé clic en el botón **Download**.

---

## Configuración del entorno local

### Requisitos previos

- **Python 3.10 o superior** — [python.org/downloads](https://www.python.org/downloads/)
- **uv** — gestor de entornos virtuales ultrarrápido

> ✦ Esta unidad tiene dependencias ligeras comparadas con la unidad 007.
> La instalación completa demora aproximadamente 2–5 minutos.

---

### Paso 1 — Instalar uv

**Linux / macOS** (terminal):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell):
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternativa universal** (si ya tenés pip):
```bash
pip install uv
```

Verificá la instalación:
```bash
uv --version
```

---

### Paso 2 — Crear el entorno virtual

Desde la carpeta `008 - vision_artificial_aplicada/`:

```bash
uv venv .venv
```

---

### Paso 3 — Activar el entorno

**Linux / macOS:**
```bash
source .venv/bin/activate
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

El prompt de la terminal va a mostrar `(.venv)` cuando el entorno esté activo.

---

### Paso 4 — Instalar las dependencias

```bash
uv pip install -r requirements.txt
```

---

### Paso 5 — Abrir los notebooks

```bash
jupyter lab
```

O si preferís la interfaz clásica:
```bash
jupyter notebook
```

---

## Nota para el notebook 02 — Control de volumen (solo Windows)

El notebook `02_Control_Volumen_con_Manos` usa la API de audio del sistema para controlar el volumen. Esto requiere dos paquetes adicionales **exclusivos de Windows**:

```bash
uv pip install pycaw comtypes
```

En Linux y macOS el loop de detección de manos va a funcionar, pero el control de volumen del sistema no está disponible sin configuración adicional.

---

## Nota para el notebook 04 — Proyecto de deploy

El notebook `04_Proyecto_Pose_y_Despliegue` genera una carpeta con los archivos `app.py` y `requirements.txt` listos para subir a Hugging Face Spaces. Para el deploy necesitás:

- Una cuenta gratuita en [huggingface.co](https://huggingface.co)
- Git instalado en el sistema
- (Opcional) Una cuenta en [github.com](https://github.com) para el repositorio de código

El proceso de deploy completo está documentado en el Cheatsheet de Extras:  
`Extras/Guias/HuggingFace-Spaces/Cheatsheet_Desarrollo_Space.ipynb`

---

## Desactivar el entorno cuando terminás

```bash
deactivate
```
