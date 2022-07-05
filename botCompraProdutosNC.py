from pickle import FALSE, TRUE
from socket import timeout
import sys
from tracemalloc import stop
from turtle import title
from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date, datetime

v = 0

def escolha_produto(esc):
    global v
    global driver
    if esc == 1:
        print("Opção 1 - Acetilcisteina")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/acetilcisteina-100mg-16-envelopes-com-5-gramas-eurofarma")
        timeout = 5
        try:
            title = driver.title
            assert("Acetilcisteina 100Mg Cx 16 Saches X 5G | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 2:
        print("Opção 2 - Captopril")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/captopril-geolab-25mg-30-s")
        timeout = 5
        try:
            title = driver.title
            assert("Captopril 25Mg Cx 30 Comp | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 3:
        print("Opção 3 - Mascara")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/mascara-descartavel-concare-com-7-unidades")
        timeout = 5
        try:
            title = driver.title
            assert("Máscara Concare de TNT | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 4:
        print("Opção 4 - Melatonina")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/melatonina-mcg-90-caps")
        timeout = 5
        try:
            title = driver.title
            assert("MELATONINA MCG 90 CAPS | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 5:
        print("Opção 5 - Protetor Solar 150Ml")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/summer-vita-fps30-spray-150ml")
        timeout = 5
        try:
            title = driver.title
            assert("Protetor Solar Summer Vita Fps30 Aerosol 150Ml | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 6:
        print("Opção 6 -  Prot. Sol. 30 200Ml")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/summer-vita-fps30-loc-200ml")
        timeout = 5
        try:
            title = driver.title
            assert("Protetor Solar Summer Vita Fps30 Locao 200Ml | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 7:
        print("Opção 7 -  Prot. Sol. FPS50 200Ml")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/summer-vita-fps50-loc-200ml")
        timeout = 5
        try:
            title = driver.title
            assert("Protetor Solar Summer Vita Fps50 Locao 200Ml | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 8:
        print("Opção 8 -  Prot. Sol. Sundown")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/protetor-solar-sundown-pele-molhada-spray-fps30-200ml")
        timeout = 5
        try:
            title = driver.title
            assert("Protetor Solar Sundown Pele Molhada Fps 30 Spray Com 200Ml | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 9:
        print("Opção 9 -  Prot. Sol. Praia e Piscina")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/protetor-solar-sundown-praia-e-piscina-fps30")
        timeout = 5
        try:
            title = driver.title
            assert("Protetor Solar Sundown Praia E Piscina Fps30 120Ml | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 10:
        print("Opção 10 -  Protovit (Não encontrado no Site!")
        sys.exit("Erro ao carregar a página!")
    elif esc == 11:
        print("Opção 11 -  Repelent On")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/repelent-on-100ml-spray")
        timeout = 5
        try:
            title = driver.title
            assert("MELATONINA MCG 90 CAPS | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    elif esc == 12:
        print("Opção 12 -  Vitacon Phytus")
        driver = webdriver.Firefox()
        driver.get("https://www.farmaconde.com.br/vitacon-phytus")
        timeout = 5
        try:
            title = driver.title
            assert("Vitacon Phytus 60S Conlife | Farma Conde") in driver.title
            pass
        except Exception as e:
            sys.exit("Erro ao carregar a página!")
    #elif esc == 99:
    #    print("Opção 99 - Todos os produtos (Experimental) ")

        #for x in range(1, 13):
        #    escolha_produto(x)
        #    pass
    else:
        print("Opção inválida.")

print("Produto Numero 1: - Acetilcisteina\nProduto Numero 2 - Captopril\nProduto Numero 3 - Mascara\nProduto Numero 4 - Melatonina")
print("Produto Numero 5: - Protetor Solar 150Ml\nProduto Numero 6 - Prot. Sol. FPS30 200Ml\nProduto Numero 7 - Prot. Sol. FPS50 200Ml\nProduto Numero 8 - Prot. Sol. Sundown")
print("Produto Numero 9: - Prot. Sol. Praia e Piscina \nProduto Numero 10 - Protovit\nProduto Numero 11 - Repelent\nProduto Numero 12 - Vitacon Phytus")

#print("99 - Todos os produtos (Experimental)")

esc = int(input("Selecione o produto por número: "))
falha = 0
i = 0
v = int(input("Selecione o numero de vezes: "))
if esc == 0: sys.exit("Saindo do programa.")

while i <= int(v):
    if v == 0: sys.exit("Saindo do programa.")
    escolha_produto(esc)
    
    driver.find_element(By.ID, "product-addtocart-button").click()
    
    time.sleep(7)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "minicart-wrapper"))).click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "top-cart-btn-checkout"))).click()

    driver.find_element(By.ID, "customer-email").send_keys("")
    driver.find_element(By.ID, "pass").send_keys("")
    driver.find_element(By.NAME, "send").send_keys(Keys.RETURN)

    #Captcha
    #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"))).click()
    #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "postcode")))
    Enable = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "postcode"))).is_enabled()
    if Enable == FALSE:
         time.sleep(5)
    else:
        pass

    driver.find_element(By.NAME, "postcode").send_keys("12242260")
    driver.find_element(By.NAME, "street[0]").send_keys("Av Salmão")
    driver.find_element(By.NAME, "street[1]").send_keys("325")
    driver.find_element(By.NAME, "street[3]").send_keys("Aquarius")
    driver.find_element(By.NAME, "city").send_keys("São José dos Campos")
    driver.find_element(By.CLASS_NAME, "select").send_keys("S", "S")
    driver.find_element(By.NAME, "telephone").send_keys("12935009608")
    
    #Método de envio
    Enable = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, 
        "//div[4]/main/div[2]/div/div[3]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input"))).is_enabled()
    if Enable == FALSE: break
    #Seleciona
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
    "//div[4]/main/div[2]/div/div[3]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input")))
    driver.find_element(By.XPATH, 
    "//div[4]/main/div[2]/div/div[3]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input").click()
    #Proximo
    driver.find_element(By.XPATH, "//div[4]/main/div[2]/div/div[3]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button").click()

    try:
        time.sleep(3)
        Enable = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "mercadopago_custom_pix"))).is_enabled()
        if Enable == FALSE: break
        else:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "mercadopago_custom_pix")))
            driver.find_element(By.ID, "mercadopago_custom_pix").click()
            print("Sucesso. Método de pagamento 'Pix' válido.")
            #pega data de agora e cria string
            my_date = date.today()
            my_date = my_date.strftime("%d%m%Y")
            captura = "Sucesso_Teste_Produto_" + str(esc) + '_' + my_date + '.png'
            #Verificar a pasta onde será salvo o print
            driver.save_screenshot(captura)
            #driver.get_screenshot_as_file("nome_do_arquivo.formato")
            i = i+1
            driver.quit()
    except Exception as e:
        falha =+ 1
        print("Falha na busca por meio de pagamento.")
        time.sleep(3)
        break
    print("Teste efetuado por ", i, " vez(es) de", v ,"vez(es) solicitado(s). Houve um total de", falha, "falha(s).")
    if i == int(v):
        print("Fim de teste.")
        break