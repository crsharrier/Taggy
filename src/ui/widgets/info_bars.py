import tkinter as tk
import customtkinter
from typing import List
import os

from model import FilesystemItem
from ui.styles import PAD, Images, Fonts


        
class Breadcrumbs(customtkinter.CTkTextbox):
    MAX_CRUMB_LENGTH = 15
    def __init__(self, master):
        super().__init__(master, height=1, corner_radius=2)
        self.configure(state="disabled")
        self.num_chars = 0

    def update_crumbs(self, item: FilesystemItem):
        crumbs = item.path.split(os.sep)
        #truncate long crumb names
        crumbs = [crumb[:self.MAX_CRUMB_LENGTH] + '...' if len(crumb) > self.MAX_CRUMB_LENGTH and index < len(crumbs) - 1  else crumb for index, crumb in enumerate(crumbs)]
        self.configure(state="normal")
        self.delete('0.0', tk.END)
        for crumb in reversed(crumbs):
            self.insert(f"0.{self.num_chars}", f"{crumb}")
            self.num_chars += len(crumb)
            self.insert(f"0.{self.num_chars}", " > ")
            self.num_chars += 3
        self.configure(state="disabled")

class TopPanel(customtkinter.CTkFrame):
    def __init__(self, master, on_analyze_click, on_settings_click, sample_folder: str):
        super().__init__(master, fg_color='transparent')
        self.on_analyze_click = on_analyze_click
        self.on_settings_click = on_settings_click

        root_folder_label = customtkinter.CTkLabel(self, text="Sample Folder: ", fg_color="transparent")
        root_folder_label.pack(side='left')
        root_folder_path = customtkinter.CTkLabel(self, text=sample_folder, fg_color="transparent", font=Fonts.bold())
        root_folder_path.pack(after=root_folder_label, side='left')

        analyze_button = customtkinter.CTkButton(self, text="Analyze", command=self.on_analyze_click, width=30, height=30)
        analyze_button.pack(side='right', padx=PAD)

        settings_button = customtkinter.CTkButton(self, text="", command=self.on_settings_click, width=30, height=30, image=Images.settings)
        settings_button.pack(side='right', after=analyze_button, padx=PAD)

class StatusBar(customtkinter.CTkTextbox):
    def __init__(self, master):
        super().__init__(master, corner_radius=2)
        self.configure(
            height=20, 
            width=800, 
            #fg_color="transparent",
            state="disabled"
            )
        
    def log(self, text: str):
        self.configure(state="normal")
        self.delete("0.0")
        self.insert("0.0", text)
        self.configure(state="disabled")