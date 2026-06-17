---
name: "hf-spaces-deploy"
description: "Desplegar una aplicación Gradio en Hugging Face Spaces con git, requirements.txt y README.md con frontmatter YAML."
tags: [huggingface, spaces, gradio, deploy, git]
---

# Skill: Hugging Face Spaces Deploy

## Cuándo usar esta skill

Cuando el agente necesita publicar una aplicación Gradio en Hugging Face Spaces para que sea accesible desde cualquier navegador, sin que el usuario instale nada.

---

## Estructura mínima del Space

```
mi-space/
├── app.py              # punto de entrada (obligatorio)
├── requirements.txt    # dependencias (obligatorio)
└── README.md           # frontmatter YAML (obligatorio)
```

---

## README.md con frontmatter

```markdown
---
title: Nombre de la Aplicación
emoji: 🔍
colorFrom: gray
colorTo: slate
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
---

# Descripción breve de la app
```

---

## requirements.txt mínimo

```
gradio>=4.0.0
transformers>=4.35.0
torch>=2.0.0
pillow>=10.0.0
mediapipe>=0.10.0
opencv-python-headless>=4.8.0
```

---

## Comandos de deploy

```bash
# 1. Crear el Space en https://huggingface.co/new-space
#    SDK: Gradio | Hardware: CPU free

# 2. Inicializar y subir
git init
git add .
git commit -m "feat: deploy inicial"
git remote add origin https://huggingface.co/spaces/TU_USUARIO/TU_SPACE
git branch -M main
git push -u origin main

# 3. Actualizaciones posteriores
git add .
git commit -m "fix: descripción del cambio"
git push
```

---

## Doble remote: HF Spaces + GitHub

```bash
git remote add origin  https://huggingface.co/spaces/USUARIO/SPACE
git remote add github  https://github.com/USUARIO/REPO

git push origin main   # → Hugging Face (ejecuta la app)
git push github main   # → GitHub (código fuente versionado)
```

---

## Checklist antes de hacer push

- [ ] `app.py` termina con `app.launch()` (sin `share=True`)
- [ ] `requirements.txt` lista todas las dependencias con versión mínima
- [ ] El modelo se carga en la **Capa 1**, fuera de la función de procesamiento
- [ ] `README.md` tiene el frontmatter YAML con `sdk: gradio`
- [ ] No hay rutas absolutas ni variables de entorno locales en el código

---

## Reglas

- Usar `opencv-python-headless` (no `opencv-python`) para evitar errores en servidores sin display.
- El hardware **CPU free** de HF Spaces no tiene GPU — evitar modelos que requieran CUDA.
- Si el Space tarda en cargar la primera vez, es normal: está instalando dependencias.
- Los logs del Space se ven en la pestaña **Logs** del Space en huggingface.co.
