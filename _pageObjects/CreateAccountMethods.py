from _pageObjects._locators.Register import RegisterLocators
from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base


class CreateAccount(Base):

    # Preenche os campos da tela de cadastro e clica no botão 'Criar Conta'
    def register_filling(self, caseInfo, fileDir):       
        jsonFile = Base.file_reading(fileDir=fileDir)

        for jsonKey, jsonValue in jsonFile.items():
            """ Print """
            Base.printSteps(self._driver, caseInfo)
            for key, value in jsonValue.items():
                if jsonKey == "textfield":
                    textfield = RegisterLocators.textfield_element(key)
                    Base.find_textfield(self._driver, textfield, value['fieldName'], value['value'])
                elif jsonKey == "radiobutton":
                    radiobutton = RegisterLocators.radiobutton_element(key, value['value'])
                    Base.find_radiobutton(self._driver, radiobutton, value['fieldName'])
                elif jsonKey == "checkbox":
                    checkbox = RegisterLocators.checkbox_element(key)
                    Base.find_checkbox(self._driver, checkbox, value['fieldName'], value['action'])

        # Clica no botão 'Criar Conta' para finalizar o cadastro
        Base.find_button(self._driver, RegisterLocators.BUTTON_FINISH_ACCOUNT_CREATION)

        """ Print """
        Base.printSteps(self._driver, caseInfo)

    # Metodo para verificar se a tela atual é a tela de cadastro
    def is_register_screen(self):
        is_register_screen = Base.find_title(self._driver, "Cadastre-se")

        print(f"Página de Registro acessada com sucesso!" if is_register_screen else "Esta não é a página de registro!")
 
        return is_register_screen
    
    # Metodo para verificar se o cadastro foi bem sucedido. Se sim, o
    # usuário é direcinado automaticamente para a tela inicial e logado.
    def is_register_successful(self, caseInfo):
        is_register_successful = Base.find_text(self._driver, LoginLocators.TEXT_USER_LOGGED)

        if is_register_successful != False:
            """ Print """
            Base.printSteps(self._driver, caseInfo)
            print("Conta criada com sucesso!")
            return True
        else:
            print("A conta não foi criada!")
            return is_register_successful