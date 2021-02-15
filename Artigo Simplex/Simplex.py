from scipy.optimize import linprog
import numpy as np
from constants import *
import csv

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    dados = []
    for row in reader:
        dados.append(list(str(row[0]).split(";")))
#print(dados)
#Custo por hora = sum(i = 1 até Ng) de (Ui(hora)*PDGi(hora)*BDGi(hora)) + sum(j = 1 até Ns) de (Uj(hora)*PDGj(hora)*BDGj(hora)) + Pg(hora)*Bg(hora) 
#Custo total = Soma dos custo por hora do dia
fun = []
for i in range(1,len(dados)): #Para cada hora do dia
    for j in range(GENERATOR_TYPES):
        fun.append(float(dados[i][j]))
    #for j in range(STORAGE_DEVICES):
    #    fun.append(dados[i+1][j+?])
    fun.append(float(dados[i][3]))

fun = np.array(fun)
print(fun)
input()
#FAZER AS RESTRIÇÕES AGORA
#where
#2x1 + 5x2 <= 10
#5x1 + 4x2 <= 25
#constraints = np.array([
#    [3,1,5],
#    [7,8,14],
#    [1,5,2],
#])
#independent = np.array([17,94,15])

#res = linprog(c=-fun, A_ub=constraints, b_ub=independent, bounds=(0,None), method='simplex')

#print(res.fun)
#assert res.fun == -136/5
#print(res.x)
#print(res.slack)
