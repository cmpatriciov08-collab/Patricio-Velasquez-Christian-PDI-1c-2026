---
name: "railway-deploy"
description: "Desplegar una aplicación (Gradio, FastAPI, Flask) en Railway usando el MCP de Railway para automatizar CI/CD."
tags: [railway, deployment, mcp, gradio, fastapi, docker, devops]
---

# Skill: Railway Deploy

## Cuándo usar esta skill

Cuando el agente necesita:
- Desplegar una app Python (Gradio, FastAPI, Flask) en Railway de forma automática
- Automatizar el flujo de CI/CD mediante el MCP de Railway
- Usar variables de entorno secretas en producción
- Crear PostgreSQL o Redis adicionales directamente desde el deploy
- Monitorear logs y métricas en tiempo real

---

## Estructura mínima del proyecto para Railway

```
mi-app/
├── app.py                 # punto de entrada (Gradio, FastAPI, etc)
├── requirements.txt       # dependencias Python
├── railway.json           # configuración de Railway (opcional pero recomendado)
├── Dockerfile             # para control total (opcional)
├── README.md              # descripción
└── .gitignore             # excluir archivos sensibles
```

---

## Configuración mínima: `requirements.txt`

```
gradio>=4.0.0
fastapi>=0.104.0
uvicorn>=0.24.0
transformers>=4.35.0
torch>=2.0.0
opencv-python-headless>=4.8.0
```

---

## Railway MCP: Instalación y Setup

### 1. Instalar Railway CLI

```bash
# macOS / Linux
curl -fsSL https://railway.app/install.sh | bash

# Windows (PowerShell)
iwr https://railway.app/install.ps1 -useb | iex
```

### 2. Autenticación con Railway MCP

```bash
# Login a Railway y guardar token
railway login

# Verificar sesión activa
railway whoami
```

### 3. Crear proyecto en Railway (local o desde CLI)

```bash
# Inicializar un nuevo proyecto Railway
railway init

# O enlazar a un proyecto existente
railway link <project-id>
```

---

## Configuración de Railway con MCP

### `railway.json` (Declarativo)

```json
{
  "buildCommand": "pip install -r requirements.txt",
  "startCommand": "python app.py",
  "enviroment": "production",
  "domains": [
    {
      "name": "mi-app",
      "baseDomain": "railway.app"
    }
  ]
}
```

### Parámetros clave:

| Parámetro | Descripción |
|-----------|-------------|
| `buildCommand` | Comando que ejecuta Railway antes de iniciar la app |
| `startCommand` | Comando para iniciar la aplicación |
| `domains` | Dominio público accesible desde el navegador |
| `environment` | `production` o `staging` |
| `rootDirectory` | Carpeta raíz si no está en la raíz del repo (ej: `"./backend"`) |

---

## Deploy con MCP Automation

### Flujo de deploy automático (GitHub Actions + Railway MCP)

```yaml
name: Deploy a Railway
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Instalar Railway CLI
        run: curl -fsSL https://railway.app/install.sh | bash
      
      - name: Deploy a Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: railway up
```

### Obtener y guardar `RAILWAY_TOKEN`:

1. Ir a https://railway.app/account/tokens
2. Crear nuevo token (seleccionar alcance "Project Admin")
3. Copiar el token y agregarlo a GitHub Secrets como `RAILWAY_TOKEN`

---

## Ejemplo 1: Desplegar app Gradio

### `app.py`

```python
import gradio as gr
import os

def clasificar_imagen(imagen):
    # Lógica de procesamiento
    return {"clase": "ejemplo", "confianza": 0.95}

with gr.Blocks() as app:
    gr.Markdown("# Clasificador de Imágenes")
    
    with gr.Row():
        entrada = gr.Image(label="Sube una imagen", type="pil")
        salida = gr.JSON(label="Resultado")
    
    entrada.change(fn=clasificar_imagen, inputs=entrada, outputs=salida)

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", "7860"))
    app.launch(server_name="0.0.0.0", server_port=puerto, share=False)
```

### `requirements.txt`

```
gradio==4.44.1
transformers==4.35.0
torch==2.0.0
Pillow==10.0.0
```

### Deploy:

```bash
railway up
```

---

## Ejemplo 2: Desplegar FastAPI

### `app.py`

```python
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Vision API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Lógica de predicción
    return {"resultado": "éxito"}

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    puerto = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=puerto)
```

### Deploy:

```bash
railway up
```

---

## Variables de Entorno en Railway

### Desde la CLI:

```bash
# Agregar variable
railway variables set API_KEY="valor_secreto"

# Ver variables
railway variables list

# Eliminar variable
railway variables delete API_KEY
```

### En el Dashboard:

1. Entrar a https://railway.app/dashboard
2. Seleccionar proyecto → Variables
3. Agregar clave-valor
4. Railway redeploya automáticamente

---

## Estructura con múltiples servicios

```yaml
services:
  - name: gradio-app
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    port: 7860
    
  - name: postgres
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      
  - name: redis
    image: redis:7
    port: 6379
```

---

## Monitoreo y Logs

```bash
# Ver logs en vivo
railway logs --follow

# Ver logs de hace N minutos
railway logs --hours 2

# Exportar logs a archivo
railway logs > app.log
```

---

## Troubleshooting

| Problema | Solución |
|----------|----------|
| App no inicia | Revisar `railway logs` y verificar `PORT` env var en código |
| 502 Bad Gateway | App tardó >60s en iniciarse; optimizar `requirements.txt` |
| Variable de entorno no visible | Ejecutar `railway redeploy` después de agregar |
| Módulo no encontrado | Verificar que `requirements.txt` esté actualizado y presente |

---

## Referencia rápida de comandos Railway MCP

```bash
railway init              # Crear nuevo proyecto
railway login             # Autenticarse
railway link <id>         # Enlazar proyecto existente
railway up                # Hacer deploy
railway redeploy          # Redeploy forzado
railway variables set K=V # Agregar variable de entorno
railway logs              # Ver logs en vivo
railway shell             # SSH a la instancia remota
railway open              # Abrir dashboard en navegador
```

---

## Recursos

- 📘 [Railway Docs](https://docs.railway.app)
- 🔌 [Railway MCP Protocol](https://railway.app/mcp)
- 🐍 [Desplegar FastAPI](https://docs.railway.app/get-started)
- 🎯 [Gradio + Railway](https://www.gradio.app/guides/hosting-gradio-apps)
