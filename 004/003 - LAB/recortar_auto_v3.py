import cv2
import numpy as np

input_path = r"004\003 - LAB\foto original.jpg"
output_path = r"004\003 - LAB\auto_recortado.jpg"

img = cv2.imread(input_path)
if img is None:
    print("No se pudo cargar la imagen")
    exit()

h, w = img.shape[:2]
print(f"Tamaño original: {w}x{h}")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lower_third = int(h * 0.4)
roi = img[lower_third:h, :]

roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(roi_gray, (5, 5), 0)
edges = cv2.Canny(blur, 30, 100)

kernel = np.ones((3,3), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    valid_contours = [c for c in contours if cv2.contourArea(c) > 500]
    if valid_contours:
        largest = max(valid_contours, key=cv2.contourArea)
        x, y, cw, ch = cv2.boundingRect(largest)
        
        full_y = lower_third + y
        full_h = ch
        full_w = cw
        full_x = x
        
        margin = 30
        full_x = max(0, full_x - margin)
        full_y = max(0, full_y - margin)
        full_w = min(w - full_x, full_w + 2*margin)
        full_h = min(h - full_y, full_h + 2*margin)
        
        cropped = img[full_y:full_y+full_h, full_x:full_x+full_w]
        cv2.imwrite(output_path, cropped)
        print(f"Coordenadas: x={full_x}, y={full_y}, ancho={full_w}, alto={full_h}")
    else:
        center_h = h // 3
        center_w = w // 2
        start_y = h - center_h - 20
        start_x = (w - center_w) // 2
        
        cropped = img[start_y:start_y+center_h, start_x:start_x+center_w]
        cv2.imwrite(output_path, cropped)
        print(f"Alternativo - Coordenadas: x={start_x}, y={start_y}, ancho={center_w}, alto={center_h}")
else:
    print("No se encontraron contornos")