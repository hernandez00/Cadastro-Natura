from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Base(object):
    def __init__(self, driver):
        self._driver = driver

    def find_button(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element)))

            element_value = WebDriverWait(self, 15).until(EC.element_to_be_clickable((
                element)))
        except TimeoutException:
            print(f"Botão não encontrado: {element}")
            return False
        print(f"Clicou em: {element_value.text}")
        return element_value.click()

    def find_textfield(self, element, content):
        try:
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element)))

        except TimeoutException:
            print(f"Campo de texto não econtrado: {element}")
            return False
        print(f"Preencheu o campo: {element_value.text} - Valor: {content}")
        return element_value

    def find_text(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))
        except TimeoutException:
            print(f"Texto não encontrado: {element}")
            return False
        return element_value.text
