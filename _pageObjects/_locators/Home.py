from selenium.webdriver.common.by import By


class HomeLocators(object):

    BUTTON_LOGIN_REGISTER = (
        By.XPATH, "//div[span = 'Entre ou cadastre-se']")
