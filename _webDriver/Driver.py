from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CDM


class Driver:
    def __init__(self):
        self.instance = webdriver.Chrome(
            service=Service(CDM().install()))
        
        self.instance.set_window_size(1600, 900)
        self.instance.get("https://www.natura.com.br/")
        