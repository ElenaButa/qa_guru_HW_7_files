import time
import os

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": '/path_to_project' + 'tmp',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

browser.config.driver_options = options

def test_file_exist():
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    file_full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp')
    size = os.path.getsize(file_full_path)
    assert size == 1

def test_size_file():
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    assert size == 1



