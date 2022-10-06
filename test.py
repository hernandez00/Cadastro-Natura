from time import sleep
from _webDriver.Driver import Driver
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.RegisterMethods import Register

driver = Driver()

HomeScreen = Home(driver.instance)
assert HomeScreen.is_home_screen()
HomeScreen.open_login_register()

LoginScreen = Login(driver.instance)
assert LoginScreen.is_login_screen()
LoginScreen.open_create_account()

RegisterScreen = Register(driver.instance)
assert RegisterScreen.is_register_screen()
RegisterScreen.register_filling()

sleep(3)
driver.instance.quit()