from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base


class Login(Base):
    def user_login_filling(self, caseInfo):
        Base.find_textfield(self._driver, LoginLocators.TEXTFIELD_LOGIN, "Login", "email@gmail.com")
        Base.find_textfield(self._driver, LoginLocators.TEXTFIELD_PASSWORD, "Senha", "Teste!1234")

        """ Print """
        Base.printSteps(self._driver, caseInfo)

        Base.find_button(self._driver, LoginLocators.BUTTON_LOGIN)


    # Metodo para chamar a tela de registro
    def open_create_account_screen(self):
        Base.find_button(self._driver, LoginLocators.BUTTON_CREATE_ACCOUNT)

    # Metodo para validar se a tela atual é a tela de login
    def is_login_screen(self, caseInfo):
        is_login_screen = Base.find_text(self._driver, LoginLocators.TEXT_LOGIN_AS)
        
        if is_login_screen != False:
            """ Print """
            Base.printSteps(self._driver, caseInfo)
            return True
        else:
            return is_login_screen
    
    # Metodo para validar se o usuário está logado
    def is_logged_user(self, caseInfo):
        is_logged_user = Base.find_text(self._driver, LoginLocators.TEXT_USER_LOGGED)

        if is_logged_user != False:
            """ Print """
            Base.printSteps(self._driver, caseInfo)
            print("Usuário logado com sucesso!")
            return True
        else:
            print("O usuário não foi logado!")
            return is_logged_user
