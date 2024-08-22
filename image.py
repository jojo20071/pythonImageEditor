import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        self.root.geometry("800x600")
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.file_menu.add_command(label="Save", command=self.save_image)
        self.file_menu.add_command(label="Save as JPEG", command=self.save_as_jpeg)
        self.file_menu.add_command(label="Save as BMP", command=self.save_as_bmp)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Convert to Grayscale", command=self.convert_to_grayscale)
        self.edit_menu.add_command(label="Pixelate", command=self.pixelate_image)
        self.edit_menu.add_command(label="Rotate 90°", command=lambda: self.rotate_image(90))
        self.edit_menu.add_command(label="Crop", command=self.crop_image)
        self.edit_menu.add_command(label="Resize", command=self.resize_image)
        self.edit_menu.add_command(label="Blur", command=lambda: self.apply_filter(ImageFilter.BLUR))
        self.edit_menu.add_command(label="Sharpen", command=lambda: self.apply_filter(ImageFilter.SHARPEN))
        self.edit_menu.add_command(label="Edge Enhance", command=lambda: self.apply_filter(ImageFilter.EDGE_ENHANCE))
        self.edit_menu.add_command(label="Find Edges", command=lambda: self.apply_filter(ImageFilter.FIND_EDGES))
        self.edit_menu.add_command(label="Adjust Brightness", command=self.adjust_brightness)
        self.edit_menu.add_command(label="Adjust Contrast", command=self.adjust_contrast)
        self.edit_menu.add_command(label="Adjust Saturation", command=self.adjust_saturation)
        self.edit_menu.add_command(label="Flip Horizontally", command=lambda: self.flip_image("horizontal"))
        self.edit_menu.add_command(label="Flip Vertically", command=lambda: self.flip_image("vertical"))
        self.edit_menu.add_command(label="Adjust Hue", command=self.adjust_hue)
        self.edit_menu.add_command(label="Invert Colors", command=self.invert_colors)
        self.edit_menu.add_command(label="Add Text", command=self.add_text)
        self.edit_menu.add_command(label="Draw Rectangle", command=self.draw_rectangle)
        self.edit_menu.add_command(label="Draw Circle", command=self.draw_circle)
        self.edit_menu.add_command(label="Draw Line", command=self.draw_line)
        self.edit_menu.add_command(label="Adjust Opacity", command=self.adjust_opacity)
        self.edit_menu.add_command(label="Add Border", command=self.add_border)
        self.edit_menu.add_command(label="Apply Sepia Filter", command=self.apply_sepia_filter)
        self.edit_menu.add_command(label="Draw Polygon", command=self.draw_polygon)
        self.edit_menu.add_command(label="Adjust Gamma", command=self.adjust_gamma)
        self.edit_menu.add_command(label="Apply Gaussian Blur", command=self.apply_gaussian_blur)
        self.edit_menu.add_command(label="Calculate Histogram", command=self.calculate_histogram)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.image = None
        self.history = []
        self.history_index = -1

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.add_to_history()
            self.display_image()

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.image.save(file_path)

    def save_as_jpeg(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                self.image.convert("RGB").save(file_path, "JPEG")

    def save_as_bmp(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".bmp")
            if file_path:
                self.image.save(file_path, "BMP")

    def display_image(self):
        img = self.image.resize((600, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def add_to_history(self):
        if self.image:
            self.history = self.history[:self.history_index + 1]
            self.history.append(self.image.copy())
            self.history_index += 1

    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.image = self.history[self.history_index]
            self.display_image()

    def redo(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.image = self.history[self.history_index]
            self.display_image()

    def convert_to_grayscale(self):
        if self.image:
            self.image = self.image.convert("L")
            self.add_to_history()
            self.display_image()

    def pixelate_image(self):
        if self.image:
            small = self.image.resize((32, 32), Image.NEAREST)
            self.image = small.resize(self.image.size, Image.NEAREST)
            self.add_to_history()
            self.display_image()

    def rotate_image(self, angle):
        if self.image:
            self.image = self.image.rotate(angle)
            self.add_to_history()
            self.display_image()

    def crop_image(self):
        if self.image:
            width, height = self.image.size
            left = width // 4
            top = height // 4
            right = 3 * width // 4
            bottom = 3 * height // 4
            self.image = self.image.crop((left, top, right, bottom))
            self.add_to_history()
            self.display_image()

    def resize_image(self):
        if self.image:
            new_size = (400, 300)
            self.image = self.image.resize(new_size, Image.ANTIALIAS)
            self.add_to_history()
            self.display_image()

    def apply_filter(self, filter_type):
        if self.image:
            self.image = self.image.filter(filter_type)
            self.add_to_history()
            self.display_image()

    def adjust_brightness(self):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(1.5)
            self.add_to_history()
            self.display_image()

    def adjust_contrast(self):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(1.5)
            self.add_to_history()
            self.display_image()

    def adjust_saturation(self):
        if self.image:
            enhancer = ImageEnhance.Color(self.image)
            self.image = enhancer.enhance(1.5)
            self.add_to_history()
            self.display_image()

    def flip_image(self, direction):
        if self.image:
            if direction == "horizontal":
                self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            elif direction == "vertical":
                self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            self.add_to_history()
            self.display_image()

    def adjust_hue(self):
        if self.image:
            self.image = ImageOps.colorize(self.image.convert("L"), "blue", "yellow")
            self.add_to_history()
            self.display_image()

    def invert_colors(self):
        if self.image:
            self.image = ImageOps.invert(self.image)
            self.add_to_history()
            self.display_image()

    def add_text(self):
        if self.image:
            text = simpledialog.askstring("Input", "Enter text to add:")
            if text:
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()
                draw.text((10, 10), text, font=font, fill="white")
                self.add_to_history()
                self.display_image()

    def draw_rectangle(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            draw.rectangle([50, 50, 150, 150], outline="red", width=5)
            self.add_to_history()
            self.display_image()

    def draw_circle(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            draw.ellipse([50, 50, 150, 150], outline="blue", width=5)
            self.add_to_history()
            self.display_image()

    def draw_line(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            draw.line([0, 0, 200, 200], fill="green", width=5)
            self.add_to_history()
            self.display_image()

    def adjust_opacity(self):
        if self.image:
            alpha = self.image.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
            self.image.putalpha(alpha)
            self.add_to_history()
            self.display_image()

    def add_border(self):
        if self.image:
            self.image = ImageOps.expand(self.image, border=10, fill="black")
            self.add_to_history()
            self.display_image()

    def apply_sepia_filter(self):
        if self.image:
            sepia = [(r//2 + 100, g//2 + 50, b//2) for (r, g, b) in self.image.getdata()]
            self.image.putdata(sepia)
            self.add_to_history()
            self.display_image()

    def draw_polygon(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            draw.polygon([(100, 100), (150, 200), (200, 150)], outline="purple", fill=None, width=5)
            self.add_to_history()
            self.display_image()

    def adjust_gamma(self):
        if self.image:
            gamma = simpledialog.askfloat("Input", "Enter gamma value (0.1 - 5.0):", minvalue=0.1, maxvalue=5.0)
            if gamma:
                inv_gamma = 1.0 / gamma
                table = [((i / 255.0) ** inv_gamma) * 255 for i in range(256)]
                self.image = self.image.point(table)
                self.add_to_history()
                self.display_image()

    def apply_gaussian_blur(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.GaussianBlur(5))
            self.add_to_history()
            self.display_image()

    def calculate_histogram(self):
        if self.image:
            histogram = self.image.histogram()
            plt.figure()
            plt.title("Histogram")
            plt.xlabel("Pixel value")
            plt.ylabel("Frequency")
            plt.plot(histogram)
            plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()