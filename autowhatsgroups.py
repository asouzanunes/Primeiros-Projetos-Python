from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # abre o navegador
driver.get("https://web.whatsapp.com/")

input("Escaneie o QR Code e pressione ENTER...")

# Procurar grupo pelo nome
grupo = "GRUPO-1, GRUPO-2, GRUPO-3"
mensagem = "Olá pessoal, essa é uma mensagem automática e apenas um teste!"

# Buscar caixa de pesquisa e digitar o nome do grupo
caixa_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
caixa_pesquisa.click()
caixa_pesquisa.send_keys(grupo)
time.sleep(2)
caixa_pesquisa.send_keys(Keys.ENTER)

# Digitar a mensagem
caixa_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
caixa_mensagem.click()
caixa_mensagem.send_keys(mensagem)
caixa_mensagem.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
