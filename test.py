import csv
from copy import copy
from node import Node
from evo import Evo
from statistic import Statistic
from math import log,sqrt,pow
import random
from operator import mul,add,sub,truediv

files_train = [
    #['datasets/keijzer-7-train.csv','datasets/keijzer-7-test.csv'],
    #[   'datasets/keijzer-10-train.csv','datasets/keijzer-10-test.csv'],
    ['datasets/house-train.csv','datasets/house-test.csv']]

operators =  [Node("add",0,2), Node("sub",0,2), Node("mul",0,2),Node("pow",0,2),Node("truediv",0,2) , Node("log",0,1)]
#terminals = [Node("x1",1,0),Node("x2",1,0),Node("(random.random()*9)",1,0)]#

def readCSVFile(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

def evaluate(ind, data):
    try:
        ind.function_string = ("lambda " + X + " :"+ ind.generate_string())
        ind.function = eval(ind.function_string)
        sum = 0
        for row in data:
            y = 0
            y = eval("ind.function(" + ( ','.join(row[0:row.__len__()-1]) ) +")")
            sum += pow(y - float(row[row.__len__()-1]),2)
        
        sum = sum/data.__len__()
        sum = sqrt(sum)
        return sum
    except Exception as e:
        sum = 200000000        
        #print(ind.function_string)
        return sum

def calculate_fitness(self):
    fitness_list = []
    
    for ind in self.population:
        sum = evaluate(ind,self.train_data)
        ind.fitness = sum
        fitness_list.append(sum)
        #print(ind.fitness)
    if self.stat_list.__len__() > 0:
        self.stat_list.append(Statistic(fitness_list,self.stat_list[self.stat_list.__len__()-1].med()))
    else: 
        self.stat_list.append(Statistic(fitness_list,None))

X = ""
for file in files_train:
    train_data =  readCSVFile(file[0])
    
    first = True
    X = "" 
    terminals = []
    for n in range(0, train_data[0].__len__()-1) :
        if first:
            X += ("x"+str(n))
            first = False
        else:
            X += (",x"+str(n))
        terminals.append(Node(("x"+str(n)),1,0))
    terminals.append(Node("(random.random()*9)",1,0))

    parameters = [
        #[50, 2, 7, 0.9, 0.05, operators, terminals, train_data, calculate_fitness, True,50],
        #[100, 2, 7, 0.9, 0.05, operators, terminals, train_data,calculate_fitness, True,50],
        [500, 2, 7, 0.9, 0.05, operators, terminals, train_data,calculate_fitness, True,50],
        [100, 2, 7, 0.9, 0.05, operators, terminals, train_data, calculate_fitness, True,100],
        [100, 2, 7, 0.9, 0.05, operators, terminals, train_data, calculate_fitness, True,500],
        [100, 5, 7, 0.9, 0.05, operators, terminals, train_data, calculate_fitness, True,100],
        [100, 2, 7, 0.8, 0.15, operators, terminals, train_data, calculate_fitness, True,100],
        [100, 2, 7, 0.7, 0.25, operators, terminals, train_data, calculate_fitness, True,100]]
    
    for param in parameters:
        print("file = "+ file[0] +", max_pop = "+ str(param[0])+", Gerações = "+str(param[10])+", tour_size = "+str(param[1])+", cross_rate = " + str(param[3]) + ", mut_rate = "+ str(param[4]))
        train = Evo(param[0],param[1],param[2],param[3],param[4],param[5],param[6],param[7],param[8],param[9],param[10])
        train.execute()
        first = True
        for l in train.stat_list:
            if first:
                print(str(l.best())+","+str(l.worse())+","+str(l.med())+","+str(l.n_rep()))
                first = False
            else:
                print(str(l.best())+","+str(l.worse())+","+str(l.med())+","+str(l.n_rep())+","+str(l.above)+","+str(l.below))

        print("----------------------------")
        test_data = readCSVFile(file[1])
        best = train.get_best()
        print(best.generate_string())
        print("Train data fitness: "+str(best.fitness)) 
        print("Test data fitness: "+str(evaluate(best,test_data)))
        print("----------------------------")