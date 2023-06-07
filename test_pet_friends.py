from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа не пройдет при невалидном email"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' != result


def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа не пройдет при невалидном password"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' != result


def test_get_api_key_for_invalid_email_and_password(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа не пройдет при невалидном email  и password"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' != result

def test_get_pet_by_nonexistent_filter(filter='uncorrect'):
        """ Проверяем , что поиск по несуществующему фильтру невозможен """

        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.get_list_of_pets(auth_key, filter)

        assert status == 500

def test_new_pet_without_name(animal_type='Piggy', name = "Piggy", age='4', pet_photo='image/piggy.txt'):
    """Проверяем, что в изображение нельзя передать текстовый формат"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key,animal_type, name, age, pet_photo)

    assert status == 500

def test_add_new_pet_with_invalid_data_name(animal_type='Piggy',
                                     age='4', pet_photo='image/piggy.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pet_with_invalid_data_animaltype(name = "Piggy",  age='4', pet_photo='image/piggy.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 400


def test_add_new_pet_with_invalid_data_age(name="Piggy",animal_type = "Piggy", pet_photo='image/piggy.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pet_with_invalid_data_photo(name="Piggy",animal_type = "Piggy",age="4"):
    """Проверяем что можно добавить питомца с некорректными данными"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_add_new_pet_with_invalid_data_key(name="Piggy",animal_type = "Piggy",age="4",  pet_photo='image/piggy.jpg'):
    """Проверяем что можно добавить питомца без авторизационного ключа """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

