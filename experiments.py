import json
from _webDriver.Driver import Driver
from _pageObjects._locators.Register import RegisterLocators
from _pageObjects.BaseMethods import Base
from _pageObjects.OthersMethods import Others
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.CreateAccountMethods import CreateAccount

driver = Driver()
others = Others(driver.instance)
others.accept_cookies()
others.close_survey()

fullPath = Base(driver.instance).evidence_folder_creation(nameDir="Natura")
caseInfo = {
    "caseDir": f"{Base(driver.instance).fixture_folder_creation(fullPath, nameDir='test_cadastro_completo')}",
    "printCounter": 0
}

HomeScreen = Home(driver.instance)
assert HomeScreen.is_home_screen(caseInfo)
HomeScreen.open_login_or_register_screen()

LoginScreen = Login(driver.instance)
assert LoginScreen.is_login_screen(caseInfo)
LoginScreen.open_create_account_screen()

RegisterScreen = CreateAccount(driver.instance)
assert RegisterScreen.is_register_screen()
#RegisterScreen.register_filling(caseInfo)


"""
texto = RegisterLocators.textfield_element(identificator="firstName", element_name="Cadastre-se")

radiob = RegisterLocators.radiobutton_element(identificator="gender", value="male")

checkb = RegisterLocators.checkbox_element(identificator="receiveNewsLetter")
"""

def file_reading(filedir):
    with open(filedir, 'r', encoding='utf-8') as file:
        jsonFile = json.loads(file.read())
    return jsonFile

jsonFile = file_reading(filedir="./_tests/cadastro.json")

for jsonKey, jsonValue in jsonFile.items():
    for key, value in jsonValue.items():
        if jsonKey == "textfield":
            textfield = RegisterLocators.textfield_element(key)
            Base.find_textfield(driver.instance, textfield, value['fieldName'], value['value'])
        elif jsonKey == "radiobutton":
            radiobutton = RegisterLocators.radiobutton_element(key, value['value'])
            Base.find_radiobutton(driver.instance, radiobutton, value['fieldName'])
        elif jsonKey == "checkbox":
            checkbox = RegisterLocators.checkbox_element(key)
            Base.find_checkbox(driver.instance, checkbox, value['fieldName'], value['action'])