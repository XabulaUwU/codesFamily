from sys import displayhook
from numpy.lib import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

#change the values to 0(one) or 1(another)

tabela = pd.read_csv("/media/xabelo/6EA83D23A83CEAEB/Programs/StrokeProbability/healthcare-dataset-stroke-data.csv")
tabela = tabela.drop('id', axis=1)
tabela = tabela.fillna(tabela.mean())
condition = [(tabela['age']<=14), (tabela['age']>=15) & (tabela['age']<=24), (tabela['age']>=25) & (tabela['age']<=64), (tabela['age']>=65)]
values = [0, 1, 2, 3]
# 0 = child, 1 = youth, 2 = adult, 3 = senior
tabela['Age_Class'] = np.select(condition, values)
tabela['smoking_status'] = tabela['smoking_status'].replace(['Unknown', 'never smoked', 'formerly smoked', 'smokes'], [0, 1, 2, 3])
# 0 = unknown, 1 = never, 2 = formerly smoked, 3 = smokes
tabela = tabela.drop(labels=[1609, 2187, 3307], axis=0)
tabela = tabela.drop(tabela.index[tabela['bmi'] > 50], inplace=False)
tabela.info()
#AI
x = tabela[['age', 'avg_glucose_level', 'bmi']]
y = tabela['stroke']
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.25)
logAI = LogisticRegression()
#AI train
logAI.fit(x_train, y_train)
logAI_pred = logAI.predict(x_test)
print(logAI_pred)
logAI_r2 = metrics.r2_score(y_test, logAI_pred)
matrix = metrics.confusion_matrix(y_test, logAI_pred, normalize='all')
sns.heatmap(matrix, annot=True)
plt.show()
# To get new patients data just create a new dataFrame with them and use in the LogisticRegression
