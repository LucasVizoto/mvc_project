from .pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    # Arrange
    mock_pets_repository = mocker.Mock()
    pet_deleter_controller = PetDeleterController(mock_pets_repository)
    pet_name = "Buddy"

    # Act
    pet_deleter_controller.delete(pet_name)

    # Assert
    mock_pets_repository.delete_pets.assert_called_once_with(pet_name)
