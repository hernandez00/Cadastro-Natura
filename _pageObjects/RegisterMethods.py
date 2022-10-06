from _pageObjects._locators.Register import RegisterLocators
from _pageObjects.BaseMethods import Base


class Register(Base):
    def register_filling(self):
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_FIRST_NAME, "Primeiro nome", "Leonardo")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_LAST_NAME, "Sobrenome", "Hernandez")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_EMAIL, "E-mail", "lhzoldin@gmail.com")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_PASSWORD, "Senha", "teste123")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_CONFIRM_PASSWORD, "Repetir senha", "teste123")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_CPF, "CPF", "51077841868")
        Base.find_textfield(self._driver, RegisterLocators.TEXTFIELD_DATE_BIRTH, "Data de Nascimento (opcional)", "08031999")
        Base.find_textfield(self._driver, RegisterLocators.TEXT_FIELD_PHONE, "Celular", "18996299733")

        Base.find_checkbox(self._driver, RegisterLocators.CHECK_NEWS_LETTER, "Novidades e promoções", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_NEWS_LETTER_SMS, "Novidades e promoções por SMS", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_INFO_PROVIDE, "Fornecer dados para consultoria da Natura", 1)
        Base.find_checkbox(self._driver, RegisterLocators.CHECK_ACCEPTED_TERMS, "Aceitar termos e condições", 1)

        Base.find_radiobutton(self._driver, RegisterLocators.RADIO_GENDER_MALE, "Gênero", "Masculino")

    
    def is_register_screen(self):
        is_register_screen = Base.find_title(
            self._driver, "Cadastre-se")

        print(f"Página de Registro acessada com sucesso!" if is_register_screen else "Esta não é a página de registro!")
        return is_register_screen