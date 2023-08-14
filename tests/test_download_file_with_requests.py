import os.path
import requests
import pytest


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь


def test_size_file():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    response = requests.get(url)
    file_full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp', 'selenium_logo.png')
    with open(file_full_path, 'wb') as file:
        file.write(response.content)

    assert os.path.isfile(file_full_path) is True
    assert os.path.getsize(file_full_path) == 30803


