from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("Configuration/config.ini")
    return config.get(category,key)