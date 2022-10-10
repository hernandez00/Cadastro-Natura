import os
import json
from datetime import date
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class Base(object):
    def __init__(self, driver):
        self._driver = driver

    # Metodo para identificar e clicar em um botão
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

    # Metodo para clicar em um botão sem apresentar mensagens
    def silence_find_button(self, element):
        try:
            element_value = WebDriverWait(self, 5).until(EC.visibility_of_element_located((
                element)))

            element_value = WebDriverWait(self, 5).until(EC.element_to_be_clickable((
                element)))

        except TimeoutException:
            return False
        return element_value.click()

    # Metodo para identificar e preencher um campo de texto
    def find_textfield(self, element, fieldName, content):
        try:
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element)))

        except TimeoutException:
            print(f"Campo de texto não econtrado: {element}")
            return False
        print(f"Preencheu o campo: {fieldName} - Valor: {content}")
        return element_value.send_keys(content)

    # Metodo para identificar e Selecionar/Desselecionar um CheckBox
    def find_checkbox(self, element, fieldName, action):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Checkbox não encontrado: {element}")
            return False

        # Action == 0 -> Desselecionar
        # Action == 1 -> Selecionar
        if element_value.is_selected() and action == 1:
            print(f"Checkbox: {fieldName} já estava selecionado!")
            return True
        elif not element_value.is_selected() and action == 0:
            print(f"O Checkbox {fieldName} já estava desselecionado!")
            return True
        elif not element_value.is_selected() and action == 1:
            print(f"Selecionou o checkbox: {fieldName}")
        else:
            print(f"Desselecionou o checkbox: {fieldName}")

        ActionChains(self)\
            .scroll_to_element(element_value)\
            .move_to_element(element_value)\
            .click()\
            .perform()

    # Metodo para identificar e Selecionar um RadioButton
    def find_radiobutton(self, element, fieldName):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Radiobutton não encontrado: {element}")
            return False

        if element_value.is_selected():
            print(f"O Radiobutton: {fieldName} já estava selecionado!")
            return True
        elif not element_value.is_selected():
            print(f"Selecionou o Radiobutton: {fieldName}")

        ActionChains(self)\
            .scroll_to_element(element_value)\
            .move_to_element(element_value)\
            .click()\
            .perform()

    # Metodo para identificar um campo e retornar seu texto
    def find_text(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element)))

        except TimeoutException:
            print(f"Texto não encontrado: {element}")
            return False
        return element_value.text

    # Metodo para verificar se o titulo da pagina contém alguma palavra ou frase
    def find_title(self, title):
        try:
            title = WebDriverWait(self, 5).until(EC.title_contains(
                title))

        except TimeoutException:
            print(f"Titulo incorreto: {title}")
            return title
        return title

    # Metodo para ler um arquivo json
    def file_reading(fileDir):
        with open(fileDir, 'r', encoding='utf-8') as file:
            jsonFile = json.loads(file.read())
        return jsonFile

    # Metodo para criar uma pasta
    def dirCreator(self, fullPath, nameDir):
        try:
            os.makedirs(fullPath)
            print("\n" + ("="*30)*2 + "\n")
            print(f"Diretório {nameDir} criado com sucesso!")
            print("\n" + ("="*30)*2 + "\n")
        except OSError:
            return fullPath
        return fullPath

    # Metodo que especifica a pasta raiz onde serão armazenadas
    # as pastas de cenários de teste.
    def evidence_folder_creation(self, nameDir):
        nameDir = f"{nameDir}_{date.today()}"
        rootDir = "./_tests/_report/"
        fullPath = os.path.join(rootDir, nameDir)

        return self.dirCreator(fullPath, nameDir)

    # Metodo que especifica a pasta que será criada para o cenário
    # de teste.
    def fixture_folder_creation(self, fullPath, nameDir):
        caseDir = os.path.join(fullPath, nameDir)

        return self.dirCreator(caseDir, nameDir)

    # Metodo que realiza as capturas de tela
    def printSteps(self, caseInfo):
        caseDir = f"{caseInfo['caseDir']}/{caseInfo['printCounter']}.png"
        caseInfo['printCounter'] += 1

        WebDriverWait(self, 5).until(EC.presence_of_element_located((
            ('xpath', "//div[@id='root']")))).screenshot(caseDir)
