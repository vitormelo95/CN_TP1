import csv
from statistic import Statistic
from copy import copy
from node import Node
from evo import Evo
from math import log,sqrt,pow
import random
from operator import mul,add,sub,truediv

def readCSVFile(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

data =  readCSVFile('datasets/house-train.csv')
#print(data)

def calculate_fitness(self):
    fitness_list = []
    self.stat_list = []
    for ind in self.population:
        ind.function_string = ("lambda " + X + " :"+ ind.generate_string())
        ind.function = eval(ind.function_string)
        sum = 0
        for row in self.train_data:
            y = 0
            try:
                y = eval("ind.function(" + ( ','.join(row[0:row.__len__()-1]) ) +")")
                sum += pow(y - float(row[row.__len__()-1]),2)
            except Exception as e:
                sum += 500000
                #print(e.message + "-" + ','.join(e.args))
            
        sum = sum/self.train_data.__len__()
        sum = sqrt(sum)
        ind.fitness = sum
        fitness_list.append(sum)
        #print(ind.fitness)
    if self.stat_list.__len__() > 0:
        self.stat_list.append(Statistic(fitness_list,self.stat_list[self.stat_list.__len__()-1].med()))
    else: 
        self.stat_list.append(Statistic(fitness_list,None))

X = "x1,x2,x3,x4,x5,x6,x7,x8"
operators =  [Node("add",0,2), Node("sub",0,2), Node("mul",0,2)]#,Node("pow",0,2), Node("log",0,1)]
terminals = [Node("x1",1,0),Node("x2",1,0), Node("x3",1,0), Node("x4",1,0), Node("x5",1,0), Node("x6",1,0),Node("x7",1,0),Node("x8",1,0)
    ,Node("(random.random()*9)",1,0)]#,Node("0.5",1,0),Node("1",1,0),Node("2",1,0),Node("3",1,0),Node("5",1,0),Node("7",1,0)]
train =  Evo(100, 2, 7, 0.8, 0.25, operators, terminals, data, calculate_fitness,True,50)
train.execute()
first = True
for l in train.stat_list:
    if first:
        print(l.best()+","+l.worse()+","+l.med()+","+l.n_rep())
    else:
    print(l.best()+","+l.worse()+","+l.med()+","+l.n_rep()+","+l.above()+","+l.below())


#for ind in train.population:
#    ind.calculate_depth()
#    function = ind.generate_string()
#    print(str(ind.depth) +" -> "+ function)
#    
#    y =  eval("lambda "+X+" :" + function)
#    print(eval("y(" + ( ','.join(V[0:V.__len__()-1]) ) +")") )


        

#teste.set_left(terminals[0])
#teste.set_right(operators[0])
#print(teste.name)
#print(teste.left.name+","+teste.right.name)
#teste.calculate_depth()
#print(teste.depth)
#operators[0].calculate_depth()
#print(operators[0].depth)
#teste.category = 3
#print(teste.category)
#print(operators[0].category)