# Trabajo Práctico 006 — Fotografía Digital  
## De la cámara oscura a la imagen intencional  
**Entrega mediante GitHub**

---

## Objetivos

Este trabajo práctico propone integrar:

- principios ópticos
- captura fotográfica
- composición visual
- análisis técnico de la imagen
- postprocesamiento digital
- reflexión crítica sobre la construcción visual

El objetivo **no** es producir fotografías “bonitas” en un sentido decorativo, sino desarrollar:

> **intención + decisión técnica + lectura visual + postproceso consciente**

Cada estudiante deberá producir una serie de imágenes aplicando los conceptos trabajados durante la cursada:

- cámara oscura
- exposición
- composición
- punto de vista
- simplificación visual
- luz
- reencuadre
- espacios de color
- procesamiento digital de imágenes

---

## Modalidad de entrega

La entrega debe realizarse mediante un repositorio **GitHub**.  
Dentro del repositorio debe existir una carpeta llamada:

### Estructura de la carpeta
006_fotografia_digital/
│
├── README.md
├── presentacion.pdf
├── imagenes/
│ ├── originales/
│ ├── procesadas/
│ └── descartes/
│
├── codigo/
│ ├── ecualizacion_hsv.py
│ ├── escala_grises.py
│ └── otros_scripts.py
│
└── recursos/
└── referencias_opcionales/
---

## Archivo principal obligatorio: `presentacion.pdf`

La entrega principal será una presentación en formato **PDF**.  
El PDF debe organizarse como una **narrativa visual y técnica** del proceso fotográfico.  
**No** debe ser una simple acumulación de imágenes.

Cada diapositiva debe:

- comunicar una idea clara
- mostrar decisiones visuales
- incluir comparaciones
- explicar brevemente el razonamiento técnico o compositivo

---

## Estructura obligatoria del PDF

### 1. Portada

Debe incluir:

- nombre y apellido
- materia
- comisión
- fecha
- título del trabajo

**Título sugerido:**  
> De la cámara oscura a la imagen intencional

**Subtítulo sugerido:**  
> Óptica, composición y postproceso en fotografía digital

---

## Parte 1 — Cámara oscura y procesamiento digital

### 2. Construcción y registro de la cámara oscura

Incluir:

- fotografía del dispositivo construido
- esquema simple del funcionamiento
- breve explicación del principio óptico

**Conceptos esperados:**

- propagación rectilínea de la luz
- proyección invertida
- plano de imagen
- relación entre apertura y nitidez

### 3. Captura con cámara oscura + ecualización HSV

**Requisitos**  
Capturar una imagen utilizando la cámara oscura. Luego:

1. convertir la imagen a **HSV**
2. separar canales **H, S y V**
3. ecualizar únicamente el **canal V**
4. recomponer la imagen

La diapositiva debe incluir:

- imagen original
- imagen ecualizada
- histograma antes/después
- explicación breve de los cambios

**Preguntas guía**

- ¿Qué mejoró visualmente?
- ¿Qué información se perdió?
- ¿Qué limitaciones tiene la cámara oscura?
- ¿Por qué se ecualiza el canal V y no RGB directamente?

---

## Parte 2 — Composición y lenguaje visual

### 4. Fotografía de simplicidad visual

**Objetivo**  
Construir una imagen donde el sujeto principal sea claramente identificable.

**Requisitos**  
Aplicar al menos una de las siguientes estrategias:

- separación sujeto/fondo
- reducción de ruido visual
- profundidad de campo
- espacio negativo
- acercamiento
- conversión a blanco y negro o escala de grises

La diapositiva debe incluir:

- imagen original
- imagen final
- breve explicación compositiva

**Preguntas guía**

- ¿Qué elementos distraían?
- ¿Qué se eliminó?
- ¿Cómo cambia la lectura en escala de grises?

### 5. Reencuadre y reinterpretación

**Objetivo**  
Demostrar que cambiar el encuadre modifica el significado de la imagen.

**Requisitos**  
Partir de una fotografía amplia y producir **al menos dos reencuadres distintos**.

La diapositiva debe incluir:

- fotografía original
- recorte A
- recorte B
- marcas indicando la región recortada

**Preguntas guía**

- ¿Qué se vuelve importante después del crop?
- ¿Qué información desaparece?
- ¿El sujeto cambia?
- ¿La imagen se vuelve más narrativa o más abstracta?

### 6. Punto de vista y construcción narrativa

**Objetivo**  
Explorar cómo la posición de la cámara modifica:

- escala
- contexto
- relación emocional
- información visual

