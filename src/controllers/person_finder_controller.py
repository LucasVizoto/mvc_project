from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInteface
from src.models.sqlite.entities.people import PeopleTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInteface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__get_person_from_db(person_id)
        formatted_response = self.__format_response(person)
        return formatted_response

    def __get_person_from_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Person not found.")
        return person

    def __format_response(self, person_info: PeopleTable) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person_info.first_name,
                    "last_name": person_info.last_name,
                    "pet_name": person_info.pet_name,
                    "pet_type": person_info.pet_type
                }
            }
        }