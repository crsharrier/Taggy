import os
import model
from typing import Set, List, Dict
from enum import Enum

class FileType(Enum):
    ONESHOT = 'oneshot'
    LOOP = 'loop'
    TRACK = 'track'

# ===================================================================================================
# DatabaseItem
# generic class from which File and Folder inherit
# ===================================================================================================
class FilesystemItem:
    def __init__(self, path: str, parent_folder=None):
        self.parent_folder: model.Folder = parent_folder
        self.path = path
    
    def __str__(self):
        return self.get_name()

    def get_path(self) -> str:
        return self.path

    def get_name(self) -> str:
        return os.path.basename(self.path)
    
    def get_parent_folder(self):
        return self.parent_folder
    
    def set_parent_folder(self, parent_folder):
        parent_folder.children.add(self)
        self.parent_folder = parent_folder


# ===================================================================================================
# File class:
# ===================================================================================================
    
class File(FilesystemItem):
    def __init__(self, path: str, parent_folder=None):
        super().__init__(path, parent_folder)
        self.tags: Set[str] = set()
        self._file_type = 'track'
        self._file_format = ''

    def __repr__(self):
        return 'FILE:' + self.get_name()
    
    def get_file_type(self):
        return self._file_type
    
    def get_file_format(self):
        return self._file_format
    
    def get_tags(self):
        return self.tags

    def set_file_type(self, file_type: FileType):
        self._file_type = file_type

    def set_file_format(self, format: str):
        self._file_format = format

    def add_tag(self, tag: str):
        if tag in model.Tags.filename_tags:
            self.tags.add
        else:
            raise ValueError(f'\"{tag}\" tag doesn\'t exist!')
        
    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise ValueError(f'\"{tag}\" tag not found!')

# ===================================================================================================
# Folder class:
# ===================================================================================================
    
class Folder(FilesystemItem):
    def __init__(self, path: str, parent_folder=None):
        super().__init__(path, parent_folder)
        self.children: Set[FilesystemItem] = set()

    def __repr__(self):
        return 'FOLDER:' + self.get_name()
    
    def get_children(self):
        return self.children
    
# ===================================================================================================
# FileFormats class:
# ===================================================================================================

class FileFormats:
    formats = {'wav', 'mp3', 'aiff'}

    @classmethod
    def add_format(cls, new_format: str):
        cls.formats.add(new_format)

    @classmethod
    def remove_format(cls, format_to_remove: str):
        if format_to_remove in cls.formats:
            cls.formats.remove(format_to_remove)
        else:
            raise ValueError(f'Attempted to delete \"{format_to_remove}\" but file format doesn\'t exist!')

# ===================================================================================================
# Tags class:
# ===================================================================================================
class Tags:
    filename_tags = {
        '808': [],
        '909': [],
        'KICK': ['bd', 'kick', 'bass drum'],
        'SNARE': ['snare', 'snr', 'sd'],
        'CLOSED_HH': ['hhc', 'chh', 'hat closed', 'closed hat'],
        'OPEN_HH': ['hho', 'ohh', 'hat open', 'open hat'],
        'VOCAL': ['vox', 'vocals'],
        'RIM': ['rim', 'rim shot', 'sidestick'],
        'TOM': [],
        'MARACA': ['maracas'],
        'RIDE': ['ride']
        }
    
    @classmethod
    def create_tag(cls, new_tag: str, aliases: List[str]=None):
        cls.filename_tags[new_tag] = aliases

    @classmethod
    def delete_tag(cls, tag_to_delete: str):
        if tag_to_delete in cls.filename_tags:
            del cls.filename_tags[tag_to_delete]
        else:
            raise ValueError(f'Attempted to delete \"{tag_to_delete}\" but tag doesn\'t exist!')
        

class Filesystem:
    root_folder: model.Folder = None
    tree: Dict = {root_folder: []}

'''
    @classmethod
    def add_item(cls, new_item: FilesystemItem):
        crumbs = get_crumbs_from_item(new_item)
        #print(f'crumbs = {crumbs}')
        current_dir = cls.tree
        for crumb in crumbs[:-1]:
            current_dir = current_dir.setdefault(crumb, {})
            current_node = current_node[crumb]
        #print(f'current node = {current_node}')
        #print(f'crumbs[-1] = {crumbs[-1]}')
        #current_node[crumbs[-1]] = ''

    @classmethod
    def remove_item(cls, item_to_delete: FilesystemItem):
        crumbs = get_crumbs_from_item(item_to_delete)
        current_node = cls.paths
        for crumb in crumbs:
            if crumb not in current_node:
                raise ValueError(f'\"{item_to_delete.path}\" item not found!')
            current_node = current_node[crumb] 
        del current_node
'''