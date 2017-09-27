from node import Node
from copy import copy
import random 
class Evo(object):
    def __init__(self, size_pop, size_tour, max_size_ind, crossover_rate, mutation_rate,
                 operators, terminals, train_data, fitness_function):        
        self.size_pop = size_pop
        self.size_tour = size_tour
        self.max_size_ind = max_size_ind
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.operators = operators
        self.terminals = terminals 
        self.population = []
        self.train_data = train_data
        self.__fitness_function__ = fitness_function

    def initialize_population(self):
        max = (int(self.size_pop//self.max_size_ind//2))
        for i in range(2,self.max_size_ind+1):
            for j in range(0,max+1):
                self.population.append(self.create_full(1,i))
                self.population.append(self.create_grow(1,i))

    def create_full(self,depth,i):
        if(depth < i):
            random_num =  random.randint(0,self.operators.__len__()-1)
            ind = copy(self.operators[random_num])
            ind.set_left(self.create_full(depth+1,i))
            ind.set_right(self.create_full(depth+1,i))
            return ind
        else:
            random_num =  random.randint(0,self.terminals.__len__()-1)
            ind = copy(self.terminals[random_num])
            return ind
    
    def create_grow(self,depth,i):
        total = self.operators.__len__() + self.terminals.__len__()
        if(depth < i):
            random_num =  random.randint(0,total-1)
            if(random_num < self.operators.__len__()):
                ind = copy(self.operators[random_num])
                ind.set_left(self.create_grow(depth+1,i))
                ind.set_right(self.create_grow(depth+1,i))
                return ind
            else:
                ind = copy(self.terminals[random_num - self.operators.__len__()])
                return ind
        else:
            random_num =  random.randint(0,self.terminals.__len__()-1)
            ind = copy(self.terminals[random_num])
            return ind

    
#    def tournament(self):
#        tour_pop = []
#        for i in range(0,self.size_tour):
#            rand = random.randint(0, self.population.__len__()-1)
#            if(!tour_pop.__contains__(self.population[rand])):
#                tour_pop.append(self.population[rand])
#