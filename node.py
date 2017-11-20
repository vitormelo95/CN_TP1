from copy import copy,deepcopy
import random
class Node(object):
    def __init__(self,name,category,max_childrens):
        self.name = name
        self.category = category
        self.max_childrens = max_childrens
        self.depth = 1
        self.left = None
        self.right = None
        self.fitness = 0
        
    def set_right(self, node):
        self.right = deepcopy(node)
    def set_left(self, node):
        self.left = deepcopy(node)

    def generate_string(self):
        
        if self.right:
            return self.name + "("+ self.left.generate_string() + " , " +self.right.generate_string()+")"
        elif self.left:
            return self.name + "("+ self.left.generate_string() +")"
        else:
            return self.name
            

    def calculate_depth(self):
        depth_right = 0
        depth_left  = 0
        if(self.right):
            self.right.calculate_depth()
            depth_right = self.right.depth
        if(self.left):
            self.left.calculate_depth()
            depth_left = self.left.depth
        
        self.depth =  depth_right + 1 if depth_right >= depth_left  else depth_left + 1

    def __size__(self):
        size_right = 0
        size_left  = 0
        
        if(self.left):
            size_left = self.left.__size__()
        if(self.right):
            size_right = self.right.__size__()
        return  size_left + size_right  + 1

    def find_node(self, n):
        if n == 0:
            return self
        elif(self.left and self.left.__size__() >= n ):
            return self.left.find_node(n-1)
        elif(self.right):
            return self.right.find_node(n - self.left.__size__() -1)
            
    def change_node(self,node_f, node, new_node):
        if(node_f.left == node):
            self.set_left(new_node)
        elif (node_f.right == node):
            self.set_right(new_node)
        else:
            if node_f.left:
                self.left.change_node(node_f.left, node, new_node)
            if node_f.right:
                self.right.change_node( node_f.right,node, new_node)