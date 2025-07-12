from pytest import raises

from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass



def test_create():
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response['data']["type"] == 'Person'
    assert response['data']["count"] == 1
    assert response['data']["attributes"] == person_info


def test_create_error():
    person_info = {
        "first_name": "Teste123",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123
    }
    controller = PersonCreatorController(MockPeopleRepository())

    with raises(Exception) as exc_info:
        controller.create(person_info)

    assert str(exc_info.value) == "First name and last name must contain only letters."