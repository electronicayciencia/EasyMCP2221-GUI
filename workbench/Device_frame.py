import tkinter as tk
from tkinter import ttk

import logging
logger = logging.getLogger(__name__)

class Device_frame(ttk.Labelframe):
    """Populate device data frame."""

    def __init__(self, root, sts):
        super().__init__(root)

        self["text"] = " Device "

        package = {
            "anchor": tk.W,
            "pady": 5,
            "padx": 10
        }

        ttk.Label(self,
            font=("", 12),
            wraplength=500,
            textvariable=sts["strings"]["description"]).pack(**package)

        ttk.Label(self,
            textvariable=sts["strings"]["serial"]).pack(**package)

        ttk.Label(self,
            textvariable=sts["strings"]["factserial"]).pack(**package)

        ttk.Label(self,
            textvariable=sts["strings"]["vendor"]).pack(**package)
