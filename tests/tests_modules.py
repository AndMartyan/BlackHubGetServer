from app import get_conf, logger
import requests


def test_config():
    assert not get_conf.get_config(
        path_config=logger.path_config) == {}


def test_connect():
    req = requests.get(url='https://blackrussia.online/politica.html')
    return req.text


def test_get():
    # input uvicorn_addr:
    uvicorn_addr = ''
    # input uvicorn_port:
    uvicorn_port = ''
    req = requests.get(url=f'http://{uvicorn_addr + ":" + uvicorn_port}/politica.html')
    assert str(req) == "<Response [200]>"
