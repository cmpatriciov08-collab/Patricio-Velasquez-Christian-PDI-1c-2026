# Unidad 009 — Modelos de Difusión

**Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Laboratorio de Tecnologías de la Imagen Digital · Matías Barreto, 2026

Colección de 6 notebooks sobre modelos generativos de difusión, que cubren desde los fundamentos teóricos hasta la aceleración mediante LCM-LoRA, optimización para CPU y aplicaciones prácticas (inpainting, super-resolution y transformaciones image-to-image).

> [!IMPORTANT]
> **Ejecución en Google Colab**: Dado que el procesamiento en esta unidad es sumamente exigente a nivel de hardware, todos los cuadernos están optimizados para ejecutarse directamente en **Google Colab** utilizando aceleración por GPU (entorno T4 gratuito o superior). Podés abrir cada cuaderno haciendo clic en el botón correspondiente en la tabla a continuación.

---

## Contenido

| Notebook | Tema | Ejecutar en Colab |
| :--- | :--- | :--- |
| `01_Introduccion_Conceptual_Difusion` | Fundamentos y visualización del proceso de difusión (forward/reverse) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/01_Introduccion_Conceptual_Difusion.ipynb) |
| `02_Paradigmas_y_Modelos_Difusion` | Del paradigma tradicional al generativo, historia y primer demo | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/02_Paradigmas_y_Modelos_Difusion.ipynb) |
| `03_Aplicaciones_Practicas_Difusion` | Inpainting, Super-Resolution e Image-to-Image paso a paso | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/03_Aplicaciones_Practicas_Difusion.ipynb) |
| `04_Text_to_Image_SDXL_Turbo` | Inferencia ultra-rápida de 1024x1024 en un solo paso | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/04_Text_to_Image_SDXL_Turbo.ipynb) |
| `05_Text_to_Image_SDXS_CPU` | Generación text-to-image de baja latencia optimizada para CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/05_Text_to_Image_SDXS_CPU.ipynb) |
| `06_Aceleracion_LCM_LoRA` | Latent Consistency Models y adaptación de bajo rango (LoRA) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mattbarreto/ifts24-lab-pdi-2026/blob/master/009%20-%20modelos_difusion/06_Aceleracion_LCM_LoRA.ipynb) |

---

## Cómo usar en Google Colab (Recomendado)

1. Hacé clic en el botón **Open in Colab** del cuaderno que quieras ejecutar.
2. Si el cuaderno requiere aceleración por hardware (GPU), recordá activarla en Colab:
   - Andá al menú `Entorno de ejecución` (Runtime) → `Cambiar tipo de entorno de ejecución` (Change runtime type).
   - En **Acelerador de hardware** (Hardware accelerator), seleccioná **GPU T4** (o superior si tenés Colab Pro).
3. Recordá ejecutar la primera celda de configuración para instalar las dependencias necesarias (`diffusers`, `transformers`, `accelerate`, `torch`, etc.).

---

## Cómo descargar esta carpeta

Esta es una subcarpeta dentro de un repositorio más grande. Para descargarla sola, sin clonar todo el repositorio, hay dos herramientas web gratuitas que no requieren registro:

### Opción 1 — Download Directory

Una de las opciones más limpias y directas:

1. Copiá el enlace completo de esta carpeta en GitHub.
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

Si contás con una GPU dedicada potente en tu máquina local y preferís correr los cuadernos sin conexión:

### Requisitos previos

- **Python 3.10 o superior** — [python.org/downloads](https://www.python.org/downloads/)
- **uv** — gestor de entornos virtuales ultrarrápido

> ✦ La instalación local requiere descargar modelos preentrenados grandes (que van de 1 GB a 7 GB según el modelo). Se recomienda una conexión estable a internet y al menos 15 GB de espacio libre en disco para almacenar los checkpoints en caché.

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

Desde la carpeta `009 - modelos_difusion/`:

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

Se recomienda instalar las dependencias básicas utilizando el gestor de paquetes de la raíz o instalando de forma directa:

```bash
uv pip install diffusers transformers accelerate torch pillow matplotlib numpy requests
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

## Notas sobre Hardware y Optimización

- **GPU con 8 GB o más de VRAM**: Podés correr `04_Text_to_Image_SDXL_Turbo` y `06_Aceleracion_LCM_LoRA` en alta resolución (1024x1024) sin problemas.
- **GPU con 4 a 6 GB de VRAM**: Se recomienda utilizar las optimizaciones de memoria detalladas en el cuaderno `04_Text_to_Image_SDXL_Turbo` (`enable_model_cpu_offload()` y `enable_vae_tiling()`), o correr `06_Aceleracion_LCM_LoRA` utilizando la versión basada en **Stable Diffusion 1.5** (resolución 512x512).
- **Sin GPU (Solo CPU)**: El cuaderno `05_Text_to_Image_SDXS_CPU` está especialmente configurado para correr en CPU con el modelo comprimido SDXS-512, requiriendo menos de 1 segundo por paso en procesadores modernos.

---

## Desactivar el entorno cuando terminás

```bash
deactivate
```
