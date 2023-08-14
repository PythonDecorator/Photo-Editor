import customtkinter as ctk
from tkinter import messagebox
from image_widgets import ImageImport, ImageOutput, CloseButton
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from styling import *
from menu import Menu
import os
import sys


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.effect_var_dict = None
        self.color_var_dict = None
        self.pos_var_dict = None
        self.pos_var = None
        self.zoom_float = None
        self.original_image = None
        self.rotation_float = None
        self.menu = None
        self.close_btn = None
        self.image_ratio = None
        self.image_tk = None
        self.image_output = None
        self.image = None

        ctk.set_appearance_mode("dark")
        self.title(" PhotoEditor App")
        self.geometry("1000x600")
        self.minsize(800, 500)
        self.iconbitmap(self.resource_path("files/image/logo.ico"))

        # VARIABLES
        self.init_parameters()
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # LAYOUT DESIGN
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=6, uniform="a")
        self.rowconfigure(0, weight=1)

        # WIDGETS
        self.image_import = ImageImport(self, self.import_image)

    def init_parameters(self):
        self.pos_var_dict = {
            "rotate": ctk.DoubleVar(value=ROTATE_DEFAULT),
            "zoom": ctk.DoubleVar(value=ZOOM_DEFAULT),
            "flip": ctk.StringVar(value=FLIP_OPTIONS[0]),
        }

        self.color_var_dict = {
            "brightness": ctk.DoubleVar(value=BRIGHTNESS_DEFAULT),
            "greyscale": ctk.BooleanVar(value=GREYSCALE_DEFAULT),
            "invert": ctk.BooleanVar(value=INVERT_DEFAULT),
            "vibrance": ctk.DoubleVar(value=VIBRANCE_DEFAULT)
        }

        self.effect_var_dict = {
            "blur": ctk.DoubleVar(value=BLUR_DEFAULT),
            "contrast": ctk.IntVar(value=CONTRAST_DEFAULT),
            "effect": ctk.StringVar(value=EFFECT_OPTIONS[0]),
        }

        all_var_list = list(self.pos_var_dict.values()) + list(self.color_var_dict.values()) + list(
            self.effect_var_dict.values())
        for var in all_var_list:
            var.trace_add("write", self.manipulate_image)

    def manipulate_image(self, *args):
        # ORIGINAL IMAGE
        self.image = self.original_image

        # ADD ROTATION
        if self.pos_var_dict["rotate"].get() != ROTATE_DEFAULT:
            self.image = self.image.rotate(self.pos_var_dict["rotate"].get())

        # ADD ZOOM
        if self.pos_var_dict["zoom"].get() != ZOOM_DEFAULT:
            self.image = ImageOps.crop(image=self.image, border=self.pos_var_dict["zoom"].get())

        # ADD FLIP
        if self.pos_var_dict["flip"].get() != FLIP_OPTIONS[0]:
            if self.pos_var_dict["flip"].get() == "X":
                self.image = ImageOps.mirror(self.image)
            if self.pos_var_dict["flip"].get() == "Y":
                self.image = ImageOps.flip(self.image)

            if self.pos_var_dict["flip"].get() == "Both":
                self.image = ImageOps.mirror(self.image)
                self.image = ImageOps.flip(self.image)

        # ADD BRIGHTNESS AND VIBRANCE
        if self.color_var_dict["brightness"].get() != BRIGHTNESS_DEFAULT:
            brightness_enhancer = ImageEnhance.Brightness(self.image)
            self.image = brightness_enhancer.enhance(self.color_var_dict["brightness"].get())

        if self.color_var_dict["vibrance"].get() != VIBRANCE_DEFAULT:
            vibrance_enhancer = ImageEnhance.Color(self.image)
            self.image = vibrance_enhancer.enhance(self.color_var_dict["vibrance"].get())

        # ADD GRAYSCALE AND INVERT
        if self.color_var_dict["greyscale"].get() != GREYSCALE_DEFAULT:
            if self.color_var_dict["greyscale"].get():
                self.image = ImageOps.grayscale(self.image)

        if self.color_var_dict["invert"].get() != INVERT_DEFAULT:
            if self.color_var_dict["invert"].get():
                try:
                    self.image = ImageOps.invert(self.image)
                except OSError:
                    messagebox.showinfo("Not Supported", message="Invert is not supported for this image mode")

        # ADD BLUR AND CONTRAST
        if self.effect_var_dict["blur"].get() != BLUR_DEFAULT:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.effect_var_dict["blur"].get()))

        if self.effect_var_dict["contrast"].get() != CONTRAST_DEFAULT:
            self.image = self.image.filter(ImageFilter.UnsharpMask(self.effect_var_dict["contrast"].get()))

        # EFFECTS OPTIONS
        match self.effect_var_dict["effect"].get():
            case "Emboss": self.image.filter(ImageFilter.EMBOSS)
            case "Fine Edges": self.image.filter(ImageFilter.FIND_EDGES)
            case "Contour": self.image.filter(ImageFilter.CONTOUR)
            case "Edge Enhance": self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)

        self.place_image()

    def import_image(self, path):
        self.original_image = Image.open(path)
        self.image = self.original_image
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_forget()

        self.image_output = ImageOutput(self, self.resized_image)
        self.close_btn = CloseButton(self, self.close_edit)
        self.menu = Menu(self, self.pos_var_dict, self.color_var_dict, self.effect_var_dict, self.export)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_btn.place_forget()
        self.menu.grid_forget()

        self.image_import = ImageImport(self, self.import_image)

    def resized_image(self, event):
        canvas_ratio = event.width / event.height
        self.canvas_width = event.width
        self.canvas_height = event.height

        if canvas_ratio > self.image_ratio:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self):
        self.image_output.delete("all")
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image((self.canvas_width / 2, self.canvas_height / 2), image=self.image_tk)

    def export(self, path, name, file):
        export_string = f"{path}/{name}.{file}"
        self.image.save(export_string)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = App()
    app.mainloop()
