import os
import json
import logging

logger = logging.getLogger(__name__)

class TaggySettings:
    _PATH_TO_DB = 'taggy.db'
    _SAMPLE_FOLDER = '/home/crsharrier/Music'
    _FILE_FORMATS = ['wav', 'mp3', 'aiff', 'm4a']

    # Singleton implementation
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            #logger.debug('Creating TaggySettings...')
            print('Creating TaggySettings...')
            cls._instance = super(TaggySettings, cls).__new__(cls)
        return cls._instance

    def set_sample_folder_path(self, path: str):
        self._SAMPLE_FOLDER = path

    def add_file_format(self, format: str):
        self._FILE_FORMATS.append(format)

    def remove_file_format(self, format: str):
        self._FILE_FORMATS.remove(format)

    @property
    def path_to_db(self):
        return self._PATH_TO_DB
    
    @property
    def sample_folder(self):
        return self._SAMPLE_FOLDER
    
    @property
    def file_formats(self):
        return self._FILE_FORMATS
    
    def save_settings(self):
        settings_dict = {
            'path to db': self._PATH_TO_DB,
            'sample folder': self._SAMPLE_FOLDER,
            'file formats': self._FILE_FORMATS
        }
        with open('settings.json', 'w') as json_file:
            json.dump(settings_dict, json_file, indent=4)

    def load_settings(self):
        if os.path.isfile('settings.json'):
            with open('settings.json', 'r') as json_file:
                settings_dict = json.load(json_file)
            self._PATH_TO_DB = settings_dict['path to db']
            self._SAMPLE_FOLDER = settings_dict['sample folder']
            self._FILE_FORMATS = settings_dict['file formats']
    
    
