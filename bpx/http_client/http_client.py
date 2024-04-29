import abc


class HttpClient(abc.ABC):
    @abc.abstractmethod
    def _get(self, url, headers=None, params=None):
        """Perform a GET request."""
        pass

    @abc.abstractmethod
    def _post(self, url, headers=None, data=None):
        """Perform a POST request."""
        pass

    @abc.abstractmethod
    def _delete(self, url, headers=None):
        """Perform a DELETE request"""
        pass
