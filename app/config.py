import os
import tomli

# input  pathConfig:
pathConfig = ''
if os.path.exists(pathConfig):
    try:
        with open(pathConfig, "rb") as f:
            config = tomli.load(f)
            f.close()
    except:
        config = {}
    LEVEL_LOG = config.get("logger", '').get('level', '')

