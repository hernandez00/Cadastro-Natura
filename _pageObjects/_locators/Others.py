from selenium.webdriver.common.by import By

class OthersLocators(object):
    COOKIE_ACCEPT = (
        By.XPATH, "//button[text() = 'Aceito todos os cookies']")
    
    SURVEY_CLOSE = (
        By.XPATH, "//div[@aria-label='Survey']/div/button")