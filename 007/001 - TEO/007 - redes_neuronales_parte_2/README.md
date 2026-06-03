# Unidad 007 — Redes Neuronales (Parte 2)

**Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Laboratorio de Tecnologías de la Imagen Digital · Matías Barreto, 2026

Colección de 10 notebooks que cubren redes neuronales densas, redes convolucionales, modelos preentrenados, Hugging Face, despliegue con Gradio y OCR crítico.

---

## Contenido

| Notebook | Tema |
|---|---|
| `01_Fundamentos_Red_Neuronal_Simple` | Perceptrón, propagación hacia adelante y función de pérdida |
| `02_Clasificacion_Letras_MLP` | Red densa (MLP) sobre el dataset EMNIST |
| `03_Clasificacion_Letras_CNN` | Red convolucional (CNN) sobre EMNIST |
| `04_Visualizacion_Filtros_y_Activaciones_CNN` | Interpretabilidad: filtros y mapas de activación |
| `05_Clasificacion_Preentrenados_ResNet18` | Inferencia con ResNet18 preentrenada (PyTorch) |
| `06_Transfer_Learning_MobileNetV2` | Transfer Learning con MobileNetV2 (Keras / TensorFlow) |
| `07_Modelos_Preentrenados_HuggingFace` | ViT, CLIP y DETR desde 🤗 Transformers |
| `08_Laboratorio_Desarrollo_Space_Gradio` | De Jupyter Notebook a Hugging Face Space con Gradio |
| `09_Laboratorio_Integrador_Redes` | Proyecto integrador de la unidad |
| `10_Laboratorio_OCR_Investigacion_Critica` | OCR con modelos de IA y análisis crítico de los resultados |

La carpeta `datos/` contiene los archivos de soporte usados por los notebooks (imágenes de ejemplo, datasets locales).

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

> ✦ Esta unidad usa TensorFlow y PyTorch simultáneamente. La instalación puede
> demorar varios minutos dependiendo de la conexión. Se recomienda una conexión
> estable y al menos 5 GB de espacio libre en disco.

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

Desde la carpeta `007 - redes_neuronales_parte_2/`:

```bash
uv venv .venv
```

Esto crea una carpeta `.venv/` con un entorno Python aislado, sin tocar el Python del sistema.

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

> La primera instalación descarga TensorFlow, PyTorch y los modelos de Hugging Face.
> Puede tomar entre 5 y 15 minutos según la conexión.

---

### Paso 5 — Abrir los notebooks

```bash
jupyter lab
```

O si preferís la interfaz clásica:
```bash
jupyter notebook
```

Se va a abrir una pestaña en el navegador con todos los notebooks de la carpeta.

---

## Notas importantes

**Sobre `from google.colab import ...`**  
Algunos notebooks tienen líneas como `from google.colab import drive` o `from google.colab import files`. Esas líneas son específicas de Google Colab y van a generar un error al ejecutarse localmente. Se pueden comentar o eliminar — solo afectan la subida de archivos en Colab y no alteran la lógica del notebook.

**Sobre GPU**  
Los notebooks funcionan en CPU, pero el entrenamiento de redes convolucionales (notebooks 03 y 06) va a ser considerablemente más lento sin GPU. Para acelerar, podés usar Google Colab (gratuito con GPU) o una máquina con CUDA.

**Sobre versiones de Python**  
TensorFlow 2.15+ requiere Python 3.9–3.11. Si tenés Python 3.12 o superior, especificá la versión al crear el entorno:

```bash
uv venv .venv --python 3.11
```

**Sobre la carpeta `datos/`**  
La carpeta `datos/` debe estar en el mismo nivel que los notebooks. Si la descarga sola (sin el resto de la carpeta), algunos notebooks no van a encontrar los archivos de ejemplo. Download Directory y DownGit descargan la carpeta completa, incluyendo `datos/`.

---

## Desactivar el entorno cuando terminás

```bash
deactivate
```