**Requisitos**  
Fotografiar un mismo sujeto desde **dos puntos de vista distintos**.  
Uno de ellos debe aportar información contextual nueva.

**Ejemplos**

- objeto desde frente y luego cenital
- sujeto desde nivel de ojos y luego desde abajo
- escena desde lejos y luego desde arriba

La diapositiva debe incluir:

- vista A
- vista B
- imagen final elegida
- explicación del cambio narrativo

**Preguntas guía**

- ¿Qué información aparece desde el nuevo ángulo?
- ¿Cómo cambia la percepción del sujeto?
- ¿Qué relación genera la cámara con la escena?

### 7. Fotografía basada en la luz

**Objetivo**  
Usar la luz como elemento estructural de la imagen.

**Requisitos**  
Trabajar conscientemente con:

- dirección de la luz
- calidad de la luz
- hora del día
- contraste
- sombras

**Opciones posibles**

- luz frontal
- luz lateral
- contraluz
- hora dorada
- hora azul
- luz suave
- luz dura

La diapositiva debe incluir:

- fotografía final
- pequeño esquema indicando dirección de la luz
- explicación breve

**Preguntas guía**

- ¿La luz revela o esconde?
- ¿Genera textura?
- ¿Construye atmósfera?
- ¿Cómo cambia el volumen?

---

## Parte 3 — Reflexión y selección

### 8. Selección crítica

**Objetivo**  
Comprender que fotografiar también implica:

- seleccionar
- descartar
- comparar
- editar

La diapositiva debe incluir:

- miniaturas de imágenes descartadas
- imagen elegida
- explicación del criterio de selección

**Preguntas guía**

- ¿Por qué una imagen funciona mejor?
- ¿Qué problema tenían las descartadas?
- ¿Qué decisiones mejoraron la imagen final?

### 9. Reflexión final

Responder brevemente:

- ¿Qué aprendiste sobre mirar?
- ¿Qué diferencia hay entre registrar y construir una imagen?
- ¿Qué relación encontrás entre óptica, percepción y composición?
- ¿Cómo modifica el postproceso la lectura de una fotografía?

### 10. Anexo técnico

Incluir:

- fragmentos de código
- scripts utilizados
- pseudocódigo
- histogramas
- pruebas de procesamiento

**Mínimo obligatorio:**

- conversión RGB ↔ HSV
- ecualización del canal V
- transformación a escala de grises

---

## Requisitos técnicos

### Captura

Las fotografías pueden realizarse con:

- teléfono celular
- cámara digital
- webcam
- cámara experimental

### Edición permitida

Se permite:

- recorte
- ajuste tonal
- ecualización
- conversión de espacio de color
- contraste
- correcciones básicas

**No se permite:**

- generación con IA
- fotomontajes complejos
- reemplazo de contenido
- imágenes tomadas de internet

---

## Criterios de evaluación

| Criterio | Peso |
|----------|------|
| Comprensión óptica y cámara oscura | 20% |
| Procesamiento HSV y operaciones digitales | 15% |
| Composición y lenguaje visual | 25% |
| Uso consciente de la luz | 15% |
| Calidad reflexiva y argumentativa | 15% |
| Organización y claridad del PDF | 10% |

> **Importante:** No se evaluará solamente la estética.  
> Se evaluará principalmente: **intención visual, coherencia, experimentación, comprensión técnica, capacidad de análisis y toma de decisiones.**

---

## Recomendaciones

- Tomar muchas fotografías
- Probar distintos encuadres
- Variar altura y distancia
- Revisar histogramas
- Mirar bordes del encuadre
- Trabajar con luz natural
- Comparar imágenes antes de elegir
- Pensar cada fotografía como una **construcción**

---

## Idea central del trabajo

> Fotografiar no es solamente registrar el mundo.  
> Es decidir:  
> - qué mostrar  
> - qué excluir  
> - desde dónde mirar  
> - y cómo transformar la luz en significado.

---

## Anexo — Postproceso: Código sugerido (Python + OpenCV)

### Ecualización HSV

```python
import cv2

img_bgr = cv2.imread("camara_oscura.jpg")
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# Ecualizar solo el brillo (V)
v_eq = cv2.equalizeHist(v)
hsv_eq = cv2.merge([h, s, v_eq])
img_eq_bgr = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

cv2.imwrite("camara_oscura_ecualizada.jpg", img_eq_bgr)

cv2.imwrite("camara_oscura_ecualizada.jpg", img_eq_bgr)

Escala de grises (Para Foto 2)
img = cv2.imread("simplicidad.jpg")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("simplicidad_grises.jpg", gris)

