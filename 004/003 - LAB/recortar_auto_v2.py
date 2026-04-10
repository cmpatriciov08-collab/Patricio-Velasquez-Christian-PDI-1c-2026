import cv2
import numpy as np

input_path = r"004\003 - LAB\foto original.jpg"
output_path = r"004\003 - LAB\auto_recortado.jpg"

img = cv2.imread(input_path)
if img is None:
    print("No se pudo cargar la imagen")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 | mask2

kernel = np.ones((5,5), np.uint8)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)

coords = cv2.findNonZero(red_mask)
if coords is not None:
    x, y, w, h = cv2.boundingRect(coords)
    
    margin = 50
    x = max(0, x - margin)
    y = max(0, y - margin)
    w = min(img.shape[1] - x, w + 2*margin)
    h = min(img.shape[0] - y, h + 2*margin)
    
    cropped = img[y:y+h, x:x+w]
    cv2.imwrite(output_path, cropped)
    print(f"Imagen recortada (color): {output_path}")
    print(f"Coordenadas: x={x}, y={y}, ancho={w}, alto={h}")
else:
    print("No se detectó color rojo, usando región central...")
    
    h, w = img.shape[:2]
    crop_h, crop_w = h // 3, w // 2
    start_y, start_x = h - crop_h - 50, (w - crop_w) // 2
    
    cropped = img[start_y:start_y+crop_h, start_x:start_x+crop_w]
    cv2.imwrite(output_path, cropped)
    print(f"Imagen recortada (alternativo): {output_path}")
    print(f"Coordenadas: x={start_x}, y={start_y}, ancho={crop_w}, alto={crop_h}")