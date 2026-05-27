"""
Restaurador de Fotos Antiguas
==============================
Herramienta GUI para restaurar fotografías dañadas usando técnicas de PDI:
  - Inpainting (reparación de rasgaduras y manchas blancas)
  - Denoising (reducción de ruido y grano)
  - CLAHE (mejora de contraste local)
  - Unsharp masking (nitidez)
  - Ajuste de brillo/contraste
  - Pipeline automático de restauración

Uso: python image_editor.py
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import cv2
import numpy as np
from PIL import Image, ImageTk


class PhotoRestorer:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Restaurador de Fotos Antiguas — PDI")
        self.root.geometry("1300x820")
        self.root.configure(bg="#1e1e1e")

        self.original_image: np.ndarray | None = None   # BGR, nunca se modifica
        self.current_image: np.ndarray | None = None    # BGR, pipeline acumulativo
        self.showing_original = False

        self._build_ui()

    # ------------------------------------------------------------------ #
    #  UI                                                                  #
    # ------------------------------------------------------------------ #

    def _build_ui(self):
        # ── Barra de herramientas ──────────────────────────────────────
        toolbar = tk.Frame(self.root, bg="#2d2d2d", pady=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_style = {"bg": "#3c3c3c", "fg": "white", "relief": tk.FLAT,
                     "padx": 10, "pady": 4, "font": ("Segoe UI", 9)}

        tk.Button(toolbar, text="📂 Abrir",    command=self.open_image,   **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(toolbar, text="💾 Guardar",  command=self.save_image,   **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(toolbar, text="🔄 Resetear", command=self.reset_image,  **btn_style).pack(side=tk.LEFT, padx=3)

        self.compare_btn = tk.Button(toolbar, text="👁 Ver Original",
                                     command=self.toggle_compare, **btn_style)
        self.compare_btn.pack(side=tk.LEFT, padx=3)

        tk.Button(toolbar, text="✨ Restauración Automática",
                  command=self.auto_restore,
                  bg="#0e639c", fg="white", relief=tk.FLAT,
                  padx=10, pady=4, font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=10)

        # ── Layout principal ───────────────────────────────────────────
        main = tk.Frame(self.root, bg="#1e1e1e")
        main.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo de controles
        ctrl_canvas = tk.Canvas(main, bg="#252526", width=270, highlightthickness=0)
        ctrl_scroll = ttk.Scrollbar(main, orient=tk.VERTICAL, command=ctrl_canvas.yview)
        ctrl_canvas.configure(yscrollcommand=ctrl_scroll.set)
        ctrl_scroll.pack(side=tk.LEFT, fill=tk.Y)
        ctrl_canvas.pack(side=tk.LEFT, fill=tk.Y)

        self.ctrl_frame = tk.Frame(ctrl_canvas, bg="#252526")
        ctrl_canvas.create_window((0, 0), window=self.ctrl_frame, anchor=tk.NW)
        self.ctrl_frame.bind("<Configure>",
            lambda e: ctrl_canvas.configure(scrollregion=ctrl_canvas.bbox("all")))

        # Canvas de imagen
        self.canvas = tk.Canvas(main, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", lambda e: self._update_canvas())

        # Barra de estado
        self.status_var = tk.StringVar(value="Abrí una imagen para comenzar (📂 Abrir)")
        tk.Label(self.root, textvariable=self.status_var,
                 bg="#007acc", fg="white", anchor=tk.W,
                 font=("Segoe UI", 9)).pack(side=tk.BOTTOM, fill=tk.X)

        self._build_controls()

    def _section(self, title: str) -> tk.LabelFrame:
        f = tk.LabelFrame(self.ctrl_frame, text=title,
                          bg="#252526", fg="#cccccc",
                          font=("Segoe UI", 8, "bold"),
                          padx=6, pady=4)
        f.pack(fill=tk.X, padx=6, pady=5)
        return f

    def _slider(self, parent, label, from_, to, default, resolution=1) -> tk.Scale:
        tk.Label(parent, text=label, bg="#252526", fg="#aaaaaa",
                 font=("Segoe UI", 8)).pack(anchor=tk.W)
        s = tk.Scale(parent, from_=from_, to=to, orient=tk.HORIZONTAL,
                     length=220, resolution=resolution,
                     bg="#252526", fg="#cccccc", troughcolor="#3c3c3c",
                     highlightthickness=0, bd=0)
        s.set(default)
        s.pack()
        return s

    def _btn(self, parent, label, command):
        tk.Button(parent, text=label, command=command,
                  bg="#3c3c3c", fg="white", relief=tk.FLAT,
                  padx=6, pady=3, font=("Segoe UI", 8),
                  width=26).pack(pady=(2, 4))

    def _build_controls(self):
        tk.Label(self.ctrl_frame, text="CONTROLES DE RESTAURACIÓN",
                 bg="#252526", fg="#ffffff",
                 font=("Segoe UI", 9, "bold")).pack(pady=(12, 4))

        # ── 1. Reparación de daños ─────────────────────────────────────
        f = self._section("1 · Reparar rasgaduras y manchas")
        self._btn(f, "Reparar daños", self.repair_damage)
        self.damage_thresh = self._slider(f, "Umbral de daño (blanco)", 180, 255, 235)
        self.inpaint_radius = self._slider(f, "Radio de inpaint (px)", 1, 20, 5)

        # ── 2. Eliminación de arañazos ─────────────────────────────────
        f2 = self._section("2 · Eliminar arañazos / rayas")
        self._btn(f2, "Eliminar arañazos", self.remove_scratches)
        self.scratch_thresh = self._slider(f2, "Sensibilidad", 5, 50, 20)

        # ── 3. Denoising ───────────────────────────────────────────────
        f3 = self._section("3 · Reducir ruido / grano")
        self._btn(f3, "Aplicar denoising", self.apply_denoise)
        self.denoise_h = self._slider(f3, "Fuerza (h)", 1, 40, 10)

        # ── 4. Contraste CLAHE ─────────────────────────────────────────
        f4 = self._section("4 · Mejorar contraste (CLAHE)")
        self._btn(f4, "Mejorar contraste", self.apply_clahe)
        self.clahe_clip = self._slider(f4, "Clip limit", 0.5, 10.0, 2.0, 0.5)
        self.clahe_tile  = self._slider(f4, "Tamaño de tile", 4, 32, 8)

        # ── 5. Nitidez ─────────────────────────────────────────────────
        f5 = self._section("5 · Nitidez (unsharp mask)")
        self._btn(f5, "Aplicar nitidez", self.apply_sharpen)
        self.sharp_amount = self._slider(f5, "Intensidad", 0.1, 5.0, 1.5, 0.1)
        self.sharp_sigma  = self._slider(f5, "Radio (sigma)", 1, 10, 3)

        # ── 6. Brillo / Contraste ──────────────────────────────────────
        f6 = self._section("6 · Brillo / Contraste global")
        self.brightness = self._slider(f6, "Brillo", -100, 100, 0)
        self.contrast   = self._slider(f6, "Contraste", -100, 100, 0)
        self._btn(f6, "Aplicar brillo/contraste", self.apply_bc)

        # ── 7. Suavizado de bordes ─────────────────────────────────────
        f7 = self._section("7 · Suavizado (bilateral)")
        self._btn(f7, "Suavizar (preserva bordes)", self.apply_bilateral)
        self.bilat_d      = self._slider(f7, "Diámetro", 3, 15, 9, 2)
        self.bilat_sigma  = self._slider(f7, "Sigma", 10, 150, 75)

    # ------------------------------------------------------------------ #
    #  Archivo                                                             #
    # ------------------------------------------------------------------ #

    def open_image(self):
        path = filedialog.askopenfilename(
            title="Abrir imagen",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp"),
                       ("Todos", "*.*")])
        if not path:
            return
        img = cv2.imread(path)
        if img is None:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{path}")
            return
        self.original_image = img.copy()
        self.current_image  = img.copy()
        self.showing_original = False
        self.compare_btn.config(text="👁 Ver Original")
        self.status_var.set(f"Cargada: {os.path.basename(path)}  —  {img.shape[1]}×{img.shape[0]} px")
        self._update_canvas()

    def save_image(self):
        if self.current_image is None:
            messagebox.showwarning("Aviso", "No hay imagen para guardar.")
            return
        path = filedialog.asksaveasfilename(
            title="Guardar imagen restaurada",
            defaultextension=".png",
            filetypes=[("PNG (sin pérdida)", "*.png"),
                       ("JPEG", "*.jpg"),
                       ("BMP", "*.bmp")])
        if path:
            cv2.imwrite(path, self.current_image)
            self.status_var.set(f"Guardada: {os.path.basename(path)}")

    def reset_image(self):
        if self.original_image is not None:
            self.current_image = self.original_image.copy()
            self.showing_original = False
            self.compare_btn.config(text="👁 Ver Original")
            self._update_canvas()
            self.status_var.set("Imagen reseteada al original")

    def toggle_compare(self):
        if self.original_image is None:
            return
        self.showing_original = not self.showing_original
        self.compare_btn.config(
            text="👁 Ver Restaurada" if self.showing_original else "👁 Ver Original")
        self._update_canvas()

    # ------------------------------------------------------------------ #
    #  Canvas                                                              #
    # ------------------------------------------------------------------ #

    def _update_canvas(self):
        img = self.original_image if self.showing_original else self.current_image
        if img is None:
            return

        cw = self.canvas.winfo_width()  or 900
        ch = self.canvas.winfo_height() or 700
        h, w = img.shape[:2]
        scale = min(cw / w, ch / h, 1.0)
        nw, nh = max(1, int(w * scale)), max(1, int(h * scale))

        img_rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img  = Image.fromarray(img_rgb).resize((nw, nh), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(pil_img)

        self.canvas.delete("all")
        self.canvas.create_image(cw // 2, ch // 2, anchor=tk.CENTER, image=self.tk_img)

        label = "◀ ORIGINAL" if self.showing_original else "▶ RESTAURADA"
        color = "#ff9900" if self.showing_original else "#00cc88"
        self.canvas.create_text(10, 10, anchor=tk.NW, text=label,
                                fill=color, font=("Segoe UI", 11, "bold"))

    # ------------------------------------------------------------------ #
    #  Helpers internos                                                    #
    # ------------------------------------------------------------------ #

    def _set_status(self, msg: str):
        self.status_var.set(msg)
        self.root.update_idletasks()

    def _finish(self, msg: str, result: np.ndarray):
        self.current_image  = result
        self.showing_original = False
        self.compare_btn.config(text="👁 Ver Original")
        self._update_canvas()
        self.status_var.set(msg)

    def _damage_mask(self, gray: np.ndarray) -> np.ndarray:
        """Máscara de píxeles dañados: zonas muy blancas (rasgaduras)."""
        thresh = int(self.damage_thresh.get())
        _, mask = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
        kernel  = np.ones((3, 3), np.uint8)
        return cv2.dilate(mask, kernel, iterations=2)

    def _scratch_mask(self, gray: np.ndarray) -> np.ndarray:
        """Detecta arañazos como estructuras lineales muy oscuras o muy claras."""
        sens = int(self.scratch_thresh.get())

        # Líneas oscuras (arañazos típicos)
        dark = cv2.adaptiveThreshold(gray, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY_INV, 11, sens)
        kv = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
        kh = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
        dark_v = cv2.morphologyEx(dark, cv2.MORPH_OPEN, kv)
        dark_h = cv2.morphologyEx(dark, cv2.MORPH_OPEN, kh)
        mask = cv2.bitwise_or(dark_v, dark_h)

        kernel = np.ones((2, 2), np.uint8)
        return cv2.dilate(mask, kernel, iterations=1)

    # ------------------------------------------------------------------ #
    #  Operaciones de restauración                                         #
    # ------------------------------------------------------------------ #

    def repair_damage(self):
        if self.current_image is None:
            return
        self._set_status("Detectando y reparando daños...")
        gray  = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        mask  = self._damage_mask(gray)
        r     = int(self.inpaint_radius.get())
        result = cv2.inpaint(self.current_image, mask, r, cv2.INPAINT_TELEA)
        self._finish("Daños reparados ✓", result)

    def remove_scratches(self):
        if self.current_image is None:
            return
        self._set_status("Eliminando arañazos...")
        gray   = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        mask   = self._scratch_mask(gray)
        result = cv2.inpaint(self.current_image, mask, 3, cv2.INPAINT_TELEA)
        self._finish("Arañazos eliminados ✓", result)

    def apply_denoise(self):
        if self.current_image is None:
            return
        self._set_status("Aplicando denoising (puede tardar unos segundos)...")
        h      = int(self.denoise_h.get())
        result = cv2.fastNlMeansDenoisingColored(self.current_image, None, h, h, 7, 21)
        self._finish("Denoising aplicado ✓", result)

    def apply_clahe(self):
        if self.current_image is None:
            return
        clip   = float(self.clahe_clip.get())
        tile   = int(self.clahe_tile.get())
        tile   = max(2, tile - tile % 2)        # debe ser par
        clahe  = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile, tile))
        lab    = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        result = cv2.cvtColor(cv2.merge([clahe.apply(l), a, b]), cv2.COLOR_LAB2BGR)
        self._finish("Contraste mejorado con CLAHE ✓", result)

    def apply_sharpen(self):
        if self.current_image is None:
            return
        amount = float(self.sharp_amount.get())
        sigma  = int(self.sharp_sigma.get())
        blurred = cv2.GaussianBlur(self.current_image, (0, 0), sigma)
        result  = cv2.addWeighted(self.current_image, 1 + amount, blurred, -amount, 0)
        self._finish("Nitidez aplicada ✓", result)

    def apply_bc(self):
        if self.current_image is None:
            return
        alpha  = 1.0 + self.contrast.get() / 100.0
        beta   = float(self.brightness.get())
        result = cv2.convertScaleAbs(self.current_image, alpha=alpha, beta=beta)
        self._finish("Brillo/Contraste ajustados ✓", result)

    def apply_bilateral(self):
        if self.current_image is None:
            return
        self._set_status("Aplicando filtro bilateral...")
        d     = int(self.bilat_d.get())
        sigma = int(self.bilat_sigma.get())
        result = cv2.bilateralFilter(self.current_image, d, sigma, sigma)
        self._finish("Filtro bilateral aplicado ✓", result)

    # ------------------------------------------------------------------ #
    #  Pipeline automático                                                 #
    # ------------------------------------------------------------------ #

    def auto_restore(self):
        """
        Pipeline recomendado para fotos antiguas en B/N dañadas:
          1. Inpaint zonas blancas (rasgaduras, bordes perdidos)
          2. Inpaint arañazos
          3. Denoising (fuerza moderada)
          4. CLAHE para recuperar rango tonal
          5. Unsharp mask suave
        """
        if self.current_image is None:
            messagebox.showwarning("Aviso", "Primero abrí una imagen.")
            return

        self._set_status("Restauración automática en progreso…")

        img = self.current_image.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 1 — Reparar zonas blancas
        bright_mask = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY)[1]
        bright_mask = cv2.dilate(bright_mask, np.ones((3, 3), np.uint8), iterations=2)
        img = cv2.inpaint(img, bright_mask, 7, cv2.INPAINT_TELEA)

        # 2 — Reparar arañazos
        gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dark  = cv2.adaptiveThreshold(gray2, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY_INV, 11, 20)
        kv = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
        kh = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
        scratch_mask = cv2.bitwise_or(
            cv2.morphologyEx(dark, cv2.MORPH_OPEN, kv),
            cv2.morphologyEx(dark, cv2.MORPH_OPEN, kh))
        scratch_mask = cv2.dilate(scratch_mask, np.ones((2, 2), np.uint8), iterations=1)
        img = cv2.inpaint(img, scratch_mask, 3, cv2.INPAINT_TELEA)

        # 3 — Denoising
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        # 4 — CLAHE
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
        lab   = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        img = cv2.cvtColor(cv2.merge([clahe.apply(l), a, b]), cv2.COLOR_LAB2BGR)

        # 5 — Nitidez suave
        blurred = cv2.GaussianBlur(img, (0, 0), 3)
        img = cv2.addWeighted(img, 2.0, blurred, -1.0, 0)

        self._finish("✨ Restauración automática completa — comparar con 👁 Ver Original", img)


# ──────────────────────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    root = tk.Tk()
    app  = PhotoRestorer(root)
    root.mainloop()

