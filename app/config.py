import os
import tomli

pathConfig = ''


def get_config(pathConfig):
    global LEVEL_LOG
    if os.path.exists(pathConfig):
        try:
            with open(pathConfig, "rb") as f:
                config = tomli.load(f)
        except:
            config = {}
        LEVEL_LOG = config.get("logger", '').get('level', '')


# input  pathConfig:
get_config(pathConfig='')

