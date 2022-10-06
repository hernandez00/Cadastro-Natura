from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base


class Login(Base):

    def open_create_account(self):
        click = Base.find_button(
            self._driver, LoginLocators.BUTTON_CREATE_ACCOUNT)

        return True if click != False else click

    def is_login_screen(self):
        is_login_screen = Base.find_text(
            self._driver, LoginLocators.TEXT_LOGIN_AS)
        
        return True if is_login_screen == "Fazer login com:" else is_login_screen
