import math
from re import T
from sys import displayhook
from typing import TypeVar
from numpy import random
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("Aula3/advertising.csv")
x = tabela.drop('Vendas', axis=1)
y = tabela['Vendas']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3 ,random_state=1)
AI_lir = LinearRegression()
AI_randFor = RandomForestRegressor()
AI_lir.fit(x_train, y_train)
AI_randFor.fit(x_train, y_train)
pred_lir = AI_lir.predict(x_test)
pred_randFor = AI_randFor.predict(x_test)
lin_r2 = metrics.r2_score(y_test, pred_lir)
randFor_r2 = metrics.r2_score(y_test, pred_randFor)
print(lin_r2)
print(randFor_r2)
print(math.sqrt(metrics.mean_squared_error(y_test, pred_randFor)))
print(math.sqrt(metrics.mean_squared_error(y_test, pred_lir)))
tabela_previsao = pd.DataFrame()
tabela_previsao['Valor Real'] = y_test
tabela_previsao['Previsão AI Linear'] = pred_lir
tabela_previsao['Previsão AI RandFor'] = pred_randFor
tabela_previsao = tabela_previsao.reset_index(drop=True)
sns.heatmap(tabela.corr(), cmap='mako', annot=True)
plt.show()
sns.lineplot(data=tabela_previsao)
plt.show()
