import logging
import logging.config
import requests
from logging_config import CONF
from fastapi import FastAPI
import asyncio
import threading

class InternalService(object):
    def __init__(self):
        self.domain_url = 'http://localhost:5566/'

    def db_read(self,delay):
        url = f"{self.domain_url}db_read/{delay}"
        payload={}
        headers = {}
        response  = requests.request("GET", url, headers=headers, data=payload).json()
        # result.append(delay)
        return response

    
    def db_write(self,data):
        url = f"{self.domain_url}db_write/"
        payload={'data':data}
        headers = {}
        requests.request("post", url, headers=headers, data=payload).json()
        return

logging.config.dictConfig(CONF)
log = logging.getLogger(__name__)
internal_service = InternalService()
app = FastAPI()
    
@app.get('/db_read/{delay}')
async def db_read_test(delay):
    await asyncio.sleep(int(delay))
    return f'delay:{delay}'

@app.post('/db_write/')
async def async_test(data):
    print(f'data:{data} write')
    return []


@app.get('/async_test/')
async def async_test():
    def wrapper_task(result, **kwargs):
        response = internal_service.db_read(**kwargs)
        result.append(response)
    tasks = []
    result = []
    for delay in [7,2,5]:
        asyncio.sleep(1)
        task = threading.Thread(target=wrapper_task, kwargs={'result':result,'delay':delay})
        task.start()
        tasks.append(task)
    while 1:
        if result:
            print(result)
            break
    return result
