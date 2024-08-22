import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

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
        self.edit_menu.add_command(label="Adjust Brightness", command=self.adjust_brightness)
        self.edit_menu.add_command(label="Adjust Contrast", command=self.adjust_contrast)
        self.edit_menu.add_command(label="Adjust Saturation", command=self.adjust_saturation)
        self.edit_menu.add_command(label="Flip Horizontally", command=lambda: self.flip_image("horizontal"))
        self.edit_menu.add_command(label="Flip Vertically", command=lambda: self.flip_image("vertical"))
        self.image = None

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.image.save(file_path)

    def display_image(self):
        img = self.image.resize((600, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def convert_to_grayscale(self):
        if self.image:
            self.image = self.image.convert("L")
            self.display_image()

    def pixelate_image(self):
        if self.image:
            small = self.image.resize((32, 32), Image.NEAREST)
            self.image = small.resize(self.image.size, Image.NEAREST)
            self.display_image()

    def rotate_image(self, angle):
        if self.image:
            self.image = self.image.rotate(angle)
            self.display_image()

    def crop_image(self):
        if self.image:
            width, height = self.image.size
            left = width // 4
            top = height // 4
            right = 3 * width // 4
            bottom = 3 * height // 4
            self.image = self.image.crop((left, top, right, bottom))
            self.display_image()

    def resize_image(self):
        if self.image:
            new_size = (400, 300)
            self.image = self.image.resize(new_size, Image.ANTIALIAS)
            self.display_image()

    def apply_filter(self, filter_type):
        if self.image:
            self.image = self.image.filter(filter_type)
            self.display_image()

    def adjust_brightness(self):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(1.5)
            self.display_image()

    def adjust_contrast(self):
        if self.image:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(1.5)
            self.display_image()

    def adjust_saturation(self):
        if self.image:
            enhancer = ImageEnhance.Color(self.image)
            self.image = enhancer.enhance(1.5)
            self.display_image()

    def flip_image(self, direction):
        if self.image:
            if direction == "horizontal":
                self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            elif direction == "vertical":
                self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
