import customtkinter
from customtkinter import ThemeManager
import tkinter as tk
from tkinter import font

class TagButton(customtkinter.CTkButton):
    unselected_colors = {
        'fg_color': 'azure4',
        'hover_color': 'grey33',
        'text_color': 'grey38'
    }
    def __init__(self, 
                 master, 
                 tag_name: str, 
                 is_selected=False):
        button_width = font.nametofont('TkDefaultFont').measure(tag_name)
        super().__init__(master,
                         width=button_width,
                         text=tag_name,
                         fg_color=TagButton.unselected_colors['fg_color'],
                         hover_color=TagButton.unselected_colors['hover_color'],
                         text_color=TagButton.unselected_colors['text_color'],
                         command=self.on_click
                         )
        self.tag_name = tag_name
        self.is_selected: bool = is_selected

    def on_click(self):
        self.is_selected = not self.is_selected
        self.configure(fg_color=ThemeManager.theme["CTkButton"]["fg_color"] if self.is_selected else TagButton.unselected_colors["fg_color"])
        self.configure(hover_color=ThemeManager.theme["CTkButton"]["hover_color"] if self.is_selected else TagButton.unselected_colors["hover_color"])
        self.configure(text_color=ThemeManager.theme["CTkButton"]["text_color"] if self.is_selected else TagButton.unselected_colors["text_color"])


class Checkbox(customtkinter.CTkCheckBox):
    def __init__(self, master, text, var):
        super().__init__(master, 
                        checkbox_height=18, 
                        checkbox_width=18, 
                        onvalue=True, 
                        offvalue=False, 
                        corner_radius=2)
        
        self.configure(text=text, variable=var)
