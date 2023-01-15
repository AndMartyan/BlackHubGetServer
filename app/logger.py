#!/usr/bin/env python3
import inspect
import logging
import os
from app import get_conf

folderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# input  pathConfig:
path_config = ''
get_conf.get_config(path_config=path_config)

level_log_map = {
    '0': logging.ERROR,
    '1': logging.WARNING,
    '2': logging.INFO,
    '3': logging.DEBUG
}

logging.basicConfig(filename=folderPath + '/black.log', level=level_log_map.get(get_conf.LEVEL_LOG, logging.DEBUG),
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def writelog(mode, message):
    if mode == "info":
        logging.info(str(message))
    elif mode == "warning":
        logging.warning(str(message))
    elif mode == "error":
        logging.error(str(message))
    else:
        logging.debug(str(message))
