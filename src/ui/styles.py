import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
import darkdetect

#customtkinter.set_default_color_theme("src/ui/Taggy_theme.json")

def get_image(light_path: str, dark_path: str, width: int, height: int):
    image = customtkinter.CTkImage(light_image=Image.open(light_path),
                                  dark_image=Image.open(dark_path),
                                  size=(width, height))
    return image

class Images:
    search = get_image('images/search_light.png', 'images/search_dark.png', 20, 20)
    settings = get_image('images/settings_light.png', 'images/settings_dark.png', 20, 20)

class Fonts:
    def bold():
        return customtkinter.CTkFont(family='Roboto', size=14, weight='bold')

# Check system appearance mode and set colors accordingly
#treeview_style = ttk.Style()
'''if darkdetect.isDark():
    treeview_style.theme_use('clam')  # Change 'clam' to your preferred theme
    treeview_style.configure("Treeview", background="#333", foreground="#fff")  # Dark mode colors
else:
    treeview_style.theme_use('clam')  # Change 'clam' to your preferred theme
    treeview_style.configure("Treeview", background="#fff", foreground="#000")  # Light mode colors
'''

#print(treeview_style.theme_use())

PAD = 4

