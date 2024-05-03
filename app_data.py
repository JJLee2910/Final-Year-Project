from UI.Login import *


# singleton data class
class AppData(object):
    _instance = None
    router = None

    def __new__(cls):
        if cls._instance is None:
            print("creating new AppData instance")
            cls._instance = super(AppData, cls).__new__(cls)
        return cls._instance
