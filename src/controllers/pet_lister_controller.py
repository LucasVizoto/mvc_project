from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets
    
    def __format_response(self, pets:list[PetsTable]) -> dict:
        formated_pets = []
        for pet in pets:
            formated_pets.append({
                "id": pet.id,
                "name": pet.name,
                "type": pet.type
            })
        return {
            "data": {
                "type": "Pets",
                "count": len(formated_pets),
                "pets": formated_pets
            }
        }
