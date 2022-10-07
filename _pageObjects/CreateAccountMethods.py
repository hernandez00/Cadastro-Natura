from _pageObjects._locators.Register import RegisterLocators
from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base


class CreateAccount(Base):
    # Preenche os campos da tela de cadastro e clica no botão 'Criar Conta'
    def register_filling(self, caseInfo):        
        # Campos de texto
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_FIRST_NAME, "Primeiro nome", "Leonardo")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_LAST_NAME, "Sobrenome", "Hernandez")

        """ Print """
        Base.printSteps(self._driver, caseInfo)
        
        # Campos de texto
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_EMAIL, "E-mail", "hernandeez00@gmail.com")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_PASSWORD, "Senha", "Teste!123")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_CONFIRM_PASSWORD, "Repetir senha", "Teste!123")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_CPF, "CPF", "51077841868")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_DATE_BIRTH, "Data de Nascimento (opcional)", "08031999")
        Base.find_textfield(self._driver, RegisterLocators.TEXT_FIELD_PHONE, "Celular", "18996299733")

        # Checkbox
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_NEWS_LETTER, "Novidades e promoções", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_NEWS_LETTER_SMS, "Novidades e promoções por SMS", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_INFO_PROVIDE, "Fornecer dados para consultoria da Natura", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_ACCEPTED_TERMS, "Aceitar termos e condições", 1)

        """ Print """
        Base.printSteps(self._driver, caseInfo)

        # RadioButtons
        Base.find_radiobutton(self._driver, RegisterLocators.RADIO_GENDER_MALE, "Gênero", "Masculino")

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
