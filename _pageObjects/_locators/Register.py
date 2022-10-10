from selenium.webdriver.common.by import By


class RegisterLocators(object):
    def textfield_element(identificator) -> tuple:
        return (By.XPATH, f"//input[@name='{identificator}']")

    def radiobutton_element(identificator, value) -> tuple:
        return (By.XPATH, f"//input[@type='radio' and @name='{identificator}' and @value='{value}']")

    def checkbox_element(identificator) -> tuple:
        return (By.XPATH, f"//input[@type='checkbox' and @name='{identificator}']")

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
        By.XPATH, "//input[@name='cpf']")
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
    
    """ Erro de campo obrigatório não preenchido (Para qualquer campo de texto, exceto CPF)"""
    #REQUIRED_TEXTFIELD_WARN = (
    #    By.XPATH, f"//input[@name='{Self}']/ancestor::div/div[span='Este campo é obrigatório']")

    """ Erro de e-mail ivalido (Apenas para e-mail)"""
    #INVALID_EMAIL_WARN = (
    #    By.XPATH, f"//input[@name='{Self}']/ancestor::div/div[span='E-mail inválido']")

    """ Erro de senha não atender aos requisitos (Apenas para senha)"""
    #OUT_OF_RULLS_PW = (
    #    By.XPATH, f"//input[@name='password']/ancestor::div/div[span='A senha deve seguir as regras abaixo.']")

    """ Erro de confirmação de senha divergente da senha (Apenas para confirmação de senha)"""
    #CONFIRMATION_PW_WRONG = (
    #    By.XPATH, f"//input[@name='confirmPassword']/ancestor::div/div[span='As senhas não coincidem']")

    """ Erro utilizado para CPF inválido e não preenchido"""
    #INVALID_CPF_WARN = (
    #    By.XPATH, "//input[@name='cpf']/ancestor::div/div[span='CPF inválido']")

    """ Erro de data inválida (Este campo é opcional)"""
    #INVALID_DATE_WARN = (
    #    By.XPATH, "//input[@name='dateOfBirth']/ancestor::div/div[span='Data inválida']")

    """ Erro de data incompleta (Aparece caso a data esteja acima de 100 anos a partir do ano atual)"""
    #INCOMPLETE_DATE_WARN = (
    #    By.XPATH, "//input[@name='dateOfBirth']/ancestor::div/div[span='Informe uma data válida']")

    """ Erro de telefone inválido ou incompleto"""
    #INVALID_PHONE_WARN = (
    #    By.XPATH, "//input[@name='homePhone']/ancestor::div/div[span='Telefone inválido']")

    """ Erro de checkbox obrigatório não selecionado (Apenas para os termos)"""
    #REQUIRED_TERMS_ACCEPT = (
    #   By.XPATH, "//input[@name='acceptedterms']/ancestor::div/div[span='É necessário aderir aos termos de uso']")