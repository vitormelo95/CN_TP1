import csv
from copy import copy
from node import Node
from evo import Evo
from math import log
import random
from operator import mul,add,sub,div
#def readCSVFile(filename):
#    with open(filename,'rb') as csvfile:
#        data = csv.reader(csvfile)
#        return data.result
#
#data =  readCSVFile('datasets/keijzer-7-train.csv')
#print(data)

X = "x1,x2"
V = ["1","2","3"]
operators =  [Node("add",0,2), Node("sub",0,2), Node("mul",0,2), Node("div",0,2), Node("log",0,2)]
terminals = [Node("x1",1,0),Node("x2",1,0),Node("random.randrange(1,9)",1,0) ]
train =  Evo(10, 3, 7, 0.9, 0.05, operators, terminals, None, None)
train.initialize_population()

for ind in train.population:
    ind.calculate_depth()
    function = ind.generate_string()
    print(str(ind.depth) +" -> "+ function)
    
    y =  eval("lambda "+X+" :" + function)
    print(eval("y(" + ( ','.join(V[0:V.__len__()-1]) ) +")") )


#def calculate_fitness(train):
#    for ind in train.population:
#        ind.function = ind.generate_string()
        

        

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