import customtkinter as ctk
from styling import *
from tkinter import filedialog, Canvas


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky="news")
        self.import_func = import_func

        ctk.CTkButton(self, text="Import Image", command=self.open_dialog).pack(expand=True)

    def open_dialog(self):
        path = filedialog.askopenfilename()
        self.import_func(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resized_image):
        super().__init__(master=parent, bg=BACKGROUND, bd=0, highlightthickness=0, relief="ridge")
        self.grid(column=1, row=0, sticky="news", padx=10, pady=10)

        self.bind("<Configure>", resized_image)


class CloseButton(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master=parent, text="x", fg_color="transparent", hover_color=CLOSE_RED, width=40,
                         height=40, corner_radius=0, text_color=WHITE, command=close_func)
        self.place(relx=0.99, rely=0.01, anchor="ne")
