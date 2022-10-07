from selenium.webdriver.common.by import By


class LoginLocators(object):

    TEXTFIELD_LOGIN = (
        By.XPATH, "//input[@name='login']")

    TEXTFIELD_PASSWORD = (
        By.XPATH, "//input[@name='password']")

    BUTTON_LOGIN = (
        By.XPATH, "//button[span='Entrar']")

    BUTTON_CREATE_ACCOUNT = (
        By.XPATH, "//button[span='Criar conta']")    

    TEXT_LOGIN_AS = (
        By.XPATH, "//p[text()='Fazer login com:']")

    TEXT_USER_LOGGED = (
        By.XPATH, "//h6[contains(text(), 'Olá')]") 

    BODY = (
        By.XPATH, "//div[@id='root']")
