from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        name = request.param["name"]
        self.__controller.delete(name)

        return HttpResponse(status_code=204)