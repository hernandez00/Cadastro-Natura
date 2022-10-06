"""
Texto <p> indicando as formas de login: //p[text() = 'Fazer login com:']

Botão para criar conta: //button[span = 'Criar conta']
"""
from selenium.webdriver.common.by import By


class LoginLocators(object):

    TEXT_LOGIN_AS = (
        By.XPATH, "//p[text() = 'Fazer login com:']")

    BUTTON_CREATE_ACCOUNT = (
        By.XPATH, "//button[span = 'Criar conta']")
