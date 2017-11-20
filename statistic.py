from collections import Counter
class Statistic(object):
    def __init__(self,fitness_list,father_med):
        self.fitness_list = fitness_list
        if father_med:
            self.calc_abovebelow(father_med)
    #high_fit, low_fit, med

    def best(self):
        first =  True
        best = None
        for fitness in self.fitness_list :
            if first:
                best = fitness
                first = False
            else:
                if fitness < best:
                    best = fitness
        return best
    
    def worse(self):
        first =  True
        worse = None
        for fitness in self.fitness_list :
            if first:
                worse = fitness
                first = False
            else:
                if fitness > worse:
                    worse = fitness
        return worse

    def med(self):
        med = 0.0 
        for fitness in self.fitness_list :
            med += float(fitness)
        return med / float(self.fitness_list.__len__())

    def n_rep(self):
        n_rep = 0
        C = Counter(self.fitness_list)
        rep =  [ [k,]*v for k,v in C.items()]
        for l in rep:
            n_rep += (l.__len__()-1)
        return n_rep
    
    def calc_abovebelow(self,father_med):
        above = 0
        below = 0
        for fitness in self.fitness_list:
            if fitness > father_med:
                above+=1
            else:
                below-=1
        self.above = above
        self.below = below

