import abc


class HttpClient(abc.ABC):
    @abc.abstractmethod
    def get(self, url, headers=None, params=None):
        """Perform a GET request."""
        pass

    @abc.abstractmethod
    def post(self, url, headers=None, data=None):
        """Perform a POST request."""
        pass

    @abc.abstractmethod
    def delete(self, url, headers=None):
        """Perform a DELETE request"""
        pass

    @abc.abstractmethod
    def patch(self, url, headers=None, data=None):
        """Perform a PATCH request"""
        pass
