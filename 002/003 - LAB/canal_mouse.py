# Actividad 2: Mezclador de canales con el mouse

import py5
from pathlib import Path
img = None


def setup():
    global img
    py5.size(800, 400)
    # Cargar la imagen desde la carpeta del script para evitar errores de ruta relativa.
    image_path = Path(__file__).resolve().parent / "flowers.jpg"
    img = py5.load_image(str(image_path))
    if img is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {image_path}")
    img.resize(400, 400)

def draw():
    py5.background(35)

    # Imagen original en la mitad izquierda (sin modificar)
    py5.image(img, 0, 0)

    # Calcular el factor de ajuste según la posición X del mouse
    # remap convierte un valor de un rango a otro
    
    factor_rojo = py5.remap(py5.mouse_x, 0, py5.width, 0, 2.5)
    
    # Factor verde: de 0 a 800 píxeles de ancho (X) → de 0 a 2.5
    factor_verde = py5.remap(py5.mouse_x, 0, py5.width, 0, 2.5)
    # Factor azul: de 0 a 400 píxeles de alto (Y) → de 0 a 2.5
    factor_azul = py5.remap(py5.mouse_y, 0, py5.height, 0, 2.5)

    # Acceder a la matriz de píxeles del lienzo completo
    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):

            # La imagen es un arreglo lineal. Para acceder al píxel (x, y):
            # índice = x + y * ancho
            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            # Separar los canales
            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            # Modificar solo el canal rojo según el mouse
            r = r * factor_rojo
            #r = 0
             # Modificar el canal verde según la posición X del mouse
            #g = g * factor_verde
            # Modificar el canal azul según la posición Y del mouse
            #b = b * factor_azul

            # Limitar el valor para que no supere 255
            # Un valor mayor haría que py5 lo interprete incorrectamente
            if r > 255:
                r = 255
            #if g > 255:
            #    g = 255
            #if b > 255:
            #    b = 255          

            # Calcular el índice del mismo píxel en el lienzo (desplazado 400px a la derecha)
            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)
            #py5.pixels[indice_canvas] = py5.color(b, g, r)

    # Aplicar los cambios al lienzo
    py5.update_pixels()

py5.run_sketch()


"""
### Para experimentar

1. **Suprimir el canal rojo por completo:** Reemplazá `r = r * factor_rojo` por `r = 0`. La imagen de la derecha debería mostrar solo los canales verde y azul. ¿Qué pasa con las zonas que eran originalmente rojas?

 
   *Las zonas que eran originalmente rojas aparecen negras en la imagen de la derecha, ya que el canal rojo se ha establecido a cero, eliminando cualquier contribución de ese canal al color final.
   Esto tambien ilustra que los colores son una combinacion de 3 canales independientes, lo que significa que al "apagar" un canal, altera los colores que lo contenian.

2. **Intercambiar canales:** Cambiá `py5.color(r, g, b)` por `py5.color(b, g, r)`. Esto intercambia el canal rojo y el azul. Los cielos de color azul deberían volverse rojizos. Pensá qué implica esto: los colores son datos, y cambiar su posición genera una imagen que parece incorrecta pero matemáticamente es válida.

    *En esta ocasion, los canales rojo y azul se intercambian. El cielo se vueleve rojizo amarillento, y las flores rojas se vuelven azules.

3. **Controlar un canal distinto:** En lugar de modificar `r`, aplicá el factor al canal verde (`g = g * factor`). Considerá también crear un segundo factor que use la posición Y del mouse para controlar el azul.
"""