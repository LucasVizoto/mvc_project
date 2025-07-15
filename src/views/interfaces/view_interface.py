from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):
    
    #Handle an HTTP request and return an HTTP response
    @abstractmethod
    def handle_request(self, request: HttpRequest) -> HttpResponse:
        ...