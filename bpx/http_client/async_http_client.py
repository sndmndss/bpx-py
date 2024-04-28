import aiohttp
from bpx.http_client.http_client import HttpClient
import json


class AsyncHttpClient(HttpClient):

    def __init__(self, proxy: str = ""):
        self.proxy = proxy

    async def get(self, url, headers=None, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, proxy=self.proxy, params=params, headers=headers) as response:
                try:
                    return await response.json()
                except json.JSONDecodeError:
                    return await response.text()
                except aiohttp.client_exceptions.ContentTypeError:
                    return await response.text()

    async def post(self, url, headers=None, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, proxy=self.proxy, headers=headers, data=json.dumps(data)) as response:
                try:
                    return await response.json()
                except json.JSONDecodeError:
                    return await response.text()
                except aiohttp.client_exceptions.ContentTypeError:
                    return await response.text()

    async def delete(self, url, headers=None, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, proxy=self.proxy, headers=headers, data=json.dumps(data)) as response:
                try:
                    return await response.json()
                except json.JSONDecodeError:
                    return await response.text()
                except aiohttp.client_exceptions.ContentTypeError:
                    return await response.text()
