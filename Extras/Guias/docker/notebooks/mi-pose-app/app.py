
# app.py — Detector de Pose con MediaPipe
# Estructura: 3 capas (Data Layer / Business Logic / Presentation Layer)

import mediapipe as mp
import gradio as gr


# ─────────────────────────────────────────────────────────────────────────
# CAPA 1 — DATA LAYER
# El modelo se carga una sola vez cuando arranca la aplicación.
# Si lo cargáramos dentro de la función, cada request esperaría la carga.
# ─────────────────────────────────────────────────────────────────────────

# Compatibilidad entre versiones de MediaPipe
if hasattr(mp, "solutions"):
    modulo_solutions = mp.solutions
else:
    import mediapipe.python.solutions as modulo_solutions

modulo_pose = modulo_solutions.pose
modulo_dibujo = modulo_solutions.drawing_utils
estilos_dibujo = modulo_solutions.drawing_styles

# TODO: completá los parámetros con los valores que encontraron en la exploración
detector_pose = modulo_pose.Pose(
    static_image_mode=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# ─────────────────────────────────────────────────────────────────────────
# CAPA 2 — BUSINESS LOGIC
# Toda la lógica de procesamiento vive acá, desacoplada de la interfaz.
# Si mañana cambian la UI de Gradio a otra tecnología, esta función no cambia.
# ─────────────────────────────────────────────────────────────────────────

def detectar_pose(imagen_entrada):
    """Recibe una imagen RGB y devuelve imagen anotada + texto de metricas."""
    if imagen_entrada is None:
        return None, "Subi una imagen para analizar."

    resultado = detector_pose.process(imagen_entrada)
    imagen_anotada = imagen_entrada.copy()

    if resultado.pose_landmarks is None:
        return imagen_anotada, "No se detecto ninguna figura humana en la imagen."

    modulo_dibujo.draw_landmarks(
        image=imagen_anotada,
        landmark_list=resultado.pose_landmarks,
        connections=modulo_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=estilos_dibujo.get_default_pose_landmarks_style(),
    )

    lista_landmarks = resultado.pose_landmarks.landmark
    punto_hombro_derecho = lista_landmarks[12]
    punto_hombro_izquierdo = lista_landmarks[11]
    punto_cadera_derecha = lista_landmarks[24]

    distancia_hombros = abs(punto_hombro_derecho.x - punto_hombro_izquierdo.x)
    distancia_hombros_redondeada = round(distancia_hombros, 3)
    distancia_vertical_hombro_cadera = abs(punto_hombro_derecho.y - punto_cadera_derecha.y)

    linea_hombros = f"Distancia entre hombros: {distancia_hombros_redondeada}"
    linea_visibilidad = f"Visibilidad hombro derecho: {round(punto_hombro_derecho.visibility, 2)}"
    linea_cadera = f"Cadera derecha y={round(punto_cadera_derecha.y, 3)}"
    linea_metrica = (
        "Distancia vertical hombro-cadera derecha: "
        f"{round(distancia_vertical_hombro_cadera, 3)}"
    )

    texto_info = "\n".join([linea_hombros, linea_visibilidad, linea_cadera, linea_metrica])
    return imagen_anotada, texto_info


# ─────────────────────────────────────────────────────────────────────────
# CAPA 3 — PRESENTATION LAYER
# La interfaz declara cómo se ve la app, sin lógica de negocio adentro.
# ─────────────────────────────────────────────────────────────────────────

with gr.Blocks(title="Detector de Pose") as aplicacion:

    gr.Markdown("## Detector de Pose corporal — MediaPipe")
    gr.Markdown(
        "Subí una imagen de una persona y el modelo va a detectar "
        "los 33 puntos clave del esqueleto corporal."
    )

    with gr.Row():
        entrada_imagen = gr.Image(label="Fotografia", type="numpy")

    with gr.Row():
        salida_imagen = gr.Image(label="Pose detectada")
        salida_texto = gr.Textbox(label="Informacion de puntos clave", lines=6)

    boton_analizar = gr.Button("Analizar pose", variant="primary")

    boton_analizar.click(
        fn=detectar_pose,
        inputs=entrada_imagen,
        outputs=[salida_imagen, salida_texto]
    )


if __name__ == "__main__":
    aplicacion.launch(
        server_name="0.0.0.0",
        server_port=7865,
        share=False,
    )
