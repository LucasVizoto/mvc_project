from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        response = self.__controller.list_pets()
        return HttpResponse(status_code=200, body=response)