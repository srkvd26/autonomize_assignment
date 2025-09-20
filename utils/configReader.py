import configparser
import os

class ConfigReader:
    def __init__(self, file_path="config.ini"):
        self.config = configparser.ConfigParser()
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found: {file_path}")
        self.config.read(file_path)

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)
