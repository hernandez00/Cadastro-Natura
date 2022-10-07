from _pageObjects._locators.Others import OthersLocators
from _pageObjects.BaseMethods import Base


class Others(Base):
    # Metodo para aceitar os cookies
    def accept_cookies(self):
        is_accepted = Base.silence_find_button(self._driver, OthersLocators.COOKIE_ACCEPT)
        
        print("Cookies aceitos!" if is_accepted != False else "Cookies não foram aceitos!")
    
    # Metodo para fechar janela de pesquisa (Questionários)
    def close_survey(self):
        is_closed = Base.silence_find_button(self._driver, OthersLocators.SURVEY_CLOSE)

        print("A janela de pesquisa foi fechada!" if is_closed != False else "A janela de pesquisa já estava fechada!")
