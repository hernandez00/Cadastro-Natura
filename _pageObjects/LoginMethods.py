from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base


class Login(Base):

    def open_create_account(self):
        Base.find_button(self._driver, LoginLocators.BUTTON_CREATE_ACCOUNT)

    def is_login_screen(self, caseInfo):
        is_login_screen = Base.find_text(self._driver, LoginLocators.TEXT_LOGIN_AS)
        
        """ Print """
        Base.printSteps(self._driver, caseInfo)
        
        return True if is_login_screen == "Fazer login com:" else is_login_screen
