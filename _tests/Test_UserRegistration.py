import unittest
import pytest
from _webDriver.Driver import Driver
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login


class Test_UserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_registration(self):
        HomeScreen = Home(self.driver.instance)
        assert HomeScreen.is_home_screen()
        HomeScreen.open_login_register()

        LoginScreen = Login(self.driver.instance)
        assert LoginScreen.is_login_screen()
        LoginScreen.open_create_account()
