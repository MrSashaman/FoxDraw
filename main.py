import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=color, width=brush_size, capstyle=tk.ROUND, smooth=True)
    draw_image.line((last_x, last_y, event.x, event.y), fill=color, width=brush_size)
    last_x, last_y = event.x, event.y

def clear_canvas():
    canvas.delete("all")
    img.paste("white", (0, 0, img.width, img.height))

def choose_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def change_brush_size(size):
    global brush_size
    brush_size = int(size)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])
    if file_path:
        img.save(file_path)

def open_image():
    global img, draw_image, tk_img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path).convert("RGB")
        draw_image = ImageDraw.Draw(img)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)

def fill_canvas():
    global img
    img.paste(color, (0, 0, img.width, img.height))
    canvas.create_rectangle(0, 0, img.width, img.height, fill=color, outline="")

# Создание главного окна
root = tk.Tk()
root.title("Расширенный Paint")

# Переменные
color = "black"
brush_size = 5
last_x, last_y = None, None

# Создание изображения для рисования
img = Image.new("RGB", (800, 600), "white")
draw_image = ImageDraw.Draw(img)

tk_img = ImageTk.PhotoImage(img)

# Создание холста
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", draw)

# Кнопки управления
frame = tk.Frame(root)
frame.pack()

clear_btn = tk.Button(frame, text="Очистить", command=clear_canvas)
clear_btn.pack(side=tk.LEFT)

color_btn = tk.Button(frame, text="Выбрать цвет", command=choose_color)
color_btn.pack(side=tk.LEFT)

size_scale = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Размер кисти", command=change_brush_size)
size_scale.set(5)
size_scale.pack(side=tk.LEFT)

save_btn = tk.Button(frame, text="Сохранить", command=save_image)
save_btn.pack(side=tk.LEFT)

open_btn = tk.Button(frame, text="Открыть", command=open_image)
open_btn.pack(side=tk.LEFT)

fill_btn = tk.Button(frame, text="Заливка", command=fill_canvas)
fill_btn.pack(side=tk.LEFT)

root.mainloop()