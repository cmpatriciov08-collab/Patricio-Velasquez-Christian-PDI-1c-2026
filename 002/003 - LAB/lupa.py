# Actividad 1: La lupa de píxeles

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
    py5.background(255)

    # Mostrar la imagen en la mitad izquierda
    py5.image(img, 0, 0)

    # Limitar las coordenadas del mouse al área de la imagen
    # Esto evita errores si el cursor sale de la imagen
    
    mx = py5.constrain(py5.mouse_x, 0, 399)
    my = py5.constrain(py5.mouse_y, 0, 399)

    #mx = py5.constrain(py5.mouse_x)
    #my = py5.constrain(py5.mouse_y)

    #mx = py5.mouse_x
    #my = py5.mouse_y

    # Obtener el color del píxel en esa posición
    color_pixel = py5.get_pixels(int(mx), int(my))

    # Separar el color en sus tres canales
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    # Mostrar el color como un cuadrado en la mitad derecha (la "lupa")
    py5.fill(color_pixel)
    #py5.fill(r, 0, 0)
    #py5.fill(255 - r, 255 - g, 255 - b)
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # Mostrar los valores numéricos
    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)

py5.run_sketch()

"""
Para experimentar:

Una vez que el sketch funcione, probá estas variaciones. Modificá una cosa a la vez y observá el resultado:

1. **Color negativo:** Reemplazá `py5.fill(color_pixel)` por `py5.fill(255 - r, 255 - g, 255 - b)`. El color del cuadrado debería ser el complementario del píxel original. ¿Qué color aparece sobre un rojo puro? ¿Y sobre el blanco?
    
    *Con este cambio, el cuadrado mostrará el color opuesto al del píxel bajo el mouse. Sobre un rojo puro, el cuadrado se volverá cian(semejante al turquesa). Sobre el blanco, el cuadrado se volverá negro. 

2. **Aislamiento de canal:** Ahora usá `py5.fill(r, 0, 0)`. Esto elimina verde y azul y muestra solo la contribución del canal rojo. Pasá el cursor por zonas azules o verdes de la imagen y observá cuánto rojo tienen en realidad.

    *En zonas azules o verde puro, el cuadraro se ve casi negro. En zonas donde le mouse pasa y hay rojo, aparece el rojo en distintos tonos.
    Tambien se puede observar que cuando se ubica el mouse sobre color azul, el rojo tiende a 0, pero cuando pasamos por el color verde, tiende
    a tener valores minimos de rojo. 

3. **Sin protección:** Comentá la línea con `py5.constrain()` reemplazándola por `mx = py5.mouse_x` y `my = py5.mouse_y`. Mové el mouse fuera de la imagen rápidamente. ¿Qué mensaje de error aparece en la terminal? ¿Qué tipo de error es?

    * Cuando el mouse aparece fuera de la imagen, toma lo parametros y el color ya que no esta delimitado a solo la imagen. Esto puede causar un error de índice fuera de rango al intentar acceder a un píxel que no existe.  

"""