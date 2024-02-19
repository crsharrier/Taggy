from repository.abstract_repository import AbstractRepository
from analyse import create_tree
import model
import os
import json

class JSONRepository(AbstractRepository):
   
    def get_tree(self, folder_path: str):
        pass

    def load_tree(self, folder_path: str):
        json_file_name = 'tree'+folder_path.replace(os.path.sep, '_')+'.json'
        if os.path.exists(json_file_name):
            with open(json_file_name) as json_file:
                model.Filesystem.tree = json.load(json_file)
        else:
            create_tree(folder_path)

    def save_tree(self, folder_path: str):
        json_file_name = 'tree'+folder_path.replace(os.path.sep, '_')+'.json'
        with open(json_file_name, 'w') as json_file:
            json.dump(dict(model.Filesystem.tree), json_file, indent=4)

    def get_settings():
        pass

    def add_file(file: model.File):
        pass

    def add_folder(folder: model.Folder):
        pass

    def get_file(path: str):
        pass

    def get_folder(path: str):
        pass

    def add_file_format(format: str):
        pass

    def add_tag(format: str):
        pass

    #Search files and folders based on selected criteria
    def search(search_term: str):
        pass
