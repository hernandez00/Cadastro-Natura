from _pageObjects._locators.Home import HomeLocators
from _pageObjects.BaseMethods import Base


class Home(Base):
    url_home = ["https://www.natura.com.br/",
                "https://www.natura.com.br/home-",
                "https://www.natura.com.br/home"]

    def open_login_or_register(self):
        Base.find_button(self._driver, HomeLocators.BUTTON_LOGIN_REGISTER)

    def is_home_screen(self, caseInfo):
        url = self._driver.current_url
        for home in self.url_home:
            if url == home:
                print(f"Página inicial acessada com sucesso! - {url}")
                
                """ Print """
                Base.printSteps(self._driver, caseInfo)
                
                return True
        print(f"Esta não é a página inicial! {url}")
        return False
