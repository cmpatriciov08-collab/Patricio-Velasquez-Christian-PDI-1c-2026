FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir jupyterlab>=4.0.0 && \
    pip install --no-cache-dir mediapipe>=0.10.0 opencv-python-headless>=4.8.0 && \
    pip install --no-cache-dir gradio>=4.0.0 && \
    pip install --no-cache-dir torch>=2.0.0 --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir transformers>=4.35.0 && \
    pip install --no-cache-dir pillow>=10.0.0 requests>=2.31.0 matplotlib>=3.7.0 numpy>=1.24.0

EXPOSE 8888 7860-7870

CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--port=8888", \
     "--no-browser", \
     "--allow-root", \
     "--NotebookApp.token=clase", \
     "--notebook-dir=/notebooks"]
