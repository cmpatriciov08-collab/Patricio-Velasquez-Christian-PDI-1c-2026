---
name: "hf-pipeline"
description: "Usar pipelines de Hugging Face para clasificación de imágenes (ViT), clasificación zero-shot (CLIP) y detección de objetos (DETR)."
tags: [huggingface, transformers, pipeline, vit, clip, detr, vision]
---

# Skill: Hugging Face Pipeline

## Cuándo usar esta skill

Cuando el agente necesita aplicar modelos de visión preentrenados sin entrenar desde cero: clasificar imágenes, buscar categorías en lenguaje natural o detectar objetos con bounding boxes.

---

## Los tres modelos del curso

### ViT — Clasificación general

Clasifica imágenes en **1000 categorías de ImageNet**. Rápido y preciso para objetos comunes.

```python
from transformers import pipeline
from PIL import Image

clasificador = pipeline("image-classification", model="google/vit-base-patch16-224")

imagen = Image.open("foto.jpg")
resultados = clasificador(imagen)

for r in resultados[:5]:
    print(f"{r['label']:30s} → {r['score']:.1%}")
```

---

### CLIP — Clasificación zero-shot

Clasifica imágenes en **categorías definidas en tiempo de ejecución** con lenguaje natural. No necesita reentrenamiento.

```python
from transformers import pipeline

clip = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

etiquetas = [
    "auriculares sobre fondo cálido",
    "computadora portátil encendida",
    "persona escuchando música"
]

resultados = clip(imagen, candidate_labels=etiquetas)

for r in resultados:
    print(f"{r['label']:35s} → {r['score']:.1%}")
```

---

### DETR — Detección de objetos

Detecta y **localiza múltiples objetos** en una imagen con bounding boxes y coordenadas exactas. 91 categorías COCO.

```python
from transformers import pipeline

detector = pipeline("object-detection", model="facebook/detr-resnet-50")

detecciones = detector(imagen)

for d in detecciones:
    caja = d["box"]
    print(f"{d['label']:15s} {d['score']:.1%} → "
          f"({caja['xmin']},{caja['ymin']}) - ({caja['xmax']},{caja['ymax']})")
```

---

## Tabla comparativa

| | ViT | CLIP | DETR |
|--|-----|------|------|
| Categorías | 1000 fijas (ImageNet) | Infinitas (texto libre) | 91 fijas (COCO) |
| Localización espacial | No | No | Sí (bounding boxes) |
| Velocidad | Alta | Alta | Moderada |
| Caso de uso | Índice general de imágenes | Búsqueda semántica | Robótica, inventario |

---

## Reglas

- Instanciar el pipeline **una sola vez**; cada llamada descarga los pesos si no están en caché.
- Para CPU usar `torch>=2.0 --index-url https://download.pytorch.org/whl/cpu` (mucho más liviano).
- CLIP requiere al menos **2 etiquetas** en `candidate_labels`.
- Para DETR filtrar por `score >= 0.7` para evitar falsos positivos.
