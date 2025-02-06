import requests
from typing import Dict, Any, List, Union
from bpx.http_client.base.http_client import HttpClient
import json


class SyncHttpClient(HttpClient):
    def __init__(self, proxies: dict = None):
        self.proxies = proxies

    def get(
        self, url, headers=None, params=None
    ) -> Union[Dict[str, Any], List[Any], str]:
        response = requests.get(
            url=url, proxies=self.proxies, headers=headers, params=params
        )

        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text

    def post(
        self, url, headers=None, data=None
    ) -> Union[Dict[str, Any], List[Any], str]:
        response = requests.post(
            url=url, proxies=self.proxies, headers=headers, json=data
        )
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text

    def delete(
        self, url, headers=None, data=None
    ) -> Union[Dict[str, Any], List[Any], str]:
        response = requests.delete(
            url, proxies=self.proxies, headers=headers, json=data
        )
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text

    def patch(
        self, url, headers=None, data=None
    ) -> Union[Dict[str, Any], List[Any], str]:
        response = requests.patch(url, proxies=self.proxies, headers=headers, json=data)
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text
