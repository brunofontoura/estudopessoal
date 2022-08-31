#Code snippets uteis de selenium
#Imports comentados estão duplicados mas são necessários

#Pega a data de agora e transforma em uma string, em seguida tira um print e salva com o nome da data em formato PNG
esc = 0
my_date = date.today()
my_date = my_date.strftime("%d%m%Y")
captura = "Sucesso_Teste_Produto_" + str(esc) + '_' + my_date + '.png'
driver.save_screenshot(captura)
#Dependencias
import sys
import time
from datetime import date, datetime
#from lib2to3.pgen2 import driver

#Verificação de elemento ativado e mini-função de verificação
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "postcode")))
Enable = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "postcode"))).is_enabled()
if Enable == FALSE:
    time.sleep(5)
else:
    pass
#Dependencias
from pickle import FALSE, TRUE
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

#Instalação e configuração remota de Firefox + Geckodriver por script
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))