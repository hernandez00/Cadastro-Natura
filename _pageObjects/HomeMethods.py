from _pageObjects._locators.Home import HomeLocators
from _pageObjects.BaseMethods import Base


class Home(Base):
    url_home = ["https://www.natura.com.br/",
                "https://www.natura.com.br/home-", "https://www.natura.com.br/home"]

    def open_login_register(self):
        click = Base.find_button(
            self._driver, HomeLocators.BUTTON_LOGIN_REGISTER)

        return True if click != False else click

    def is_home_screen(self):
        url = self._driver.current_url
        for home in self.url_home:
            if url == home:
                print(f"Página inicial acessada com sucesso! - {url}")
                return True
        print(f"Esta não é a página inicial! {url}")
        return False
