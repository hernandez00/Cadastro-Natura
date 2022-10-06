from distutils.log import Log
from _webDriver.Driver import Driver
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login

driver = Driver()

HomeScreen = Home(driver.instance)
assert HomeScreen.is_home_screen()
HomeScreen.open_login_register()

LoginScreen = Login(driver.instance)
assert LoginScreen.is_login_screen()
LoginScreen.open_create_account()

driver.instance.quit()
