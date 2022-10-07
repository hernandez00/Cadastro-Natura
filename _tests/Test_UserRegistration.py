# Executar teste: pytest ./_tests/ --html=./_tests/_report/teste1.html
from time import sleep
import unittest
import pytest
from _webDriver.Driver import Driver
from _pageObjects.BaseMethods import Base
from _pageObjects.OthersMethods import Others
from _pageObjects.HomeMethods import Home
from _pageObjects.LoginMethods import Login
from _pageObjects.CreateAccountMethods import CreateAccount


class TestNatura(unittest.TestCase, Base):
    def setUp(self):
        self.driver = Driver()
        self.others = Others(self.driver.instance)
        self.others.accept_cookies()
        self.others.close_survey()
        self.fullPath = Base(self.driver.instance).evidence_folder_creation(nameDir="Natura")

    def tearDown(self):
        self.driver.instance.quit()

    def test_cadastro_completo(self):
        # Cabeçalho com o titulo da pasta dos casos de testes
        # e um contador para numerar os prints.
        caseInfo = {
            "caseDir": f"{Base(self.driver.instance).fixture_folder_creation(self.fullPath, nameDir='test_cadastro_completo')}",
            "printCounter": 0
        }

        # Abrir a tela de login
        homeScreen = Home(self.driver.instance)
        assert homeScreen.is_home_screen(caseInfo)        
        homeScreen.open_login_or_register_screen()

        # Abrir a tela de cadastro através da tela de login
        loginScreen = Login(self.driver.instance)
        assert loginScreen.is_login_screen(caseInfo)
        loginScreen.open_create_account_screen()

        # Preencher os campos de cadastro
        registerScreen = CreateAccount(self.driver.instance)
        assert registerScreen.is_register_screen()
        registerScreen.register_filling(caseInfo)

        assert registerScreen.is_register_successful(caseInfo), "Erro"
    
    def test_login_bem_sucedido(self):
        caseInfo = {
            "caseDir": f"{Base(self.driver.instance).fixture_folder_creation(self.fullPath, nameDir='test_login_bem_sucedido')}",
            "printCounter": 0
        }

        # Abrir a tela de login
        homeScreen = Home(self.driver.instance)
        assert homeScreen.is_home_screen(caseInfo)        
        homeScreen.open_login_or_register_screen()

        # Validar se a tela atual é a tela de login
        loginScreen = Login(self.driver.instance)
        assert loginScreen.is_login_screen(caseInfo)
        
        # Preencher os campos de login
        loginScreen.user_login_filling(caseInfo)
        assert loginScreen.is_logged_user(caseInfo)
