from time import sleep
from _webDriver.Driver import Driver
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
RegisterScreen.register_filling(caseInfo)

RegisterScreen.is_register_successful(caseInfo)

sleep(3)
driver.instance.quit()