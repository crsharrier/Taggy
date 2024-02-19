import tkinter as tk
from tkinter import ttk
from model import Filesystem, FilesystemItem
from typing import Dict
import os
from analyse import map_tree


class TreeView(ttk.Treeview):
    def __init__(self, master):
        self.column_names = ['File', 'Tags']
        super().__init__(master, columns=self.column_names, height=20)
        self.heading('#0', text='Folder')
        for name in self.column_names:
            title_case = ' '.join(word.capitalize() for word in name.split('_'))
            self.heading(name, text=title_case)

        self.attached_nodes = dict()
        self.detached_nodes = dict()

        self.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        pass
        row_clicked = self.identify_row(event.y)
        col_clicked = self.identify_column(event.x)
        current_state = self.item(row_clicked, 'open')
        print(row_clicked)
        #if col_clicked != '#0':    
        #    self.item(row_clicked, open=not current_state)
        item = FilesystemItem(row_clicked)
        #self.master.update_breadcrumbs(item)

    def insert_node(self, node: Dict):
        node_path = node['path']
        node_name = node['path'].split(os.sep)[-1]
        parent_path = os.sep.join(node['path'].split(os.sep)[:-1])   
        #if node is a folder, not a file:
        if 'format' not in node.keys():
            self.insert(iid=node_path
                        ,parent=parent_path
                        ,open=node['visible']
                        ,index=tk.END
                        ,text=node_name)
        else:
            values = [os.path.splitext(node_name)[0], node['tags']]
            self.insert(iid=node_path
                        ,parent=parent_path
                        ,open=True
                        ,index=tk.END
                        ,values=values) 

    def insert_node_into_flat_list(self, node: Dict):
        #print('node = '+str(node))
        node_path = node['path']
        node_name = node['path'].split(os.sep)[-1]
        values = [os.path.splitext(node_name)[0], node['tags']]
        self.insert(iid=node_path
                    ,parent=''
                    ,open=True
                    ,index=tk.END
                    ,values=values)  

    def clear(self):
        for item in self.get_children():
            self.delete(item)

    def rebuild_tree(self, tree: Dict, flat=False):
        self.clear()
        #print('tree = '+str(tree))
        if flat:
            map_tree(self.insert_node_into_flat_list, tree)
        else: 
            map_tree(self.insert_node, tree)
    