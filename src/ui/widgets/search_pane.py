import tkinter as tk
import customtkinter
from customtkinter import ThemeManager
from analyse import filter_results

from typing import List

from model import File, Tags, Filesystem
from ui.styles import PAD, Images
from ui.widgets.treeview import TreeView 
from ui.widgets.elements import Checkbox, TagButton

class SearchPaneLabel(customtkinter.CTkLabel):
    def __init__(self, master, text):
        super().__init__(master=master, text=text)
            
class SearchPane(customtkinter.CTkFrame):
    def __init__(self, master, treeview):
        self.treeview: TreeView = treeview
        super().__init__(master)
        
        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._var_Should_search_file_name = customtkinter.BooleanVar(value=True)
        self._var_Should_search_parent_folders = customtkinter.BooleanVar(value=True)

        self._var_Should_show_loops = customtkinter.BooleanVar(value=True)
        self._var_Should_show_oneshots = customtkinter.BooleanVar(value=True)
        self._var_Should_show_tracks = customtkinter.BooleanVar(value=True)

        self.create_search_box()
        self.create_search_checkboxes()
        self.create_file_type_checkboxes()
        self.create_tag_selection_pane()
    
    def create_search_box(self):
        search_box = customtkinter.CTkTextbox(self, height=1)
        search_box.grid(row=0, column=0, padx=PAD, pady=(PAD, 0), sticky="new")
        search_box.bind("<KeyRelease>", self.on_text_change)

        image_label = customtkinter.CTkLabel(search_box, image=Images.search, text="", width=20, height=20)
        image_label.place(relx=0.9, rely=0.5, anchor=tk.CENTER)

    def create_search_checkboxes(self):
        frame = customtkinter.CTkFrame(self, height=2)
        frame.grid(row=1, column=0, padx=PAD, pady=(PAD, 0), sticky='new')
        frame.grid_rowconfigure((0, 1), weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        text = 'Match:'
        label = SearchPaneLabel(frame, text)
        file_name_cb = Checkbox(frame, 'File Name', self._var_Should_search_file_name)
        parent_folders_cb = Checkbox(frame, 'Parent Folders', self._var_Should_search_parent_folders)

        label.grid(row=0, column=0, padx=PAD, sticky='w')
        file_name_cb.grid(row=1, column=0, padx=PAD, sticky='w')
        parent_folders_cb.grid(row=1, column=1, padx=PAD, sticky='w')

    def create_file_type_checkboxes(self):
        frame = customtkinter.CTkFrame(self, height=2)
        frame.grid(row=2, column=0, padx=PAD, pady=(PAD, 0), sticky='new')
        frame.grid_rowconfigure((0, 1), weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        text = 'Show:'
        label = SearchPaneLabel(frame, text)
        loops_cb = Checkbox(frame, 'Loops', self._var_Should_show_loops)
        oneshots_cb = Checkbox(frame, 'Oneshots', self._var_Should_show_oneshots)
        tracks_cb = Checkbox(frame, 'Tracks', self._var_Should_show_tracks)

        label.grid(row=0, column=0, padx=PAD, sticky='w')
        loops_cb.grid(row=0, column=1, padx=PAD, sticky='w')
        oneshots_cb.grid(row=1, column=1, padx=PAD, sticky='w')
        tracks_cb.grid(row=1, column=0, padx=PAD, sticky='w')

    def create_tag_selection_pane(self):
        frame = tk.Text(self, state='disabled', cursor='arrow', background='gray13')
        frame.grid(row=3, column=0, padx=PAD, pady=(PAD, 0), sticky='nesw')
        for tag in Tags.filename_tags:
            tag_button = TagButton(frame, tag_name=tag)
            frame.window_create(tk.INSERT, window=tag_button, padx=5, pady=5)
    
    def on_text_change(self, event):    
        search_term = event.widget.get("1.0", "end-1c")  # Get the content of the Text widget
        if search_term == '':
            self.treeview.rebuild_tree(Filesystem.tree)
            return
    
        search_result = dict()
        filter_results(Filesystem.tree, search_term, search_result, search_ancestors=self._var_Should_search_parent_folders)
        #print('result = '+str(search_result))
        self.treeview.rebuild_tree(search_result, flat=True)