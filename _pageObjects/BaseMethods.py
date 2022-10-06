from sqlite3 import Time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import Keys, ActionChains


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

    def find_textfield(self, element, fieldName, content):
        try:
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element)))

        except TimeoutException:
            print(f"Campo de texto não econtrado: {element}")
            return False
        print(f"Preencheu o campo: {fieldName} - Valor: {content}")
        return element_value.send_keys(content)

    def find_checkbox(self, element, content, action):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Checkbox não encontrado: {element}")
            return False

        # Action == 0 -> Desmarcar // Action == 1 -> Marcar
        if element_value.is_selected() and action == 1:
            print(f"Checkbox: {content} já estava selecionado!")
            return True
        elif not element_value.is_selected() and action == 0:
            print(f"O Checkbox {content} já estava desselecionado!")
            return True
        elif not element_value.is_selected() and action == 1:
            print(f"Selecionou o checkbox: {content}")
        else:
            print(f"Desselecionou o checkbox: {content}")

        ActionChains(self)\
            .scroll_to_element(element_value)\
            .move_to_element(element_value)\
            .pause(1)\
            .click()\
            .perform()

    def find_radiobutton(self, element, content, value):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Radiobutton não encontrado: {element}")
            return False

        # Action == 0 -> Desmarcar // Action == 1 -> Marcar
        if element_value.is_selected():
            print(f"O Radiobutton: {value} já estava selecionado!")
            return True
        elif not element_value.is_selected():
            print(f"Selecionou o Radiobutton: {content} - Valor: {value}")

        ActionChains(self)\
            .scroll_to_element(element_value)\
            .move_to_element(element_value)\
            .pause(1)\
            .click()\
            .perform()

    def find_text(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Texto não encontrado: {element}")
            return False
        return element_value.text

    def find_title(self, title):
        try:
            title = WebDriverWait(self, 5).until(EC.title_contains(
                title))

        except TimeoutException:
            print(f"Titulo incorreto: {title}")
            return title
        return title
