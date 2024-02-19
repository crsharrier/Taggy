import asyncio
import customtkinter
import os
# import tkSnack

from model import Filesystem

from ui.widgets.elements import *
from ui.widgets.info_bars import TopPanel, StatusBar, Breadcrumbs
from ui.widgets.treeview import TreeView
from ui.widgets.search_pane import SearchPane
from ui.styles import PAD

from settings import TaggySettings

settings = TaggySettings()

class App(customtkinter.CTk):
    def __init__(self):
        print('Creating tkinter App object...')
        super().__init__()

        self.title("Taggy")
        self.geometry("900x600")
        self.grid_columnconfigure(0, weight=2, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        #self.grid_rowconfigure(0, weight=6, uniform='a')
        self.grid_rowconfigure((0, 1, 3), weight=0, uniform='a')
        self.grid_rowconfigure(2, weight=42, uniform='b')

        _top_panel = TopPanel(self, self.analyze_tags, self.open_settings, settings.sample_folder)
        _top_panel.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=PAD)

        _breadcrumbs = Breadcrumbs(self)
        _breadcrumbs.grid(row=1, column=0, columnspan=2, sticky="esw", padx=PAD)

        _treeview = TreeView(self)
        _treeview.grid(row=2, column=0, sticky='nesw', padx=PAD, pady=(PAD, 0))
        #_treeview.update_treeview(cousin_ids)
        _treeview.rebuild_tree(Filesystem.tree)
        #=============================================================================

        _search_pane = SearchPane(self, _treeview)
        _search_pane.grid(row=2, column=1, sticky='nesw')

        status_bar = StatusBar(self)
        status_bar.grid(row=3, column=0, padx=PAD, pady=PAD, columnspan=2, sticky="esw")
          
    def update_breadcrumbs(self, item: str):
        print(f'update_breadcrumbs({item}) called from APP')
        return
        self._breadcrumbs.update_crumbs(item)

    def analyze_tags(self):
        print("button pressed")
        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(self.db.tag_files())

    def open_settings(self):
        pass
        #SettingsWindow()