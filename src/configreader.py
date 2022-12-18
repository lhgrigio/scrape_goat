import json
from pathlib import Path

with open(Path().parent / 'config' / 'config.json') as _config_file:
    _config = json.load(_config_file)

def getConfig():
    return _config

def saveConfig(config):
    try:
        with open(Path().parent / 'config' / 'config.json', 'w') as _config_file:
            json.dump(config, _config_file, indent=4)
    except Exception as e:
        print('ERROR: ', e)