# Executar teste: pytest ./_tests/ --html=./_tests/_report/teste1.html

import unittest
import pytest
from _webDriver.Driver import Driver
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.RegisterMethods import Register


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

        RegisterScreen = Register(self.driver.instance)
        assert RegisterScreen.is_register_screen()
        RegisterScreen.register_filling()