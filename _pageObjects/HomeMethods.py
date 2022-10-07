from _pageObjects._locators.Home import HomeLocators
from _pageObjects.BaseMethods import Base


class Home(Base):
    url_home = ["https://www.natura.com.br/",
                "https://www.natura.com.br/home-",
                "https://www.natura.com.br/home"]

    # Metodo para chamar a tela de login
    def open_login_or_register_screen(self):
        Base.find_button(self._driver, HomeLocators.BUTTON_LOGIN_REGISTER)

    # Metodo para validar se a tela atual é a tela inicial
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
