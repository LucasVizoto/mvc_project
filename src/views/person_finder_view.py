from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.__controller = controller
    
    def handle_request(self, request: HttpRequest) -> HttpResponse:
        person_id = request.param["person_id"]
        response = self.__controller.find(person_id)
        return HttpResponse(status_code=200, body=response)