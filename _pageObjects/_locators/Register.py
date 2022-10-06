from selenium.webdriver.common.by import By


class RegisterLocators(object):

    TEXTFIELD_FIRST_NAME = (
        By.XPATH, "//input[@name='firstName']")
    TEXTFIELD_LAST_NAME = (
        By.XPATH, "//input[@name='lastName']")
    TEXTFIELD_EMAIL = (
        By.XPATH, "//input[@name='email']")
    TEXTFIELD_PASSWORD = (
        By.XPATH, "//input[@name='password']")
    TEXTFIELD_CONFIRM_PASSWORD = (
        By.XPATH, "//input[@name='confirmPassword']")
    TEXTFIELD_CPF = (
        By.XPATH, "//input[@name='confirmPassword']")
    TEXTFIELD_DATE_BIRTH = (
        By.XPATH, "//input[@name='dateOfBirth']")
    TEXT_FIELD_PHONE = (
        By.XPATH, "//input[@name='homePhone']")

    RADIO_GENDER_FEMALE = (
        By.XPATH, "//input[@type='radio' and @value='female']")
    RADIO_GENDER_MALE = (
        By.XPATH, "//input[@type='radio' and @value='male']")
    RADIO_GENDER_NOSPECIFY = (
        By.XPATH, "//input[@type='radio' and @value='noSpecify']")

    CHECK_NEWS_LETTER = (
        By.XPATH, "//input[@type='checkbox' and @name='receiveNewsLetter']")
    CHECK_NEWS_LETTER_SMS = (
        By.XPATH, "//input[@type='checkbox' and @name='receiveNewsLetterSms']")
    CHECK_INFO_PROVIDE = (
        By.XPATH, "//input[@type='checkbox' and @name='infContOptIn']")
    CHECK_ACCEPTED_TERMS = (
        By.XPATH, "//input[@type='checkbox' and @name='acceptedterms']")

    BUTTON_FINISH_ACCOUNT_CREATION = (
        By.XPATH, "//button[span = 'Criar Conta']")
