import model
import os
from settings import TaggySettings
from pathlib import Path
from typing import Dict, List, Callable

num_audio_files = 0
settings = TaggySettings()

def analyse_tags():
    pass

def analyse_types():
    pass

#============================================================
# Create Tree:
#============================================================

def create_tree(folder_path: str):
    model.Filesystem.tree = parse_filesystem_tree(folder_path)
    map_tree(search_filename_tags, model.Filesystem.tree)

# Walk through directory structure and return recursively built filesystem_dict.
#
# directory node ==> 'directory_name': [{path: 'relative_path'}, {}]
# file node      ==> 'file_name': {path: 'relative_path'} 
def parse_filesystem_tree(root_path):
    root_path = Path(root_path)
    filesystem_dict = {}

    for current_path in root_path.rglob('*'):
        # Relative path from the root
        relative_path = current_path.relative_to(root_path)

        # Create nested dictionaries for directories
        current_dict = filesystem_dict
        for part in relative_path.parts[:-1]:
            current_dict = current_dict.setdefault(part, [{'path': str(relative_path.parent)
                                                           ,'visible': True
                                                           }
                                                           ,{}])[1]
        filename = relative_path.parts[-1]
        if filename.lower().endswith(tuple(settings.file_formats)):
            current_dict = current_dict.setdefault(os.path.splitext(filename)[0], {'path': str(relative_path)
                                                              ,'visible': True
                                                              ,'type': ''
                                                              ,'format': os.path.splitext(relative_path)[1][1:]
                                                              ,'tags': []
                                                              })

    return filesystem_dict

# Traverse filesystem tree, applying function to each node 
def map_tree(function: Callable, tree: Dict):
    for _, value in tree.items():
        if isinstance(value, list):
            function(value[0])
            map_tree(function, value[1])
        else:
            function(value)

# Take a single file node and check for tags in filename
def search_filename_tags(file_node: Dict):
    for tag, aliases in model.Tags.filename_tags.items():
        for alias in aliases:
            if (alias.lower() in file_node['path'].lower() or 
                tag.lower() in file_node['path'].lower() ) and 'tags' in file_node:
                file_node['tags'].append(tag) if tag not in file_node['tags'] else file_node['tags'] 



#============================================================
# Search and Filter:
#============================================================
                                
# build list of nodes containing search term 
def filter_results(tree: Dict, search_term: str, result: Dict, search_ancestors=False):
    for _, value in tree.items():
        if isinstance(value, list):
            folder_node = value[0]
            folder_content = value[1]
            #node_path = value[1]['path']
            #parent_path = os.sep.join(value[1]['path'].split(os.sep)[:-1])
            #if search_term in folder_name:
            #    keyword_found = True
            filter_results(folder_content, search_term, result)
        else:
            file_node = value
            *parent_path_parts, file_name = file_node['path'].split(os.sep)
            if (search_term in file_name) or \
                (search_ancestors and search_term in parent_path_parts):
                result[file_node['path']] = file_node    

'''
def get_node_from_tree(key, var):
    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in get_node_from_tree(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in get_node_from_tree(key, d):
                        yield result
                        '''