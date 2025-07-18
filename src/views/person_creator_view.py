from src.validators.person_creator_validator import person_creator_validator
from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller
        

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        person_creator_validator(request)
        
        person_info = request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)