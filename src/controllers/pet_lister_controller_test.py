from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self) -> list:
        return [
            PetsTable(id=1, name="Buddy", type="Dog"),
            PetsTable(id=2, name="Mittens", type="Cat"),
        ]

def test_pet_lister():
    mock_repository = MockPetsRepository()
    controller = PetListerController(mock_repository)
    
    response = controller.list_pets()
    
    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "pets": [
                {"id": 1, "name": "Buddy", "type": "Dog"},
                {"id": 2, "name": "Mittens", "type": "Cat"}
            ]
        }
    }

    assert response == expected_response