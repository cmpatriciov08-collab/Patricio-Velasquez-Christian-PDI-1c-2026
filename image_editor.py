import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

def open_image():
    pass

def save_image():
    pass

root = tk.Tk()
root.title('Image Editor')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_image)
filemenu.add_command(label="Save", command=save_image)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

root.mainloop()
