from typing import Optional


class RequestConfiguration:
    def __init__(self, url: str, headers: Optional[dict] = None, params: Optional[dict] = None, data: Optional[dict] = None):
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data
