from repository.abstract_repository import AbstractRepository
import sqlite3
import model
from settings import PATH_TO_DB
from typing import Set, List

class SQLRepository(AbstractRepository):
    def __init__(self):
        self.conn = sqlite3.connect(PATH_TO_DB)
        self.cursor = self.conn.cursor()
        print(f'Connected to database @ {PATH_TO_DB}!')
        self.files: Set[model.File] = set()
        self.folders: Set[model.Folder] = set()
    
    def add_file(self, file: model.File):
        self.cursor.execute(
            '''INSERT OR IGNORE INTO filesystem_item 
                (path, parent_folder_path, file_format) 
                VALUES (?, ?, ?)''', (file.path, file.parent_folder.path, file.get_file_format())
                )

    def add_folder(self, folder: model.Folder):
        self.cursor.execute(
            '''INSERT OR IGNORE INTO filesystem_item 
                (path, parent_folder_path, type) 
                VALUES (?, ?, ?)''', (folder.path, folder.parent_folder.path, 'folder')
                )
        
    def add_item_relation(self, parent_folder: model.Folder, child_item: model.FilesystemItem):
        self.cursor.execute(
            '''INSERT OR IGNORE INTO item_item 
                (parent_path, child_path) 
                VALUES (?, ?)''', (parent_folder.path, child_item.parent_folder.path)
                )
    
    def add_file_format(self, file_format: str):
        if file_format not in model.FileFormats.formats:
            raise ValueError(f'\"{file_format}\" not on list of file_formats!')
        else:
            self.cursor.execute(
                '''INSERT OR IGNORE INTO file_format
                    (format_name)
                    VALUES (?)''', (file_format,)
                    )
            
    def add_tag(self, tag_name: str, aliases: List[str]):
        if tag_name not in model.Tags.filename_tags:
            raise ValueError(f'\"{tag_name}\" not on list of filename_tags!')
        self.cursor.execute(
            '''INSERT OR IGNORE INTO tag
                (tag_name)
                VALUES (?)''', (tag_name,)
                )
        for alias in aliases:
            self.cursor.execute(
                '''INSERT OR IGNORE INTO tag_alias
                    (tag_name, alias)
                    VALUES (?, ?)''', (tag_name, alias)
                    )
    
    def add_tag_item_relation(self, item: model.FilesystemItem, tag_name: str):
        if tag_name not in model.Tags.filename_tags:
            raise ValueError(f'\"{tag_name}\" not on list of filename_tags!')
        self.cursor.execute(
            '''INSERT OR IGNORE INTO tag_item
                (tag_name, file_path)
                VALUES (?, ?)''', (tag_name, item.path)
                )

    def get_file(self, path: str):
        self.cursor.execute(
            '''SELECT parent_folder_path, type, file_format FROM filesystem_item 
                WHERE path = ?''', (path,)
                )
        search_result = self.cursor.fetchone()
        file = model.File(search_result[0])
        file.set_file_type(search_result[1])
        file.set_file_format(search_result[2])

        return file

    def get_folder(self, path: str):
        self.cursor.execute(
            '''SELECT parent_folder_path, type, file_format FROM filesystem_item 
                WHERE path = ?''', (path,)
                )
        return model.File(self.cursor.fetchone()[0])

    #Search files and folders based on selected criteria
    def search(search_term: str):
        pass

    def commit_changes(self):
        self.conn.commit()

    def close_connection(self):
        self.close_connection()
        
