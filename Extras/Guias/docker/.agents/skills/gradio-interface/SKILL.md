---
name: "gradio-interface"
description: "Construir interfaces web con Gradio usando gr.Interface o gr.Blocks, siguiendo el patrón de 3 capas."
tags: [gradio, interface, web, python, deployment]
---

# Skill: Gradio Interface

## Cuándo usar esta skill

Cuando el agente necesita construir una interfaz web para un modelo de visión artificial o función Python, ya sea para prototipo rápido (`gr.Interface`) o layout personalizado (`gr.Blocks`).

---

## Patrón rápido: `gr.Interface`

Ideal para una sola función con entradas y salidas fijas.

```python
import gradio as gr

def procesar(imagen):
    # lógica de negocio
    return imagen_procesada

interfaz = gr.Interface(
    fn=procesar,
    inputs=gr.Image(label="Entrada", type="numpy"),
    outputs=gr.Image(label="Resultado"),
    title="Nombre de la app",
    description="Descripción breve.",
    flagging_mode="never"
)

interfaz.launch()
```

---

## Patrón completo: `gr.Blocks` (3 capas)

Para apps con layout personalizado o múltiples funciones.

```python
import gradio as gr
from transformers import pipeline

# ── CAPA 1: carga única del modelo ──────────────────────────────────────
modelo = pipeline("image-classification", model="google/vit-base-patch16-224")

# ── CAPA 2: lógica de negocio ───────────────────────────────────────────
def clasificar(imagen):
    if imagen is None:
        return "Sin imagen."
    resultados = modelo(imagen)
    return {r["label"]: float(r["score"]) for r in resultados[:5]}

# ── CAPA 3: interfaz declarativa ────────────────────────────────────────
with gr.Blocks(title="Clasificador") as app:
    gr.Markdown("## Título de la aplicación")

    with gr.Row():
        entrada = gr.Image(type="pil", label="Imagen")
        salida  = gr.Label(label="Predicciones")

    boton = gr.Button("Analizar", variant="primary")
    boton.click(fn=clasificar, inputs=entrada, outputs=salida)

if __name__ == "__main__":
    app.launch()
```

---

## Componentes de referencia

```python
# Entradas
gr.Image(type="numpy")          # array NumPy RGB
gr.Image(type="pil")            # objeto PIL
gr.Textbox()                    # texto libre
gr.Slider(minimum=0, maximum=1) # deslizador numérico
gr.Radio(choices=[...])         # selección exclusiva

# Salidas
gr.Image()                      # imagen procesada
gr.Label()                      # clasificación con barras de confianza
gr.Textbox()                    # texto o métricas
gr.JSON()                       # diccionario estructurado

# Layout
gr.Row()     # componentes en fila horizontal
gr.Column()  # componentes en columna vertical
gr.Tab()     # pestañas
```

---

## Reglas

- El modelo se carga **una vez** en la capa 1, nunca dentro de la función.
- La función de la capa 2 no importa ni referencia `gr` — es Python puro testeable.
- Los `outputs` del `.click()` deben coincidir **en orden y cantidad** con el `return` de la función.
- Para deploy en HF Spaces, el archivo se llama `app.py` y termina con `app.launch()`.
