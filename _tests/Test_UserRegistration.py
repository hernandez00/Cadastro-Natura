# Executar teste: pytest ./_tests/ --html=./_tests/_report/teste1.html
from time import sleep
import unittest
import pytest
from _webDriver.Driver import Driver
from _pageObjects.BaseMethods import Base
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.RegisterMethods import Register


class TestNatura(unittest.TestCase, Base):
    def setUp(self):
        self.driver = Driver()
        self.fullPath = Base(self.driver.instance).evidence_folder_creation(nameDir="Natura")

    def tearDown(self):
        self.driver.instance.quit()

    @pytest.mark.skip(reason="Acceso ao site.")
    def test_acessar_pagina_cadastro(self):
        caseInfo = {
            "caseDir": f"{Base(self.driver.instance).fixture_folder_creation(self.fullPath, nameDir='test_acessar_pagina_cadastro')}",
            "printCounter": 0
        }
        
        print("\n" + ("="*30)*2 + "\n")

        self.homeScreen = Home(self.driver.instance)
        assert self.homeScreen.is_home_screen(caseInfo)        
        self.homeScreen.open_login_or_register()

        loginScreen = Login(self.driver.instance)
        assert loginScreen.is_login_screen(caseInfo)
        loginScreen.open_create_account()

        print("\n" + ("="*30)*2 + "\n")

    def test_cadastro_completo(self):
        self.test_acessar_pagina_cadastro()

        caseInfo = {
            "caseDir": f"{Base(self.driver.instance).fixture_folder_creation(self.fullPath, nameDir='test_cadastro_completo')}",
            "printCounter": 0
        }

        registerScreen = Register(self.driver.instance)
        assert registerScreen.is_register_screen()
        registerScreen.register_filling(caseInfo)
