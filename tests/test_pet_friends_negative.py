from api import PetFriends
from settings import valid_email, valid_password, invalid_password
import os


pf = PetFriends()


def test_get_api_key_for_invalid_user(email='', password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_user(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_invalid_filter(filter='all pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0


def test_get_all_pets_with_invalid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, invalid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0


def test_add_new_pet_with_invalid_data(name='Леопольд', animal_type='дружный', age='4', pet_photo=''):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_data(name='Леопольд', animal_type='дружный', age='4', pet_photo='images\cat1.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

