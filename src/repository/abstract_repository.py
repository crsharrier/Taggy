from abc import ABC, abstractmethod
import model

class AbstractRepository(ABC):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print('Creating repository...')
            cls._instance = super(AbstractRepository, cls).__new__(cls)
        return cls._instance
    
    @abstractmethod
    def add_file(file: model.File):
        pass

    @abstractmethod
    def add_folder(folder: model.Folder):
        pass

    @abstractmethod
    def get_file(path: str):
        pass

    @abstractmethod
    def get_folder(path: str):
        pass

    #Search files and folders based on selected criteria
    @abstractmethod
    def search(search_term: str):
        pass

    