# _*_coding: utf-8_*_
#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from selenium import webdriver
import time
import logger

app = FastAPI()


# getting html-file with selenium
def get_html(url: str):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(6)
    html = browser.page_source
    browser.quit()
    return str(html)


# getting a GET request
@app.get("/{path}", response_class=HTMLResponse)
async def read_items(path: str):
    logger.writelog('info', f"get request to {path}")
    if len(path) > 0:
        # URL formation
        url = f"https://blackrussia.online/{path}"
        # Replace "black russia" to "Black Hub Games"
        page = get_html(url).replace("black russia", "Black Hub Games")
        logger.writelog('error', f"good request /{path}")
        return HTMLResponse(content=page, status_code=200)
    else:
        logger.writelog('error', f"bad request")
        return HTMLResponse(status_code=404)

