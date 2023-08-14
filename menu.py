from abc import ABC
import customtkinter as ctk
from styling import *
from panels import SliderPanel, SegmentedPanel, SwitchPanel, DropdownPanel, RevertButton, FileNamePanel, \
    FilePathPanel, SaveButton


class Menu(ctk.CTkTabview, ABC):
    def __init__(self, parent, pos_var_dict, color_var_dict, effect_var_dict, export_func):
        super().__init__(master=parent)
        self.grid(column=0, row=0, sticky="news", padx=10, pady=10)

        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        PositionFrame(self.tab("Position"), pos_var_dict)
        ColorFrame(self.tab("Color"), color_var_dict)
        EffectFrame(self.tab("Effects"), effect_var_dict)
        ExportFrame(self.tab("Export"), export_func)


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_var_dict):
        super().__init__(master=parent)
        self.pack(expand=True, fill="both")

        SliderPanel(self, text="Rotate", min_value=0, max_value=360, data_var=pos_var_dict["rotate"])
        SliderPanel(self, text="Zoom", min_value=0, max_value=250, data_var=pos_var_dict['zoom'])
        SegmentedPanel(self, text="Invert", data_var=pos_var_dict['flip'], options=FLIP_OPTIONS)
        RevertButton(self, (pos_var_dict["rotate"], ROTATE_DEFAULT), (pos_var_dict["zoom"], ZOOM_DEFAULT),
                     (pos_var_dict["flip"], FLIP_OPTIONS[0]))


class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_var_dict):
        super().__init__(master=parent)
        self.pack(expand=True, fill="both")

        SwitchPanel(self, (color_var_dict["greyscale"], "B/W"), (color_var_dict["invert"], "Invert"))
        SliderPanel(self, text="Brightness", min_value=0, max_value=5, data_var=color_var_dict["brightness"])
        SliderPanel(self, text="Vibrance", min_value=0, max_value=5, data_var=color_var_dict['vibrance'])
        RevertButton(self, (color_var_dict["greyscale"], GREYSCALE_DEFAULT), (color_var_dict["invert"], INVERT_DEFAULT),
                     (color_var_dict["brightness"], BRIGHTNESS_DEFAULT), (color_var_dict['vibrance'], VIBRANCE_DEFAULT))


class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_var_dict):
        super().__init__(master=parent)
        self.pack(expand=True, fill="both")

        DropdownPanel(self, data_var=effect_var_dict["effect"], options=EFFECT_OPTIONS)
        SliderPanel(self, text="Blur", min_value=0, max_value=30, data_var=effect_var_dict["blur"])
        SliderPanel(self, text="Contrast", min_value=0, max_value=10, data_var=effect_var_dict['contrast'])
        RevertButton(self, (effect_var_dict["effect"], EFFECT_OPTIONS[0]), (effect_var_dict["blur"], BLUR_DEFAULT),
                     (effect_var_dict['contrast'], CONTRAST_DEFAULT))


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_func):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")

        self.export_func = export_func

        # VARIABLES
        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value="jpg")
        self.folder_string = ctk.StringVar()

        # WIDGETS
        FileNamePanel(self, name_string=self.name_string, path_string=self.file_string)
        FilePathPanel(self, folder_string=self.folder_string)
        SaveButton(self, self.export_func, self.name_string, self.file_string, self.folder_string)
