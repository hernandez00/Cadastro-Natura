from time import sleep
from _webDriver.Driver import Driver
from _pageObjects.BaseMethods import Base
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.RegisterMethods import Register

driver = Driver()


def teste():
    fullPath = Base(driver.instance).evidence_folder_creation(nameDir="Natura")
    caseInfo = {
        "caseDir": f"{Base(driver.instance).fixture_folder_creation(fullPath, nameDir=teste.__name__)}",
        "printCounter": 0
    }

    HomeScreen = Home(driver.instance)
    assert HomeScreen.is_home_screen()
    HomeScreen.open_login_or_register(caseInfo)

    LoginScreen = Login(driver.instance)
    assert LoginScreen.is_login_screen(caseInfo)
    LoginScreen.open_create_account()

    RegisterScreen = Register(driver.instance)
    assert RegisterScreen.is_register_screen(caseInfo)
    RegisterScreen.register_filling()

    sleep(3)
    driver.instance.quit()


teste()
