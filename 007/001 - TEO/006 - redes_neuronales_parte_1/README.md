# Entorno de trabajo con uv

Este documento indica cómo instalar `uv`, cómo crear y activar un entorno de trabajo, y qué librerías instalar para ejecutar los cuadernos de la clase.

## 1. Instalar uv

`uv` es una herramienta para crear entornos virtuales e instalar paquetes de Python de forma rápida.

### macOS y Linux

Abrí una terminal y ejecutá:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cerrá y volvé a abrir la terminal. Luego verificá la instalación:

```bash
uv --version
```

Si el comando no aparece, podés reiniciar la terminal o ejecutar:

```bash
source ~/.zshrc
```

Si usás Bash en lugar de Zsh:

```bash
source ~/.bashrc
```

### Windows

Abrí PowerShell y ejecutá:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cerrá y volvé a abrir PowerShell. Luego verificá la instalación:

```powershell
uv --version
```

## 2. Crear el proyecto

Dentro de la carpeta del material, ejecutá:

```bash
uv init
```

Este comando crea la estructura básica del proyecto.

## 3. Crear y activar el entorno virtual

Creá el entorno virtual con:

```bash
uv venv
```

### Activar en macOS y Linux

```bash
source .venv/bin/activate
```

### Activar en Windows con PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Activar en Windows con CMD

```cmd
.venv\Scripts\activate.bat
```

Cuando el entorno está activo, suele aparecer `(.venv)` al comienzo de la línea de la terminal.

## 4. Instalar las librerías necesarias

Después de `uv init` y `uv venv`, instalá las librerías con:

```bash
uv add pandas numpy matplotlib seaborn scikit-learn tensorflow tensorflow-datasets pillow gradio opencv-python-headless jupyter ipykernel
```

Estas librerías cubren los cuadernos de redes neuronales, clasificación de imágenes, Teachable Machine y Gradio.

## 5. Registrar el entorno para Jupyter

Para que Jupyter pueda usar el entorno virtual, ejecutá:

```bash
python -m ipykernel install --user --name neural-networks-uv --display-name "Python (neural-networks-uv)"
```

Luego, al abrir un notebook, seleccioná el kernel:

```text
Python (neural-networks-uv)
```

## 6. Abrir Jupyter

Podés iniciar Jupyter con:

```bash
uv run jupyter notebook
```

También podés usar JupyterLab si lo instalás:

```bash
uv add jupyterlab
uv run jupyter lab
```

## 7. Librerías incluidas

- `pandas`: lectura y manejo de tablas.
- `numpy`: operaciones numéricas y arreglos.
- `matplotlib`: visualización básica.
- `seaborn`: visualización estadística, por ejemplo matrices de confusión.
- `scikit-learn`: métricas y herramientas de evaluación.
- `tensorflow`: construcción y entrenamiento de redes neuronales.
- `tensorflow-datasets`: descarga de datasets como MNIST, EMNIST y cats_vs_dogs.
- `pillow`: manejo de imágenes.
- `gradio`: creación de interfaces web simples para probar modelos.
- `opencv-python-headless`: procesamiento de imágenes sin interfaz gráfica.
- `jupyter`: ejecución de notebooks.
- `ipykernel`: conexión entre el entorno virtual y Jupyter.

## 8. Comando rápido

Si ya instalaste `uv`, podés preparar todo con estos comandos:

```bash
uv init
uv venv
source .venv/bin/activate
uv add pandas numpy matplotlib seaborn scikit-learn tensorflow tensorflow-datasets pillow gradio opencv-python-headless jupyter ipykernel
python -m ipykernel install --user --name neural-networks-uv --display-name "Python (neural-networks-uv)"
uv run jupyter notebook
```

En Windows, reemplazá la línea de activación por:

```powershell
.venv\Scripts\Activate.ps1
```
