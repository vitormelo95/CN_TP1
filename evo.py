from node import Node
from copy import copy,deepcopy
import random 
class Evo(object):
    def __init__(self, size_pop, size_tour, max_size_ind, crossover_rate, mutation_rate,
                 operators, terminals, train_data, fitness_function, elitism, n_gen):        
        self.size_pop = size_pop
        self.size_tour = size_tour
        self.max_size_ind = max_size_ind
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.operators = operators
        self.terminals = terminals 
        self.population = []
        self.train_data = train_data
        self.fitness_function = fitness_function 
        self.elitism = elitism
        self.n_gen = n_gen
        self.stat_list = []
        

    def initialize_population(self):
        max = (int(self.size_pop//(self.max_size_ind-1)//2))
        for i in range(2,self.max_size_ind+1):
            for j in range(0,max+1):
                self.population.append(self.create_full(1,i))
                self.population.append(self.create_grow(1,i))
        pass

    def create_full(self,depth,i):
        if(depth < i):
            random_num =  random.randint(0,self.operators.__len__()-1)
            ind = copy(self.operators[random_num])
            ind.set_left(self.create_full(depth+1,i))
            if ind.max_childrens > 1:
                ind.set_right(self.create_full(depth+1,i))
            return ind
        else:
            random_num =  random.randint(0,self.terminals.__len__()-1)
            ind = copy(self.terminals[random_num])
            if( "random" in ind.name):
                ind.name =  str(eval(ind.name))
            return ind
    
    def create_grow(self,depth,i):
        total = self.operators.__len__() + self.terminals.__len__()
        if(depth < i):
            if depth == 1:
                total = self.operators.__len__() 
            random_num =  random.randint(0,total-1)
            if(random_num < self.operators.__len__()):
                
                ind = copy(self.operators[random_num])
                ind.set_left(self.create_grow(depth+1,i))
                if ind.max_childrens > 1: 
                    ind.set_right(self.create_grow(depth+1,i))
                return ind
            else:
                index = random_num - self.operators.__len__()
                ind = copy(self.terminals[index])
                if( "random" in ind.name):
                    ind.name =  str(eval(ind.name))
                return ind
        else:
            random_num =  random.randint(0,self.terminals.__len__()-1)
            ind = copy(self.terminals[random_num])
            if( "random" in ind.name):
                ind.name =  str(eval(ind.name))
            return ind

    
    def tournament(self):
        tour_pop = []
        max = 0
        first = True
        while tour_pop.__len__() < self.size_tour:
            rand = random.randint(0, self.population.__len__()-1)
            if self.population[rand] not in tour_pop :
                tour_pop.append(self.population[rand])
                if first:
                    max = rand
                    first = False
                else:
                    if self.population[rand].fitness < self.population[max].fitness:
                        max = rand
        return max

    def evolve(self):
        new_pop = []
        if self.elitism:
            new_pop.append(self.get_best()) 
        while new_pop.__len__() < self.size_pop:
            i = self.tournament()
            rand_cross =  random.random()
            if rand_cross <= self.crossover_rate :
                j = self.tournament()
                while j == i: j = self.tournament()
                new_pop.extend(self.crossover(i,j))
            rand_mut = random.random()
            if rand_mut <= self.mutation_rate :
                new_pop.append(self.mutation(i))
        #print("------------")
        self.population =  new_pop
                
    
    def get_best(self):
        first =  True
        best = None
        for ind in self.population:
            if first:
                best = ind
                first = False
            else:
                if ind.fitness < best.fitness:
                    best = ind
        return deepcopy(best)
    
    def crossover(self,i,j):
        #print(self.population[i].function_string)
        #print(self.population[j].function_string)
        sizei = self.population[i].__size__()
        sizej = self.population[j].__size__()
        random_num1 = random.randint(0,sizei-1)
        random_num2 = random.randint(0,sizej-1)
        node1 = self.population[i].find_node(random_num1)
        node2 = self.population[j].find_node(random_num2)
        self.population[i].calculate_depth()
        self.population[j].calculate_depth()
        if( (self.population[i].depth - node1.depth + node2.depth > self.max_size_ind)
                or ( self.population[j].depth - node2.depth + node1.depth > self.max_size_ind) ):
            random_num1 = random.randint(0,sizei-1)
            node1 = self.population[i].find_node(random_num1)
            random_num2 = random.randint(0,sizej-1)
            node2 = self.population[j].find_node(random_num2)
        #print(node1.generate_string())
        #print(node2.generate_string())
        node_s1 = deepcopy(self.population[i])
        node_s2 = deepcopy(self.population[j])
       
        if node1 == self.population[i] : 
             node_s1 = deepcopy(node2)
        else:
            node_s1.change_node(self.population[i],node1,node2)
        if node2 == self.population[j]:
            node_s2 = deepcopy(node1)
        else:
            node_s2.change_node(self.population[j],node2, node1)
        #print(self.population[i].generate_string())
        #print(self.population[j].generate_string())
        #print(node_s1.generate_string())
        #print(node_s2.generate_string())
        #print("---------------")
        return [node_s1, node_s2]

    def mutation(self, i ):
        random_num1 = random.randint(0,self.population[i].__size__()-1)
        node = self.population[i].find_node(random_num1)
        node.calculate_depth()
        self.population[i].calculate_depth()
        new_node = self.create_grow((self.population[i].depth - node.depth), self.max_size_ind  )
        new_ind = copy(self.population[i])
        if node == self.population[i]:
            new_ind = new_node
        else:
            new_ind.change_node(self.population[i],node,new_node)
        #print(self.population[i].generate_string())
        #print(new_ind.generate_string())

        return new_ind

    def execute(self):
        self.initialize_population()
        self.fitness_function(self)
        for i in range (0,self.n_gen):
            self.evolve()
            self.fitness_function(self)
            #print(self.get_best().generate_string())
            print(str(i))
        print("--------------")
        pass