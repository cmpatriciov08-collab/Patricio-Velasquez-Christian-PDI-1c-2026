#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Análisis de texto impreso con TrOCR (Microsoft)
Modelo: microsoft/trocr-base-printed

Uso:
    1. Colocá tu imagen en la carpeta "img/"
    2. Ejecutá: python analizar_texto_impreso.py
"""

import os
import sys

# Verificar que existe la carpeta img
if not os.path.exists("img"):
    os.makedirs("img")
    print("✓ Carpeta 'img/' creada.")
    print("⚠ Colocá tu imagen con texto impreso dentro de 'img/' antes de continuar.")
    sys.exit(1)

# Verificar que hay al menos una imagen
imagenes = [f for f in os.listdir("img") if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
if not imagenes:
    print("⚠ No se encontraron imágenes en 'img/'.")
    print("   Colocá una imagen con texto impreso (.png, .jpg, etc.)")
    sys.exit(1)

print("✓ Imagen encontrada:", imagenes[0])

# Instalar dependencias (solo si es necesario)
try:
    import torch
    import transformers
    from PIL import Image
    import matplotlib.pyplot as plt
    print("✓ Dependencias ya instaladas.")
except ImportError:
    print("\nInstalando dependencias necesarias...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "transformers", "torch", "pillow", "matplotlib", "-q"])
    print("✓ Dependencias instaladas.")
    
    # Importar nuevamente
    import torch
    import transformers
    from PIL import Image
    import matplotlib.pyplot as plt

# Importar TrOCR
from transformers import TrOCRProcessor, TrOCRForVision2Seq

print("\n" + "="*60)
print("ANÁLISIS DE TEXTO IMPRESO CON TrOCR")
print("="*60)

# Cargar el modelo (se descarga la primera vez ~1.6 GB)
print("\n⏳ Cargando modelo 'microsoft/trocr-base-printed'...")
print("   (Primera vez: descarga ~1.6 GB. Paciencia.)")

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = TrOCRForVision2Seq.from_pretrained("microsoft/trocr-base-printed")

print("✓ Modelo cargado.")

# Cargar y procesar la imagen
ruta_imagen = os.path.join("img", imagenes[0])
print(f"\n📷 Procesando imagen: {ruta_imagen}")

imagen = Image.open(ruta_imagen).convert("RGB")

# Mostrar la imagen
plt.figure(figsize=(10, 6))
plt.imshow(imagen)
plt.title("Imagen de entrada")
plt.axis("off")
plt.show()

# Preparar para el modelo
pixel_values = processor(images=imagen, return_tensors="pt").pixel_values

# Generar texto
print("\n⏳ Reconociendo texto...")
with torch.no_grad():
    generated_ids = model.generate(pixel_values)

texto_reconocido = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("\n" + "="*60)
print("TEXTO RECONOCIDO:")
print("="*60)
print(texto_reconocido)
print("="*60)

# Guardar resultado
with open("resultado_ocr.txt", "w", encoding="utf-8") as f:
    f.write(texto_reconocido)
print("\n✓ Resultado guardado en 'resultado_ocr.txt'")
