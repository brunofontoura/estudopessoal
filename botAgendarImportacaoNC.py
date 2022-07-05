import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.farmaconde.com.br/admfarmaconde/admin/")
timeout = 5
driver.fullscreen_window()

try:
    title = driver.title
    assert("Administração do Magento | Farma Conde") in driver.title
    pass
except Exception as e:
        sys.exit("Erro ao carregar a página!")

try:
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "login").send_keys("")
    driver.find_element(By.ID, "login").send_keys(Keys.RETURN)
except Exception as e:
    sys.exit("Falha na inserção de credenciais no painel de admin")

#Magento sendo magento
time.sleep(7)

try:
    driver.find_element(By.ID, 'menu-magento-backend-system').click()
except Exception as e:
    sys.exit("Falha ao localizar a opção de 'Sistema' no menu lateral")

try:
    driver.find_element(By.LINK_TEXT, 'Agendar Importação/Exportação').click()
except Exception as e:
    sys.exit("Falha ao localizar a opção de 'Agendar Importação/Exportação'")

#Magento sendo magento
time.sleep(5)

try:
    executar = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div/div[2]/table/tbody/tr/td[9]/select")
    executar.click()
    selecionar_objeto = Select(executar)
    selecionar_objeto.select_by_visible_text('Executar')
    time.sleep(5)
    mensagem = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div"))).text
    if mensagem == "A operação ocorreu com sucesso.":
        print("Agendar Importação/Exportação executado com sucesso.")
        driver.close()
    else:
        print("Falha no processo de Importação/Exportação.")
        print(mensagem)
        driver.close()
except Exception as e:
    print("Falha na obtenção do Select/Execução")
    driver.close()