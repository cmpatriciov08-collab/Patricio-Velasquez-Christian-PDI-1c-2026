# UTN Knowledge Base

Materiales de laboratorio para la **Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Materia: *Procesamiento Digital de Imágenes*  
Autor: Matías Barreto, 2026

---

## Notebooks

| # | Notebook | Contenido |
|---|----------|-----------|
| 01 | `Entornos_de_Desarrollo` | Entornos virtuales vs Docker: cuándo usar cada uno |
| 02 | `Control_Volumen_con_Manos` | MediaPipe Hand Landmarker + control de volumen en tiempo real |
| 03 | `Integracion_Gradio_y_MediaPipe` | Skills, `gr.Interface`, `gr.Blocks`, Face Mesh en Gradio |
| 04 | `Proyecto_Pose_y_Despliegue` | MediaPipe Pose + deploy en Hugging Face Spaces |
| 05 | `Modelos_Preentrenados_HuggingFace` | ViT, CLIP (zero-shot) y DETR con `pipeline` de HF |
| 06 | `Cheatsheet_Desarrollo_Space` | Referencia rápida: git, Gradio, Transformers, 3 capas |

---

## Opción A — Docker (recomendado para clase)

Levanta JupyterLab con todas las dependencias ya instaladas.

```bash
# Primera vez (construye la imagen, ~10 min por torch)
docker compose up --build

# Las siguientes veces
docker compose up
```

Abrí **http://localhost:8888** — token: `clase`

> **Nota:** el notebook 02 usa webcam y audio del sistema. Esas funciones no funcionan dentro del contenedor. Usá la Opción B para ese notebook.

---

## Opción B — VSCode (local, recomendado para notebook 02)

### Requisitos previos

- Python 3.10 o 3.11
- Extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) en VSCode
- Extensión [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) en VSCode

### Setup

```bash
# 1. Clonar el repo
git clone https://github.com/kobogithub/utn_knowledge_base.git
cd utn_knowledge_base

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar el entorno
# macOS / Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt
```

### Abrir los notebooks

```bash
# Desde VSCode
code .
```

Luego abrí cualquier `.ipynb` desde la carpeta `notebooks/`.  
VSCode va a pedir seleccionar el kernel — elegí el entorno `.venv` que creaste.

### Notebook 02 en Windows

El control de volumen en Windows requiere `pycaw`:

```bash
pip install pycaw comtypes
```

---

## Agentes y Skills (IA)

El repo incluye definiciones para trabajar con agentes de IA (Copilot, Claude, HF Agents):

```
.github/
└── copilot-instructions.md   # instrucciones de contexto para GitHub Copilot

agents/
├── vision-lab-assistant.md   # ayuda con MediaPipe, Gradio y TODOs de los labs
└── deploy-assistant.md       # migra notebooks a app.py y guía el deploy

skills/
├── mediapipe-vision/         # landmarks de manos, cara y pose
├── gradio-interface/         # gr.Interface, gr.Blocks, patrón 3 capas
├── hf-pipeline/              # ViT, CLIP zero-shot, DETR
└── hf-spaces-deploy/         # git + HF Spaces + doble remote GitHub
```

---

## Dependencias principales

| Librería | Uso |
|----------|-----|
| `mediapipe` | Detección de landmarks (manos, cara, pose) |
| `opencv-python-headless` | Procesamiento de imágenes |
| `gradio` | Interfaces web interactivas |
| `transformers` | Modelos preentrenados de HuggingFace |
| `torch` (CPU) | Backend para modelos de HF |
