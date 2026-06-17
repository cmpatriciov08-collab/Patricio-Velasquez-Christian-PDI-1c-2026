---
name: "mediapipe-vision"
description: "Detectar landmarks de manos, cara y pose con MediaPipe en imágenes o video en tiempo real."
tags: [mediapipe, landmarks, opencv, vision, python]
---

# Skill: MediaPipe Vision

## Cuándo usar esta skill

Cuando el agente necesita detectar puntos clave del cuerpo humano en imágenes o video:
- 21 landmarks de mano (Hand Landmarker)
- 478 landmarks faciales (Face Mesh)
- 33 landmarks corporales (Pose)

---

## Modelos disponibles

| Modelo | Landmarks | Descarga |
|--------|-----------|----------|
| Hand Landmarker | 21 (por mano) | `mediapipe-models/.../hand_landmarker.task` |
| Face Mesh | 478 | `mp.solutions.face_mesh` |
| Pose | 33 | `mp.solutions.pose` |

---

## Patrón: imagen estática (Face Mesh / Pose)

```python
import mediapipe as mp
import numpy as np

modulo = mp.solutions.face_mesh          # o mp.solutions.pose
dibujo = mp.solutions.drawing_utils
estilos = mp.solutions.drawing_styles

detector = modulo.FaceMesh(
    static_image_mode=True,
    max_num_faces=2,
    refine_landmarks=True,
    min_detection_confidence=0.5
)

def detectar(imagen_rgb: np.ndarray) -> np.ndarray:
    resultado = detector.process(imagen_rgb)
    imagen_anotada = imagen_rgb.copy()
    if resultado.multi_face_landmarks is None:
        return imagen_anotada
    for landmarks in resultado.multi_face_landmarks:
        dibujo.draw_landmarks(
            image=imagen_anotada,
            landmark_list=landmarks,
            connections=modulo.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=estilos.get_default_face_mesh_tesselation_style()
        )
    return imagen_anotada
```

## Patrón: Hand Landmarker (Task API)

```python
import mediapipe as mp
import urllib.request, os

MODEL_PATH = "hand_landmarker.task"
MODEL_URL  = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

if not os.path.exists(MODEL_PATH):
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

OpcionesBase  = mp.tasks.BaseOptions
Detector      = mp.tasks.vision.HandLandmarker
Opciones      = mp.tasks.vision.HandLandmarkerOptions
ModoEjecucion = mp.tasks.vision.RunningMode

opciones = Opciones(
    base_options=OpcionesBase(model_asset_path=MODEL_PATH),
    running_mode=ModoEjecucion.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.5,
)
```

## Coordenadas normalizadas → píxeles

```python
alto, ancho = imagen.shape[:2]
x_pixel = int(landmark.x * ancho)
y_pixel = int(landmark.y * alto)
```

## Reglas importantes

- Instanciar el detector **una sola vez** fuera de la función de procesamiento.
- MediaPipe espera imágenes en **RGB**; OpenCV usa BGR — convertir con `cv2.cvtColor`.
- Dibujar siempre sobre una **copia** (`imagen.copy()`), nunca sobre el array original.
- `visibility` (0–1) indica certeza de que el punto es visible; filtrar por `>0.5` para poses.
