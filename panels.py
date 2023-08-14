from tkinter import filedialog

import customtkinter as ctk
from styling import *


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill="x", pady=4, ipady=8)


class SliderPanel(Panel):
    def __init__(self, parent, text, max_value, min_value, data_var):
        super().__init__(parent=parent)

        self.data_var = data_var

        for n in range(2):
            self.columnconfigure(n, weight=1)
            self.rowconfigure(n, weight=1)

        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky="w", padx=5)
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(column=1, row=0, sticky="e", padx=5)

        ctk.CTkSlider(self, from_=min_value, to=max_value, fg_color=SLIDER_BG,
                      variable=data_var).grid(column=0, row=1, columnspan=2, sticky="we", padx=5)

        self.data_var.trace_add("write", self.update_slider)

    def update_slider(self, *args):
        self.num_label.configure(text=f"{round(self.data_var.get(), 2)}")


class SegmentedPanel(Panel):
    def __init__(self, parent, text, data_var, options):
        super().__init__(parent=parent)

        ctk.CTkLabel(self, text=text).pack()
        ctk.CTkSegmentedButton(self, variable=data_var, values=options).pack(expand=True, fill="both", padx=5, pady=5)


class SwitchPanel(Panel):
    def __init__(self, parent, *args: tuple):
        super().__init__(parent=parent)

        for var, text in args:
            ctk.CTkSwitch(self, variable=var, text=text, button_color=BLUE, fg_color=SLIDER_BG
                          ).pack(side="left", expand=True, fill="both", padx=5, pady=5)


class FileNamePanel(Panel):
    def __init__(self, parent, name_string, path_string):
        super().__init__(parent=parent)

        self.name_string = name_string
        self.name_string.trace_add("write", self.update_text)
        self.path_string = path_string

        # WIDGETS
        ctk.CTkEntry(self, textvariable=self.name_string).pack(expand=True, fill="x", pady=5, padx=20)

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(expand=True, fill="x", padx=20)

        jpg_check_btn = ctk.CTkCheckBox(frame, text="jpg", variable=self.path_string, onvalue="jpg", offvalue="png",
                                        command=lambda: self.click(value="jpg"))
        jpg_check_btn.pack(side="left", expand=True, fill="x")

        png_check_btn = ctk.CTkCheckBox(frame, text="png", variable=self.path_string, onvalue="png", offvalue="jpg",
                                        command=lambda: self.click(value="png"))
        png_check_btn.pack(side="left", expand=True, fill="x")

        self.output_label = ctk.CTkLabel(self, text=" ")
        self.output_label.pack()

    def click(self, value):
        self.path_string.set(value)
        self.update_text()

    def update_text(self, *args):
        if self.name_string.get():
            text = self.name_string.get().replace(" ", "_") + "." + self.path_string.get()
            self.output_label.configure(text=text)


class FilePathPanel(Panel):
    def __init__(self, parent, folder_string):
        super().__init__(parent=parent)

        self.folder_string = folder_string

        ctk.CTkButton(self, text="Open Explorer", command=self.open_file_dialog).pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.folder_string).pack(expand=True, fill="both", pady=5, padx=5)

    def open_file_dialog(self):
        self.folder_string.set(filedialog.askdirectory())


class DropdownPanel(ctk.CTkOptionMenu):
    def __init__(self, parent, data_var, options):
        super().__init__(master=parent, values=options, variable=data_var, fg_color=DARK_GREY,
                         dropdown_fg_color=DROPDOWN_MENU, button_hover_color=DROPDOWN_HOVER, button_color=DROPDOWN_BG)
        self.pack(fill="x", pady=5)


class RevertButton(ctk.CTkButton):
    def __init__(self, parent, *args: tuple):
        super().__init__(master=parent, text="Revert", command=self.revert)
        self.pack(side="bottom", pady=10)

        self.args = args

    def revert(self):
        for var, value in self.args:
            var.set(value)


class SaveButton(ctk.CTkButton):
    def __init__(self, parent, export_func, name_string, file_string, folder_string):
        super().__init__(master=parent, text="Save", command=self.save)
        self.pack(side="bottom", pady=10)

        self.folder_string = folder_string
        self.name_string = name_string
        self.file_string = file_string

        self.export_func = export_func

    def save(self):
        self.export_func(self.folder_string.get(), self.name_string.get(), self.file_string.get())
