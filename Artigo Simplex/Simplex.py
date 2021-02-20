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

#print(fun)
#print(fun[2])
restricoesIgualdade = [] #Restrições de igualdade energetica
for i in range(24): #Para cada hora do dia
    rest = [0 for i in range(len(fun))] #Tabela inicial base
    for j in range(GENERATOR_TYPES+1):
        rest[i*4+j] = 1
    restricoesIgualdade.append(rest)

independent = []
for i in range(1,len(dados)):
    independent.append(dados[i][6])
#print(independent)
bounds = []
for i in range(1,len(dados)):
    for j in range(GENERATOR_TYPES+1):
        bound = None
        if j < 2:
            bound = (0,float(dados[i][4+j]))
        if j is 2:
            bound = (6,30)
        elif j is 3:
            bound = (0,95)
        bounds.append(bound)
bounds = tuple(bounds)
#print(bounds)
#print(independent)
fun = np.array(fun)
restricoesIgualdade = np.array(restricoesIgualdade)
independent = np.array(independent)

res = linprog(c = fun, A_eq=restricoesIgualdade, b_eq=independent,bounds=bounds,method='simplex')
#print(list(res.x))
print(res.fun)
org = []
for i in range(0,len(list(res.x))+1, 4):
    org.append(list(res.x)[i:i+4])
for hora in org:
    print(hora)
input()

