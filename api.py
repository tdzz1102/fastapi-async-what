import threading
from fastapi import FastAPI
from time import sleep
from hashlib import md5
from random import randint

app = FastAPI()


def work(n):
    sleep(n)
    b = randint(602, 2021).to_bytes(4, 'big')
    return md5(b).hexdigest()


async def awork(n):
    sleep(n)
    b = randint(602, 2021).to_bytes(4, 'big')
    return md5(b).hexdigest()


@app.get('/awork')
async def awk(n: int = 7):
    res = await awork(n)
    print(123)
    return res


@app.get('/work')
def wk(n: int = 7):
    res = work(n)
    return res


@app.get('/aping')
async def aping():
    return 'APONG!'


@app.get('/ping')
def ping():
    return 'PONG!'


@app.get('/tid')
def tid():
    return threading.get_ident()
