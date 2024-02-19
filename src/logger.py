import logging

LOGFILE = 1
APP_BAR = 2


class TaggyLogger:
    # Singleton implementation
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            #logger.debug('Creating TaggyLogger...')
            print('Creating TaggyLogger...')
            cls._instance = super(TaggyLogger, cls).__new__(cls)
        return cls._instance
    
    logging.basicConfig(filename='taggy.log', level=logging.DEBUG)

    pass