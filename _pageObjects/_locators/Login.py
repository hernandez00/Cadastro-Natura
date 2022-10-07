from selenium.webdriver.common.by import By


class LoginLocators(object):

    TEXT_LOGIN_AS = (
        By.XPATH, "//p[text() = 'Fazer login com:']")

    BUTTON_CREATE_ACCOUNT = (
        By.XPATH, "//button[span = 'Criar conta']")

    BODY = (
        By.XPATH, "//div[@id='root']")
