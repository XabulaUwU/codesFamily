from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import displayhook

cor = webdriver.Chrome()
cor.get("https://www.google.com/")
cor.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação do dolar")
cor.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotdol = cor.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotdol)
cor.get("https://www.google.com/")
cor.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação do euro")
cor.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
coteur = cor.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(coteur)
cor.get("https://www.melhorcambio.com/")
abaor = cor.window_handles[0]
cor.find_element_by_xpath('//*[@id="commodity-hoje"]/tbody/tr[2]/td[2]/a/img').click()
abanew = cor.window_handles[1]
cor.switch_to_window(abanew)
cotour = cor.find_element_by_id('comercial').get_attribute('value')
cotour = cotour.replace(',', '.')
print(cotour)
import pandas as pd
produtos = pd.read_excel('/media/xabelo/6EA83D23A83CEAEB/Programs/Aula4/Produtos.xlsx')
produtos.loc[produtos['Moeda'] == 'Dólar', 'Cotação'] = float(cotdol)
produtos.loc[produtos['Moeda'] == 'Euro', 'Cotação'] = float(coteur)
produtos.loc[produtos['Moeda'] == 'Ouro', 'Cotação'] = float(cotour)
produtos['Preço Base Reais'] = produtos['Preço Base Original'] * produtos['Cotação']
produtos['Preço Final'] = produtos['Preço Base Reais'] * produtos['Margem']
produtos.to_excel("/media/xabelo/6EA83D23A83CEAEB/Programs/Aula4/ProdutosAtualizados.xlsx", index=False)
