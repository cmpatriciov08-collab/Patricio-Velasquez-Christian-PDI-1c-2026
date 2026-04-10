import cv2
import numpy as np

input_path = r"004\003 - LAB\foto original.jpg"
output_path = r"004\003 - LAB\auto_recortado.jpg"

img = cv2.imread(input_path)
if img is None:
    print("No se pudo cargar la imagen")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

kernel = np.ones((5,5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=2)
eroded = cv2.erode(dilated, kernel, iterations=1)

contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    margin = 20
    x = max(0, x - margin)
    y = max(0, y - margin)
    w = min(img.shape[1] - x, w + 2*margin)
    h = min(img.shape[0] - y, h + 2*margin)
    
    cropped = img[y:y+h, x:x+w]
    cv2.imwrite(output_path, cropped)
    print(f"Imagen recortada guardada como: {output_path}")
    print(f"Coordenadas: x={x}, y={y}, ancho={w}, alto={h}")
else:
    print("No se encontraron contornos")