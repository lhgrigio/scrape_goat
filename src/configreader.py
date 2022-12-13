import json;
from pathlib import Path

with open(Path().parent / 'config' / 'config.json') as _config_file:
    _config = json.load(_config_file)

def getConfig():
    return _config

def saveConfig():
    print('TO DO!')