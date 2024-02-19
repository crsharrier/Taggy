from repository.abstract_repository import AbstractRepository
import model
from typing import Set


class FakeRepository(AbstractRepository):
    files: Set[model.File] = set()
    folders: Set[model.Folder] = set()

    def add_file(self, file: model.File):
        self.files.add(file)

    def add_folder(self, folder: model.Folder):
        self.folders.add(folder)

    def get_file(self, path: str):
        for file in self.files:
            if file.id == id:
                return file
        return None

    def get_folder(self, path: str):
        for folder in self.folders:
            if folder.id == id:
                return folder
        return None

    #Search files and folders based on selected criteria
    def search(search_term: str):
        pass