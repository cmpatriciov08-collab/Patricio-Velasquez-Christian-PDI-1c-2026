# Copilot Instructions — UTN Knowledge Base

## Contexto del proyecto

Material de laboratorio para la materia **Procesamiento Digital de Imágenes** (Tecnicatura Superior en Ciencias de Datos e IA, IFTS24). Los notebooks combinan visión artificial en tiempo real, interfaces web con Gradio y modelos preentrenados de Hugging Face.

## Stack principal

- **MediaPipe** — detección de landmarks (manos, cara, pose)
- **OpenCV** (headless) — procesamiento de frames e imágenes
- **Gradio** — interfaces web interactivas para modelos de visión
- **Hugging Face Transformers** — pipelines de clasificación, zero-shot y detección
- **PyTorch** (CPU) — backend de inferencia
- **JupyterLab** — entorno de ejecución de notebooks

## Convenciones de código

### Idioma
- Comentarios, docstrings y nombres de variables **en español**
- Nombres de funciones y variables en `snake_case` descriptivo en español
- Mensajes de consola con prefijo `✓` para éxito y `✗` para error

### Estructura de apps Gradio (patrón de 3 capas)

Toda aplicación Gradio sigue esta separación obligatoria:

```python
# CAPA 1 — DATA LAYER: carga única del modelo al iniciar
modelo = pipeline("task", model="org/modelo")

# CAPA 2 — BUSINESS LOGIC: función pura, sin referencias a Gradio
def procesar(imagen_entrada):
    resultado = modelo(imagen_entrada)
    return resultado

# CAPA 3 — PRESENTATION LAYER: interfaz declarativa con gr.Blocks
with gr.Blocks() as app:
    ...
    boton.click(fn=procesar, inputs=entrada, outputs=salida)
```

### MediaPipe
- Instanciar el detector **una sola vez** fuera del loop o función de procesamiento
- Usar `static_image_mode=True` para imágenes sueltas, `False` para video
- Trabajar siempre sobre una **copia** de la imagen original antes de dibujar landmarks
- Coordenadas normalizadas (0.0–1.0): multiplicar por `ancho` / `alto` para obtener píxeles

### Loops de webcam (OpenCV)
- Siempre envolver el loop en `try / finally` para liberar `captura.release()`
- Aplicar cambios al sistema operativo cada N frames, nunca en cada frame
- Usar suavizado exponencial para valores continuos (volumen, posición)

## Qué generar y qué evitar

- **Generar:** código autocontenido que corre en una celda de Jupyter sin dependencias externas no declaradas
- **Generar:** funciones con docstring en español explicando parámetros y retorno
- **Evitar:** importar dentro de funciones salvo que sea necesario por conflictos de estado
- **Evitar:** cargar modelos dentro de funciones que se llaman en cada request
- **Evitar:** comentarios que repiten lo que el nombre ya dice

## Notebooks de referencia

| Archivo | Qué enseña |
|---------|-----------|
| `notebooks/01_Entornos_de_Desarrollo.ipynb` | venv vs Docker, cuándo usar cada uno |
| `notebooks/02_Control_Volumen_con_Manos.ipynb` | Hand Landmarker + control de sistema en tiempo real |
| `notebooks/03_Integracion_Gradio_y_MediaPipe.ipynb` | Skills, `gr.Interface`, `gr.Blocks`, Face Mesh |
| `notebooks/04_Proyecto_Pose_y_Despliegue.ipynb` | Pose estimation + deploy a HF Spaces |
| `notebooks/05_Modelos_Preentrenados_HuggingFace.ipynb` | ViT, CLIP zero-shot, DETR con bounding boxes |
| `notebooks/06_Cheatsheet_Desarrollo_Space.ipynb` | Referencia rápida de comandos y componentes |
