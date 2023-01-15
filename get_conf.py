#!/usr/bin/env python3
import os
import tomli


def get_config(path_config: str):
    global LEVEL_LOG
    if os.path.exists(path_config):
        try:
            with open(path_config, "rb") as f:
                config = tomli.load(f)
        except:
            config = {}
            return config
        LEVEL_LOG = config.get("logger", '').get('level', '')
        return config
    else:
        config = {}
        return config